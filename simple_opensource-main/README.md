# feeling
문장을 입력했을 때, 문장의 긍정, 부정을 가려주는 패키지입니다.

패키지를 다운로드받고, 문장 리스트에 문장들을 넣었을 때, 각 문장에 대한, 긍정도와 부정도를 보여줍니다.

입력: 문장 리스트 (**영어** important.. In English plz..)
출력: 
    Text: I love this product! It's amazing.
    Polarity: 0.6125, Subjectivity: 0.75
    Sentiment:  Positive

입력 example
    # 감정 분석을 수행할 텍스트
    
texts = [
    "I love this product! It's amazing.",
    "This is the worst experience I've ever had.",
    "I'm not sure how I feel about this.",
    "The service was okay, but could be improved.",
    "Absolutely fantastic! I will buy it again."
]
    
myadd(texts)