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

<h3 align="center">轻量级终端天气智能助手 CLI</h3>

<p align="center">
  零依赖核心 · ASCII艺术可视化 · 智能位置检测 · 天气预警 · 穿衣建议
</p>

---

## 🎉 项目介绍

**SkyPulse** 是一款专为终端用户打造的轻量级天气智能助手。它采用**零依赖核心设计**，仅使用Python标准库，让你无需安装任何第三方包即可获取实时天气信息。

### 💡 设计灵感

作为开发者，我们每天都在终端中工作。切换到浏览器查看天气会打断工作流程。SkyPulse 让你在终端中即可获取完整的天气信息，包括精美的ASCII艺术可视化、智能穿衣建议和天气预警。

### ✨ 核心特性

- 🌡️ **实时天气查询** - 温度、体感温度、湿度、风速、气压等完整数据
- 🎨 **ASCII艺术可视化** - 精美的天气状态ASCII艺术展示
- 📊 **温度条可视化** - 直观的温度条颜色显示
- 📍 **智能位置检测** - 基于IP自动检测当前位置
- 📅 **多日天气预报** - 支持最多16天天气预报
- ⚠️ **天气预警系统** - 自动检测极端天气并发出警告
- 👔 **智能穿衣建议** - 根据天气条件推荐合适的穿着
- 🔧 **多API支持** - Open-Meteo API，免费无需密钥
- 📤 **JSON输出** - 支持JSON格式输出，便于集成
- 🌡️ **单位切换** - 支持摄氏度/华氏度切换
- 🎨 **彩色输出** - 终端彩色显示，支持禁用

---

## 🚀 快速开始

### 📋 环境要求

- Python 3.8 或更高版本
- 无需任何第三方依赖！

### 📦 安装方式

#### 方式一：直接运行（推荐）

```bash
# 克隆仓库
git clone https://github.com/gitstq/SkyPulse.git
cd SkyPulse

# 直接运行
python skypulse.py
```

#### 方式二：pip 安装

```bash
pip install skypulse
```

### 🎯 基本使用

```bash
# 自动检测位置并显示天气
skypulse

# 查询指定城市天气
skypulse Beijing
skypulse "New York"
skypulse Tokyo

# 显示7天天气预报
skypulse --forecast
skypulse Beijing --forecast

# 显示天气预警
skypulse --alert

# 获取穿衣建议
skypulse --clothing

# JSON格式输出
skypulse --json

# 使用华氏度
skypulse --units fahrenheit

# 禁用彩色输出
skypulse --no-color
```

---

## 📖 详细使用指南

### 🌡️ 当前天气查询

```bash
# 查询北京当前天气
$ skypulse Beijing

==================================================
  🌤️  SkyPulse Weather Report
==================================================

  📍 Location: Beijing, China
  🕐 Time: 2026-05-09 17:07:24

     \   /
      .-.
   ― (   ) ―
      `-´
     /   \

  🌡️  Temperature: 18.0°C
     Feels like: 17.7°C
     [███████████░░░░░░░░░]

  ☁️  Condition: Clear sky

  💨 Wind: 2.2 km/h NNW
  💧 Humidity: 59%
  📊 Pressure: 1005.6 hPa
  🌧️  Precipitation: 0.0 mm
  ☀️  UV Index: 7.3
  🌅 Sunrise: 05:04
  🌇 Sunset: 19:17

==================================================
```

### 📅 天气预报

```bash
# 显示3天预报
$ skypulse Beijing --forecast --days 3

============================================================
  🌤️  SkyPulse 3-Day Forecast for Beijing, China
============================================================

  2026-05-10: ☁️ Overcast
     ↑ 34°C  ↓ 15°C  🌧️ 0%

  2026-05-11: 🌧️ Light drizzle
     ↑ 32°C  ↓ 20°C  🌧️ 2%

  2026-05-12: ☁️ Overcast
     ↑ 32°C  ↓ 20°C  🌧️ 0%

