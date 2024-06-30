# main app file
from flask import Flask, render_template, request
from textblob import TextBlob

# Initialize Flask app
app = Flask(__name__)


# Route to render the home page with input form
@app.route('/')
def home():
    return render_template('index.html')


# Route to handle form submission and perform sentiment analysis
@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the input text from the form
    text = request.form['text']

    # Perform sentiment analysis using TextBlob
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity

    # Determine sentiment label
    if sentiment_score > 0:
        sentiment_label = 'Positive'
    elif sentiment_score < 0:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    # Render results template with sentiment analysis results
    return render_template('results.html', text=text, sentiment=sentiment_label)


if __name__ == '__main__':
    app.run(debug=True)
