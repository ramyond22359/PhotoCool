import os
import shutil
import hashlib
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp', '.tiff')

def get_file_md5(file_path, block_size=65536):
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(block_size), b''):
                hasher.update(chunk)
        return hasher.hexdigest(), file_path
    except Exception as e:
        print(f"⚠️ 無法讀取檔案 {file_path}: {e}")
        return None, file_path

def get_unique_filename(target_folder, original_filename):
    base, ext = os.path.splitext(original_filename)
    candidate = original_filename
    counter = 1
    while os.path.exists(os.path.join(target_folder, candidate)):
        candidate = f"{base}_{counter}{ext}"
        counter += 1
    return candidate

def process_and_split_images(source_folder):
    if not os.path.exists(source_folder):
        print(f"❌ 找不到資料夾：{source_folder}")
        return

    clean_folder = os.path.join(source_folder, "已過濾_無重複圖片")
    duplicate_folder = os.path.join(source_folder, "已分流_重複照片")
    
    os.makedirs(clean_folder, exist_ok=True)
    os.makedirs(duplicate_folder, exist_ok=True)

    file_list = []
    print("📁 正在掃描圖片庫資料夾...")
    for root, dirs, files in os.walk(source_folder):
        if "已過濾_無重複圖片" in root or "已分流_重複照片" in root:
            continue
        for file in files:
            if file.lower().endswith(VALID_EXTENSIONS):
                file_list.append(os.path.join(root, file))

    if not file_list:
        print("ℹ️ 資料夾內沒有發現可處理的圖片。")
        return

    print(f"📸 找到 {len(file_list)} 張圖片，開始計算指紋與比對...")

    md5_dict = defaultdict(list)
    with ThreadPoolExecutor() as executor:
        results = executor.map(get_file_md5, file_list)
        for md5_val, file_path in results:
            if md5_val:
                md5_dict[md5_val].append(file_path)

    print("\n🚚 開始自動分流搬移檔案...")
    moved_clean_count = 0
    moved_dup_count = 0

    for md5_val, paths in md5_dict.items():
        paths_sorted = sorted(paths, key=lambda x: (len(os.path.basename(x)), x))
        
        # 移至無重複資料夾
        unique_file = paths_sorted[0]
        filename = os.path.basename(unique_file)
        dest_filename = get_unique_filename(clean_folder, filename)
        shutil.move(unique_file, os.path.join(clean_folder, dest_filename))
        moved_clean_count += 1

        # 移至重複資料夾
        for dup_file in paths_sorted[1:]:
            dup_filename = os.path.basename(dup_file)
            dest_dup_filename = get_unique_filename(duplicate_folder, dup_filename)
            shutil.move(dup_file, os.path.join(duplicate_folder, dest_dup_filename))
            moved_dup_count += 1

    print("\n" + "=" * 50)
    print("🎉 分流整理完成！摘要如下：")
    print(f" 🟢 已過濾（獨一無二原檔）: {moved_clean_count} 張 ➔ 存於 [{clean_folder}]")
    print(f" 🔴 已隔離（重複圖片檔案）: {moved_dup_count} 張 ➔ 存於 [{duplicate_folder}]")
    print("=" * 50)

if __name__ == "__main__":
    import sys
    
    # 支援手動輸入或直接拖曳資料夾
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        target_dir = input("請輸入或拖曳您的照片資料夾路徑至此，然後按 Enter: ").strip('"\' ')
        
    process_and_split_images(target_dir)
