function showMenu() {
  var nav = document.getElementsByTagName("nav")[0];
  var article = document.getElementsByTagName("article")[0];
  var footer = document.getElementsByTagName("footer")[0];

  nav.classList.add("nav-show");
  article.classList.add("article-hide");
  footer.classList.add("footer-clear-left");
}

function hideMenu() {
  var nav = document.getElementsByTagName("nav")[0];
  var article = document.getElementsByTagName("article")[0];
  var footer = document.getElementsByTagName("footer")[0];

  nav.classList.remove("nav-show");
  article.classList.remove("article-hide");
  footer.classList.remove("footer-clear-left");
}
