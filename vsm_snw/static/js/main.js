//Only Globally required JS here
// A Slider is not a global requirement
import 'vite/modulepreload-polyfill';
import Alpine from 'alpinejs';
import headerMenuNavigation from "./headerMenu";
// AlpineJS
window.Alpine = Alpine;

window.onload = function () {
    new headerMenuNavigation();
}

// Start AlpineJs
Alpine.start();