
News Website using API

This project is a news website built with Flask that dynamically loads news articles from various categories using the NewsAPI. It uses JavaScript to display images based on the month, making the site more visually interactive.

Features

Fetches news articles using the NewsAPI.

Categorizes news into topics like Technology, Sports, Health, etc.

Dynamically changes footer logo based on the current month using JavaScript.

Responsive design with dynamic loading of news.


Technology Stack

Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

API: NewsAPI (https://newsapi.org/)

Static Files: Images, CSS, and JavaScript stored in Flask's static folder


Setup

Prerequisites

Make sure you have the following installed:

Python 3.x

Flask


Installation

1. Clone this repository:

git clone https://github.com/eliezersunny/News-API-Flask-ALX.git
cd News-API-Flask-ALX


2. Install required dependencies:

pip install -r requirements.txt


3. Get your API key from NewsAPI, and replace the placeholder API_KEY in app.py with your key:

API_KEY = 'YOUR_NEWSAPI_KEY'


4. Run the Flask application:

python app.py


5. Open your browser and go to http://127.0.0.1:5000/ to see the website in action.



Usage

On visiting the homepage, you'll see news articles from different categories.

The footer logo will change depending on the current month (e.g., maxnews2.png for December and January).

Clicking on any news item will direct you to the full article via the NewsAPI link.


License

This project is open-source and available under the MIT License.



