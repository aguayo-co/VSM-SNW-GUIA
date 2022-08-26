//Only Globally required JS here
// A Slider is not a global requirement
import 'vite/modulepreload-polyfill';
import Alpine from 'alpinejs';

import headerMenuNavigation from "./components/headerMenu";
import renderSliders from "./components/swiperSlider";
import Dropdown from "./components/dropdown";
import showOrHideCookie from "./components/cookies";

// AlpineJS
window.Alpine = Alpine;

window.onload = function () {
    new headerMenuNavigation();
    renderSliders();
    showOrHideCookie();
    
    // Init dropdown
    const dropdownButtons = document.querySelectorAll(".js-dropdown-button");
    dropdownButtons.forEach(currentDropdown => {
        new Dropdown({
            element: currentDropdown
        });
    });
}

// Start AlpineJs
Alpine.start();
