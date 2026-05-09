#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SkyPulse - Lightweight Terminal Weather Intelligence Assistant CLI
轻量级终端天气智能助手CLI

A zero-dependency core, multi-API weather assistant with ASCII art visualization,
smart location detection, weather alerts, and clothing recommendations.
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Tuple, Any
from dataclasses import dataclass
from enum import Enum
import textwrap


class WeatherCondition(Enum):
    """Weather condition types"""
    CLEAR = "clear"
    CLOUDY = "cloudy"
    RAINY = "rainy"
    SNOWY = "snowy"
    STORMY = "stormy"
    FOGGY = "foggy"
    WINDY = "windy"
    UNKNOWN = "unknown"


@dataclass
class WeatherData:
    """Weather data structure"""
    location: str
    temperature: float
    feels_like: float
    humidity: int
    wind_speed: float
    wind_direction: str
    pressure: float
    visibility: float
    condition: WeatherCondition
    description: str
    uv_index: int
    precipitation: float
    sunrise: str
    sunset: str
    timestamp: str
    air_quality: Optional[int] = None


@dataclass
class ForecastData:
    """Forecast data structure"""
    date: str
    temp_max: float
    temp_min: float
    condition: WeatherCondition
    description: str
    precipitation_prob: int


class ASCIIArt:
    """ASCII art generator for weather visualization"""
    
    WEATHER_ART = {
        WeatherCondition.CLEAR: [
            r"     \   /     ",
            r"      .-.      ",
            r"   ― (   ) ―   ",
            r"      `-´      ",
            r"     /   \     ",
        ],
        WeatherCondition.CLOUDY: [
            r"      .--.     ",
            r"   .-(    ).   ",
            r"  (___.__)__)  ",
            r"               ",
            r"               ",
        ],
        WeatherCondition.RAINY: [
            r"      .--.     ",
            r"   .-(    ).   ",
            r"  (___.__)__)  ",
            r"   ´´´´´´´´´   ",
            r"    ´´´´´´´    ",
        ],
        WeatherCondition.SNOWY: [
            r"      .--.     ",
            r"   .-(    ).   ",
            r"  (___.__)__)  ",
            r"   * * * * *   ",
            r"  * * * * * *  ",
        ],
        WeatherCondition.STORMY: [
            r"      .--.     ",
            r"   .-(    ).   ",
            r"  (___.__)__)  ",
            r"   ⚡´´´´´⚡   ",
            r"    ´´´´´´´    ",
        ],
        WeatherCondition.FOGGY: [
            r"   _ - _ - _   ",
            r"    - _ - _    ",
            r"   _ - _ - _   ",
            r"    - _ - _    ",
            r"   _ - _ - _   ",
        ],
        WeatherCondition.WINDY: [
            r"   ~~ ~~ ~~    ",
            r"  ~~ ~~ ~~ ~~  ",
            r"   ~~ ~~ ~~    ",
            r"  ~~ ~~ ~~ ~~  ",
            r"   ~~ ~~ ~~    ",
        ],
        WeatherCondition.UNKNOWN: [
            r"      ???      ",
            r"    ???????    ",
            r"   ?????????   ",
            r"    ???????    ",
            r"      ???      ",
        ],
    }
    
    @classmethod
    def get_weather_art(cls, condition: WeatherCondition, colored: bool = True) -> str:
        """Get ASCII art for weather condition"""
        art_lines = cls.WEATHER_ART.get(condition, cls.WEATHER_ART[WeatherCondition.UNKNOWN])
        
        if colored:
            colors = {
                WeatherCondition.CLEAR: "\033[93m",      # Yellow
                WeatherCondition.CLOUDY: "\033[90m",     # Dark gray
                WeatherCondition.RAINY: "\033[94m",      # Blue
                WeatherCondition.SNOWY: "\033[97m",      # White
                WeatherCondition.STORMY: "\033[95m",     # Magenta
                WeatherCondition.FOGGY: "\033[37m",      # Light gray
                WeatherCondition.WINDY: "\033[96m",      # Cyan
                WeatherCondition.UNKNOWN: "\033[0m",     # Default
            }
            color = colors.get(condition, "\033[0m")
            reset = "\033[0m"
            return "\n".join(f"{color}{line}{reset}" for line in art_lines)
        return "\n".join(art_lines)
    
    @classmethod
    def get_temperature_bar(cls, temp: float, unit: str = "celsius") -> str:
        """Generate temperature bar visualization"""
        if unit == "fahrenheit":
            temp_c = (temp - 32) * 5 / 9
        else:
            temp_c = temp
        
        # Temperature scale: -20 to 45 Celsius
        min_temp, max_temp = -20, 45
        normalized = max(0, min(1, (temp_c - min_temp) / (max_temp - min_temp)))
        bar_length = 20
        filled = int(normalized * bar_length)
        
        # Color based on temperature
        if temp_c < 0:
            color = "\033[96m"  # Cyan - freezing
        elif temp_c < 10:
            color = "\033[94m"  # Blue - cold
        elif temp_c < 20:
            color = "\033[92m"  # Green - mild
        elif temp_c < 30:
            color = "\033[93m"  # Yellow - warm
        else:
            color = "\033[91m"  # Red - hot
        
        reset = "\033[0m"
        bar = f"[{color}{'█' * filled}{'░' * (bar_length - filled)}{reset}]"
        return bar


