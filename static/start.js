const main = document.querySelector("#main");
const qna = document.querySelector("#qna");
const result = document.querySelector("#result");

const endPoint = 8;
const select = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

function calResult() {
  function sanitizeArray(arr) {
    return arr.map((value) => {
      if (isNaN(value)) {
        console.log(`NaN detected, converting to 0`);
        return 0;
      }
      return value;
    });
  }

  let sanitizedSelect = sanitizeArray(select);
  console.log(select);
  var result = sanitizedSelect.indexOf(Math.max(...sanitizedSelect));
  console.log(result);
  return result;
}

function setResult() {
  let point = calResult();
  const resultName = document.querySelector(".resultname");
  console.log(point);
  resultName.innerHTML = infoList[point].name;

  var resultImg = document.createElement("img");
  const imgDiv = document.querySelector("#resultImg");
  var imgURL = "../static/img/image-" + point + ".png";
  resultImg.src = imgURL;
  resultImg.alt = point;
  resultImg.classList.add("img-fluid");
  imgDiv.appendChild(resultImg);

  const resultDesc = document.querySelector(".resultDesc");
  resultDesc.innerHTML = infoList[point].desc;
}

function goResult() {
  qna.style.WebkitAnimation = "fadeOut 1s";
  qna.style.animation = "fadeOut 1s";
  setTimeout(() => {
    result.style.WebkitAnimation = "fadeIn 1s";
    result.style.animation = "fadeIn 1s";
    setTimeout(() => {
      qna.style.display = "none";
      result.style.display = "block";
    }, 450);
  });
  setResult();
}

function addAnswer(answerText, qIdx, idx) {
  var a = document.querySelector(".answerBox");
  var answer = document.createElement("button");
  answer.classList.add("answerList");
  answer.classList.add("my-3");
  answer.classList.add("py-3");
  answer.classList.add("mx-auto");
  answer.classList.add("fadeIn");

  a.appendChild(answer);
  answer.innerHTML = answerText;

  answer.addEventListener(
    "click",
    function () {
      var children = document.querySelectorAll(".answerList");
      for (let i = 0; i < children.length; i++) {
        children[i].disabled = true;
        children[i].style.WebkitAnimation = "fadeOut 0.5s";
        children[i].style.animation = "fadeOut 0.5s";
      }
      setTimeout(() => {
        var target = qnaList[qIdx].a[idx].type;
        for (let i = 0; i < target.length; i++) {
          select[target[i]] += 1;
        }

        for (let i = 0; i < children.length; i++) {
          children[i].style.display = "none";
        }
        goNext(++qIdx);
      }, 450);
    },
    false
  );
}

function goNext(qIdx) {
  if (qIdx === endPoint) {
    goResult();
    return;
  }

  var q = document.querySelector(".qBox");
  q.innerHTML = qnaList[qIdx].q;
  for (let i in qnaList[qIdx].a) {
    addAnswer(qnaList[qIdx].a[i].answer, qIdx, i);
  }
  var status = document.querySelector(".statusBar");
  status.style.width = (100 / endPoint) * (qIdx + 1) + "%";
}

function begin() {
  main.style.WebkitAnimation = "fadeOut 1s";
  main.style.animation = "fadeOut 1s";
  setTimeout(() => {
    qna.style.WebkitAnimation = "fadeIn 1s";
    qna.style.animation = "fadeIn 1s";
    setTimeout(() => {
      main.style.display = "none";
      qna.style.display = "block";
    }, 450);
    let qIdx = 0;
    goNext(qIdx);
  }, 450);
}

async function fetchData() {
  try {
    let response = await fetch(
      "https://every-type-test-99a8ee6461c8.herokuapp.com/"
    );
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Fetch error:", error);
  }
}

fetchData();
