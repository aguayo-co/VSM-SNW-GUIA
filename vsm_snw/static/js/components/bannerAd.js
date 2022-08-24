function clickToScrollInToComponentSelected(event) {
  const sectionId = document.getElementById(event.target.dataset.idScrollTo);
  if (sectionId) {
    document.getElementById(event.target.dataset.idScrollTo).scrollIntoView()
  }
}

function hideBannerAd(event) {
  event.target.closest(".js-target-banner-ad").classList.add("u-hidden")
}
