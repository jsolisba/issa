document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("employeeForm");
  const tableBody = document.querySelector("#employeeTable tbody");

  form.addEventListener("submit", (event) => {
    event.preventDefault(); // Evitar el envío del formulario por defecto

    // Capturar los valores de los campos
    const name = document.getElementById("name").value.trim();
    const ced = document.getElementById("ced").value.trim();
    const cel = document.getElementById("cel").value.trim();
    const email = document.getElementById("email").value.trim();
    const dir = document.getElementById("dir").value.trim();

    // Validar solo el campo "Nombre"
    if (!name) {
      alert("El campo 'Nombre' es obligatorio.");
      return;
    }

    // Crear una nueva fila para la tabla
    const newRow = document.createElement("tr");

    // Agregar celdas con los valores
    newRow.innerHTML = `
      <td>${name}</td>
      <td>${ced || "-"}</td>
      <td>${cel || "-"}</td>
      <td>${email || "-"}</td>
      <td>${dir || "-"}</td>
      <td>
        <button class="edit-btn">Editar</button>
        <button class="delete-btn">Eliminar</button>
      </td>
    `;

    // Agregar eventos a los botones
    const editButton = newRow.querySelector(".edit-btn");
    const deleteButton = newRow.querySelector(".delete-btn");

    editButton.addEventListener("click", () => editRow(newRow));
    deleteButton.addEventListener("click", () => deleteRow(newRow));

    // Añadir la nueva fila al cuerpo de la tabla
    tableBody.appendChild(newRow);

    // Limpiar el formulario después de guardar
    form.reset();
  });

  // Función para editar una fila
  function editRow(row) {
    const cells = row.querySelectorAll("td");
    document.getElementById("name").value = cells[0].textContent;
    document.getElementById("ced").value = cells[1].textContent !== "-" ? cells[1].textContent : "";
    document.getElementById("cel").value = cells[2].textContent !== "-" ? cells[2].textContent : "";
    document.getElementById("email").value = cells[3].textContent !== "-" ? cells[3].textContent : "";
    document.getElementById("dir").value = cells[4].textContent !== "-" ? cells[4].textContent : "";

    // Eliminar la fila seleccionada para actualizarla
    row.remove();
  }

  // Función para eliminar una fila
  function deleteRow(row) {
    row.remove();
  }
});
