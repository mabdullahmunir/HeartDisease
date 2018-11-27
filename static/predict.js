function predict() {
  const age = $('#age').val();
  const sex = $('#sex').val();
  const chest = $('#chest').val();
  const bpressure = $('#bpressure').val();
  const cholesterol = $('#cholesterol').val();
  const bloodSugar = $('#blood_sugar').val();
  const ecg = $('#ecg').val();
  const maxHeart = $('#max_heart').val();
  const angina = $('#angina').val();
  const stDepression = $('#st_depression').val();
  const peakSt = $('#peak_st').val();
  const cVessel = $('#c_vessel').val();
  const thal = $('#thal').val();

  const param = {
    age,
    sex,
    chest,
    bpressure,
    cholesterol,
    bloodSugar,
    ecg,
    maxHeart,
    angina,
    stDepression,
    peakSt,
    cVessel,
    thal,
  };

  return param;
}
