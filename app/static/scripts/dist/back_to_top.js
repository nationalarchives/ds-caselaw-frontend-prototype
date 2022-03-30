/******/ (() => { // webpackBootstrap
var __webpack_exports__ = {};
/*!***********************************************!*\
  !*** ./app/static/scripts/src/back_to_top.js ***!
  \***********************************************/
var handler = function handler(entries) {
  manage_class(entries[0].isIntersecting);
};

var createObserver = function createObserver(element) {
  var options = {
    root: null,
    rootMargin: "0px"
  };
  var observer = new IntersectionObserver(handler, options);
  observer.observe(element);
};

var manage_class = function manage_class(intersecting) {
  var button = document.getElementById('js-back-to-top-link');

  if (intersecting) {
    button.classList.add('show');
  } else {
    button.classList.remove('show');
  }
};

createObserver(document.querySelector('.judgment-body'));
/******/ })()
;