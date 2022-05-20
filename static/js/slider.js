window.onload = function () {
  slideMin();
  slideMax();
}

const sliderMin = document.getElementById("slider-1");
const sliderMax = document.getElementById("slider-2");
const displayValMin = document.getElementById("min-mag-val");
const displayValMax = document.getElementById("max-mag-val");
const minGap = 0.5;
const sliderTrack = document.querySelector(".slider-track");
const sliderMaxValue = document.getElementById("slider-1").max;

function slideMin() {
  if (parseFloat(sliderMax.value) - parseFloat(sliderMin.value) <= minGap) {
    sliderMin.value = parseFloat(sliderMax.value) - minGap;
  }
  displayValMin.textContent = sliderMin.value;
  displayValMin.style.left = `${(Math.abs(parseFloat(sliderMin.value) + 1) / 11.46) * 100}%`

  fillColor();
}

function slideMax() {
  if (parseFloat(sliderMax.value) - parseFloat(sliderMin.value) <= minGap) {
    sliderMax.value = parseFloat(sliderMin.value) + minGap;
  }
  displayValMax.textContent = sliderMax.value;
  displayValMax.style.left = `${(Math.abs(parseFloat(sliderMax.value) + 1) / 11.46) * 100}%`
  fillColor();
}

function fillColor() {
  percent1 = (Math.abs(parseFloat(sliderMin.value) + 1) / 11) * 100;
  percent2 = (Math.abs(parseFloat(sliderMax.value) + 1) / 11) * 100;
  sliderTrack.style.background = `linear-gradient(to right,
    #dadae5 ${percent1}%,
    #3264fe ${percent1}%,

    #3264fe ${percent2}%,
    #dadae5 ${percent2}%)`;
}