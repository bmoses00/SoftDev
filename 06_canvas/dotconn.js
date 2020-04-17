var canvas = document.getElementById("playground");
var ctx = canvas.getContext("2d");
var btn = document.getElementById("clear");

var lastX;
var lastY;

var clear = function(e) {
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	lastX = -1;
};

var plot = function(e) {
	if (lastX == -1) {
		lastX = e.offsetX;
		lastY = e.offsetY;
	}
	ctx.beginPath();
    ctx.arc(e.offsetX, e.offsetY, 5, 0, 2 * Math.PI);
    ctx.fill();
    ctx.closePath();

    ctx.beginPath();

    ctx.moveTo(lastX, lastY);
    ctx.lineTo(e.offsetX, e.offsetY);

    ctx.stroke();
    ctx.closePath();

    lastX = e.offsetX;
    lastY = e.offsetY;
};

btn.addEventListener("click", clear);
canvas.addEventListener("click", plot);
