<p align="center">
  <a href="README.md">简体中文</a> | 
  <a href="README_EN.md">English</a> | 
  <a href="README_TW.md">繁體中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/python-3.8+-green.svg" alt="Python">
  <img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="License">
  <img src="https://img.shields.io/badge/dependencies-zero-brightgreen.svg" alt="Dependencies">
</p>

<h1 align="center">🌤️ SkyPulse</h1>

<h3 align="center">輕量級終端天氣智慧助手 CLI</h3>

<p align="center">
  零依賴核心 · ASCII藝術視覺化 · 智慧位置偵測 · 天氣預警 · 穿衣建議
</p>

---

## 🎉 專案介紹

**SkyPulse** 是一款專為終端使用者打造的輕量級天氣智慧助手。它採用**零依賴核心設計**，僅使用 Python 標準函式庫，讓你無需安裝任何第三方套件即可取得即時天氣資訊。

### 💡 設計靈感

作為開發者，我們每天都在終端機中工作。切換到瀏覽器查看天氣會打斷工作流程。SkyPulse 讓你在終端機中即可取得完整的天氣資訊，包括精美的 ASCII 藝術視覺化、智慧穿衣建議和天氣預警。

### ✨ 核心特性

- 🌡️ **即時天氣查詢** - 溫度、體感溫度、濕度、風速、氣壓等完整資料
- 🎨 **ASCII 藝術視覺化** - 精美的天氣狀態 ASCII 藝術展示
- 📊 **溫度條視覺化** - 直觀的溫度條顏色顯示
- 📍 **智慧位置偵測** - 基於 IP 自動偵測目前位置
- 📅 **多日天氣預報** - 支援最多 16 天天氣預報
- ⚠️ **天氣預警系統** - 自動偵測極端天氣並發出警告
- 👔 **智慧穿衣建議** - 根據天氣條件推薦合適的穿著
- 🔧 **多 API 支援** - Open-Meteo API，免費無需金鑰
- 📤 **JSON 輸出** - 支援 JSON 格式輸出，便於整合
- 🌡️ **單位切換** - 支援攝氏/華氏切換
- 🎨 **彩色輸出** - 終端彩色顯示，支援停用

---

## 🚀 快速開始

### 📋 環境要求

- Python 3.8 或更高版本
- 無需任何第三方依賴！

### 📦 安裝方式

#### 方式一：直接執行（推薦）

```bash
# 複製儲存庫
git clone https://github.com/gitstq/SkyPulse.git
cd SkyPulse

# 直接執行
python skypulse.py
```

#### 方式二：pip 安裝

```bash
pip install skypulse
```

### 🎯 基本使用

```bash
# 自動偵測位置並顯示天氣
skypulse

# 查詢指定城市天氣
skypulse Taipei
skypulse "New York"
skypulse Tokyo

# 顯示 7 天天氣預報
skypulse --forecast
skypulse Taipei --forecast

# 顯示天氣預警
skypulse --alert

# 取得穿衣建議
skypulse --clothing

# JSON 格式輸出
skypulse --json

# 使用華氏度
skypulse --units fahrenheit

# 停用彩色輸出
skypulse --no-color
```

---

## 📖 詳細使用指南

### 🌡️ 目前天氣查詢

```bash
# 查詢台北目前天氣
$ skypulse Taipei

==================================================
  🌤️  SkyPulse Weather Report
==================================================

  📍 Location: Taipei, Taiwan
  🕐 Time: 2026-05-09 17:07:24

     \   /
      .-.
   ― (   ) ―
      `-´
     /   \

  🌡️  Temperature: 26.0°C
     Feels like: 28.5°C
     [███████████████░░░░░]

  ☁️  Condition: Partly cloudy

  💨 Wind: 8.5 km/h E
  💧 Humidity: 75%
  📊 Pressure: 1010.2 hPa
  🌧️  Precipitation: 0.0 mm
  ☀️  UV Index: 6.5
  🌅 Sunrise: 05:15
  🌇 Sunset: 18:30

==================================================
```

### 📅 天氣預報

```bash
# 顯示 3 天預報
$ skypulse Taipei --forecast --days 3

============================================================
  🌤️  SkyPulse 3-Day Forecast for Taipei, Taiwan
============================================================

  2026-05-10: ☁️ Partly cloudy
     ↑ 30°C  ↓ 24°C  🌧️ 10%

  2026-05-11: 🌧️ Light rain
     ↑ 28°C  ↓ 23°C  🌧️ 45%

  2026-05-12: ☁️ Cloudy
     ↑ 29°C  ↓ 24°C  🌧️ 20%

