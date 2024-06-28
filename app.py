from flask import Flask, render_template, request, redirect, url_for
import file_changer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/update')
def update_files_from_concept():
    # `concept.py` 파일의 내용을 기반으로 HTML 및 JavaScript 파일 업데이트
    file_changer.update_html_file(app)
    file_changer.update_js_file()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
