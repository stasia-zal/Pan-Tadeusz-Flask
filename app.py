from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<book>')
def show_book(book):
    return render_template(f"{book}.html")

# Run the application
if __name__ == '__main__':
    app.run()