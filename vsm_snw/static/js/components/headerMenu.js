export default class headerMenuNavigation {
  constructor() {
    this.element = document.querySelector(".js-header-target");
    this.targetSubmenu = ".js-header-target-submenu";

    this.btnBurgerMenu = this.element.querySelector(".js-header-toggle-menu");
    this.btnsSubMenu = this.element.querySelectorAll(".js-header-submenu-btn");
    this.btnsBackSubMenu = this.element.querySelectorAll(".js-header-back-btn");

    // Class to show menus
    this.classIsOpenBurgerMenu = "is-open" // Toggle burger menu
    this.classIsOpenSubMenu = "is-open-submenu" // Show sub menu
    this.classIsAnimationActive = "is-animation-submenu" // Show sub menu with animation

    this.init()
  }

  init() {
    this.addClassToAnimateMenu()
    this.toggleMenuToMobile()
    this.clickToShowSubMenu()
    this.clickToBackToMenu()
  }

  addClassToAnimateMenu() {
    setTimeout(() => {

      const targetSubMenu = document.querySelectorAll(this.targetSubmenu);
      targetSubMenu.forEach(element => {
        element.classList.add(this.classIsAnimationActive)
      });

    }, 500)
  }

  toggleMenuToMobile() {
    this.btnBurgerMenu.addEventListener("click", () => {
      this.element.classList.toggle(this.classIsOpenBurgerMenu)

      var listOfTargetSubMenu = document.querySelectorAll(this.targetSubmenu);
      listOfTargetSubMenu.forEach(currentSubMenu => {
        if (currentSubMenu.classList.contains(this.classIsOpenSubMenu)) {
          currentSubMenu.classList.remove(this.classIsOpenSubMenu)
        }
      });
    })
  }

  clickToShowSubMenu() {

    this.btnsSubMenu.forEach(currentBtn => {

      currentBtn.addEventListener("click", () => {

        var parentCurrentBtn = currentBtn.closest(this.targetSubmenu);

        if (parentCurrentBtn.classList.contains(this.classIsOpenSubMenu)) {

          parentCurrentBtn.classList.remove(this.classIsOpenSubMenu)

        } else {
          var parentCurrentBtn = currentBtn.closest(this.targetSubmenu);

          if (this.element.classList.contains("is-search-open")) {
            this.element.classList.remove("is-search-open")
          }

          this.btnsSubMenu.forEach(siblingsMenu => {

            var parentSiblings = siblingsMenu.closest(this.targetSubmenu);

            if (parentSiblings.classList.contains(this.classIsOpenSubMenu)) {
              siblingsMenu.closest(this.targetSubmenu).classList.remove(this.classIsOpenSubMenu)
            }

          });

          currentBtn.closest(this.targetSubmenu).classList.add(this.classIsOpenSubMenu)

        }

      })

    });
  }

  clickToBackToMenu() {
    this.btnsBackSubMenu.forEach(currentBackBtn => {
      currentBackBtn.addEventListener("click", () => {
        if (currentBackBtn.closest(this.targetSubmenu)) {
          currentBackBtn.closest(this.targetSubmenu).classList.remove(this.classIsOpenSubMenu)
        }
      })
    });
  }

}
