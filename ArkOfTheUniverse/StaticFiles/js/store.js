// Menu Triggers
let menuShip = document.querySelector("#store-content-ship");
let menuConsumable = document.querySelector("#store-content-consumable");
let menuUpgrade = document.querySelector("#store-content-upgrade");
let menuResource = document.querySelector("#store-content-resource");

function openShips() {
  menuConsumable.classList.remove("active");
  menuUpgrade.classList.remove("active");
  menuResource.classList.remove("active");
  menuConsumable.classList.add("inactive");
  menuUpgrade.classList.add("inactive");
  menuResource.classList.add("inactive");

  menuShip.classList.remove("inactive");
  menuShip.classList.add("active");
}
function openConsumables() {
  menuShip.classList.remove("active");
  menuUpgrade.classList.remove("active");
  menuResource.classList.remove("active");
  menuShip.classList.add("inactive");
  menuUpgrade.classList.add("inactive");
  menuResource.classList.add("inactive");

  menuConsumable.classList.remove("inactive");
  menuConsumable.classList.add("active");
}
function openUpgrade() {
  menuShip.classList.remove("active");
  menuConsumable.classList.remove("active");
  menuResource.classList.remove("active");
  menuShip.classList.add("inactive");
  menuConsumable.classList.add("inactive");
  menuResource.classList.add("inactive");

  menuUpgrade.classList.remove("inactive");
  menuUpgrade.classList.add("active");
}
function openResource() {
  menuShip.classList.remove("active");
  menuUpgrade.classList.remove("active");
  menuConsumable.classList.remove("active");
  menuShip.classList.add("inactive");
  menuUpgrade.classList.add("inactive");
  menuConsumable.classList.add("inactive");

  menuResource.classList.remove("inactive");
  menuResource.classList.add("active");
}

// End Menu Triggers

// Confirm Buy

let confirmBuy = document.querySelectorAll("#confirm-buy");
let closeConfirmX = 0;

function closeConfirm() {
  switch (closeConfirmX) {
    case 0:
      confirmBuy[0].classList.remove("active");
      confirmBuy[0].classList.add("inactive");
    case 1:
      confirmBuy[1].classList.remove("active");
      confirmBuy[1].classList.add("inactive");
    case 2:
      confirmBuy[2].classList.remove("active");
      confirmBuy[2].classList.add("inactive");
    case 3:
      confirmBuy[3].classList.remove("active");
      confirmBuy[3].classList.add("inactive");
  }
}

// Confirm Buy Ships

function buyHangar() {
  confirmBuy[0].classList.add("active");
  confirmBuy[0].innerHTML =
    '<span>Confirm</span><button onclick="buyHangarConfirm()"> Yes </button><div class="divider"></div><button onclick="closeConfirm()"> NO </button>';
}

function buyShip() {
  confirmBuy[0].classList.add("active");
  confirmBuy[0].innerHTML =
    '<span>Confirm</span><button onclick="buyShipConfirm()"> Yes </button><div class="divider"></div><button onclick="closeConfirm()"> NO </button>';
}

// End Confirm Buy Ships

// Confirm Buy Consumables

function buyRepair(x) {
  confirmBuy[1].classList.add("active");
  confirmBuy[1].innerHTML = `<span>Confirm</span><button onclick="buyRepair${x}Confirm()"> Yes </button><div class="divider"></div><button onclick="closeConfirm()"> NO </button>`;
}

function buyFuel(x) {
  confirmBuy[1].classList.add("active");
  confirmBuy[1].innerHTML = `<span>Confirm</span><button onclick="buyFuel${x}Confirm()"> Yes </button><div class="divider"></div><button onclick="closeConfirm()"> NO </button>`;
}

function buyRadar(x) {
  confirmBuy[1].classList.add("active");
  confirmBuy[1].innerHTML = `<span>Confirm</span><button onclick="buyRadar${x}Confirm()"> Yes </button><div class="divider"></div><button onclick="closeConfirm()"> NO </button>`;
}

// End Confirm Buy Consumables

// Confirm Buy Upgrades

