import Swiper, { Navigation, Pagination } from 'swiper';

export default renderSliders => {
  sliderTestimonials();
  sliderHero();
  sliderProduct();
}

function sliderHero() {
  let el = document.querySelector(".js-slider-hero");

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

      // configure Swiper to use modules
      modules: [Navigation, Pagination],

      slidesPerView: 1,
      spaceBetween: 2,
      effect: "fade",

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
      },

      // Custom functions
      on: {
        init: function () {
          if (this.slides.length <= 1) {
            this.el.classList.add("is-not-slider-hero");
          }
        }
      }

    });
  }
}

function sliderTestimonials() {
  new Swiper('.js-slider-testimonial', {

    // configure Swiper to use modules
    modules: [Navigation, Pagination],

    initialSlide: 1,
    centeredSlides: true,
    slidesPerView: "auto",
    slideActiveClass: "is-testimonial-active",
    spaceBetween: 8,

    breakpoints: {
      768: {
        spaceBetween: 32,
      }
    },

    // Pagination bullets
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },

    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

  });
}

function sliderProduct() {
  new Swiper('.js-slider-product', {

    // configure Swiper to use modules
    modules: [Navigation, Pagination],

    slidesPerView: "auto",
    spaceBetween: 8,
    centeredSlides: true,

    breakpoints: {
      768: {
        centeredSlides: false,
        spaceBetween: 32,
        slidesPerView: 3,
      }
    },

    // Pagination bullets
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },

    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

  });
}
