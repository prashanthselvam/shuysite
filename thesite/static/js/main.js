$('#small-nav').click(function() {
	$('#small-menu').animate({
		opacity: 0.92,
	}, 400).css('z-index',1400);
	$(this).animate( {opacity:'0'}, {duration:250});
});

$('#close-button').click(function() {
$('#small-menu').animate( {opacity:'0'}, {duration:250}).fadeTo('slow', 0 ).css('z-index',-1);
$('#small-nav').animate( {opacity:'100'}, {duration:200});
});

$(document).ready(function(){
	$("a[rel^='lightbox']").prettyPhoto();
});

$(document).ready(function() {

	$('#page_content').css('display', 'none');

	$('#page_content').fadeIn(1000);



	$('.link').click(function() {

		event.preventDefault();

		newLocation = this.href;

		$('#page_content').fadeOut(1000, newpage);

	});

	function newpage() {

		window.location = newLocation;

	}

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


