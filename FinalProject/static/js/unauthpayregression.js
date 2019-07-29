
var defaultURL = "/static/resources/v1/unauthpayment/mlr";
d3.json(defaultURL).then(function(rawdata) {
  console.log(rawdata)
  var data = rawdata.results;
  var training_score = data[0][0];
  var testing_score = data[0][1];
  var mse = data[1][0];
  var r2 = data[1][1];

  var lasso_mse = data[2][0];
  var lasso_r2 = data[2][1];

  var ridge_mse = data[3][0];
  var ridge_r2=data[3][1];
  d3.select('#demo').text(training_score);
  d3.select('#demo1').text(testing_score);

  d3.select('#demo2').text(mse);
  d3.select('#demo3').text(r2);

  d3.select('#demo4').text(lasso_mse);
  d3.select('#demo5').text(lasso_r2);


  d3.select('#demo6').text(ridge_mse);
  d3.select('#demo7').text(ridge_r2);
});



// var endpoint = "/static/resources/v1/agent/mlr";
// d3.json(endpoint).then(function(rawdata) {
//   console.log(rawdata)
//   var data = rawdata.results;

//   var mse1 = data[0][0];
//   var r21= data[0][1];

//   var mse2 = data[1][0];
//   var r22 = data[1][1];

//   var mse3 = data[2][0];
//   var r23 = data[2][1];

//   var mse4 = data[3][0];
//   var r24 = data[3][1];

//   d3.select('#grp').text(mse1);
//   d3.select('#grp1').text(r21);

//   d3.select('#grp2').text(mse2);
//   d3.select('#grp3').text(r22);

//   d3.select('#grp4').text(mse3);
//   d3.select('#grp5').text(r23);


//   d3.select('#grp6').text(mse4);
//   d3.select('#grp7').text(r24);
// });



