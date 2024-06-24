from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "제주 올레길 테스트"
    paragraph = "누구나 쉽게 마음대로 만드는 유형테스트, 제주 올레길 유형테스트"
    return render_template('home.html', title=title, paragraph=paragraph)

if __name__ == '__main__':
    app.run(debug=True)
