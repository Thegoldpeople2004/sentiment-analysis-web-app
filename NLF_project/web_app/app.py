from flask import Flask, request, render_template
from sentiment_analysis import predict_sentiment

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    if request.method == 'POST':
        user_text = request.form['user_text']
        sentiment = predict_sentiment(user_text)
    return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)