export default class HideSearch {
  constructor() {
    this.searchTarget = document.querySelector(".js-search-target");
    this.btnOpen = document.querySelector(".js-search-open");
    this.btnClose = document.querySelector(".js-search-close");
    this.headerTarget = document.querySelector(".js-header-target");
    this.classToToggleSearch = "is-search-open";

    this.inputQuery = document.querySelector(".js-input-field")
    this.btnClearInput = document.querySelector(".js-input-clear")

    this.init()
  }

  init() {
    if (this.searchTarget) {
      this.showSearch()
      this.HideSearch()
      this.hideSearchAnyClick()
    }

    this.clearInput()
  }

  showSearch() {
    this.btnOpen.addEventListener("click", () => {

      if (!this.headerTarget.classList.contains(this.classToToggleSearch)) {
        this.headerTarget.classList.add(this.classToToggleSearch)

        if (this.headerTarget.querySelector(".is-open-submenu")) {
          this.headerTarget.querySelector(
            ".is-open-submenu"
          ).classList.remove("is-open-submenu")
        }
      }

    })
  }

  HideSearch() {
    this.btnClose.addEventListener("click", () => {
      if (this.headerTarget.classList.contains(this.classToToggleSearch)) {
        this.headerTarget.classList.remove(this.classToToggleSearch)
      }
    })
  }

  hideSearchAnyClick() {
    document.addEventListener("click", function (e) {
      var clic = e.target;
      if (!clic.closest(".js-header-target")) {
        if (document.querySelector(
          ".js-header-target"
        ).classList.contains("is-search-open")) {
          document
            .querySelector(".js-header-target")
            .classList.remove("is-search-open")
        }
      }
    });
  }

  clearInput() {
    this.btnClearInput.addEventListener("click", () => {
      this.inputQuery.value = ""
      this.inputQuery.removeAttribute("value")
    })
  }
}
