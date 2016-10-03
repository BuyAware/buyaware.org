    
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
            }
        },
        legend: {
            display: false,
        },
        responsive: false,
    } 

    /*
    ** When document is ready...
    */

    $(function(){

    /*
    ** Change color of rating label according to rating value
    */
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

    /*
    ** Generate radar chart for each product
    */

    $(".product-img canvas").each(function (arg) {

        // get color
        var bg = $(this).parent().parent().siblings(".product-text").children("#productName").children(".label").css("backgroundColor").replace(/^rgba?\(|\s+|\)$/g,'').split(',');

        var data = {
            labels: ["", "", "", "", "", ""],
            datasets: [
                {
                    label: "Phone Rating",
                    backgroundColor: "rgba("+bg[0]+","+bg[1]+","+bg[2]+", 0.3)",
                    borderColor: "rgba("+bg[0]+","+bg[1]+","+bg[2]+", 1)",
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
                        parseInt($(this).attr("PR"))]
                },
            ]
        };
        var myChart1 = new Chart($(this), {
            type: 'radar',
            data: data,
            options: options,
        });
    })

    /*
    ** Hover over product images makes radar chart appear
    */

    $(".product-img").hover(
        function (e) {
            var height = parseInt($(this).children("img").css("height"), 10);
            $(this).children("img").css({"opacity": "0.3"});
            $(this).children("canvas").css({
                "-ms-transform": "translateY(-" + height + "px)", /* IE 9 */
                "-webkit-transform": "translateY(-" + height + "px)", /* Chrome, Safari, Opera */
                "transform": "translateY(-" + height + "px)",
            });
        },
        function (e) {
            $(this).children("img").css({"opacity": "1"});
            $(this).children("canvas").css({
                "-ms-transform": "translateY( 0px)", /* IE 9 */
                "-webkit-transform": "translateY(0px)", /* Chrome, Safari, Opera */
                "transform": "translateY(0px)",

            });
        });

    $(".product-img").click(
        function (e) {
            $(this).children("img").css({"opacity": "1"});
            $(this).children("canvas").css({
                "-ms-transform": "translateY( 0px)", /* IE 9 */
                "-webkit-transform": "translateY(0px)", /* Chrome, Safari, Opera */
                "transform": "translateY(0px)",
            });
    });
});