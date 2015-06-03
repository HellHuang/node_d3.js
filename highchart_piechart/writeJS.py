__author__ = 'fen'
filepath="piechart.js"
comNum=10
dict={0:10,1:90,2:50,3:10,4:70,5:20,6:17,7:86,8:34,9:20}
def writJS(filepath,comNum,dict):
    JSfile=open(filepath,"w")
    JSfile.write("var  chart2;"+"\n")
    JSfile.write("$(document).ready(function() {"+"\n"+
    "chart2 = new Highcharts.Chart({"+"\n"+
        "chart: {"+"\n"+
            "renderTo: 'chart_2',"+"\n"+
            "plotBackgroundColor: null,"+"\n"+
            "plotBorderWidth: null,"+"\n"+
            "plotShadow: false,"+"\n"+
            "height: 350,"+"\n"+
        "},"+"\n"+
        "title: {"+"\n"+
            "text: 'community '"+"\n"+
        "},"+"\n"+
        "tooltip: {"+"\n"+
            "pointFormat: '<b>{point.percentage}%</b>',"+"\n"+
            "percentageDecimals: 1"+"\n"+
        "},"+"\n"+
        "plotOptions: {"+"\n"+
            "pie: {"+"\n"+
                "allowPointSelect: true,"+"\n"+
                "cursor: 'pointer',"+"\n"+
                "dataLabels: {"+"\n"+
                    "enabled: false"+"\n"+
                "},"+"\n"+
                "showInLegend: true"+"\n"+
            "}"+"\n"+
        "},"+"\n"+
             "series: [{"+"\n"+
         "type: 'pie',"+"\n"+
            "name: 'Dev #1',"+"\n"+
            "data: ["+"\n")
    for i in range(comNum):
        JSfile.write("['com"+str(i+1)+"',"+str(dict[i])+"],"+"\n")
    JSfile.write("]"+"\n"+"}]"+"\n"+"});"+"\n"+"});")
    JSfile.close()

writJS(filepath,comNum,dict)