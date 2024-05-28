def myadd(a):
    from textblob import TextBlob

    texts=a
    
    # 텍스트에 대한 감정 분석
    for text in texts:
        blob = TextBlob(text)
        sentiment = blob.sentiment
        print(f"Text: {text}")
        print(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")
        print("Sentiment: ", "Positive" if sentiment.polarity > 0 else "Negative" if sentiment.polarity < 0 else "Neutral")
        print()
