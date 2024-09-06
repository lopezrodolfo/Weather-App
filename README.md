# Weather App

A simple Python application that fetches and displays current weather information for a given city.

## Author

Rodolfo Lopez

## Date

Summer 2024

## Features

- Retrieves real-time weather data from OpenWeatherMap API
- Displays temperature in Fahrenheit and weather description
- Uses environment variables for API key management

## Prerequisites

- Python 3.6+
- `requests` library
- `python-dotenv` library

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install requests python-dotenv
   ```
3. Create a `.env` file in the project root and add your OpenWeatherMap API key:
   ```
   API_KEY=your_api_key_here
   ```

## Usage

Run the script:

```python
   python main.py
```

Enter a city name when prompted to see the current weather information.

## Notes

I created this script to practice using the requests library and APIs.