class WeatherAPI:
    """Weather API handler with multiple providers"""
    
    OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
    GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
    
    @staticmethod
    def _make_request(url: str, params: Dict[str, Any] = None, timeout: int = 10) -> Dict:
        """Make HTTP request with error handling"""
        if params:
            query = "&".join(f"{k}={v}" for k, v in params.items())
            url = f"{url}?{query}"
        
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "SkyPulse/1.0.0 (Terminal Weather CLI)",
                "Accept": "application/json",
            }
        )
        
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.URLError as e:
            raise ConnectionError(f"Network error: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON response: {e}")
    
    @classmethod
    def get_coordinates(cls, location: str) -> Tuple[float, float, str]:
        """Get coordinates for a location name"""
        try:
            data = cls._make_request(cls.GEOCODING_URL, {
                "name": location,
                "count": 1,
                "language": "en",
                "format": "json"
            })
            
            if not data.get("results"):
                raise ValueError(f"Location not found: {location}")
            
            result = data["results"][0]
            lat = result["latitude"]
            lon = result["longitude"]
            name = result.get("name", location)
            country = result.get("country", "")
            full_name = f"{name}, {country}" if country else name
            
            return lat, lon, full_name
        except Exception as e:
            raise ValueError(f"Geocoding failed: {e}")
    
    @classmethod
    def get_current_weather(cls, lat: float, lon: float) -> WeatherData:
        """Get current weather data"""
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,"
                       "precipitation,weather_code,cloud_cover,pressure_msl,wind_speed_10m,"
                       "wind_direction_10m",
            "daily": "sunrise,sunset,uv_index_max",
            "timezone": "auto",
            "forecast_days": 1
        }
        
        data = cls._make_request(cls.OPEN_METEO_URL, params)
        current = data.get("current", {})
        daily = data.get("daily", {})
        
        # Parse weather code
        weather_code = current.get("weather_code", 0)
        condition = cls._parse_weather_code(weather_code)
        
        # Get wind direction
        wind_dir = cls._degrees_to_direction(current.get("wind_direction_10m", 0))
        
        return WeatherData(
            location="",  # Will be set by caller
            temperature=current.get("temperature_2m", 0),
            feels_like=current.get("apparent_temperature", 0),
            humidity=current.get("relative_humidity_2m", 0),
            wind_speed=current.get("wind_speed_10m", 0),
            wind_direction=wind_dir,
            pressure=current.get("pressure_msl", 0),
            visibility=10.0,  # Not provided by Open-Meteo
            condition=condition,
            description=cls._get_weather_description(weather_code),
            uv_index=daily.get("uv_index_max", [0])[0] if daily.get("uv_index_max") else 0,
            precipitation=current.get("precipitation", 0),
            sunrise=daily.get("sunrise", [""])[0] if daily.get("sunrise") else "",
            sunset=daily.get("sunset", [""])[0] if daily.get("sunset") else "",
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    
    @classmethod
    def get_forecast(cls, lat: float, lon: float, days: int = 7) -> List[ForecastData]:
        """Get weather forecast"""
        params = {
            "latitude": lat,
            "longitude": lon,
            "daily": "weather_code,temperature_2m_max,temperature_2m_min,"
                    "precipitation_probability_max",
            "timezone": "auto",
            "forecast_days": days
        }
        
        data = cls._make_request(cls.OPEN_METEO_URL, params)
        daily = data.get("daily", {})
        
        forecasts = []
        dates = daily.get("time", [])
        for i, date in enumerate(dates):
            weather_code = daily.get("weather_code", [])[i] if i < len(daily.get("weather_code", [])) else 0
            forecasts.append(ForecastData(
                date=date,
                temp_max=daily.get("temperature_2m_max", [])[i] if i < len(daily.get("temperature_2m_max", [])) else 0,
                temp_min=daily.get("temperature_2m_min", [])[i] if i < len(daily.get("temperature_2m_min", [])) else 0,
                condition=cls._parse_weather_code(weather_code),
                description=cls._get_weather_description(weather_code),
                precipitation_prob=daily.get("precipitation_probability_max", [])[i] if i < len(daily.get("precipitation_probability_max", [])) else 0
            ))
        
        return forecasts
    
    @staticmethod
    def _parse_weather_code(code: int) -> WeatherCondition:
        """Parse WMO weather code to condition"""
        if code == 0:
            return WeatherCondition.CLEAR
        elif code in [1, 2, 3]:
            return WeatherCondition.CLOUDY
        elif code in [45, 48]:
            return WeatherCondition.FOGGY
        elif code in [51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82]:
            return WeatherCondition.RAINY
        elif code in [71, 73, 75, 77, 85, 86]:
            return WeatherCondition.SNOWY
        elif code in [95, 96, 99]:
            return WeatherCondition.STORMY
        else:
            return WeatherCondition.UNKNOWN
    
    @staticmethod
    def _get_weather_description(code: int) -> str:
        """Get weather description from code"""
        descriptions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Depositing rime fog",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Dense drizzle",
            56: "Light freezing drizzle",
            57: "Dense freezing drizzle",
            61: "Slight rain",
            63: "Moderate rain",
            65: "Heavy rain",
            66: "Light freezing rain",
            67: "Heavy freezing rain",
            71: "Slight snow",
            73: "Moderate snow",
            75: "Heavy snow",
            77: "Snow grains",
            80: "Slight rain showers",
            81: "Moderate rain showers",
            82: "Violent rain showers",
            85: "Slight snow showers",
            86: "Heavy snow showers",
            95: "Thunderstorm",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail",
        }
        return descriptions.get(code, "Unknown")
    
    @staticmethod
    def _degrees_to_direction(degrees: int) -> str:
        """Convert wind degrees to direction"""
        directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                     "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        index = int((degrees + 11.25) / 22.5) % 16
        return directions[index]


