// declare our margins and dimensions
var margin = {bottom: 100, left: 100, top: 50};
var width = 1000 - margin.left;
var height = 500 - margin.bottom - margin.top;

var c = d3.select(".curtain");

var x;
var y;

function draw_graph(country, dataset, color) {
  // Get the data
  let svg = d3.select("#graph")
  .attr("width", width + margin.left)
  .attr("height", height + margin.bottom + margin.top)
  .append("g")
  .attr("transform",
  "translate(" + margin.left + "," + margin.top + ")");
  d3.csv("static/csv/" + dataset).then(function(data) {


    create_path(country, dataset, color, data);


    // we get this data now because we want it before it's changed by adding axes labels
    var svg_data = svg._groups[0][0].getBBox();
    var svg_margin = 10;

    let x_label_container = document.getElementById("x_label");
    if (x_label_container != null) x_label_container.remove()
    svg.append("text")
    .attr("id", "x_label")
    .attr("transform",
          "translate(" + (width/2) + " ," +
                         (height + 50) + ")")
    .style("text-anchor", "middle")
    .text("Year");

    let y_label;

    if (dataset == "co2_per_gdp.csv")         y_label = "co2 emissions (kg) per $ of GDP (PPP)"
    else if (dataset == "co2_per_capita.csv") y_label = "co2 emissions (metric tons) per capita"
    else                                      y_label = "co2 emissions (kilotons)"

    let y_label_container = document.getElementById("y_label");
    if (y_label_container == null) {
      svg.append("text")
      .attr("id", "y_label") // needs a unique ID because we may need to change its text
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left)
      .attr("x",0 - (height / 2))
      .attr("dy", "1em")
      .style("text-anchor", "middle")
      .text(y_label);
    }
    else {
      y_label_container.innerHTML = y_label;
    }

    let title = country + " - " + y_label;

    let title_container = document.getElementById("title");
    if (title_container == null) {
      svg.append("text")
        .attr("id", "title")
        .attr("x", width / 2)
        .attr("y", -margin.top / 2)
        .attr("text-anchor", "middle")
        .style("font-size", "16px")
        .style("text-decoration", "underline")
        .text(title);
    }
    else {
      title_container.innerHTML = title;
    }

    // Add the x Axis
    let axis_bottom_container = document.getElementById("axis_bottom")
    if (axis_bottom_container != null) axis_bottom_container.remove();
    svg.append("g")
    .attr("id", "axis_bottom")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x))

    // Add the y Axis
    let axis_left_container = document.getElementById("axis_left")
    if (axis_left_container != null) axis_left_container.remove();
    svg.append("g")
    .attr("id", "axis_left")
    .call(d3.axisLeft(y));


    c
      .style("width", width)
      .style("height", height)
      .style("position", "absolute")
      .style("top", margin.top + svg_margin - 2)
      .style("left", margin.left + svg_margin)
      .style("background-color", "white")

  });
}

function create_path(country, dataset, color, data) {
  // create svg bounding box
  let svg = d3.select("#graph")
  // .attr("width", width + margin.left)
  // .attr("height", height + margin.bottom + margin.top)
  // .append("g")
  // .attr("transform",
  // "translate(" + margin.left + "," + margin.top + ")");

  console.log(margin.left)

  // set the ranges
  x = d3.scaleLinear().range([0, width]);
  y = d3.scaleLinear().range([height, 0]);

  // define the line
  var valueline = d3.line()

  .x(function(d) { return x(d.Year); })
  .y(function(d) { return y(d[country]); });


  // format the data
  data.forEach(function(d) {
    d.Year = +d.Year;
    d[country] = +d[country];
  });

  // Scale the range of the data
  x.domain([1990, 2013]); // most countries have no data past 2014
  y.domain([0, d3.max(data, function(d) { return d[country]; })]);

  // Add the valueline path.
  svg.append("path")
  .attr("id", "path_" + country + "_" + dataset)
  .data([data])
  .attr("stroke", color)
  .attr("fill", "none")
  .attr("stroke-width", 2)
  .attr("d", valueline);
}

var animation_id;

var render_graph = function() {
  let curtain_left = +c.style("left").slice(0, c.style("left").length - 2);
  let curtain_width = +c.style("width").slice(0, c.style("width").length - 2);

  let change_factor = 8;

  c.style("left", curtain_left + change_factor);
  c.style("width", curtain_width - change_factor);

  if (curtain_left < width + margin.left)
    animation_id = window.requestAnimationFrame(render_graph);
  else {
    window.cancelAnimationFrame(animation_id);
  }
}
var btn = document.getElementById("render");
btn.addEventListener("click", render_graph);

draw_graph("United States", "co2_per_gdp.csv", "red")
draw_graph("China", "co2.csv", "red")
