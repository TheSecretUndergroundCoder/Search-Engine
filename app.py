from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy data for search
data = [
    {"title": "Flask Tutorial", "content": "Learn Flask for web development."},
    {"title": "Python Basics", "content": "Introduction to Python programming."},
    {"title": "HTML and CSS", "content": "Basics of web design with HTML and CSS."},
    {"title": "JavaScript Guide", "content": "Learn JavaScript for interactive web pages."},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        results = [item for item in data if query.lower() in item['title'].lower() or query.lower() in item['content'].lower()]
    else:
        results = []
    return render_template('results.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
