var margin = {top: 100, left: 100};
var width = 1000 - margin.left;
var height = 500 - margin.top;

var curtain_offset = 200;


var svg = d3.select("body").append("svg")
  .attr("width", width + margin.left)
  .attr("height", height + margin.top)
  .append("g")
  .attr("transform",
      "translate(" + margin.left + ",0)");


// set the ranges
var x = d3.scaleLinear().range([0, width]);
var y = d3.scaleLinear().range([height, 0]);

/*
function x(input) {
  return (width - 0) * input;
}

function y(input) {
  return (0 - height) * input;
}
*/

// define the line
var valueline = d3.line()

    .x(function(d) { return x(d.Year); })
    .y(function(d) { return y(d.co2); });


// Get the data
d3.csv("static/csv/afghanistan.csv").then(function(data) {

  // format the data
  data.forEach(function(d) {
      d.Year = +d.Year;
      d.co2 = +d.co2;
  });

  // Scale the range of the data
  x.domain(d3.extent(data, function(d) { return d.Year; }));
  y.domain([0, d3.max(data, function(d) { return d.co2; })]);

  // Add the valueline path.
  svg.append("path")
      .data([data])
      .attr("class", "line")
      .attr("d", valueline);

  // Add the x Axis
  svg.append("g")
  .attr("transform", "translate(0," + height + ")")
  .call(d3.axisBottom(x));

  // Add the y Axis
  svg.append("g")
  .call(d3.axisLeft(y));
});


var c = d3.select(".curtain")
  .style("width", width)
  .style("height", height)
  .style("position", "absolute")
  .style("top", 0)
  .style("left", curtain_offset)
  .style("background-color", "white")

var animation_id;

var render_graph = function() {
  let left = +c.style("left").slice(0, c.style("left").length - 2);
  let width = +c.style("width").slice(0, c.style("width").length - 2);

  let change_factor = 8;

  c.style("left", left + change_factor);
  c.style("width", width - change_factor);

  if (left < width + margin.left + curtain_offset)
    animation_id = window.requestAnimationFrame(render_graph);
  else {
    window.cancelAnimationFrame(animation_id);
  }
}
var btn = document.getElementById("render");
btn.addEventListener("click", render_graph);
