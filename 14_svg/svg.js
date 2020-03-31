var pic = document.getElementById("vimage");
var clr = document.getElementById("clear");
var mv = document.getElementById("move");
var xtr = document.getElementById("xtra");

var animation_id;
let c;

var clear = function() {
  window.cancelAnimationFrame(animation_id);
  pic.innerHTML = '';
}

var plot = function(e) {
  if (e.target.localName == "svg") {
    c = document.createElementNS(
    "http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", e.offsetX);
    c.setAttribute("cy", e.offsetY);
    c.setAttribute("r", 20);
    c.setAttribute("dx", 1);
    c.setAttribute("dy", 1);
    c.setAttribute("dr", 1);
    c.setAttribute("fill", "blue");

    pic.appendChild(c);
  }
}

var move = function() {
  var children = pic.children;
  for (var i = 0; i < children.length; i++) {

    x =  parseInt(children[i].getAttribute("cx"));
    y =  parseInt(children[i].getAttribute("cy"));
    dx = parseInt(children[i].getAttribute("dx"));
    dy = parseInt(children[i].getAttribute("dy"));
    r =  parseInt(children[i].getAttribute("r") );

    children[i].setAttribute("cx", x + dx);
    children[i].setAttribute("cy", y + dy);

  	if (x < r || x > pic.getAttribute("width") - r) {
      children[i].setAttribute("dx", -dx);
      children[i].setAttribute("cx", x - dx * 3);
    }
  	if (y < r || y > pic.getAttribute("height") - r) {
      children[i].setAttribute("dy", -dy);
      children[i].setAttribute("cy", y - dy * 3);
    }
  };
  animation_id = window.requestAnimationFrame(move);
};

var extra = function() {
  var children = pic.children;
  for (var i = 0; i < children.length; i++) {

    r =  parseInt(children[i].getAttribute("r") );
    dr = parseInt(children[i].getAttribute("dr"));

    children[i].setAttribute("r", r + dr);

    if (r > 40 || r < 0) {
      children[i].setAttribute("dr", -dr);
      children[i].setAttribute("r", r - dr * 3);
    }

  }
  animation_id = window.requestAnimationFrame(extra);
}

clr.addEventListener("click", clear);
mv.addEventListener("click", move);
xtr.addEventListener("click", extra);
pic.addEventListener("click", plot);
