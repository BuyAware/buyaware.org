$(function(){
    var animspeed = 950; // animation speed in milliseconds
    var last_opened = null; // last opened expand button
  
    // **********************************
    // Text expnasion for timeline events
    // **********************************

    $(".bigtext.timeline-body").each( function(e){
	var height = $(this).height();
	var mini = 0;
	
	$(this).attr('data-fullheight',height+'px');
	$(this).attr('data-miniheight',mini+'px');
	$(this).css('height',mini+'px');
  });  
    
    // **********************************
    // Text expansion for member profiles 
    // **********************************

    $(".bigtext.profile").each( function(e){
	var height = $(this).height() + 10;
	var mini = 100;
	
    $(this).attr('data-fullheight',height+'px');
	$(this).attr('data-miniheight',mini+'px');
	$(this).css('height',mini+'px');
    });
    
    // **********************************
    // Expand and reduce animations
    // **********************************

    // Usage:
    // <div class="bigtext [other class]">...</div>
    // <p class="expand [close-last]">More <i class="fa fa-arrow-down"></i></p>
    // <p class="contract hide">Hide <i class="fa fa-arrow-up"></i></p>

    // Function: close last expanded bigtext
    // Usage: class="expand close-last" (always use with expand)
     $('.close-last').on('click', function(e){
	if(last_opened){
	    $text = last_opened.prev();
	
	    $text.animate({
		'height': $text.attr('data-miniheight')
	    }, animspeed);
	    last_opened.removeClass('hide');
	    last_opened.next('.contract').addClass('hide');
	}
    });
    

    // Function: expand bigtext
    $('.expand').on('click', function(e){
	$text = $(this).prev();
	last_opened = $(this);
	
	$text.animate({
	    'height': $text.attr('data-fullheight')
	}, animspeed);
	$(this).next('.contract').removeClass('hide');
	$(this).addClass('hide');
    });
    
    // Function: contract bigtext
    $('.contract').on('click', function(e){
	$text = $(this).prev().prev();
	
	$text.animate({
	    'height': $text.attr('data-miniheight')
	}, animspeed);
	$(this).prev('.expand').removeClass('hide');
	$(this).addClass('hide');
    });

});