============================================================
```

### ⚠️ 天氣預警

```bash
$ skypulse --alert

==================================================
  ⚠️  Weather Alerts for Taipei, Taiwan
==================================================

  ✅ No active weather alerts

==================================================
```

### 👔 穿衣建議

```bash
$ skypulse Taipei --clothing

==================================================
  👔 Clothing Recommendations for Taipei, Taiwan
==================================================

  👕 T-shirt and light pants
  🕶️ Consider sunglasses for extended outdoor time

==================================================
```

### 📤 JSON 輸出

```bash
$ skypulse Taipei --json

{
  "location": "Taipei, Taiwan",
  "timestamp": "2026-05-09 17:07:47",
  "temperature": 26.0,
  "feels_like": 28.5,
  "humidity": 75,
  "wind_speed": 8.5,
  "wind_direction": "E",
  "pressure": 1010.2,
  "visibility": 10.0,
  "condition": "cloudy",
  "description": "Partly cloudy",
  "uv_index": 6.5,
  "precipitation": 0.0,
  "sunrise": "2026-05-10T05:15",
  "sunset": "2026-05-10T18:30"
}
```

### 🎨 ASCII 天氣藝術

SkyPulse 為不同天氣狀態提供精美的 ASCII 藝術視覺化：

| 天氣狀態 | ASCII 藝術 |
|---------|-----------|
| ☀️ 晴天 | 太陽圖案 |
| ☁️ 多雲 | 雲朵圖案 |
| 🌧️ 雨天 | 雲+雨滴 |
| ❄️ 雪天 | 雲+雪花 |
| ⛈️ 雷暴 | 雲+閃電 |
| 🌫️ 霧天 | 霧氣線條 |
| 💨 大風 | 風流線條 |

---

## 💡 設計思路與迭代規劃

### 🏗️ 技術架構

```
SkyPulse
├── WeatherAPI        # 天氣 API 介面層
├── LocationDetector  # 位置自動偵測
├── ASCIIArt          # ASCII 藝術產生器
├── ClothingAdvisor   # 穿衣建議引擎
├── AlertSystem       # 天氣預警系統
└── SkyPulseCLI       # 命令列介面
```

### 🔧 技術選型

- **零依賴設計**: 僅使用 Python 標準函式庫，降低安裝門檻
- **Open-Meteo API**: 免費開源天氣 API，無需註冊 API 金鑰
- **資料類別設計**: 使用 dataclass 提高程式碼可讀性
- **型別註解**: 完整的型別提示，便於 IDE 支援和程式碼維護

### 📋 後續迭代計畫

- [ ] 支援更多天氣 API（OpenWeatherMap、WeatherAPI 等）
- [ ] 新增空氣品質指數(AQI)顯示
- [ ] 支援設定檔儲存常用位置
- [ ] 新增天氣趨勢圖表
- [ ] 支援多語言介面
- [ ] 新增桌面通知功能
- [ ] 支援天氣歷史資料查詢

---

## 📦 打包與部署指南

### 本地開發

```bash
# 複製儲存庫
git clone https://github.com/gitstq/SkyPulse.git
cd SkyPulse

# 安裝開發依賴
pip install -e ".[dev]"

# 執行測試
pytest

# 程式碼格式化
black skypulse.py
isort skypulse.py

# 型別檢查
mypy skypulse.py
```

### 建構 PyPI 套件

```bash
# 安裝建構工具
pip install build

# 建構
python -m build

# 上傳到 PyPI
pip install twine
twine upload dist/*
```

---

## 🤝 貢獻指南

我們歡迎所有形式的貢獻！

### 如何貢獻

1. 🍴 Fork 本儲存庫
2. 🌿 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 💾 提交變更 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 📤 推送到分支 (`git push origin feature/AmazingFeature`)
5. 🎉 提交 Pull Request

### 程式碼規範

- 遵循 PEP 8 編碼規範
- 新增適當的型別註解
- 為新功能撰寫測試
- 更新相關文件

### 提交規範

使用 Angular 提交規範：

- `feat:` 新功能
- `fix:` 修復問題
- `docs:` 文件更新
- `refactor:` 程式碼重構
- `test:` 測試相關
- `chore:` 建構/工具相關

---

## 📄 開源協議

本專案採用 [MIT](LICENSE) 協議開源。

---

<p align="center">
  Made with ❤️ by SkyPulse Team
</p>
