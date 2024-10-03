let div    = document.querySelector('div');

fetch('http://localhost:8000/products/')
  .then(response => response.text())
  .then(text => div.innerHTML = text)