class LocationDetector:
    """Auto-detect user location"""
    
    IP_API_URL = "http://ip-api.com/json/"
    
    @classmethod
    def detect_location(cls) -> Tuple[float, float, str]:
        """Detect location by IP"""
        try:
            request = urllib.request.Request(
                cls.IP_API_URL,
                headers={"User-Agent": "SkyPulse/1.0.0"}
            )
            with urllib.request.urlopen(request, timeout=5) as response:
                data = json.loads(response.read().decode("utf-8"))
                
                if data.get("status") == "success":
                    lat = data.get("lat", 0)
                    lon = data.get("lon", 0)
                    city = data.get("city", "Unknown")
                    country = data.get("country", "")
                    location_name = f"{city}, {country}" if country else city
                    return lat, lon, location_name
        except Exception:
            pass
        
        # Default to Beijing if detection fails
        return 39.9042, 116.4074, "Beijing, China"


class ClothingAdvisor:
    """Smart clothing recommendation engine"""
    
    @staticmethod
    def get_recommendation(weather: WeatherData) -> List[str]:
        """Get clothing recommendations based on weather"""
        recommendations = []
        temp = weather.temperature
        condition = weather.condition
        
        # Temperature-based recommendations
        if temp < -10:
            recommendations.append("🧥 Heavy winter coat, thermal layers, gloves, hat, scarf")
        elif temp < 0:
            recommendations.append("🧥 Winter coat, warm layers, gloves, hat")
        elif temp < 10:
            recommendations.append("🧥 Warm jacket or coat, long sleeves")
        elif temp < 15:
            recommendations.append("🧥 Light jacket or sweater")
        elif temp < 20:
            recommendations.append("👕 Long sleeves or light sweater")
        elif temp < 25:
            recommendations.append("👕 T-shirt and light pants")
        elif temp < 30:
            recommendations.append("👕 Light, breathable clothing")
        else:
            recommendations.append("👕 Very light clothing, stay hydrated")
        
        # Condition-based recommendations
        if condition == WeatherCondition.RAINY:
            recommendations.append("☔ Bring an umbrella or wear a raincoat")
        elif condition == WeatherCondition.SNOWY:
            recommendations.append("❄️ Wear waterproof boots and warm socks")
        elif condition == WeatherCondition.STORMY:
            recommendations.append("⛈️ Stay indoors if possible, avoid open areas")
        elif condition == WeatherCondition.FOGGY:
            recommendations.append("🌫️ Use headlights when driving")
        elif condition == WeatherCondition.WINDY:
            recommendations.append("💨 Secure loose items, wear windbreaker")
        
        # UV-based recommendations
        if weather.uv_index >= 6:
            recommendations.append("🕶️ Wear sunglasses and apply sunscreen")
        elif weather.uv_index >= 3:
            recommendations.append("🕶️ Consider sunglasses for extended outdoor time")
        
        # Humidity-based recommendations
        if weather.humidity > 80:
            recommendations.append("💧 High humidity - stay hydrated")
        
        return recommendations


