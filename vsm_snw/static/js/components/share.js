export default function copyUrl() {
  const aux = document.createElement("input");
  const msgLinkCopy = document.getElementsByClassName("js-copyUriMsg")[0];

  aux.setAttribute("value", window.location.href);
  document.body.appendChild(aux);
  aux.select();
  document.execCommand("copy");
  document.body.removeChild(aux);
  toggleMessage(msgLinkCopy);
};

const copyUriBtn = document.getElementsByClassName("js-copyUri")[0];

function toggleMessage(msgLinkCopy) {
  msgLinkCopy.classList.add("is-ico-list_show");

  setTimeout(() => {
    msgLinkCopy.classList.remove("is-ico-list_show");
  }, 2000);
}

copyUriBtn && copyUriBtn.addEventListener("click", copyUrl);
