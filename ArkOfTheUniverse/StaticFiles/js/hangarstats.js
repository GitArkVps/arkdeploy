// Ship Rank

let rank = document.querySelector("#rank");
let rankActive = 4; /* Calculate ship rank, example = 3 */
let rankInactive = 3; /* Calculate ship rank , example = 4 */

function shipGrade() {
  for (i = 0; i < rankActive; i++) {
    rank.innerHTML +=
      "<i class='fa-solid fa-star rank-star-active'></i> <br />";
  }
  for (h = 0; h < rankInactive; h++) {
    rank.innerHTML +=
      "<i class='fa-solid fa-star rank-star-unactive'></i> <br />";
  }
}

shipGrade();

// Ship Fuel

let progressBar = document.querySelector(".circular-progress-health");
let valueContainer = document.querySelector(".value-container-health");

let progressValue = 0;
let progressEndValue = 75;
let speed = 50;

let progress = setInterval(() => {
  progressValue++;
  valueContainer.textContent = `${progressValue}%`;
  progressBar.style.background = `conic-gradient(
          #ff18f6 ${progressValue * 3.6}deg,
          #efefef ${progressValue * 3.6}deg
      )`;
  if (progressValue == progressEndValue) {
    clearInterval(progress);
  }
}, speed);

let progressBarFuel = document.querySelector(".circular-progress-fuel");
let valueContainerFuel = document.querySelector(".value-container-fuel");

let progressValueFuel = 0;
let progressEndValueFuel = 33;
let speedfuel = 50;

let progressfuel = setInterval(() => {
  progressValueFuel++;
  valueContainerFuel.textContent = `${progressValueFuel}%`;
  progressBarFuel.style.background = `conic-gradient(
          #CBCF03 ${progressValueFuel * 3.6}deg,
          #efefef ${progressValueFuel * 3.6}deg
      )`;
  if (progressValueFuel == progressEndValueFuel) {
    clearInterval(progressfuel);
  }
}, speedfuel);
