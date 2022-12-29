let a = document.querySelector(".menu-btn-hangar");

a.addEventListener("mousemove", (e) => {
  let { x, y } = a.getBoundingClientRect();
  a.style.setProperty("--x", e.clientX - x);
  a.style.setProperty("--y", e.clientY - y);
});

let b = document.querySelector(".menu-btn-refinary");

b.addEventListener("mousemove", (e) => {
  let { x, y } = b.getBoundingClientRect();
  b.style.setProperty("--x", e.clientX - x);
  b.style.setProperty("--y", e.clientY - y);
});

let c = document.querySelector(".menu-btn-store");

c.addEventListener("mousemove", (e) => {
  let { x, y } = c.getBoundingClientRect();
  c.style.setProperty("--x", e.clientX - x);
  c.style.setProperty("--y", e.clientY - y);
});
