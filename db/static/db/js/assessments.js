    
    /*
    ** Radar chart options
    */ 
    var options = {
        scale: {
            ticks: {
                display: false,
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
    ** Generate radar chart for each product
    */

    $(".product-img canvas").each(function (arg) {
        var data = {
            labels: ["", "", "", "", "", ""],
            datasets: [
                {
                    label: "My First dataset",
                    backgroundColor: "rgba(179,181,198,0.2)",
                    borderColor: "rgba(179,181,198,1)",
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

});