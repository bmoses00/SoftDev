var canvas = document.getElementById("playground");
var ctx = canvas.getContext("2d");
var anim = document.getElementById("animate");
var stop = document.getElementById("stop");

var animation_id;
var is_running = false;
var is_increasing = true;
var radius = 0;

var start_animate = function(e) {
	e.preventDefault();
	if (!is_running) {
		is_running = true;
		animation_id = window.requestAnimationFrame(animate);
	}
};

var stop_animate = function(e) {
	window.cancelAnimationFrame(animation_id);
	is_running = false;
};

var animate = function(e) {
	if (is_increasing) radius++;
	else               radius--;

	if (radius == canvas.width / 2) is_increasing = false;
	else if (radius == 0)           is_increasing = true;

	ctx.beginPath();
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	ctx.arc(canvas.width / 2, canvas.height / 2, radius, 0, 2 * Math.PI);
	ctx.fill();
	ctx.closePath();

	if (is_running)
		window.requestAnimationFrame(animate);
}

anim.addEventListener("click", start_animate);
stop.addEventListener("click", stop_animate);
