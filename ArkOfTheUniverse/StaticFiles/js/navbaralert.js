let navBar = document.querySelector("#navbar-alert");
let navBarToggle = document.querySelector("#navbar-alert-toggle");

navBar.onmouseover = function () {
  navBarOver();
};
navBar.onmouseout = function () {
  navBarOut();
};

function navBarOver() {
  if (navBarToggle.classList.contains("unactive") == true) {
    navBarToggle.classList.remove("unactive");
    navBarToggle.classList.add("active");
  } else {
    navBarToggle.classList.remove("active");
    navBarToggle.classList.add("unactive");
  }
}

function navBarOut() {
  if (navBarToggle.classList.contains("active") == true) {
    navBarToggle.classList.remove("active");
    navBarToggle.classList.add("unactive");
  } else {
    navBarToggle.classList.remove("unactive");
    navBarToggle.classList.add("active");
  }
}
