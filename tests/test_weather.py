import pytest
import sys
from weather.main import get_weather, run

def test_get_weather_valid_city():
    """Test that valid cities return the correct weather string."""
    assert get_weather("London") == "15°C and Cloudy"
    assert get_weather("Lisbon") == "25°C and Clear"

def test_get_weather_invalid_city():
    """Test that an unknown city returns the fallback message."""
    assert "not available" in get_weather("Mars")

def test_run_with_argument(capsys, monkeypatch):
    """Test the full CLI 'run' function with a city argument."""
    # Simulate: weather-check London
    monkeypatch.setattr(sys, "argv", ["weather-check", "London"])
    run()
    captured = capsys.readouterr()
    assert "City: London" in captured.out
    assert "15°C and Cloudy" in captured.out

def test_run_no_argument(capsys, monkeypatch):
    """Test the CLI 'run' function when no city is provided."""
    # Simulate: weather-check (with no args)
    monkeypatch.setattr(sys, "argv", ["weather-check"])
    run()
    captured = capsys.readouterr()
    assert "Usage: weather-check <city_name>" in captured.out
