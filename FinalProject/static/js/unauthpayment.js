var endpoint = "/static/resources/v1/agent/mlr";
d3.json(endpoint).then(function(rawdata) {
  console.log(rawdata)
  var data = rawdata.results;

  var mse1 = data[0][0];
  var r21= data[0][1];

  var mse2 = data[1][0];
  var r22 = data[1][1];

  var mse3 = data[2][0];
  var r23 = data[2][1];

  var mse4 = data[3][0];
  var r24 = data[3][1];

  d3.select('#grp').text(mse1);
  d3.select('#grp1').text(r21);

  d3.select('#grp2').text(mse2);
  d3.select('#grp3').text(r22);

  d3.select('#grp4').text(mse3);
  d3.select('#grp5').text(r23);


  d3.select('#grp6').text(mse4);
  d3.select('#grp7').text(r24);
});
