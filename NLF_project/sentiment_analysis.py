from transformers import pipeline

# 加载情感分析模型
sentiment_pipeline = pipeline('sentiment-analysis')

def predict_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result['label']

# 测试函数
if __name__ == "__main__":
    test_texts = [
        "I love this movie, it was fantastic!",
        "This movie was terrible, I hated it.",
        "The new phone has amazing features but the battery life is too short.",
        "I had a wonderful experience at the restaurant, the food was delicious.",
        "The recent news is very concerning and upsetting."
    ]

    for text in test_texts:
        sentiment = predict_sentiment(text)
        print(f'Text: {text}\nSentiment: {sentiment}\n')