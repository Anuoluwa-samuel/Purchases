function showPage(pageId, clickedItem) {
  // Hide all pages
  const pages = document.querySelectorAll(".page");
  pages.forEach(page => page.classList.remove("active"));

  // Show selected page
  const activePage = document.getElementById(pageId);
  if (activePage) {
    activePage.classList.add("active");
  }

  // Remove 'active' from all nav items
  const navItems = document.querySelectorAll(".nav-item");
  navItems.forEach(item => item.classList.remove("active-nav"));

  // Add 'active' class to the clicked nav item
  if (clickedItem) {
    clickedItem.classList.add("active-nav");
  }
}

window.onload = function () {
  const defaultItem = document.querySelector(".nav-item");
  showPage('dashboard', defaultItem);
}
