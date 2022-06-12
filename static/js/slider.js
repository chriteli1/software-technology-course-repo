window.onload = function () {
  slideOne();
  slideTwo();
}

let sliderOne = document.getElementById("slider-1");
let sliderTwo = document.getElementById("slider-2");
let displayValOne = document.getElementById("range1");
let displayValTwo = document.getElementById("range2");
let minGap = 0.5;
let sliderTrack = document.querySelector(".slider-track");
let sliderMaxValue = document.getElementById("slider-1").max;

let test = 11

function slideOne() {
  if (parseFloat(sliderTwo.value) - parseFloat(sliderOne.value) <= minGap) {
    sliderOne.value = parseFloat(sliderTwo.value) - minGap;
  }
  displayValOne.textContent = sliderOne.value;
  fillColor();
}
function slideTwo() {
  if (parseFloat(sliderTwo.value) - parseFloat(sliderOne.value) <= minGap) {
    sliderTwo.value = parseFloat(sliderOne.value) + minGap;
  }
  displayValTwo.textContent = sliderTwo.value;
  fillColor();
}
function fillColor() {
  percent1 = (Math.abs(parseFloat(sliderOne.value) ) / 10) * 100;
  percent2 = (Math.abs(parseFloat(sliderTwo.value) ) / 10) * 100;
  sliderTrack.style.background = `linear-gradient(to right,
    #dadae5 ${percent1}%,
    #ede23a ${percent1}%,

    #ede23a ${percent2}%,
    #dadae5 ${percent2}%)`;
}