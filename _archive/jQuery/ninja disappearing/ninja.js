"use strict";
/* yung chou.
	 The parameterization below is not all necessary and 
	 code is for demonstraing jQuery usage, not optimizaiton.
*/
var go = console.log("ninja's ready...");

var jqcontainer='container',
		htag='h1',
	 	heading='Disappearing Ninja',
		imgsrc='ninja.png',
		abutton='<input id="restore" type="button" value="Restore">';

$(document).ready(function(){
	go;
	
	//--------------------
	// 1. BUILD HTML PAGE
	//--------------------

	// Add a container for dynamic content from jQuery
	$('body').html('<div id="container"></div>');
	$('#container').css({
		'width': '770px'
		,'margin':'10px auto'
		,'padding': '0px'
	})
	
	// Add the heading
	$('#container').html('<h1>'+heading+'</h1>');
	$('#container h1').css({'text-align':'center'});
	
	// Load the images
	for (var row=1;row<3;row++){

		// Make each row a div for positioning
		$('#container').append('<div id="row'+row+'"></div>');
		$("#row"+row).css({'width': '100%'})

		// Add the img tag. Also notice "#row"+row results as a string
		// and there is no need to be wrapped with '' or "". 
		$("#row"+row).html('<img src="'+imgsrc+'">');

		for (var i=2;i<5;i++){
			$("#row"+row).append('<img src="'+imgsrc+'">');
			$("#row"+row+' img').css({
				'border':		'1px solid black'
				,'display':	'inline-block'
				,'margin':		'10px 10px'
				,'width':		'170px'
			})
		}			
	}

	// Add a buttonfor restoring the image
	$('#container').append(abutton);
	$('#restore').css({
		'margin':'0px 10px'
		,'padding':'5px 20px'
		,'background-color':'lightgreen'
	});
	
	//--------------------------------
	// 2. Connfigure jQuery selectors
	//--------------------------------

	$('#container img').click(function(){
		$(this).css('visibility','hidden');
	});
	$('#restore').click(function(){
		$('#container img').css('visibility','visible')
	});
})