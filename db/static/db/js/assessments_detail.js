animspeed = 0.5;

$(function(){

    // color badges
    $(".label").each(function(args){
        var rating_value = parseInt($(this).html());
        if( rating_value >= 50){
          if(rating_value >= 75){
            $(this).css("backgroundColor", "green");
          } else {
            $(this).css("backgroundColor", "yellow");
          }
        }else{
          if(rating_value >=25){
            $(this).css("backgroundColor", "orange"); 
          } else {
            $(this).css("backgroundColor", "red"); 
          }
        }
    });

    // Make chart
    var canvas = $("canvas");
    var baseChart;
    var bg = $("#overall").css("backgroundColor").replace(/^rgba?\(|\s+|\)$/g,'').split(',');
    var data = {
        labels: ["CE", "EC", "WR", "CM", "TR", "PR"],
        datasets: [
        {
            label: $("canvas").attr("id"),
            backgroundColor: "rgba("+bg[0]+","+bg[1]+","+bg[2]+", 0.3)",
            borderColor: "rgba("+bg[0]+","+bg[1]+","+bg[2]+", 1)",
            pointBackgroundColor: "rgba(179,181,198,1)",
            pointBorderColor: "#fff",
            pointHoverBackgroundColor: "#fff",
            pointHoverBorderColor: "rgba(179,181,198,1)",
            data: [
            parseInt(canvas.attr("CE")),
            parseInt(canvas.attr("EC")),
            parseInt(canvas.attr("WR")),
            parseInt(canvas.attr("CM")),
            parseInt(canvas.attr("TR")),
            parseInt(canvas.attr("PR")),
            ]
        },
        ]
    };
    baseChart = new Chart(canvas, {
        type: 'radar',
        data: data,
        options: {
            scale: {
                ticks: {
                    beginAtZero: true,
                    max: 100,
                    stepSize: 20,
                }
            },
            legend:{
              display:false,
          }
      }
    }); 

    // Make comparison charts appear when other phone is selected
    $("ul.product-selector > li > a").click(function (args){
        // add dataset of other product
        data.datasets[1] = ({
            label: $(this).html(),
            backgroundColor: "rgba(0, 0, 255, 0.3)",
            borderColor: "rgba(0, 0, 255, 1)",
            pointBackgroundColor: "rgba(179,181,198,1)",
            pointBorderColor: "#fff",
            pointHoverBackgroundColor: "#fff",
            pointHoverBorderColor: "rgba(179,181,198,1)",
            data: [
            parseInt($(this).attr("CE")),
            parseInt($(this).attr("EC")),
            parseInt($(this).attr("WR")),
            parseInt($(this).attr("CM")),
            parseInt($(this).attr("TR")),
            parseInt($(this).attr("PR")),
            ]
        });
        //display it
        baseChart.update();
        //change the label on the dropdown menu to the one of the selected phone
        $(this).parent().parent().parent().children("button").html($(this).html());
    });  

});
