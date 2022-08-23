import Swiper, { Navigation, Pagination } from 'swiper';

export default renderSliders => {
  sliderTestimonials();
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
