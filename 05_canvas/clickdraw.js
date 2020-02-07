var rectangle = true;

var toggle_button = document.getElementById("toggler");
var clear_button = document.getElementById("clear");
var canvas = document.getElementById("slate");
var ctx = canvas.getContext("2d");

var toggle = function(e) {
    // preventDefault stops the default behavior of a certain action from triggering
    e.preventDefault();
    if (rectangle) toggle_button.innerHTML = "Click to toggle to rectangle";
    else           toggle_button.innerHTML = "Click to toggle to dot";
    rectangle = !rectangle;
}

var clear = function(e) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}


var draw = function(e) {
    if (rectangle) {
        /* e.offsetX and e.offsetY give the distance, in pixels,
        between the cursor and the upper left corner of the element */
        ctx.fillRect(e.offsetX, e.offsetY, 25, 25);
    }
    else {
        /* we need to call beginPath() to let the canvas know that we are
        beginning a new set of drawing instructions */
        ctx.beginPath();
        ctx.arc(e.offsetX, e.offsetY, 25, 0, 2 * Math.PI);
        ctx.fill();
    }
}

clear_button.addEventListener("click", clear);
canvas.addEventListener("click", draw);
toggle_button.addEventListener("click", toggle);
