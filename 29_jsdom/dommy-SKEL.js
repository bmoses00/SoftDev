var button = document.getElementById("b");
console.log(button);

var addItem = function(e) {
	console.log("addItem called");
	var list = document.getElementById("thelist");
	console.log(list);
	var item = document.createElement("li");
	item.innerHTML = "WORD";
	list.appendChild(item);
	list.addEventListener('mouseover', changeHeading);
	list.addEventListener('mouseout', function(e) {document.getElementById("h").innerHTML = "Hello World!"});
}

button.addEventListener("click", addItem);

var changeHeading = function(e) {
	console.log(e.target.innerHTML);
	var h = document.getElementById("h");
	h.innerHTML = e.target.innerHTML;
	var lis = document.getElementsByTagName("li");
}

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
	lis[i].addEventListener('mouseover', changeHeading);
	lis[i].addEventListener('mouseout', function(e) {document.getElementById("h").innerHTML = "Hello World!"});
}
