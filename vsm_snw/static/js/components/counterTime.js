export default class CounterTime {
  constructor({ element }) {

    this.element = element
    // formato fecha: mm/dd/yyyy
    this.dateTimeTarget = this.element.querySelector(".js-counter-datetime").getAttribute("datetime")
    this.dateTarget = new Date(`${this.dateTimeTarget}`);

    this.hours = this.element.querySelector(".js-counter-hours");
    this.minutes = this.element.querySelector(".js-counter-minutes");
    this.seconds = this.element.querySelector(".js-counter-seconds");

    this.milisecondsOfSecond = 1000;
    this.milisecondsOfMinute = this.milisecondsOfSecond * 60;
    this.milisecondsOfHour = this.milisecondsOfMinute * 60;
    this.milisecondsOfDay = this.milisecondsOfHour * 24;

    this.duration = 0;
    this.remaining_days = 0;
    this.remaining_hours = 0;
    this.remaining_minutes = 0;
    this.remaining_seconds = 0;

    this.timerTarget = this.element.querySelector(".js-counter-timer");
    this.callToAction = this.element.querySelector(".js-counter-callto");

    this.init();
  }

  init() {

    const intervalTimer = setInterval(() => {
      this.updateCountdown()

      if (this.hours) {
        if (this.hours.innerHTML == "00" && this.minutes.innerHTML == "00" && this.seconds.innerHTML == "00") {
          clearInterval(intervalTimer);
        }
      }
    }, this.milisecondsOfSecond);

  }

  updateCountdown() {
    const now = new Date();

    this.duration = this.dateTarget - now;

    this.remaining_days = Math.floor(this.duration / this.milisecondsOfDay);

    this.remaining_hours = Math.floor(
      (this.duration) / this.milisecondsOfHour
    );

    this.remaining_minutes = Math.floor(
      (this.duration % this.milisecondsOfHour) / this.milisecondsOfMinute
    );

    this.remaining_seconds = Math.floor(
      (this.duration % this.milisecondsOfMinute) / this.milisecondsOfSecond
    );

    this.renderCounterInDom();
  }

  renderCounterInDom() {
    if (this.hours) {

      const hourInt = parseInt(this.hours.innerHTML)

      if (hourInt > 24) {
        this.timerTarget.classList.add("u-hidden")
      } else {
        this.timerTarget.classList.remove("u-hidden")
      }

      if (this.remaining_hours <= 0 && this.remaining_minutes <= 0 && this.remaining_seconds <= 0) {

        this.hours.innerHTML = "00"
        this.minutes.innerHTML = "00"
        this.seconds.innerHTML = "00"
        this.timerTarget.classList.add("u-hidden")
        this.changeRedirectToButton();

      } else {

        // Remaining Hours
        this.concatZeroInToDate(this.remaining_hours, this.hours);

        // Remaining Minutes
        this.concatZeroInToDate(this.remaining_minutes, this.minutes);

        // Remaining Seconds
        this.concatZeroInToDate(this.remaining_seconds, this.seconds);

      }

    }
  }

  concatZeroInToDate(remainingTime, objectHTML) {
    if (remainingTime < 10) {
      objectHTML.innerHTML = `0${remainingTime}`;
    } else {
      objectHTML.innerHTML = remainingTime;
    }
  }

  changeRedirectToButton() {
    const hrefNew = this.callToAction.dataset.hrefBtnCourse;
    const textNew = this.callToAction.dataset.textBtnCourse;

    this.callToAction.removeAttribute("target");
    this.callToAction.setAttribute('href', hrefNew);
    this.callToAction.innerHTML = textNew
    this.callToAction.classList.add("o-btn_secondary")
    this.callToAction.classList.add("o-btn_outline-grey")
  }

}
