d3.json('/names', (error, response) => {
    var todoList = document.querySelector("#selDataset");
    todoHTML = '';
    for (var i = 0; i < response.length; i++) {
        todoHTML += "<option>" + response[i] + "</option>";
    }
    todoList.innerHTML = todoHTML;
});

function updateOtuDes(labels) {
    d3.json('/otu', (error, response) => {
        // var todoList = document.querySelector("#selOtu");
        hoverList=[];
        for (var i = 0; i < labels.length; i++) {
            value_otudes = labels[i];
            hoverList.push(response[value_otudes]) 
        }
    })
};
    

Plotly.d3.json('/values', function (error, response) {
    // if (error) return console.warn(error);
    var layout1 = {
        height: 500,
        width: 500,
        title: "PIE CHART",
        l: 50,
        r: 50,
        // plot_bgcolor='rgba(0,0,0,0)'
        // margin: { t: 30, b:100 }
    }
    Plotly.plot('pie4', [response], layout1);
});

d3.json('/metadata/<sample>', function (error, response) {
    if (error) return console.warn(error);
    var todoList = document.querySelector("#selMeta");
    var todoHTML='';
    var sample = 'BB_1233'
    var j = 0;

    for (i = 0; i < response.length; i++) {
        var object = response[j];
        // otu_ids_list = object[sample]['otu_ids'];
        if (Object.keys(object) == sample) {
            // todoHTML = '';
            todoHTML += "<p> AGE: " + parseInt(object[sample].AGE) + "</p>";
            todoHTML += "<p> BBTYPE: " + String(object[sample].BBTYPE) + "</p>";
            todoHTML += "<p> ETHNICITY: " + object[sample].ETHNICITY + "</p>";
            todoHTML += "<p> GENDER: " + object[sample].GENDER + "</p>";
            todoHTML += "<p> LOCATION: " + object[sample].LOCATION + "</p>";
            todoHTML += "<p> SAMPLEID: " + parseInt(object[sample].SAMPLEID) + "</p>";
            todoList.innerHTML = todoHTML;
        }
        j++;
    }

})




// Plotly.d3.json('/samples/<sample>', function(error, response) {
//     // if (error) return console.warn(error);
//     plot_trace = {
//         "labels": response[0].BB_940.otu_ids,
//         "values": response[0].BB_940.sample_values,
//         "type": "pie"
//     }
//     console.log("plot_trace", plot_trace)
//     var layout1 = {
//         height: 500,
//         width:500,
//         title: "PIE CHART",
//         l: 50,
//         r: 50
//         // margin: { t: 30, b:100 }
//         }
//     var data_val = [plot_trace]
//     Plotly.plot('pie4', data_val, layout1);
// });

// Update the plot with new data
function updatePlotly(newdata) {
    var Bar = document.getElementById('pie4');
    Plotly.restyle(Bar, 'labels', [newdata.labels])
    Plotly.restyle(Bar, 'values', [newdata.values])
    // Plotly.restyle(Bar, 'hoverinfo', [newdata.hoverinfo])
}

function updateScatter(trace, error) {
    if (error) return console.warn(error);
    var Bar = document.getElementById('pie6');

    // var size_val = [];
    // for (i = 0; i < values.length; i++) {
    //     size_val.push(values[i]*10)
    // }
    // var trace1 = {
    //     x: labels,
    //     y: values,
    //     mode: 'markers',
    //     marker: {
    //     size: size_val ,
    //     color: [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]
    //     }
    //   };

    // var data = [trace];

    // var layout = {
    //     height: 550,
    //     width: 1750,
    //     title: 'Scatter Plot with a Color Dimension'
    // };

    Plotly.restyle('pie6', 'x', [trace.x]);
    Plotly.restyle('pie6', 'y', [trace.y]);
}

// // Get new data whenever the dropdown selection changes
// function optionChanged(sample) { 
//     // console.log(sample);
//     Plotly.d3.json('/samples/<sample>', function(error, response) {
//         if (error) return console.warn(error);
//         sample_index = parseInt(sample.slice(3,));
//         plot_trace = {
//             "labels": response[sample_index].otu_ids,
//             "values": response[sample_index].sample_values,
//             "type": "pie"
//         }
//         // route_date = data.index
//         // console.log("newdata", data);
//         updatePlotly(plot_trace);
//     });
// }

