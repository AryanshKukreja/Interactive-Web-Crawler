from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crawl', methods=['POST'])
def crawl():
    if request.method == 'POST':
        url = request.form['url']
        result = scrape_website(url)
        return render_template('index.html', result=result)

def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Modify this part based on your crawling logic
        # Here, we're just printing the title of the page.
        title = soup.title.string if soup.title else 'No Title Found'
        return f'Title of the page: {title}'
    except Exception as e:
        return f'Error: {e}'

if __name__ == '__main__':
    app.run(debug=True)
