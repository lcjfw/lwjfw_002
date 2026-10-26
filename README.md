# 課間｜個人課表維護系統（Django）

免登入的三頁式課表專案，使用 Django 5.2、SQLite、HTML/CSS/JavaScript。

## Windows 執行

1. 安裝 Python 3.10 以上，勾選 Add Python to PATH。啟動檔會優先使用 py，沒有時改用 python。
2. 下載 ZIP 並完整解壓縮。使用檔案總管雙擊 `run_windows.bat`（不要在 VS Code 中開啟編輯）。
3. 第一次需網路安裝套件。看到伺服器啟動後，開啟 http://127.0.0.1:8000/ 。
4. 使用期間保持命令視窗開啟；結束時按 Ctrl+C。

## macOS / Linux 或手動執行

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Windows 手動啟用環境改用 `.venv\Scripts\activate`。

## 功能與作業要求

- 個人課表 `/`：點空白格新增；點課程修改或刪除；儲存到 SQLite，重新整理保留資料。
- 同時檢查衝堂、提供搜尋、清單、列印、JSON 匯入匯出與上次操作復原。
- 預設 10 門課程，17:15–18:05 節次已設定；可自訂節次。
- 選課資訊 `/courses/`：課程搜尋與篩選，僅供參考，不是正式加退選。
- 專注計時 `/focus/`：自訂專注及休息時間，開始、暫停、繼續、重設。

## GitHub 提交方式

將本資料夾內容上傳至公開 GitHub 儲存庫，根目錄要看得到 manage.py、requirements.txt、README.md、config、pages。交作業請提供程式碼儲存庫連結與示範錄影。

GitHub Pages 只能提供靜態頁面，不能執行本 Django 後端。老師可 clone 本專案後依上述步驟執行。原本 Pages 靜態版可保留展示；若要公開 Django 網址，需要另設 Python 主機，此包未部署公開主機。

## 10 分鐘內示範流程

1. 說明 Django + SQLite 與三個頁面（1 分鐘）。
2. 空白格新增「測試課程」，填老師、教室、星期及節次（1 分鐘）。
3. 點該課程修改名稱與教室，重新整理確認保留（1 分鐘）。
4. 新增相同時間課程，展示衝堂攔截（1 分鐘）。
5. 刪除測試課程，重新整理確認消失（1 分鐘）。
6. 匯出備份，展示選課搜尋及自訂計時（2 分鐘）。

## 資料保存

課表在 SQLite 中以目前瀏覽器 session Cookie 區分，免登入。不同裝置不會自動同步；清除 Cookie 可能失去原資料入口。請用 JSON 匯出／匯入搬移資料。舊 GitHub Pages 課表也可匯出後匯入此版本。

計時分鐘設定保存在瀏覽器，離頁或重新整理會重設倒數。備份伺服器請先關閉後備份 db.sqlite3 與 .dev-secret，勿上傳實際資料庫與金鑰。此為本機課堂展示設定。

## 驗證

```sh
python manage.py check
python manage.py test
```

## 本次修正

統一使用 manage.py、requirements.txt 等正確檔名，移除下載重複的 (1)；補齊 config、pages 與 migration；更新為三頁式課表維護說明；移除無效的 class:main 指令與不必要的建置依賴。啟動檔會檢查每一步結果，首次自動建立環境及資料庫。

請完整解壓縮到新資料夾，避免混用舊版檔案及資料庫。舊課表請先匯出 JSON，再於新版匯入。Windows 啟動檔已檢查內容，尚未在實體 Windows 電腦實跑。
