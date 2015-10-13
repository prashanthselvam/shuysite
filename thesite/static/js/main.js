$('#small-nav').click(function() {
	$('#small-menu').animate({
		opacity: 0.92,
	}, 400).css('z-index',1400);
	$(this).animate( {opacity:'0'}, {duration:250});
});

$('#close-button').click(function() {
	$('#small-menu').animate({
		opacity:0,
	}, 250, function() {
		$('#small-menu').css('z-index', -5);
	});
	$('#small-nav').animate( {opacity:'100'}, {duration:200});
});

$(document).ready(function(){
	$("a[rel^='lightbox']").prettyPhoto();
});

$(document).ready(function() {
    $('#page-content').fadeIn();
});


$(function(){
	$(window).scroll(function() {
		if ($(this).scrollTop() >= 144) {
			$('#prof-pic').addClass('fixed');
		}
		else {
			$('#prof-pic').removeClass('fixed');
		}
	});
});


$('.carousel').carousel();


var fadeStart=80 // 100px scroll or less will equiv to 1 opacity
    ,fadeUntil=250 // 200px scroll or more will equiv to 0 opacity
    ,fading = $('#gd-cover')
;

$(window).bind('scroll', function(){
    var offset = $(window).scrollTop()
    ;
    if( offset<=fadeStart ){
        opacity=0;
        display='none';
    }else if (offset <= $(document).height()) {
        opacity= 0 + ((offset - fadeStart)/($(document).height()-$(window).height()-fadeStart));
        display='block';
    }
    fading.css('opacity',opacity).css('display',display).html(opacity);
});

