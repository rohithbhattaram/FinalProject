var defaultURL = "/static/resources/v1/failure/visualization";
console.log(document.getElementById('reload'));
d3.json(defaultURL).then(function(rawdata) {
  var data = rawdata.results[0];
  console.log(data);
  if (data == 0)
  {
    console.log("eneterd if block");
    d3.select('#demo').text("Success");
  }
  else 
  {
    console.log("eneterd else block");
    d3.select('#demo').text("Failure");
  }

});


