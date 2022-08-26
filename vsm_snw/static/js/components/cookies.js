// Cookie window
function setCookie(cname, cvalue, exdays) {
  let d = new Date();
  d.setTime(d.getTime() + exdays * 24 * 60 * 60 * 1000);
  let expires = "expires=" + d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(";");
  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

export default function showOrHideCookie() {
  let cookiesNotified = getCookie("cookiesNotified");
  let closeButton = document.querySelector(".js-btn-remove-cookie");

  if (closeButton) {
    if (!cookiesNotified) {
      closeButton.closest(".js-target-cookie").classList.add("is-cookie-show");
    }

    closeButton.addEventListener("click", function () {
      this.closest(".js-target-cookie").classList.remove("is-cookie-show");
      setCookie("cookiesNotified", true, 7);
    });
  }
}
