



// Two charts definition
var  chart2;

// Once DOM (document) is finished loading
$(document).ready(function() {


    // Second chart initialization (pie chart)
    chart2 = new Highcharts.Chart({
        chart: {
            renderTo: 'chart_2',
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            height: 350,
        },
        title: {
            text: 'community '
        },
        tooltip: {
            pointFormat: '<b>{point.percentage}%</b>',
            percentageDecimals: 1
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false
                },
                showInLegend: true
            }
        },
         series: [{
         type: 'pie',
            name: 'Dev #1',
            data: [
                ['com1', 5],
                ['com2', 15],
                ['com3', 20],
                ['com4', 22],
                ['com5', 25],
      
            ]
         }]
    });


});