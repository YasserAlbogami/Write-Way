const togglePassword = document.querySelector("#togglePassword");
const password = document.querySelector("#password1");

togglePassword.addEventListener("click", function () {
  // toggle the type attribute
  const type =
    password.getAttribute("type") === "password" ? "text" : "password";
  password.setAttribute("type", type);

  // toggle the eye icon
  this.classList.toggle("fa-eye");
});

const togglePassword2 = document.querySelector("#togglePassword2");
const password2 = document.querySelector("#password2");

togglePassword2.addEventListener("click", function () {
  // toggle the type attribute
  const type =
    password2.getAttribute("type") === "password" ? "text" : "password";
  password2.setAttribute("type", type);

  // toggle the eye icon
  this.classList.toggle("momo");
});

////////////////////////////// POST request to delete a note

function deleteNote(noteID) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteID: noteID }),
  }).then((_res) => {
    window.location.href = "/Home";
  });
}
////////////////////////////

function showSideBar() {
  const sidebar = document.querySelector(".sidebar");
  sidebar.style.display = "flex";
}

function closeSideBar() {
  const sidebar = document.querySelector(".sidebar");
  sidebar.style.display = "none";
}
