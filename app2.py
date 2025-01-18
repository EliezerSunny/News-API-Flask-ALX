from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Replace with your NewsAPI key
API_KEY = 'NewsAPI_Key'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

# Categories to fetch
CATEGORIES = ['today', 'technology', 'sports', 'entertainment', 'world', 'health']

# Function to fetch news for a category
def fetch_news(category, page_size=5, page=1):
    params = {
        'apiKey': API_KEY,
        'language': 'en',  # English news only
        'pageSize': page_size,  # Number of articles to fetch
        'page': page        # Pagination
    }
    if category != 'today':  # Fetch global news for "Today"
        params['category'] = category

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return [
            {
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("url"),
                "image": article.get("urlToImage"),
            }
            for article in data.get("articles", [])
        ]
    return []

@app.route('/')
def index():
    news_data = {category: fetch_news(category, page_size=5) for category in CATEGORIES}
    return render_template('index.html', news_data=news_data)

@app.route('/load_more/<category>/<int:page>', methods=['GET'])
def load_more(category, page):
    articles = fetch_news(category, page_size=2, page=page)
    return jsonify(articles)


@app.route('/news/<int:news_id>/<category>')
def news_details(news_id, category):
    news_list = fetch_news(category)
    if 0 <= news_id < len(news_list):
        article = news_list[news_id]
        return render_template('news_details.html', article=article)
    return "News not found", 404



@app.route('/trending')
def trending():
    trending_news = fetch_news('technology')  # You can adjust category or filter
    return render_template('trending.html', news_list=trending_news)

@app.route('/about_us')
def about_us():
    technology_news = fetch_news('technology')
    return render_template('about_us.html', news_list=technology_news)


@app.route('/eliazer')
def eliazer():
    today_news = fetch_news('today')
    return render_template('eliazer.html', news_list=today_news)

@app.route('/contact_us')
def contact_us():
    sports_news = fetch_news('sports')
    return render_template('contact_us.html', news_list=sports_news)

@app.route('/search')
def search():
    sports_news = fetch_news('sports')
    # Add more logic here if needed
    return sports_news


@app.route('/today')
def today():
    today_news = fetch_news('today')
    return render_template('today.html', news_list=today_news)




if __name__ == '__main__':
    app.run(debug=True)
