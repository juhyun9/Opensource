from flask import render_template
import concept

def update_html_file(app):
    with app.app_context():
        updated_html_content = render_template(
            'home.html',
            paragraph=concept.paragraph,
            og_title=concept.og_title,
            og_description=concept.og_description,
            page_title=concept.page_title,
            heading=concept.heading
        )

    html_template_path = "./templates/home.html"
    with open(html_template_path, 'w', encoding='utf-8') as file:
        file.write(updated_html_content)
    print(f"Updated HTML content written to {html_template_path}")

def update_js_file():
    select_values = [0] * concept.select_values_count  # 지정된 개수만큼 0으로 채워진 리스트 생성
    js_file_path = "./static/start.js"
    with open(js_file_path, 'r', encoding='utf-8') as file:
        js_content = file.read()

    updated_js_content = js_content.replace(
        "const endPoint = 8;", f"const endPoint = {concept.end_point};"
    ).replace(
        "const select = [0];",
        f"const select = {select_values};"
    )

    with open(js_file_path, 'w', encoding='utf-8') as file:
        file.write(updated_js_content)
    print(f"Updated JS content written to {js_file_path}")

def main():
    from app import app  # Flask 애플리케이션 객체를 가져옴
    update_html_file(app)
    update_js_file()
    print("Files updated successfully")

if __name__ == "__main__":
    main()
