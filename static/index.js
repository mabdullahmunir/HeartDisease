function predict() {
  let age = document.getElementById("age").value;
  let sex = document.getElementById("sex").value;
  let chest = document.getElementById("chest").value;
  let bpressure = document.getElementById("bpressure").value;
  let cholesterol = document.getElementById("cholesterol").value;
  let blood_sugar = document.getElementById("blood_sugar").value;
  let ecg = document.getElementById("ecg").value;
  let max_heart = document.getElementById("max_heart").value;
  let angina = document.getElementById("angina").value;
  let st_depression = document.getElementById("st_depression").value;
  let peak_st = document.getElementById("peak_st").value;
  let c_vessel = document.getElementById("c_vessel").value;
  let thal = document.getElementById("thal").value;

  var param = {
    "age" : age,
    "sex" : sex,
    "chest" : chest,
    "bpressure" : bpressure,
    "cholesterol" : cholesterol,
    "blood_sugar" : blood_sugar,
    "ecg" : ecg,
    "max_heart" : max_heart,
    "angina" : angina,
    "st_depression" : st_depression,
    "peak_st" : peak_st,
    "c_vessel" : c_vessel,
    "thal" : thal,
  }

  var requestBody = JSON.stringify(param);

  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", "../app.py", true);
  xhttp.setRequestHeader("Content-type","application/json");
  xhttp.send(requestBody);

  xhttp.onreadystatechange = function(){
    createResultContainer(JSON.parse(this.responseText));
  }
}

function createResultContainer(data){
  var dataContainer = document.createElement("div");
  var dataText = document.createElement("span");
  var dataResult = document.createElement("h2");
  var resultExplain = document.createElement("div");

  dataContainer.classlist.add("data-container");
  dataText.classlist.add("data-text");
  dataResult.classlist.add("data-result");
  resultExplain.classlist.add("result-explain");

  dataText.textContent = "Hasil dari prediksi adalah : ";
  dataResult.textContent = data['diagnosis'];
  if(data['diagnosis'] == 0){
    resultExplain.textContent = "absence";
  } else {
    resultExplain.textContent = "presence";

  }

}