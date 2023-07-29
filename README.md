# Weather Forecast App

A web application that provides weather forecast information for different cities.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Weather Forecast App is a Django-based web application that allows users to view weather forecasts for their current location and other cities. It uses data from the OpenWeatherMap API and Web Scraping to provide accurate weather information.

The application consists of three main components:

1. **`weather.views`**: Handles the main weather view, displaying the weather for the user's current location and other cities added by the user. It also allows users to add and delete cities from their list.

2. **`registration.views`**: Manages user registration and login functionality. Users can register with a username and password or log in with their existing credentials.

3. **`forecast.views`**: Retrieves weather forecast data for a specific city using the OpenWeatherMap API. It provides detailed weather forecasts for the next 5 days.

## Features

- Display current weather information for the user's location.
- Allow users to add and delete cities to their weather forecast list.
- Provide detailed weather forecasts for up to 5 days for each city.
- User registration and login functionality.

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- Bootstrap
- OpenWeatherMap API

## Setup

1. Clone the repository to your local machine.
2. Install the required Python packages using `pip`:
3. Create a virtual environment (optional but recommended).
4. Obtain an API key from OpenWeatherMap by signing up on their website.
5. Replace the `api_key` variable in `forecast.views` and `weather.views` with your valid API key.

## Usage

1. Run the Django development server: **python manage.py runserver**
2. Open your web browser and go to `http://localhost:8000/` to access the Weather Forecast App.
3. The app will display the weather for your current location. You can add more cities to the list by using the "Add City" form.
4. Clicking on the "View Weather Details" link will show the detailed weather forecast for the selected city.
5. To log out, use the "Logout" button.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

