var fact = function(n) {
	if (n == 1){
    return 1;
  }
  else {
    return n * (fact(n - 1));
  }
};

var fibonacci = function(n) {
  var first = 0;
  var second = 1;
  while (n > 0){
    var temp = first;
    first = second;
    second = temp + second;
    n -= 1;
  }
  return first;
};

var gcd = function(a, b) {
  var dend, dsor, r;
  if (a > b){
    dend = a;
    dsor = b;
    r = a % b;
  }
  else{
    dend = b;
    dsor = a;
    r = b % a;
  }
  while (r > 0){
    dend = dsor;
    dsor = r;
    r = dend % dsor;
  }
  return dsor;
};

var randomStudent = function() {
  var list = ['William', 'Joseph', 'Calvin', 'Ethan', 'Moody', 'Mo', 'Big Mo', 'Peihua', 'Saad', 'Benjamin', 'Justin', 'Alice', 'Hilary', 'Ayham', 'Michael', 'Matthew', 'Jionghao', 'Devin', 'David', 'Jacob', 'Will', 'Hannah', 'Alex'];
  return list[Math.floor(Math.random() * list.length)];
};

var run_fib = function() {
  var ans = fibonacci(12);
  console.log(ans); //print the answer to the console
  
  var text = document.createTextNode("fib(12) = "+ans); //forms text in HTML
  var par = document.createElement("p"); //forms a <p> ... </p> tag in HTML
  par.appendChild(text); //puts text inside par
  var body = document.getElementsByTagName("body")[0]; //getElementsByTagName is a list, so we need the first element in the list (the body)
  body.appendChild(par); //puts the paragraph in the body
}

var run_gcd = function() {
  var ans = gcd(102,36);
  console.log(ans); //print the answer to the console
  var par = document.createElement("p"); //forms a <p> ... </p> tag in HTML
  var text = document.createTextNode("gcd(102,36) = "+ans); //forms text in HTML
  par.appendChild(text); //puts text inside par
  var body = document.getElementsByTagName("body")[0]; //getElementsByTagName is a list, so we need the first element in the list (the body)
  body.appendChild(par); //puts the paragraph in the body
}

var run_name = function() {
  var ans = randomStudent(); /*Making the answer to the function a variable, rather than recomputing it every time, is very important here,
  to make sure that the answers that the console and the browser get are the same*/
  console.log(ans); //print the answer to the console
  var par = document.createElement("p"); //forms a <p> ... </p> tag in HTML
  var text = document.createTextNode("A random student is ... "+ans); //forms text in HTML
  par.appendChild(text); //puts text inside par
  var body = document.getElementsByTagName("body")[0]; //getElementsByTagName is a list, so we need the first element in the list (the body)
  body.appendChild(par); //puts the paragraph in the body
}

var fib_button = document.getElementById("fibonacci"); //the fib button in the HTML page
//console.log(fib);
fib_button.addEventListener('click',run_fib); //runs the function run_fib once fib_button is clicked
var gcd_button = document.getElementById("gcd"); //the gcd button in the HTML page
gcd_button.addEventListener('click',run_gcd); //runs the function run_fib once fib_button is clicked
var name_button = document.getElementById("name"); //the name button in the HTML page
name_button.addEventListener('click',run_name); //runs the function run_fib once fib_button is clicked
