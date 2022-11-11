export default class Dropdown {
  constructor({ element }) {
    this.element = element;
    this.targetContentDropdown = this.element.nextElementSibling;
    this.contentDropdown = this.element.nextElementSibling.querySelector(".js-dropdown-wrap");
    this.siblingsLength = this.element.parentNode.childNodes;
    this.classToShowContent = "is-dropdown-show";
    this.isDefaultOpen = this.element.dataset.isDropdownOpen;
    this.init();
  }

  init() {
    this.toggleDropdown();
    this.defaultOpenDropdown();
    this.setContentMaxHeight();
    this.resizeContextMaxHeight()
  }

  toggleDropdown() {

    this.element.addEventListener("click", () => {

      if (this.element.classList.contains(this.classToShowContent)) {
        this.element.classList.remove(this.classToShowContent)
        this.hideTarget(this.element)
      } else {

        for (let i = 0; i < this.siblingsLength.length; i++) {
          const sibling = this.siblingsLength[i]

          if (sibling.classList) {
            if (sibling.classList.contains(this.classToShowContent)) {
              sibling.classList.remove(this.classToShowContent)
              this.hideTarget(sibling)
            }
          }
        }

        this.element.classList.add(this.classToShowContent)
        this.showTarget(this.element);
      }

    })

  }

  setContentMaxHeight() {
    if (this.contentDropdown) {
      this.targetContentDropdown.setAttribute("data-maxheight", this.contentDropdown.clientHeight)
    }
  }

  resizeContextMaxHeight() {
    window.addEventListener("resize", () => {
      this.setContentMaxHeight()
      if (this.element.classList.contains(this.classToShowContent)) {
        this.showTarget(this.element)
      }
    })
  }

  showTarget(target) {
    setTimeout(() => {
      const dataMaxHeight = target.nextElementSibling.dataset.maxheight;

      target.nextElementSibling.setAttribute("style", `max-height: ${dataMaxHeight}px`)

      if (target.nextElementSibling.querySelector("[data-maxheight]")) {
        const parentDataMaxHeight = target.nextElementSibling.querySelector(
          "[data-maxheight]").dataset.maxheight
        target.nextElementSibling.setAttribute(
          "style", `max-height: ${dataMaxHeight + parentDataMaxHeight}px`
        );
      }

    }, 100)
  }

  hideTarget(target) {
    target.nextElementSibling.removeAttribute("style")
  }

  defaultOpenDropdown() {
    if (this.isDefaultOpen) {
      this.element.classList.add(this.classToShowContent)
      this.showTarget(this.element);
    }
  }

}
