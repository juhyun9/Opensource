# 2024 Opensource 
> 제주대학교
Team 펠롱즈(김주현, 김소연, 곽예본)

### 사용 기술
- Front-end: React Hook, Styled Components
- Back-end: Django, GCP, mySQL

### 프로젝트 소개

 <유형 테스트 틀 개발>
초보 개발자도, 개발 입문자도, 또는 개발을 이용할 마음이 큰 마케터도! 
누구나 유형 테스트 웹서비스를 쉽게 개발할 수 있도록, 라이브러리를 만들어 배포하려 합니다.

더욱 풍부하고, 다양한 컨텐츠가 세상에 많아지길 바라며!

### 참고문헌
1. 숙명여대 Team Gitribute(권은지, 남수연, 서희, 유지연)의 '2021 DSC KR Hackathon: ❄️눈송이 유형 테스트❄️'
2. 판다코딩(nani6765)의 MyMBTI 프로젝트

### 실행 방법
1. 프로젝트 다운받기 (git clone https://github.com/juhyun9/Opensource)
2. app.py파일로 이동
3. 플라스크 설치 (pip install flask)
4. app.py 파일 실행
5. 로컬 링크로 이동


### 변형 방법
1. 컨셉 변경 파일 바꿔주세요!(파일 위치)
   - #아래의 "" 큰따옴표 안을 원하는 컨셉으로 고쳐주세요.
   - og_title = "테스트 제목을 적어주세요"
   - og_description = "테스트에 대한 설명을 적어주세요(메타 검색용)"
   - page_title = "서비스 페이지 제목을 적어주세요"
   - heading = "가장 상단에 보일 문구를 적어주세요"
   - paragraph = "서비스를 안내하는 문구를 적어주세요!"
   - end_point = 8 #질문 개수
   - select_values_count = 4  # 유형 개수
3. data.js 내의 오브젝트 타입의 데이터 파일을 원하는 형태의 파일로 바꿔주세요! (./static/data.js)
   - const infoList : 결과에 해당하는 유형을 순서대로 이름과 설명 적기
   - const qnaList : 질문 및 답변 작성, 답변 및 type에는 해당 답변에 연결되는 유형 번호 적기.
4. 이미지를 바꿔주세요!
   - 이미지 제목은 아래의 규칙을 무조건 따라야 합니다!
     1. main.png, share.png, favicon.ico 이름 유지하기
     2. 유형 개수만큼의 이미지올리기
     3. 제목 = image-0.png -> 가운데 숫자만 바뀌게
     4. data.js의 infoList의 순서에 맞게 넘버 부여하기
