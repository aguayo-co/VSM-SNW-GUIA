import Swiper from 'https://cdn.jsdelivr.net/npm/swiper@8/swiper-bundle.esm.browser.min.js'

function sliderHero(element) {
  let el = document.querySelector(element);

  if (el) {
    var nextEl;
    var prevEl;
    var wrapper = el.closest(".js-slide-wrapper");

    if (wrapper) {
      nextEl = wrapper.querySelector(".swiper-button-next");
      prevEl = wrapper.querySelector(".swiper-button-prev");
    } else {
      nextEl = this.element.querySelector(".swiper-button-next");
      prevEl = this.element.querySelector(".swiper-button-prev");
    }

    new Swiper(el, {
      slidesPerView: 1,
      spaceBetween: 2,
      speed: 900,
      autoHeight: true,
      loop: true,
  
      
      navigation: {
        nextEl: nextEl,
        prevEl: prevEl,
      },
    });
  }
}

sliderHero(".js-slider-hero");
