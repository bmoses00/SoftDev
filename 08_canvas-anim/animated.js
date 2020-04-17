var canvas = document.getElementById("playground");
var ctx = canvas.getContext("2d");

var circle_btn = document.getElementById("animate");
var dvd_btn = document.getElementById("corner");
var stop = document.getElementById("stop");

var logo = new Image(50, 50);
logo.src = "logo_dvd.jpg"

var animation_id;
var x, y;
var dx = 1;
var dy = 1;
var is_running = false;
var is_increasing = true;
var radius = 0;

var start_circle = function(e) {
	e.preventDefault();
	window.cancelAnimationFrame(animation_id);
	animation_id = window.requestAnimationFrame(animate_circle);
};

var animate_circle = function(e) {
	if (is_increasing) radius++;
	else               radius--;

	if (radius == canvas.width / 2) is_increasing = false;
	else if (radius == 0)           is_increasing = true;

	ctx.beginPath();
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	ctx.arc(canvas.width / 2, canvas.height / 2, radius, 0, 2 * Math.PI);
	ctx.fill();
	ctx.closePath();

	animation_id = window.requestAnimationFrame(animate_circle);
}

var start_logo = function(e) {
	e.preventDefault();
	// we want to prevent logo from spawning on edges of canvas
	x = canvas.width  / 4 + Math.random() * (canvas.width  / 2);
	y = canvas.height / 4 + Math.random() * (canvas.height / 2);

	window.cancelAnimationFrame(animation_id);
	animation_id = window.requestAnimationFrame(animate_logo);
};

var animate_logo = function(e) {
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	// modify location based on velocity
	x += dx;
	y += dy;
	// if logo hits edge, change direction
	if (x < 0 || x > canvas.width  - logo.width) dx = -dx;
	if (y < 0 || y > canvas.height - logo.height) dy = -dy;

	ctx.drawImage(logo, x, y, logo.width, logo.height);
	animation_id = window.requestAnimationFrame(animate_logo);
};

var stop_animation = function(e) {
	window.cancelAnimationFrame(animation_id);
	is_running = false;
};

circle_btn.addEventListener("click", start_circle);
dvd_btn.addEventListener("click", start_logo);
stop.addEventListener("click", stop_animation);
