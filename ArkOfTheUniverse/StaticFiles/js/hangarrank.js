// Items Stats

let itemSection = document.querySelectorAll(".item-box-section");
let item1 = document.querySelector("#item-1");
let item2 = document.querySelector("#item-2");
let item3 = document.querySelector("#item-3");
let item4 = document.querySelector("#item-4");
let item5 = document.querySelector("#item-5");

// Mouseover Utilities

item1.onmouseover = function () {
  itemSection[0].classList.remove("inactive");
  itemSection[1].classList.remove("active");
  itemSection[2].classList.remove("active");
  itemSection[3].classList.remove("active");
  itemSection[4].classList.remove("active");
  itemSection[0].classList.add("active");
  itemSection[1].classList.add("inactive");
  itemSection[2].classList.add("inactive");
  itemSection[3].classList.add("inactive");
  itemSection[4].classList.add("inactive");
};

item2.onmouseover = function () {
  itemSection[1].classList.remove("inactive");
  itemSection[0].classList.remove("active");
  itemSection[2].classList.remove("active");
  itemSection[3].classList.remove("active");
  itemSection[4].classList.remove("active");
  itemSection[1].classList.add("active");
  itemSection[0].classList.add("inactive");
  itemSection[2].classList.add("inactive");
  itemSection[3].classList.add("inactive");
  itemSection[4].classList.add("inactive");
};

item3.onmouseover = function () {
  itemSection[2].classList.remove("inactive");
  itemSection[0].classList.remove("active");
  itemSection[1].classList.remove("active");
  itemSection[3].classList.remove("active");
  itemSection[4].classList.remove("active");
  itemSection[2].classList.add("active");
  itemSection[0].classList.add("inactive");
  itemSection[1].classList.add("inactive");
  itemSection[3].classList.add("inactive");
  itemSection[4].classList.add("inactive");
};

item4.onmouseover = function () {
  itemSection[3].classList.remove("inactive");
  itemSection[0].classList.remove("active");
  itemSection[1].classList.remove("active");
  itemSection[2].classList.remove("active");
  itemSection[4].classList.remove("active");
  itemSection[3].classList.add("active");
  itemSection[0].classList.add("inactive");
  itemSection[1].classList.add("inactive");
  itemSection[2].classList.add("inactive");
  itemSection[4].classList.add("inactive");
};

item5.onmouseover = function () {
  itemSection[4].classList.remove("inactive");
  itemSection[0].classList.remove("active");
  itemSection[1].classList.remove("active");
  itemSection[2].classList.remove("active");
  itemSection[3].classList.remove("active");
  itemSection[4].classList.add("active");
  itemSection[0].classList.add("inactive");
  itemSection[1].classList.add("inactive");
  itemSection[2].classList.add("inactive");
  itemSection[3].classList.add("inactive");
};