// Get new data whenever the dropdown selection changes
function optionChanged(sample) {
    // console.log(sample);
    Plotly.d3.json('/samples/<sample>', function (error, response) {
        if (error) return console.warn(error);
        var labels = [];
        var values = [];
        // var hoverList = [];
        var j = 0;
        for (i = 0; i < response.length; i++) {
            var object = response[j];
            // otu_ids_list = object[sample]['otu_ids'];
            if (Object.keys(object) == sample) {
                labels = object[sample].otu_ids;
                values = object[sample].sample_values;
            }
            j++;
        }
        

        // Plotly.d3.json('/otu', function (error, response) {
        //     if (error) return console.warn(error);
        //     for (o = 0; o < labels.length; o++) {
        //         var val = labels[o];
        //         hoverList.push(response[val]);
        //     }
        
        var hoverList = updateOtuDes(labels);
        plot_trace = {
            "labels": labels,
            "values": values,
            "type": "pie",
            "text": hoverList,
            hovertext: 'text'
        },

        updatePlotly(plot_trace)

        var size_val = [];
        for (i = 0; i < values.length; i++) {
            size_val.push(values[i]*10)
        }
        trace1 = {
            x: labels,
            y: values,
            mode: 'markers',
            marker: {
            size: size_val ,
            color: [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]
            }
        };
        updateScatter(trace1, error),

        // updateTable(sample);
        d3.json('/metadata/<sample>', function (error, response) {
            if (error) return console.warn(error);
            var todoList = document.querySelector("#selMeta");
            var j = 0;
            var AGE = 0;
            var BBTYPE = '';
            var ETHNICITY = '';
            var GENDER = '';
            var LOCATION = '';
            var SAMPLEID = 0;
            for (i = 0; i < response.length; i++) {
                var object = response[j];
                // otu_ids_list = object[sample]['otu_ids'];
                if (Object.keys(object) == sample) {
                    var AGE = object[sample].AGE;
                    var BBTYPE = object[sample].BBTYPE;
                    var ETHNICITY = object[sample].ETHNICITY;
                    var GENDER = object[sample].GENDER;
                    var LOCATION = object[sample].LOCATION;
                    var SAMPLEID = object[sample].SAMPLEID;
                }
                j++;
            }

            todoHTML = '';
            todoHTML += "<p> AGE: " + parseInt(AGE) + "</p>";
            todoHTML += "<p> BBTYPE: " + String(BBTYPE) + "</p>";
            todoHTML += "<p> ETHNICITY: " + ETHNICITY + "</p>";
            todoHTML += "<p> GENDER: " + GENDER + "</p>";
            todoHTML += "<p> LOCATION: " + LOCATION + "</p>";
            todoHTML += "<p> SAMPLEID: " + parseInt(SAMPLEID) + "</p>";
            todoList.innerHTML = todoHTML;

        })
        
        })
    }
    







    // -----------------------------------------------------------------

    // d3.select("#pie4").on("mouseover", function() {
    // // Grab otuid from pie slice on mouseover
    // //   var otu_id_hover = d3.select(this)
    //   console.log(this);



    // var queryURL = "https://api.giphy.com/v1/gifs/trending?api_key=dc6zaTOxFJmzC";
    // d3.json(queryURL, function (error, response) {
    //     if (error) return console.warn(error);
    //     console.log("url", response);
    //     var url = response.data[0].images.fixed_height.url;
    //     d3.select(".imgGoesHere").append("img").attr("src", url);
    // })




    var data = [{
        values: [19, 26, 55],
        labels: ['Residential', 'Non-Residential', 'Utility'],
        type: 'pie'
    }];
    var layout = {
        height: 500,
        width: 500,
        l: 50,
        r: 50
    };
    Plotly.plot('pie5', data, layout);
    // Plotly.plot('pie6', data, layout);
// -----------------------------------------------------------------------------

function examplePlot() {
    Plotly.d3.json('/samples/<sample>', function (error, response) {
        if (error) return console.warn(error);
        var sample = 'BB_1233'
        var labels = [];
        var values = [];
        // var hoverList = [];
        var j = 0;
        for (i = 0; i < response.length; i++) {
            var object = response[j];
            // otu_ids_list = object[sample]['otu_ids'];
            if (Object.keys(object) == sample) {
                labels = object[sample].otu_ids;
                values = object[sample].sample_values;
            }
            j++;
        }
    var size_val = [];
    for (i = 0; i < values.length; i++) {
        size_val.push(values[i]*10)
    }
    var trace1 = {
        x: labels,
        y: values,
        mode: 'markers',
        marker: {
        size: size_val ,
        color: [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]
        }
      };

    var data = [trace1];

    var layout = {
        height: 550,
        width: 1750,
        title: 'Scatter Plot with a Color Dimension'
    };

    Plotly.newPlot('pie6', data, layout);
});
}
examplePlot();
