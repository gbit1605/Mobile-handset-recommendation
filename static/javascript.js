$(document).ready(function() {

	$('form').on('submit', function(event) {
		
		var btn = $(document.activeElement).val();

		$.ajax({
			data : {
				name1 : btn,
				name2 : "",
				name3 : "",
				name4 : "",
				name5 : ""
				
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

				$('#p1').text(data.name1).show();
				$('#p2').text(data.name2).show();
				$('#p3').text(data.name3).show();
				$('#p4').text(data.name4).show();
				$('#p5').text(data.name5).show();
				
				

		});

		event.preventDefault();

	});

});