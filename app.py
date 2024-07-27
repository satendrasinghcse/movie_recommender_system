from flask import Flask, render_template, request
from src.component.recommend import recommend




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    movies_input = request.form['movies']
    # For simplicity, we are using a predefined list of movies
    movie_list = recommend(movies_input)
    
    return render_template('index.html', movie_list=movie_list)

if __name__ == '__main__':
    app.run(debug=True)
