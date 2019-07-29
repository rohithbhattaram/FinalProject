var endpoint = "/static/resources/v1/native/nlp";
d3.json(endpoint).then(function(rawdata) {
  console.log(rawdata)
  var data = rawdata.results;

  var aacc = data[0];
  var iacc= data[0];

 
  d3.select('#demo').text(aacc).style('fill','red');

  d3.select('#demo1').text(iacc).style('fill','red');


});