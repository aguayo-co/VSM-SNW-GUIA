//Only Globally required JS here
// A Slider is not a global requirement
import 'vite/modulepreload-polyfill';
import Alpine from 'alpinejs';
import testModule from "./ejemplo";
// AlpineJS
window.Alpine = Alpine;

window.onload = function () {
    console.log("Prueba de Main");
    testModule();
}

// Start AlpineJs
Alpine.start();