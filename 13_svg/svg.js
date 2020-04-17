var pic = document.getElementById("vimage");
var btn = document.getElementById("clear");

let c;

var clear = function() {
  pic.innerHTML = '';
}

var plot = function(e) {
  c = document.createElementNS(
  "http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cx", e.offsetX);
  c.setAttribute("cy", e.offsetY);
  c.setAttribute("r", 20);
  c.setAttribute("fill", "blue");
  c.addEventListener("click", circle_clicked);

  pic.appendChild(c);
}

var circle_clicked = function(e) {
  // console.log(e.toElement.getAttribute("fill")); this for google chrome (below doesn't work in ffox)
  if (e.originalTarget.getAttribute("fill") == "blue") {
    e.originalTarget.setAttribute("fill", "cyan");
  }
  else {
    e.originalTarget.setAttribute("cx", Math.random() * pic.getAttribute("width"));
    e.originalTarget.setAttribute("cy", Math.random() * pic.getAttribute("width"));
    e.originalTarget.setAttribute("fill", "blue");
  }
  e.stopPropagation();
}

btn.addEventListener("click", clear);
pic.addEventListener("click", plot);
