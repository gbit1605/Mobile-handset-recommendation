$(document).ready(function() {

	$('form').on('submit', function(event) {
		
		var btn = $(document.activeElement).val();

		$.ajax({
			data : {
				name1 : btn,
				name2 : "",
				name3 : "",
				name4 : "",
				name5 : "",
				reviews : "",
				description: "",
				features: "",
				namess: ""
				
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {
			
				
				disp_head1="PEOPLE ALSO VIEWED";
				disp_head2="REVIEWERS ALSO SAID";
				disp_head3="DESCRIPTION";
				disp_head4="FEATURES";
				disp1=data.name1;
				disp2=data.name2;
				disp3=data.name3;
				disp4=data.name4;
				disp5=data.name5;
				
				disp_r=data.reviews;
				
				d=data.description;
				f=data.features; 
				final_name=data.namess;
				
				$('#n').text(final_name).show();
				$('#descrip').text(disp_head3).show();
				$('#descri').text(d).show();
				$('#feas').text(disp_head4).show();
				$('#fea').text(f).show();
				$('#head2').text(disp_head2).show()
				$('#rws').text(disp_r).show();
				$('#head1').text(disp_head1).show();
				$('#p1').text(disp1).show();
				$('#p2').text(disp2).show();
				$('#p3').text(disp3).show();
				$('#p4').text(disp4).show();
				$('#p5').text(disp5).show();
								
				
				

		});

		event.preventDefault();

	});

});


var status=1;
function changeStyle()
{
	var x=document.getElementById();
	
	if (status==1)
	{
		x.style.background= 'yellow';
	}
	
	document.getElementById('bigpic').style.display='block';
}
