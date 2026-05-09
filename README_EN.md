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

<h3 align="center">Lightweight Terminal Weather Intelligence Assistant CLI</h3>

<p align="center">
  Zero Core Dependencies · ASCII Art Visualization · Smart Location Detection · Weather Alerts · Clothing Recommendations
</p>

---

## 🎉 Introduction

**SkyPulse** is a lightweight weather intelligence assistant designed specifically for terminal users. It features a **zero-dependency core design**, using only Python's standard library, allowing you to get real-time weather information without installing any third-party packages.

### 💡 Inspiration

As developers, we work in the terminal every day. Switching to a browser to check the weather interrupts our workflow. SkyPulse lets you get complete weather information right in your terminal, including beautiful ASCII art visualization, smart clothing recommendations, and weather alerts.

### ✨ Key Features

- 🌡️ **Real-time Weather** - Temperature, feels like, humidity, wind speed, pressure, and more
- 🎨 **ASCII Art Visualization** - Beautiful weather state ASCII art display
- 📊 **Temperature Bar** - Intuitive color-coded temperature bar
- 📍 **Smart Location Detection** - Auto-detect current location via IP
- 📅 **Multi-day Forecast** - Support up to 16 days weather forecast
- ⚠️ **Weather Alert System** - Automatically detect extreme weather conditions
- 👔 **Smart Clothing Advice** - Recommend appropriate clothing based on weather
- 🔧 **Multi-API Support** - Open-Meteo API, free with no API key required
- 📤 **JSON Output** - Support JSON format output for easy integration
- 🌡️ **Unit Switching** - Support Celsius/Fahrenheit switching
- 🎨 **Color Output** - Terminal color display with option to disable

---

## 🚀 Quick Start

### 📋 Requirements

- Python 3.8 or higher
- No third-party dependencies required!

### 📦 Installation

#### Option 1: Direct Run (Recommended)

```bash
# Clone the repository
git clone https://github.com/gitstq/SkyPulse.git
cd SkyPulse

# Run directly
python skypulse.py
```

#### Option 2: pip Install

```bash
pip install skypulse
```

### 🎯 Basic Usage

```bash
# Auto-detect location and show weather
skypulse

# Query weather for a specific city
skypulse Beijing
skypulse "New York"
skypulse Tokyo

# Show 7-day forecast
skypulse --forecast
skypulse Beijing --forecast

# Show weather alerts
skypulse --alert

# Get clothing recommendations
skypulse --clothing

# JSON format output
skypulse --json

# Use Fahrenheit
skypulse --units fahrenheit

# Disable colored output
skypulse --no-color
```

---

## 📖 Detailed Usage Guide

### 🌡️ Current Weather Query

```bash
# Query current weather in Beijing
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

### 📅 Weather Forecast

```bash
# Show 3-day forecast
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

### ⚠️ Weather Alerts

```bash
$ skypulse --alert

==================================================
  ⚠️  Weather Alerts for Beijing, China
==================================================

  ✅ No active weather alerts

==================================================
```

### 👔 Clothing Recommendations

```bash
$ skypulse Beijing --clothing

==================================================
  👔 Clothing Recommendations for Beijing, China
==================================================

  👕 Long sleeves or light sweater
  🕶️ Wear sunglasses and apply sunscreen

==================================================
```

### 📤 JSON Output

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

### 🎨 ASCII Weather Art

SkyPulse provides beautiful ASCII art visualization for different weather conditions:

| Weather | ASCII Art |
|---------|-----------|
| ☀️ Clear | Sun pattern |
| ☁️ Cloudy | Cloud pattern |
| 🌧️ Rainy | Cloud + Rain drops |
| ❄️ Snowy | Cloud + Snowflakes |
| ⛈️ Stormy | Cloud + Lightning |
| 🌫️ Foggy | Fog lines |
| 💨 Windy | Wind flow lines |

---

## 💡 Design Philosophy & Roadmap

### 🏗️ Technical Architecture

```
SkyPulse
├── WeatherAPI        # Weather API interface layer
├── LocationDetector  # Auto location detection
├── ASCIIArt          # ASCII art generator
├── ClothingAdvisor   # Clothing recommendation engine
├── AlertSystem       # Weather alert system
└── SkyPulseCLI       # Command-line interface
```

### 🔧 Technology Choices

- **Zero Dependency Design**: Only uses Python standard library to lower installation barrier
- **Open-Meteo API**: Free open-source weather API, no API key registration required
- **Dataclass Design**: Uses dataclass for better code readability
- **Type Annotations**: Complete type hints for IDE support and code maintenance

### 📋 Future Roadmap

- [ ] Support more weather APIs (OpenWeatherMap, WeatherAPI, etc.)
- [ ] Add Air Quality Index (AQI) display
- [ ] Support config file to save favorite locations
- [ ] Add weather trend charts
- [ ] Support multi-language interface
- [ ] Add desktop notification feature
- [ ] Support weather history query

---

## 📦 Packaging & Deployment

### Local Development

```bash
# Clone the repository
git clone https://github.com/gitstq/SkyPulse.git
cd SkyPulse

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Code formatting
black skypulse.py
isort skypulse.py

# Type checking
mypy skypulse.py
```

### Build PyPI Package

```bash
# Install build tools
pip install build

# Build
python -m build

# Upload to PyPI
pip install twine
twine upload dist/*
```

---

## 🤝 Contributing

We welcome all forms of contributions!

### How to Contribute

1. 🍴 Fork this repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🎉 Submit a Pull Request

### Code Standards

- Follow PEP 8 coding conventions
- Add appropriate type annotations
- Write tests for new features
- Update relevant documentation

### Commit Convention

Use Angular commit convention:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation update
- `refactor:` Code refactoring
- `test:` Test related
- `chore:` Build/tool related

---

## 📄 License

This project is licensed under the [MIT](LICENSE) License.

---

<p align="center">
  Made with ❤️ by SkyPulse Team
</p>
