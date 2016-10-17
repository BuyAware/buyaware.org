    
    /*
    ** colors
    */

    var colors = {
        green: "0,128,0,", // green 
        orange: "255,165,0,", //orange
        red: "255,0,0,", //red
        yellow: "255,255,0,", //yellow
    };

    /*
    ** Radar chart options
    */ 
    var options = {
        scale: {
            ticks: {
                display: false,
                beginAtZero: true,
                max: 100,
                stepSize: 20,
            },
            gridLines: {
                color: "white",
            },
            angleLines: {
                color: "white",
            },
        },
        legend: {
            display: false,
        },
        responsive: false,
    } 

    /*
    **  Random data functions 
    */

    function getRandomData(dataPoints){
        var data = [];
        for(var i=0; i<dataPoints; i++){
            data.push(Math.floor(Math.random()*100));
        }
        return data;
    }

    function getColorString(colorName, alpha){
        return "rgba(" + colors[colorName] + alpha + ")";
    }

    function getRandomColorKey(){
        var colorKeys = Object.keys(colors);
        return colorKeys[Math.floor(Math.random()*colorKeys.length)]
    }


$(function(){

    // initial dataset
    var data = {
        labels: ["", "", "", "", "", ""],
        datasets: [
        {
            label: "",
            backgroundColor: "rgba(0,128,0,0.7)", //green
            borderColor: "rgba(0,128,0,1)",
            pointBackgroundColor: "rgba(0,128,0,1)",
            pointBorderColor: "#fff",
            pointHoverBackgroundColor: "#fff",
            pointHoverBorderColor: "rgba(179,181,198,1)",
            data: [65, 59, 90, 81, 56, 55]
        },
        ]
    };

    var  animatedChart = new Chart($("canvas#animatedChart"), {
        type: 'radar',
        data: data,
        options: options,
    }); 


    /*
    ** Intervall timer to update the animated chart
    */
    setInterval(function (){ 

        var randomColor = getRandomColorKey();

        //update randomly one of two displayed charts
        data.datasets[Math.floor(Math.random()*2)] = ({
            backgroundColor: getColorString(randomColor, 0.7),
            borderColor: getColorString(randomColor, 1),
            pointBackgroundColor: getColorString(randomColor, 1),
            pointBorderColor: "#fff",
            pointHoverBackgroundColor: "#fff",
            pointHoverBorderColor: "rgba(179,181,198,1)",
            data: getRandomData(6),
        });

        //display it
        animatedChart.update();

    }, 5000); // update every 5 seconds

});