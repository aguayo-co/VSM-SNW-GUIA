//Only Globally required JS here
// A Slider is not a global requirement
import 'vite/modulepreload-polyfill';
import Alpine from 'alpinejs';

import headerMenuNavigation from "./components/headerMenu";
import renderSliders from "./components/swiperSlider";
import Dropdown from "./components/dropdown";
import showOrHideCookie from "./components/cookies";
import CounterTime from "./components/counterTime";
import VideoPlay from "./components/videoPlay";
import initFilters, { toggleCounterOfFilter, removeChipIntoClick, clearFilters, goToPage, orderElements } from "./components/filter";

// AlpineJS
window.Alpine = Alpine;

window.onload = function () {
  new headerMenuNavigation();
  renderSliders();
  showOrHideCookie();

  // Init counter time
  const counterTimeTargets = document.querySelectorAll(".js-counter-target");
  counterTimeTargets.forEach(currentCounter => {
    new CounterTime({
      element: currentCounter
    });
  });

  // Init dropdown
  const dropdownButtons = document.querySelectorAll(".js-dropdown-button");
  dropdownButtons.forEach(currentDropdown => {
    new Dropdown({
      element: currentDropdown
    });
  });

  // Init videoPlay
  const targetVideoPlay = document.querySelectorAll(".js-play-video-btn");
  targetVideoPlay.forEach((item) => {
    new VideoPlay({
      element: item,
    });
  });

  initFilters()

  window.toggleCounterOfFilter = function (e) {
    toggleCounterOfFilter(e)
  }

  window.removeChipIntoClick = function (e) {
    removeChipIntoClick(e)
  }

  // Paginator
  window.goToPage = function (e) {
    goToPage(e);
  }

  // Order by
  window.orderElements = function (e) {
    orderElements(e);
  }

  window.clearFilters = function () {
    clearFilters()
  }
}

// Start AlpineJs
Alpine.start();
