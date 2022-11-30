export default function initFilters() {
  // Clase target para los filtros
  const formFilter = document.querySelector(".js-filter-target");

  if (formFilter) {
    const choicesFilter = formFilter.querySelectorAll(".js-filter-choice");

    // Recorrer elementos del formulario
    Array.from(choicesFilter).filter(element => {

      // Guardar y convertir el valor que trae el dataset del padre
      const parentChoice = element.closest(".js-filter-item");
      let datasetFilterCounter = parseInt(parentChoice.dataset.filterCounter);

      // Validar si hay filtros para mostrar burbuja
      if (datasetFilterCounter > 0) {
        parentChoice.classList.add("is-show");
      }

      // Validar si hay o no filtros aplicados para crear los chips
      if (element.previousElementSibling.checked) {
        createChip(element.textContent)
      }

      const filterType = document.querySelector("[name='type']");
      if (filterType) {
        getCurrentSelection(filterType.value)
      }

      // Ocultar o mostrar el botón de borrar filtros
      hideOrShowClearButton()
    })
  }
}

export function toggleCounterOfFilter(element) {
  // Guardar y convertir el valor que trae el dataset del padre
  const parentChoice = element.target.closest(".js-filter-item");
  let datasetFilterCounter = parseInt(parentChoice.dataset.filterCounter);
  const classNumberCounter = "js-filter-number-counter";
  let numberCounter = parentChoice.querySelector(`.${classNumberCounter}`);

  // Mostrar burbuja al agregar o eliminar filtro
  parentChoice.classList.add("is-show");

  // Valida el check del input para manipular el contador de filtros
  if (element.target.previousElementSibling.checked) {
    parentChoice.setAttribute("data-filter-counter", --datasetFilterCounter)

    // Elimina el chip seleccionado
    removeChipIntoCheckbox(element.target)
  } else {
    parentChoice.setAttribute("data-filter-counter", ++datasetFilterCounter)

    // Crea el chip seleccionado
    createChip(element.target.textContent)
  }

  // Ocultar o mostrar el botón de borrar filtros
  hideOrShowClearButton()

  // Renderizar en el DOM el resultado del contador
  numberCounter.innerHTML = datasetFilterCounter
}

export function removeChipIntoCheckbox(element) {
  const filterChip = document.querySelectorAll(".c-filter__chip");

  // Recorrer el listado de chips generado
  filterChip.forEach(chip => {

    // Valida si los contenidos del chip y el input son iguales para removerlo
    if (chip.dataset.idFilter.trim() == element.textContent.trim()) {
      removeChip(chip)
    }
  });

}

export function removeChipIntoClick(element) {
  const formFilter = document.querySelector(".js-filter-target");

  // Recorrer elementos del formulario
  Array.from(formFilter.elements).filter(input => {
    if (input.tagName == "INPUT") {
      if (input.labels[0]) {
        const inputParent = element.target.closest(".c-filter__chip")

        // Valida que exita el label en el elemento
        if (input.labels[0]) {
          // Valida si los contenidos del chip y el input son iguales para removerlo
          if (input.labels[0].textContent.trim() == inputParent.getAttribute("data-id-filter").trim()) {
            // Pasa todos los inputs a unchecked
            input.checked = false
            getNumberCounter(input);
            removeChip(element.target.closest(".c-filter__chip"))
          }
        }
      }
    }

  })

  // Ocultar o mostrar el botón de borrar filtros
  hideOrShowClearButton()
}

function createChip(text) {
  const templateChip = document.getElementById("js-filter-chip-template");
  const clonChip = templateChip.content.cloneNode(true);

  const setOfFilterChips = document.getElementById("js-filter-chip-set")
  if (setOfFilterChips.classList.contains("u-hidden")) {
    setOfFilterChips.classList.remove("u-hidden")
  }

  clonChip.querySelector(".c-filter__chip").setAttribute("data-id-filter", text);
  clonChip.querySelector(".c-filter__chip-text").textContent = text

  setOfFilterChips.appendChild(clonChip);
}

function removeChip(element) {
  const setOfFilterChips = document.getElementById("js-filter-chip-set")

  if (setOfFilterChips.contains(element)) {
    setOfFilterChips.removeChild(element)

    if (setOfFilterChips.childElementCount == 0) {
      setOfFilterChips.classList.add("u-hidden")
    }
  }

}

function getNumberCounter(element) {
  const parentChoice = element.closest(".js-filter-item");
  let datasetFilterCounter = parseInt(parentChoice.dataset.filterCounter);
  let numberCounter = parentChoice.querySelector(".js-filter-number-counter");

  parentChoice.setAttribute("data-filter-counter", --datasetFilterCounter)

  numberCounter.innerHTML = datasetFilterCounter
}

function hideOrShowClearButton() {
  const setOfFilterChips = document.getElementById("js-filter-chip-set")
  const btnClear = document.querySelector(".js-filter-clear-btn")

  if (setOfFilterChips.childElementCount == 0) {
    btnClear.classList.add("u-hidden")
  } else {
    btnClear.classList.remove("u-hidden")
  }
}

export function goToPage(event) {
  getUrlSearchParams("page", event.target.dataset.page)
}

export function orderElements(event) {
  getUrlSearchParams("order_by", event.target.getAttribute("for"))
}

function getUrlSearchParams(paramName, filterValue) {
  if ('URLSearchParams' in window) {
    const searchParams = new URLSearchParams(window.location.search);
    if (filterValue !== "") {
      searchParams.set(paramName, filterValue);
    } else {
      searchParams.delete(paramName)
    }
    window.location.search = searchParams.toString();
  }
}

export function clearFilters() {
  const formFilter = document.querySelector(".js-filter-target");
  const setChips = document.getElementById("js-filter-chip-set");

  Array.from(formFilter.elements).filter(element => {
    element.checked = false

    if (element.closest(".js-filter-item")) {
      element.closest(".js-filter-item").classList.remove("is-show")
      element.closest(".js-filter-item").setAttribute("data-filter-counter", 0)
    }
  })

  setChips.classList.add("u-hidden")
  setChips.textContent = ""

  hideOrShowClearButton()
}

export function hiddenFormFilter(event) {
  getCurrentSelection(event.target.value);
}

function getCurrentSelection(element) {
  const filter_catalogo = document.querySelector(".js_filter_catalogo");

  if (element == 'catalog') {
    filter_catalogo.classList.remove('u-hidden')
  } else {
    filter_catalogo.classList.add('u-hidden')
  }
}
