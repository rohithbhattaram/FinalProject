


var defaultURL = "/static/resources/v1/data/failure";
d3.json(defaultURL).then(function(rawdata) {
  var data = rawdata.results;

  

// var fail_info = data;
var counter = true 

function base_lodaing(info)
{
    
    //console.log(data);
    var tbody = d3.select("tbody");
    tbody.html("");
    info.forEach(faildata => {
    //console.log(faildata)
    var row= tbody.append("tr");
        Object.entries(faildata).forEach(([key,value])=> {
                //console.log(key,value);
                var cell = row.append("td");
                cell.text(value)
            })
    })
}


base_lodaing(data);










var filter = d3.select("#filter-btn");

// Use D3 `.on` to attach a click handler for the filter
filter.on("click", function() {

counter = false; 
d3.event.preventDefault();
    // Select the input element and get the raw HTML node
var inputElement = d3.select("#LoginID");
var inputValue = inputElement.property("value");
console.log(inputValue);


function id_filter(fail) 
{
    console.log("Control enetered here");
    console.log(fail.LOGINID);
    return fail.LOGINID===inputValue;
        
}

if (inputValue.length > 0){
var selected_type = data.filter(id_filter);
console.log(`xyz : ${selected_type}`);

base_lodaing(selected_type);}
else {
    base_lodaing(data);
}


});
});
