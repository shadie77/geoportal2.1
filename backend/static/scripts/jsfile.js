// const slideshow = document.querySelectorAll('.slideshow-item'),
// dot = document.querySelectorAll('.dot');

// let counter = 1;
// slidefun(counter);

// let timer = setInterval(autoslide, 8000);
// function autoslide() {
//     counter += 1;
//     slidefun(counter);
// }

// function plusslide(n) {
//     counter += n;
//     slidefun(counter);
//     resetTimer();
// }

// function currentslide(n) {
//     counter = n;
//     slidefun(counter);
//     resetTimer();
// }

// function resetTimer() {
//     clearInterval(timer);
//     timer = setInterval(autoslide, 8000);
// }

// function slidefun(n) {
//     let i; 
//     for(i = 0; i<slideshow.length; i++) {
//         slideshow[i].getElementsByClassName.display = "none";
//     }

//     for(i = 0; i<dot.length; i++) {
//         dot[i].classList.remove('active')
//     }
//     if(n > slideshow.length) {
//         counter = 1;
//     }
//     if(n < i) {
//         counter = slideshow.length;
//     }
//     slideshow[counter - 1].style.display = "block";
//     dot[counter - 1].classList.add('active');
// }

const ctx = document.getElementById('myChart').getContext("2d");

const ptx = document.getElementById('donutChart').getContext("2d");


//Gradient fill
Chart.defaults.font.size = 10;
let gradient = ctx.createLinearGradient(0, 0, 0, 400);
gradient.addColorStop(0, "rgba(58, 123, 123, 1");
gradient.addColorStop(1, "rgba(0, 210, 255, 0.4");


// LINE CHART
//myChart labels
const labels = [
    '2012',
    '2013',
    '2014',
    '2015',
    '2016',
    '2017',
    '2018',
    '2019',
    '2020',
];

//myChart data
const data = {
    labels,
    datasets: [
        {
            data: [211, 326, 165, 350, 420, 370, 500, 375, 415],
            label: "Depth Travelled by Distance",
            fill: true,
            backgroundColor: gradient
        },
    ],
};


//myChart config
const config = {
    type : "line",
    data:data,
    options: {
        pointHoverBackgroundColor: 'rgba(54, 162, 235, 0.7)',
        pointRadius: 2,
        pointHoverRadius: 4,
        borderWidth: 1,
        
        responsive: true,
        scales: {
            y: {
                ticks: {
                    callback: function (value){
                        return '$' + value + "M"
                    }
                }
            }
        }
    },
};


// DOUGHNUT CHART
// donut data
const datapie = {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    datasets: [{
      title: 'Weekly Sales',
      data: [738, 732, 496, 611, 490, 226, 190],
      backgroundColor: [
        'rgba(255, 26, 104, 0.7)',
        'rgba(54, 162, 235, 0.7)',
        'rgba(255, 206, 86, 0.7)',
        'rgba(75, 192, 192, 0.7)',
        'rgba(153, 102, 255, 0.7)',
        'rgba(255, 159, 64, 0.7)',
        'rgba(0, 0, 0, 0.7)'
      ],
      hoverBackgroundColor:[
        'rgba(255, 26, 104, 0.9)',
        'rgba(54, 162, 235, 0.9)',
        'rgba(255, 206, 86, 0.9)',
        'rgba(75, 192, 192, 0.9)',
        'rgba(153, 102, 255, 0.9)',
        'rgba(255, 159, 64, 0.9)',
        'rgba(0, 0, 0, 0.9)'
      ],
      borderColor: [
        'rgba(255, 26, 104, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)',
        'rgba(0, 0, 0, 1)'
      ],
      borderWidth: 1,
      hoverOffset: 6,
    }]
  };

//donut config
const configpie = {
    type: 'doughnut',
    data: datapie,
    options: {
        rotation: 50,
        animation: {
            delay: 3000,
            duration: 2200,
            easing: 'easeInOutBounce',
            animateRotate: true,
            animateScale: true,
        },
        reponsive: true,
      scales: {
      },
      plugins: {
            title: {
                text: 'Daily boat count',
                display: true,
                color: 'rgba(0, 0, 0, .7)',
                position: 'top',
                align: 'start',
                font: {
                    size: 13,
                    weight: 500,
                },
                padding: {
                    top:8
                }
            },
            subtitle: {
                text: 'Badore Terminal',
                display: true,
                position: 'bottom',
                align: 'start'
            },
            legend: {
              display: true,
              position: 'right',
              align: 'center',
              labels: {
                  boxWidth: 15,
                  boxHeight: 10,
                  padding: 5,
                  usePointStyle: true,
                  pointStyle: 'rect'
                },
            },
            datalabels: {
              formatter: (value, context) => {
                const datapoints =context.chart.data.datasets[0].data;
                function totalSum(total, datapoint) {
                    return total + datapoint;
                }
                const totalValue = datapoints.reduce(totalSum, 0);
                const percentageValue = (value / totalValue * 100).toFixed(1);

                return `${percentageValue}%`
                }
            }
        }
    },
    plugins: [ChartDataLabels]
};

const myChart = new Chart(ctx, config)
const donutChart = new Chart(ptx, configpie)