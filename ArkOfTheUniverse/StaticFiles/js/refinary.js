// Help Section

let refinaryHelp = document.querySelector("#refinary-help");
let refinaryHelpToggle = document.querySelector("#refinary-help-content");

refinaryHelp.onmouseover = function () {
  refinaryHelpOver();
};

refinaryHelp.onmouseout = function () {
  refinaryHelpOut();
};

function refinaryHelpOver() {
  refinaryHelpToggle.classList.remove("inactive");
  refinaryHelpToggle.classList.add("active");
  document.querySelector("#overlay").classList.remove("inactive");
  document.querySelector("#overlay").classList.add("active");
}
function refinaryHelpOut() {
  refinaryHelpToggle.classList.remove("active");
  refinaryHelpToggle.classList.add("inactive");
  document.querySelector("#overlay").classList.remove("active");
  document.querySelector("#overlay").classList.add("inactive");
}
