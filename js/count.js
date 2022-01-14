(function($){
    $.fn.numberRock=function(options){
        var defaults={
            lastNumber:100,
            duration:2000,
            easing:'swing'  //linear(匀速)
        };
        var opts=$.extend({}, defaults, options);

        $(this).animate({
            num : "numberRock",
        },{
            duration : opts.duration,
            easing : opts.easing,
            complete : function(){
                console.log("success");
            },
            step : function(a,b){
                $(this).html(parseInt(b.pos * opts.lastNumber));
            }
        });

    }

})(jQuery);