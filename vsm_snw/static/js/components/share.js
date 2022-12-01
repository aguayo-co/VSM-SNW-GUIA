export default function copyUrl(e) {
  const aux = document.createElement("input");
  const msgLinkCopy = e.querySelector(".js-copyUriMsg");

  aux.setAttribute("value", window.location.href);
  document.body.appendChild(aux);
  aux.select();
  document.execCommand("copy");
  document.body.removeChild(aux);
  toggleMessage(msgLinkCopy);
};

const copyUriBtns = document.querySelectorAll(".js-copyUri");
copyUriBtns.forEach(copyUriBtn => {
  copyUriBtn && copyUriBtn.addEventListener("click", () => {
    copyUrl(copyUriBtn)
  });
});

function toggleMessage(msgLinkCopy) {
  msgLinkCopy.classList.add("is-ico-list_show");

  setTimeout(() => {
    msgLinkCopy.classList.remove("is-ico-list_show");
  }, 2000);
}
