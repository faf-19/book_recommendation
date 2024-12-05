from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['BookComass']
collection = db['books']

@app.route('/', methods=['GET', 'POST'])
def index():
    genres = collection.distinct('genre')  # Get unique genres from the database
    recommended_books = []

    if request.method == 'POST':
        selected_genres = request.form.getlist('genres')  # Get list of selected genres
        if selected_genres:
            recommended_books = list(collection.find({'genre': {'$in': selected_genres}}))  
    return render_template('index.html', genres=genres, recommended_books=recommended_books)
if __name__ == '__main__':
    app.run(debug=True)