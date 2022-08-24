//Only Globally required JS here
// A Slider is not a global requirement
import 'vite/modulepreload-polyfill';
import Alpine from 'alpinejs';

import headerMenuNavigation from "./components/headerMenu";
import renderSliders from "./components/swiperSlider";

// AlpineJS
window.Alpine = Alpine;

window.onload = function () {
    new headerMenuNavigation();
    renderSliders();
}

// Start AlpineJs
Alpine.start();
