export default class Dropdown {
  constructor({ element }) {
    this.element = element;
    this.siblingsLength = this.element.parentNode.childNodes;
    this.classToShowContent = "is-dropdown-show";
    this.init();
  }

  init() {
    this.toggleDropdown();
  }

  toggleDropdown() {

    this.element.addEventListener("click", () => {

      if (this.element.classList.contains(this.classToShowContent)) {
        this.element.classList.remove(this.classToShowContent)
      } else {

        for (let i = 0; i < this.siblingsLength.length; i++) {
          const sibling = this.siblingsLength[i]

          if (sibling.classList.contains(this.classToShowContent)) {
            sibling.classList.remove(this.classToShowContent)
          }
        }

        this.element.classList.add(this.classToShowContent)
      }

    })

  }

}
