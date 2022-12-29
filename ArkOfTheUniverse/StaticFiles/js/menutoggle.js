function toggleMenu() {
  let menutoggle = document.querySelector("#menutoggle");

  if (menutoggle.classList.contains("active")) {
    menutoggle.classList.remove("active");
    document.body.style.overflow = "auto";
    document.querySelector(".toggle-button").style.display = "block";
  } else {
    menutoggle.classList.add("active");
    document.body.style.overflow = "hidden";
    document.querySelector(".toggle-button").style.display = "none";
  }
}
