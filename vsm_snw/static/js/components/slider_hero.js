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
      loop: false,
      navigation: {
        nextEl: nextEl,
        prevEl: prevEl,
        disabledClass: 'swiper-button-disabled'
      },
      pagination: {
        el: ".l-slide__footer",
        type: "custom",
        renderCustom: function (swiper, current, total) {
          const hero_pagination_texts = JSON.parse(document.getElementById("hero_pagination_texts").textContent)
          prevEl.children[1].textContent = hero_pagination_texts[current].prev
          nextEl.children[0].textContent = hero_pagination_texts[current].next
        }
      }
    });
  }
}

sliderHero(".js-slider-hero");