function buyUpgrade(x) {
  confirmBuy[2].classList.add("active");
  confirmBuy[2].innerHTML = `<span>Confirm</span><button onclick="buyUpgrade${x}Confirm()"> Yes </button><div class="divider"></div><button onclick="closeConfirm()"> NO </button>`;
}

// End Confirm Buy Upgrades

// End Confirm Buy

// SubNav Consumable

let subnavConsumableItems = document.querySelectorAll(".carousel-item");
let consumableRepair = document.querySelector("#consumableRepair");
let consumableFuel = document.querySelector("#consumableFuel");
let consumableRadar = document.querySelector("#consumableRadar");

function openConsumableRepair() {
  consumableFuel.classList.add("inactive");
  consumableFuel.classList.remove("active");
  consumableRadar.classList.add("inactive");
  consumableRadar.classList.remove("active");
  consumableRepair.classList.add("active");
  consumableRepair.classList.remove("inactive");
}
function openConsumableFuel() {
  consumableRepair.classList.add("inactive");
  consumableRepair.classList.remove("active");
  consumableRadar.classList.add("inactive");
  consumableRadar.classList.remove("active");
  consumableFuel.classList.add("active");
  consumableFuel.classList.remove("inactive");
}
function openConsumableRadar() {
  consumableRepair.classList.add("inactive");
  consumableRepair.classList.remove("active");
  consumableRadar.classList.add("active");
  consumableRadar.classList.remove("inactive");
  consumableFuel.classList.add("inactive");
  consumableFuel.classList.remove("active");
}

function subnavConsumableNext() {
  if (subnavConsumableItems[0].classList.contains("active")) {
    openConsumableFuel();
  } else if (subnavConsumableItems[1].classList.contains("active")) {
    openConsumableRadar();
  } else if (subnavConsumableItems[2].classList.contains("active")) {
    openConsumableRepair();
  }
}

function subnavConsumablePrev() {
  if (subnavConsumableItems[0].classList.contains("active")) {
    openConsumableRadar();
  } else if (subnavConsumableItems[1].classList.contains("active")) {
    openConsumableRepair();
  } else if (subnavConsumableItems[2].classList.contains("active")) {
    openConsumableFuel();
  }
}

// End SubNav Consumable

// SubNav Resource

let subnavResourceItems = document.querySelectorAll(".resource-item");
let resourceOre1 = document.querySelector("#resourceOre1");
let resourceOre2 = document.querySelector("#resourceOre2");
let resourceOre3 = document.querySelector("#resourceOre3");

function openResourceOre1() {
  resourceOre2.classList.add("inactive");
  resourceOre2.classList.remove("active");
  resourceOre3.classList.add("inactive");
  resourceOre3.classList.remove("active");
  resourceOre1.classList.add("active");
  resourceOre1.classList.remove("inactive");
}
function openResourceOre2() {
  resourceOre1.classList.add("inactive");
  resourceOre1.classList.remove("active");
  resourceOre3.classList.add("inactive");
  resourceOre3.classList.remove("active");
  resourceOre2.classList.add("active");
  resourceOre2.classList.remove("inactive");
}
function openResourceOre3() {
  resourceOre1.classList.add("inactive");
  resourceOre1.classList.remove("active");
  resourceOre3.classList.add("active");
  resourceOre3.classList.remove("inactive");
  resourceOre2.classList.add("inactive");
  resourceOre2.classList.remove("active");
}

function subnavResourceNext() {
  if (subnavResourceItems[0].classList.contains("active")) {
    openResourceOre2();
  } else if (subnavResourceItems[1].classList.contains("active")) {
    openResourceOre3();
  } else if (subnavResourceItems[2].classList.contains("active")) {
    openResourceOre1();
  }
}

function subnavResourcePrev() {
  if (subnavResourceItems[0].classList.contains("active")) {
    openResourceOre3();
  } else if (subnavResourceItems[1].classList.contains("active")) {
    openResourceOre1();
  } else if (subnavResourceItems[2].classList.contains("active")) {
    openResourceOre2();
  }
}
// 'ore1' - 'ore2' - 'ore3'
// End SubNav Resource
