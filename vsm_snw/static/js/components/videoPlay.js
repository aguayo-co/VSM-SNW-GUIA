export default class VideoPlay {
  constructor({ element }) {
    this.element = element;
    this.targetVideo = document.querySelector(".js-play-video-target");
    if (this.targetVideo) {
      this.btnToStopVideo = document.querySelector(".js-play-video-close");
      this.iframe = this.targetVideo.querySelector("iframe");
      this.videoSrc = this.iframe.getAttribute("src")
      this.classToOpenModal = "is-video-play";
      this.init();
    }
  }

  init() {
    this.clickEventToPlayVideo();
    this.clickEventoToStopVideo();
  }

  /**
   * Function that active the click in the overlay
   */
  clickEventToPlayVideo() {
    this.element.addEventListener("click", () => {
      this.targetVideo.classList.add(this.classToOpenModal);
      this.addAutoplayToSrc();
    });
  }

  clickEventoToStopVideo() {
    this.btnToStopVideo.addEventListener("click", () => {
      this.targetVideo.classList.remove(this.classToOpenModal);
      this.resetIframeSrc();
    })
  }

  /**
   * Add the autoplay param to the iframe
   */
  addAutoplayToSrc() {
    const symbol = this.iframe.src.indexOf("?") > -1 ? "&" : "?";
    this.iframe.setAttribute("src", this.iframe.src + symbol + "autoplay=1");
  }

  resetIframeSrc() {
    this.iframe.setAttribute("src", "");

    setTimeout(() => {
      this.iframe.setAttribute("src", this.videoSrc);
    }, 300)
  }

}
