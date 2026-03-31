# Playwright pytest 指令說明

## 基本執行

```bash
# 執行所有測試
pytest

# 執行指定資料夾
pytest base-pratice/

# 執行指定檔案
pytest base-pratice/test_initTesting.py

# 執行指定測試函式
pytest base-pratice/test_initTesting.py::test_verifyPageUrl
```

---

## 常用參數

| 參數 | 說明 | 範例 |
|------|------|------|
| `-s` | 顯示 `print()` 輸出（不截斷 stdout） | `pytest -s` |
| `-v` | 詳細模式，顯示每個測試名稱與結果 | `pytest -v` |
| `-sv` | 同時啟用 `-s` 和 `-v` | `pytest -sv` |
| `-x` | 遇到第一個失敗即停止 | `pytest -x` |
| `-k` | 只執行名稱符合關鍵字的測試 | `pytest -k "Url"` |
| `--tb=short` | 縮短錯誤 traceback 輸出 | `pytest --tb=short` |
| `--tb=no` | 不顯示 traceback | `pytest --tb=no` |
| `-n` | 平行執行（需安裝 `pytest-xdist`） | `pytest -n 4` |
| `--headed` | 以有頭模式執行（顯示瀏覽器視窗） | `pytest --headed` |
| `--browser` | 指定瀏覽器（chromium / firefox / webkit） | `pytest --browser firefox` |
| `--slowmo` | 每個操作間加入延遲（毫秒） | `pytest --slowmo 500` |
| `--timeout` | 設定單一測試逾時秒數 | `pytest --timeout=30` |

---

## Playwright 專用參數

```bash
# 有頭模式（看得到瀏覽器）
pytest --headed

# 指定瀏覽器
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit

# 有頭 + 慢速執行（方便 debug）
pytest --headed --slowmo 1000

# 指定視窗大小（需在 conftest.py 設定，或透過 browser_context_args）
```

---

## 多視窗 / 多瀏覽器測試

### 同一測試內開多個頁面（sync）

```python
from playwright.sync_api import Browser

def test_multiple_pages(browser: Browser):
    page1 = browser.new_page()
    page2 = browser.new_page()

    page1.goto("https://www.saucedemo.com/")
    page2.goto("https://www.google.com/")

    print(page1.title())
    print(page2.title())

    page1.close()
    page2.close()
```

### 同一測試內開多個 context（隔離 session）

```python
from playwright.sync_api import Browser

def test_multiple_contexts(browser: Browser):
    context1 = browser.new_context()
    context2 = browser.new_context()

    page1 = context1.new_page()
    page2 = context2.new_page()

    page1.goto("https://www.saucedemo.com/")
    page2.goto("https://www.saucedemo.com/")

    context1.close()
    context2.close()
```

### 平行執行多個測試檔（需安裝 pytest-xdist）

```bash
pip install pytest-xdist

# 使用 4 個 worker 平行執行
pytest -n 4

# 自動偵測 CPU 數量
pytest -n auto
```

---

## async 測試（pytest-asyncio）

```bash
# 安裝依賴
pip install pytest-asyncio

# 執行 async 測試
pytest base-pratice/test_initTesting_async.py -v
```

---

## 組合範例

```bash
# 詳細輸出 + 顯示 print + 有頭模式
pytest -sv --headed base-pratice/

# 只跑名稱含 "Title" 的測試，並顯示輸出
pytest -s -k "Title"

# 失敗立即停止 + 短 traceback
pytest -x --tb=short

# 平行 + 詳細
pytest -n 4 -v
```

---

## 安裝指令

```bash
# 安裝 playwright
pip install playwright
playwright install

# 安裝 pytest-playwright
pip install pytest-playwright

# 安裝 async 支援
pip install pytest-asyncio

# 安裝平行執行支援
pip install pytest-xdist
```