class AlertSystem:
    """Weather alert system"""
    
    @staticmethod
    def check_alerts(weather: WeatherData) -> List[str]:
        """Check for weather alerts"""
        alerts = []
        
        # Temperature alerts
        if weather.temperature > 35:
            alerts.append("🔥 EXTREME HEAT WARNING: Risk of heatstroke")
        elif weather.temperature < -15:
            alerts.append("🥶 EXTREME COLD WARNING: Risk of frostbite")
        
        # Wind alerts
        if weather.wind_speed > 50:
            alerts.append("💨 HIGH WIND WARNING: Secure loose objects")
        elif weather.wind_speed > 30:
            alerts.append("💨 WIND ADVISORY: Strong winds expected")
        
        # Precipitation alerts
        if weather.precipitation > 10:
            alerts.append("🌧️ HEAVY RAIN WARNING: Possible flooding")
        
        # UV alerts
        if weather.uv_index >= 8:
            alerts.append("☀️ UV WARNING: Very high UV index")
        
        # Condition alerts
        if weather.condition == WeatherCondition.STORMY:
            alerts.append("⛈️ STORM WARNING: Seek shelter immediately")
        
        return alerts


class SkyPulseCLI:
    """Main CLI application"""
    
    VERSION = "1.0.0"
    
    def __init__(self):
        self.parser = self._create_parser()
    
    def _create_parser(self) -> argparse.ArgumentParser:
        """Create argument parser"""
        parser = argparse.ArgumentParser(
            prog="skypulse",
            description="🌤️ SkyPulse - Lightweight Terminal Weather Intelligence Assistant",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  skypulse                    Show weather for auto-detected location
  skypulse Beijing            Show weather for Beijing
  skypulse --forecast         Show 7-day forecast
  skypulse --alert            Check weather alerts
  skypulse --clothing         Get clothing recommendations
  skypulse --json             Output in JSON format
            """
        )
        
        parser.add_argument(
            "location",
            nargs="?",
            help="Location name (city, country)"
        )
        
        parser.add_argument(
            "-f", "--forecast",
            action="store_true",
            help="Show weather forecast"
        )
        
        parser.add_argument(
            "-d", "--days",
            type=int,
            default=7,
            help="Number of forecast days (default: 7)"
        )
        
        parser.add_argument(
            "-a", "--alert",
            action="store_true",
            help="Show weather alerts"
        )
        
        parser.add_argument(
            "-c", "--clothing",
            action="store_true",
            help="Show clothing recommendations"
        )
        
        parser.add_argument(
            "-j", "--json",
            action="store_true",
            help="Output in JSON format"
        )
        
        parser.add_argument(
            "-u", "--units",
            choices=["celsius", "fahrenheit"],
            default="celsius",
            help="Temperature units (default: celsius)"
        )
        
        parser.add_argument(
            "--no-color",
            action="store_true",
            help="Disable colored output"
        )
        
        parser.add_argument(
            "-v", "--version",
            action="version",
            version=f"%(prog)s {self.VERSION}"
        )
        
        return parser
    
    def run(self, args: List[str] = None):
        """Run the CLI application"""
        parsed = self.parser.parse_args(args)
        
        try:
            # Get location
            if parsed.location:
                lat, lon, location_name = WeatherAPI.get_coordinates(parsed.location)
            else:
                lat, lon, location_name = LocationDetector.detect_location()
            
            # Get weather data
            weather = WeatherAPI.get_current_weather(lat, lon)
            weather.location = location_name
            
            # Output
            if parsed.json:
                self._output_json(weather)
            elif parsed.forecast:
                forecasts = WeatherAPI.get_forecast(lat, lon, parsed.days)
                self._display_forecast(weather, forecasts, parsed)
            elif parsed.alert:
                self._display_alerts(weather, parsed)
            elif parsed.clothing:
                self._display_clothing(weather, parsed)
            else:
                self._display_current(weather, parsed)
        
        except ValueError as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)
        except ConnectionError as e:
            print(f"❌ Network error: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"❌ Unexpected error: {e}", file=sys.stderr)
            sys.exit(1)
    
    def _display_current(self, weather: WeatherData, args):
        """Display current weather"""
        colored = not args.no_color
        
        # Header
        print("\n" + "=" * 50)
        print(f"  🌤️  SkyPulse Weather Report")
        print("=" * 50)
        
        # Location and time
        print(f"\n  📍 Location: {weather.location}")
        print(f"  🕐 Time: {weather.timestamp}")
        
        # ASCII art
        print("\n" + ASCIIArt.get_weather_art(weather.condition, colored))
        
        # Temperature
        temp_unit = "°C" if args.units == "celsius" else "°F"
        temp = weather.temperature if args.units == "celsius" else weather.temperature * 9/5 + 32
        feels = weather.feels_like if args.units == "celsius" else weather.feels_like * 9/5 + 32
        
        print(f"\n  🌡️  Temperature: {temp:.1f}{temp_unit}")
        print(f"     Feels like: {feels:.1f}{temp_unit}")
        print(f"     {ASCIIArt.get_temperature_bar(weather.temperature, args.units)}")
        
        # Condition
        print(f"\n  ☁️  Condition: {weather.description}")
        
        # Details
        print(f"\n  💨 Wind: {weather.wind_speed:.1f} km/h {weather.wind_direction}")
        print(f"  💧 Humidity: {weather.humidity}%")
        print(f"  📊 Pressure: {weather.pressure:.1f} hPa")
        print(f"  🌧️  Precipitation: {weather.precipitation:.1f} mm")
        print(f"  ☀️  UV Index: {weather.uv_index}")
        
        # Sun times
        if weather.sunrise:
            sunrise = weather.sunrise.split("T")[1] if "T" in weather.sunrise else weather.sunrise
            print(f"  🌅 Sunrise: {sunrise}")
        if weather.sunset:
            sunset = weather.sunset.split("T")[1] if "T" in weather.sunset else weather.sunset
            print(f"  🌇 Sunset: {sunset}")
        
        print("\n" + "=" * 50 + "\n")
    
    def _display_forecast(self, weather: WeatherData, forecasts: List[ForecastData], args):
        """Display weather forecast"""
        colored = not args.no_color
        temp_unit = "°C" if args.units == "celsius" else "°F"
        
        print("\n" + "=" * 60)
        print(f"  🌤️  SkyPulse {len(forecasts)}-Day Forecast for {weather.location}")
        print("=" * 60 + "\n")
        
        for forecast in forecasts:
            temp_max = forecast.temp_max if args.units == "celsius" else forecast.temp_max * 9/5 + 32
            temp_min = forecast.temp_min if args.units == "celsius" else forecast.temp_min * 9/5 + 32
            
            # Get mini weather icon
            icon = self._get_mini_icon(forecast.condition)
            
            print(f"  {forecast.date}: {icon} {forecast.description}")
            print(f"     ↑ {temp_max:.0f}{temp_unit}  ↓ {temp_min:.0f}{temp_unit}  🌧️ {forecast.precipitation_prob}%")
            print()
        
        print("=" * 60 + "\n")
    
    def _display_alerts(self, weather: WeatherData, args):
        """Display weather alerts"""
        alerts = AlertSystem.check_alerts(weather)
        
        print("\n" + "=" * 50)
        print(f"  ⚠️  Weather Alerts for {weather.location}")
        print("=" * 50 + "\n")
        
        if alerts:
            for alert in alerts:
                print(f"  {alert}")
        else:
            print("  ✅ No active weather alerts")
        
        print("\n" + "=" * 50 + "\n")
    
    def _display_clothing(self, weather: WeatherData, args):
        """Display clothing recommendations"""
        recommendations = ClothingAdvisor.get_recommendation(weather)
        
        print("\n" + "=" * 50)
        print(f"  👔 Clothing Recommendations for {weather.location}")
        print("=" * 50 + "\n")
        
        for rec in recommendations:
            print(f"  {rec}")
        
        print("\n" + "=" * 50 + "\n")
    
    def _output_json(self, weather: WeatherData):
        """Output weather data as JSON"""
        data = {
            "location": weather.location,
            "timestamp": weather.timestamp,
            "temperature": weather.temperature,
            "feels_like": weather.feels_like,
            "humidity": weather.humidity,
            "wind_speed": weather.wind_speed,
            "wind_direction": weather.wind_direction,
            "pressure": weather.pressure,
            "visibility": weather.visibility,
            "condition": weather.condition.value,
            "description": weather.description,
            "uv_index": weather.uv_index,
            "precipitation": weather.precipitation,
            "sunrise": weather.sunrise,
            "sunset": weather.sunset,
        }
        print(json.dumps(data, indent=2))
    
    @staticmethod
    def _get_mini_icon(condition: WeatherCondition) -> str:
        """Get mini weather icon"""
        icons = {
            WeatherCondition.CLEAR: "☀️",
            WeatherCondition.CLOUDY: "☁️",
            WeatherCondition.RAINY: "🌧️",
            WeatherCondition.SNOWY: "❄️",
            WeatherCondition.STORMY: "⛈️",
            WeatherCondition.FOGGY: "🌫️",
            WeatherCondition.WINDY: "💨",
            WeatherCondition.UNKNOWN: "❓",
        }
        return icons.get(condition, "❓")


def main():
    """Main entry point"""
    cli = SkyPulseCLI()
    cli.run()


if __name__ == "__main__":
    main()
