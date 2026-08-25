# 📸 重複照片自動分流工具 <br> PhotoCool（Cull）

<p align="left">
  <a href="https://github.com/ramyond22359/duplicate-photo-sorter/releases"><img src="https://img.shields.io/badge/Download-.exe%20v1.0.0-blue?style=for-the-badge&logo=windows&logoColor=white" /></a>
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" />
</p>

---

## Part 1: 專案介紹 / Overview

### 📖 簡介 / Description
⚡ **一鍵清理硬碟空間！** 專為解決照片庫重複問題打造的極速分流工具。採用二進位 MD5 雜湊指紋，**100% 精確比對**，自動將原檔與重複檔案隔離。

### 💡 核心優勢 / Features
* 🎯 **100% 精準**：採用 MD5 位元組級指紋比對，絕不誤判。
* 🛡️ **安全隔離**：自動分流至獨立資料夾，不直接刪除檔案。
* 🚀 **極速處理**：支援多線程並行，上萬張照片秒級完成。
* 🎁 **零門檻**：提供 Windows 免安裝 `.exe` 執行檔。

### 📁 自動分流結構 / Folder Structure
程式執行後會自動建立兩個子資料夾：

```text
📁 您的照片資料夾 (Your Photo Directory)
 ├── 🟢 已過濾_無重複圖片/   <-- 保留 1 張原檔 (Clean Photos)
 └── 🔴 已分流_重複照片/     <-- 所有多餘的重複檔 (Duplicate Photos)
```
## Part 2: 使用與開發說明 / Guide & Development

### 🚀 快速開始 / Quick Start

**方案 A：下載 `.exe` 執行檔 (推薦一般使用者)**
1. 前往 **[Releases 頁面](https://github.com/ramyond22359/PhotoCool/releases)** 下載最新版的 `PhotoCool.exe`。
2. 雙擊開啟 `.exe` 檔案。
3. 將照片資料夾**拖曳進視窗內**，按下 `Enter` 即可完成！

**方案 B：執行 Python 原始碼 (Windows / Linux)**
1. 確保電腦已安裝 **Python 3.8+**。
2. 開啟命令提示字元 (CMD) 或 Terminal 執行：

```bash
python photocool.py
```
**方案 C：macOS 使用者**
1. 開啟終端機 (Terminal)。
2. 輸入 `cd `（後方加一空格），將專案資料夾拖入終端機並按 `Enter`。
3. 執行：
```bash
python3 photocool.py
```
4. 將照片資料夾拖入終端機，按下 Enter 即可。

### 🛠️ 開發與打包 / Developer Guide

```bash
# 1. 安裝 PyInstaller
py -m pip install pyinstaller

# 2. 一鍵打包成單一執行檔
py -m PyInstaller --onefile --name "Leaf" photocool.py
```
###📜 授權條款 / License
本專案採用 MIT License 開源授權。
