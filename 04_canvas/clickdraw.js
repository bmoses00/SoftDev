var type = "rectangle";

var t = document.getElementById("toggler");
var c = document.getElementById("clear");
var d = document.getElementById("slate");
var ctx = d.getContext("2d");

var toggle = function(e) {
    if (type == "rectangle"){
        type = "dot";
        e["srcElement"]["firstChild"]["data"] = "Click to toggle to rectangle";
    }
    else {
        type = "rectangle"
        e["srcElement"]["firstChild"]["data"] = "Click to toggle to dot";
    }
}
t.addEventListener("click", toggle);


var clear = function(e) {
    ctx.clearRect(0, 0, 300, 150);
}
c.addEventListener("click", clear);


var draw = function(e) {
    console.log(e)
    if (type == "dot") {
        ctx.beginPath();
        ctx.arc(e.clientX, e.clientY, 25, 0, 2 * Math.PI);
        ctx.fill();
    }
    else {
        ctx.fillRect(e.clientX, e.clientY, 25, 25);
    }
}
d.addEventListener("click", draw);