============================================================
```

### ⚠️ 天气预警

```bash
$ skypulse --alert

==================================================
  ⚠️  Weather Alerts for Beijing, China
==================================================

  ✅ No active weather alerts

==================================================
```

### 👔 穿衣建议

```bash
$ skypulse Beijing --clothing

==================================================
  👔 Clothing Recommendations for Beijing, China
==================================================

  👕 Long sleeves or light sweater
  🕶️ Wear sunglasses and apply sunscreen

==================================================
```

### 📤 JSON 输出

```bash
$ skypulse Beijing --json

{
  "location": "Beijing, China",
  "timestamp": "2026-05-09 17:07:47",
  "temperature": 18.0,
  "feels_like": 17.7,
  "humidity": 59,
  "wind_speed": 2.2,
  "wind_direction": "NNW",
  "pressure": 1005.6,
  "visibility": 10.0,
  "condition": "clear",
  "description": "Clear sky",
  "uv_index": 7.3,
  "precipitation": 0.0,
  "sunrise": "2026-05-10T05:04",
  "sunset": "2026-05-10T19:17"
}
```

### 🎨 ASCII 天气艺术

SkyPulse 为不同天气状态提供精美的 ASCII 艺术可视化：

| 天气状态 | ASCII 艺术 |
|---------|-----------|
| ☀️ 晴天 | 太阳图案 |
| ☁️ 多云 | 云朵图案 |
| 🌧️ 雨天 | 云+雨滴 |
| ❄️ 雪天 | 云+雪花 |
| ⛈️ 雷暴 | 云+闪电 |
| 🌫️ 雾天 | 雾气线条 |
| 💨 大风 | 风流线条 |

---

## 💡 设计思路与迭代规划

### 🏗️ 技术架构

```
SkyPulse
├── WeatherAPI        # 天气API接口层
├── LocationDetector  # 位置自动检测
├── ASCIIArt          # ASCII艺术生成器
├── ClothingAdvisor   # 穿衣建议引擎
├── AlertSystem       # 天气预警系统
└── SkyPulseCLI       # 命令行接口
```

### 🔧 技术选型

- **零依赖设计**: 仅使用Python标准库，降低安装门槛
- **Open-Meteo API**: 免费开源天气API，无需注册API密钥
- **数据类设计**: 使用dataclass提高代码可读性
- **类型注解**: 完整的类型提示，便于IDE支持和代码维护

### 📋 后续迭代计划

- [ ] 支持更多天气API（OpenWeatherMap、WeatherAPI等）
- [ ] 添加空气质量指数(AQI)显示
- [ ] 支持配置文件保存常用位置
- [ ] 添加天气趋势图表
- [ ] 支持多语言界面
- [ ] 添加桌面通知功能
- [ ] 支持天气历史数据查询

---

## 📦 打包与部署指南

### 本地开发

```bash
# 克隆仓库
git clone https://github.com/gitstq/SkyPulse.git
cd SkyPulse

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 代码格式化
black skypulse.py
isort skypulse.py

# 类型检查
mypy skypulse.py
```

### 构建 PyPI 包

```bash
# 安装构建工具
pip install build

# 构建
python -m build

# 上传到 PyPI
pip install twine
twine upload dist/*
```

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 如何贡献

1. 🍴 Fork 本仓库
2. 🌿 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 💾 提交更改 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 📤 推送到分支 (`git push origin feature/AmazingFeature`)
5. 🎉 提交 Pull Request

### 代码规范

- 遵循 PEP 8 编码规范
- 添加适当的类型注解
- 为新功能编写测试
- 更新相关文档

### 提交规范

使用 Angular 提交规范：

- `feat:` 新功能
- `fix:` 修复问题
- `docs:` 文档更新
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建/工具相关

---

## 📄 开源协议

本项目采用 [MIT](LICENSE) 协议开源。

---

<p align="center">
  Made with ❤️ by SkyPulse Team
</p>
