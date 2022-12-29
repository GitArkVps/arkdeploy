function sidebarToggle() {
  let xtoggle = document.querySelector("#sidebar-toggle");
  let ysidebar = document.querySelector("#sidebar");
  let zcontent = document.querySelector(".content-sidebar");

  if (xtoggle.classList.contains("active") === true) {
    xtoggle.classList.remove("active");
    xtoggle.classList.add("unactive");
    ysidebar.classList.add("unactive");
    ysidebar.classList.remove("active");
  } else {
    xtoggle.classList.remove("unactive");
    xtoggle.classList.add("active");
    ysidebar.classList.remove("unactive");
    ysidebar.classList.add("active");
  }

  if (xtoggle.classList.contains("active") === true) {
    /* Mostrar Foto Profile + Nome + Chat*/
    zcontent.innerHTML =
      '<div class="d-flex flex-column"><div class="d-flex flex-row justify-content-around align-items-center"><img class=" profile" src="../../includes/img/logo-br.png" alt=""><span class="username text-light" id="username">Username</span></div><div class="chat"><div class="chat-online col-100">Online (0)</div><div class="chat-offline col-100">Offline (0)</div></div></div>';
  } else {
    zcontent.innerHTML =
      "<img class=' profile' src='../../includes/img/logo-br.png' alt=''>";
  }
}
