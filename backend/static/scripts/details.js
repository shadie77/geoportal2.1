/*--------------------------------------------------------------------------------- */
/* DECLARE VARIABLES HERE */
/*--------------------------------------------------------------------------------- */
var ctx = document.getElementById("piechart").getContext('2d');
var ctx2 = document.getElementById('passengerpiechart').getContext('2d');
var ctx3 = document.getElementById("boatpiechart").getContext('2d');
var linechart1 = document.getElementById('linechart').getContext('2d');
var linechart2 = document.getElementById('linechart2').getContext('2d');
var traveloutchart = document.getElementById('travelout').getContext('2d');

const data = {
  labels: val.label_in,
  datasets: [{
    label: 'In',
    backgroundColor: 'rgb(255, 99, 132)',
    borderColor: 'rgb(255, 99, 132)',
    data: val.passenger_in,
    },
    {
        label: 'out',
        backgroundColor: 'rgb(25, 23, 12)',
        borderColor: 'rgb(25, 23, 12)',
        data: val.passenger_out, 
    }

    ]
  };

/*-----------------------------------------------------------------------------------*/

/*------------------------------------------------------------------------------------ */
//SLIDE DOWN FUCTION
/*------------------------------------------------------------------------------------ */



/*------------------------------------------------------------------------------------*/
/* CHART FUNCTIONS
/*------------------------------------------------------------------------------------*/

function showPie(docid, data1, data2){
var myChart = new Chart(docid, {
    type: 'doughnut',
    data: {
        datasets: [{    
            data: [data1, data2], // Specify the data values array
          
            borderColor: ['#2196f38c', '#f443368c'], // Add custom color border 
            backgroundColor: ['#2196f38c', '#f443368c'], // Add custom color background (Points and Fill)
            borderWidth: 0 // Specify bar border width
        }]},         
    options: {
        layout :{
            margin: {
                left:0
            },
            padding:{
                left:-10
            }
        },
        
    cutoutPercentage: 84,
    responsive: true, // Instruct chart js to respond nicely.
    maintainAspectRatio: false, // Add to prevent default behaviour of full-width/height 
    }
});
}

function showLineChart(docid){
    const showLine = new Chart(docid, {
        type: 'line',
        data: data,
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'top',
            },
            title: {
              display: true,
              text: 'Chart.js Line Chart'
            }
          }
        },
      })

}

/*------------------------------------------------------------------------------------------------------------*/

/*------------------------------------------------------------------------------------------------------------*/
// 3D SURFACE PLOT HERE
/*------------------------------------------------------------------------------------------------------------*/
 
// Turn this to function
var bathymetry_data = [{
            x: bathymetry.x,
            y: bathymetry.y,
           z: bathymetry.z,
           type: 'surface'
        }];

var bathymetry_layout = {
  autosize: true,
  width: 500,
  height: 300,
  margin: {
    l: 0,
    r: 0,
    b: 0,
    t: 0,
  },
  scene: {
    aspectmode: "manual",
    aspectratio: {
        x: 1.2, y: 1.6, z: 1,
    },
}
};
Plotly.newPlot('batthyy', bathymetry_data, bathymetry_layout,{displayModeBar: false, responsive: true});




// 3D SURFACE PLOT ENDS
/*------------------------------------------------------------------------------------------------------------*/


/*------------------------------------------------------------------------------------------------------------*/
// HORIZONTAL BAR CHART HERE
/*------------------------------------------------------------------------------------------------------------*/
function plotBar(chartdata, chartlabels, div){
  var testdata = {
    labels: chartlabels,
    datasets: [
    {
      "label": "Total V",
      "yAxisID": "A",
      "backgroundColor": "rgba(53,81,103,1)",
      "borderColor": "rgba(53,81,103,.4)",
      "data": chartdata
    }]
  };
  
    var options = {scales:{
    yAxes:
    [
    {id: 'A',
    position: 'right',
  display:true,
  gridLines:{color:"rgba(53,81,103,.4)"}
  },],
  xAxes: 
  [{ 
    barPercentage: 0.4,
    display:true,
    id:"1",
    position: 'top',
  
    ticks:{
      fontColor: 'rgb(0, 0, 0)'},
    fontSize:500,
    beginAtZero: true
  }],
  }};
new Chart(div, {type: "horizontalBar",data:testdata, options:options});
}
//END OF BAR CHART HERE
/*------------------------------------------------------------------------------------------------------------*/

showPie(ctx, 70,30)
showPie(ctx2, passengerOut, passengerIn)
showPie(ctx3, boatOut, boatIn)
showLineChart(linechart1)
showLineChart(linechart2)

lebl = ['Lel1', 'Label2', 'Label3', 'Label4', 'Label5', 'Label6', 'Label7','label8', "label9", 'label10']
plotBar([100,40,30,70,60, 10, 70, 20, 30, 20], lebl, traveloutchart)
