// Plot the default route once the page loads
var defaultURL = "/static/resources/v1/agent/searchinfo";
d3.json(defaultURL).then(function(rawdata) {
  var data = [rawdata.results[0]];
  var layout = {title: "Agent Trends for Yesterday", margin: { t: 60, b: 120 }, height: 700, width: 1000
  ,xaxis: { title: "Agent Activity Frequency" },yaxis: { title: "Hours of the day" }  };
  Plotly.plot("graph_bar", data, layout);
});

// Update the plot with new data
function updatePlotly(newdata) {
Plotly.purge(document.getElementById('graph_bar'));
console.log(newdata)
updated_data = newdata
var updated_layout = { title: "Agent Trends for Yesterday", margin: { t: 60, b: 120 }, height: 700, width: 1000
,xaxis: { title: "Hours of the day" },yaxis: { title: "Agent Activity Frequency" } };

Plotly.plot(document.getElementById('graph_bar'), updated_data, updated_layout);

}

// Get new data whenever the dropdown selection changes
function getData(route) {
  console.log(route);
  d3.json(`v1/${route}`).then(function(rawdata) {
    console.log("newdata", rawdata);
    // data = [data.results[0],data.results[1],data.results[2]]
    console.log(rawdata.results.length)
    if(rawdata.results.length==3)
    {
        data = [rawdata.results[0],rawdata.results[1],rawdata.results[2]]
        console.log("CONTROL ENETERD IF BLOCK")
    }
    else if(rawdata.results.length==2)
    {
        data = [rawdata.results[0],rawdata.results[1]]
        console.log("CONTROL ENETERD IF-ELSE BLOCK")
    }
    else 
    {
        console.log("CONTROL ENETERD ELSE BLOCK")
        data = [rawdata.results[0]]
    }
    console.log(data.length)
    updatePlotly(data);
  });
}
