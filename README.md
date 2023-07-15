# Weather App

Weather App is a Django web application that displays weather information for different cities. It uses web scraping to fetch weather data from Google and stores the city information in a PostgreSQL database.

## Features

- Display weather information for the current location based on IP geolocation.
- Add and delete cities to track their weather information.
- Fetch weather data from Google using web scraping.
- Store city information in a PostgreSQL database.
- Responsive UI design using Bulma CSS framework.
- User Autherntication
- Register and Login

## Prerequisites

Before running the application, ensure that you have the following installed:

- Python: Install Python from the official website: https://www.python.org/downloads/
- Django: Install Django using pip: `pip install django`
- BeautifulSoup: Install BeautifulSoup using pip: `pip install beautifulsoup4`
- Requests: Install Requests using pip: `pip install requests`
- PostgreSQL: Install PostgreSQL from the official website: https://www.postgresql.org/download/

## Getting Started

1. Clone the repository to your local machine

2. Navigate to the app directory

3. Install the dependencies:
    pip install -r requirements.txt
4. Set up the PostgreSQL database:
- Create a new database in PostgreSQL for the project.
- Update the DATABASES configuration in the settings.py file with your database credentials.
5. Apply the database migrations:
  python manage.py migrate
6. Start the Django development server:
  python manage.py runserver
7. Open a web browser and visit http://localhost:8000 to access the Weather App.

## File Structure
The project contains the following files and directories:

- `weather/`: The main Django application directory.
- `models.py`: Defines the City model for storing city information in the database.
- `forms.py`: Contains the CityForm and DeleteCityForm for handling city-related forms.
- `views.py`: Defines the view functions for rendering templates and processing form submissions.
- `templates/`: Directory for storing HTML templates.
- `weather/`: Directory for weather app templates.
- `index.html`: The main template for displaying the weather information.
- `add_city.html`: Template for adding a city.
- `delete_city.html`: Template for deleting a city.
- `manage.py`: The Django management script for running the development server and executing management commands.

##Technologies Used
- Django: A high-level Python web framework for building web applications.
- BeautifulSoup: A Python library for web scraping and parsing HTML and XML.
- Requests: A Python library for making HTTP requests.
- PostgreSQL: A powerful, open-source relational database system.
- Bulma: A CSS framework for building responsive and modern web interfaces.
##License
This project is licensed under the MIT License. You can find the license information in the LICENSE file.

##Acknowledgments
This project is based on a example that demonstrates the implementation of a weather app using Django and web scraping.
Feel free to modify and enhance the project according to your requirements. Happy coding!
