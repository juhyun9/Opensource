from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "제목을 입력해주세요"
    paragraph = "<나만의 MBTI 사이트입니다!> 와 같은 한 줄 설명해주세요."
    return render_template('home.html', title=title, paragraph=paragraph)

if __name__ == '__main__':
    app.run(debug=True)
