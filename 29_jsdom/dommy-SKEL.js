var button = document.getElementById("b");
console.log(button);

var addItem = function(e) {
	// console.log("addItem called");
	var list = document.getElementById("thelist");
	// console.log(list);
	var item = document.createElement("li");
	item.innerHTML = "WORD";
	list.appendChild(item);
	item.addEventListener('mouseover', changeHeading);
	item.addEventListener('mouseout', function(e) {document.getElementById("h").innerHTML = "Hello World!"});
	item.addEventListener('click', removeItem);
}

button.addEventListener("click", addItem);

var changeHeading = function(e) {
	// console.log(e.target.innerHTML);
	var h = document.getElementById("h");
	h.innerHTML = e.target.innerHTML;
	var lis = document.getElementsByTagName("li");
}

var removeItem = function(e) {
	console.log(e);
	this.remove();
}
var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
	lis[i].addEventListener('mouseover', changeHeading);
	lis[i].addEventListener('mouseout', function(e) {document.getElementById("h").innerHTML = "Hello World!"});
	lis[i].addEventListener('click', removeItem);
}

var fib = function(n) {
	if (n < 2) {
		return 1;
	}
	else {
		return fib(n - 1) + fib(n - 2);
	}
};


var fib2 = function(n) {
  var first = 1;
  var second = 1;
  while (n > 0){
    var temp = first;
    first = second;
    second = temp + second;
    n -= 1;
  }
  return first;
};

var addFib = function(e) {
	// console.log(e);
	var fblist = document.getElementById("fiblist");
	var fbnumber = fblist.childElementCount;
	var item = document.createElement("li");
	
	var r = 255 * Math.sin(fbnumber) + 256;
	var g = 255 * Math.cos(fbnumber) + 256;
	var b = 255 * Math.sin(fbnumber + 5) + 256;
	item.setAttribute('style', 'color: rgb(' + r + ',' + g + ',' + b + ')');
	item.innerHTML = fib2(fbnumber);
	fblist.appendChild(item);
}


var fb = document.getElementById("fb");
fb.addEventListener("click", addFib);

var body = document.getElementsByTagName("body")[0];
console.log(body);
body.style.fontFamily = "Comic Sans";



