from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    title = "제목을 입력해주세요"
    paragraph = "<나만의 MBTI 사이트입니다!> 와 같은 한 줄 설명해주세요."
    return render_template('home.html', title=title, paragraph=paragraph)

@app.route('/update', methods=['POST'])
def update_content():
    title = "새로운 제목"
    paragraph = "새로운 내용입니다! <br> 새로운 텍스트로 시작해 주십시오."
    return render_template('home.html', title=title, paragraph=paragraph)


@app.route('/result', methods=['POST'])
def result():
    # 여기서 로직에 따라 결과 페이지를 결정합니다.
    # 예를 들어, 사용자의 응답을 바탕으로 점수를 계산하고 결과를 결정합니다.
    # 계산 로직 및 알고리즘 짜야 해요!
    user_input = request.form.get('user_input')
    score = int(user_input)

    if score == 0:
        result_page = 'result-0.html'
    elif score == 1:
        result_page = 'result-1.html'
    elif score == 2:
        result_page = 'result-2.html'
    elif score == 3:
        result_page = 'result-3.html'
    elif score == 4:
        result_page = 'result-5.html'
    elif score == 5:
        result_page = 'result-6.html'
    elif score == 6:
        result_page = 'result-7.html'
    elif score == 7:
        result_page = 'result-8.html'
    elif score == 8:
        result_page = 'result-9.html'
    else:
        result_page = 'result-10.html'

    return render_template(f'page/{result_page}')

if __name__ == '__main__':
    app.run(debug=True)
