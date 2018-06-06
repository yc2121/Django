"use strict";
/* yung chou.
	 The parameterization below is not all necessary and 
	 code is for demonstraing jQuery usage, not optimizaiton.
*/
var go = console.log("ninja2cat is ready...");

var 
	htag='h1'
	,heading='Ninja2cat'
	,imgfolder='img'
	,n=['ninja0.png','ninja1.png','ninja2.png','ninja3.png','ninja4.png']
	,c=['cat0.png','cat1.png','cat2.png','cat3.png','cat4.png']
	,abutton='<input id="restore" type="button" value="Restore">'
	;

$(document).ready(function(){
	go;
	
	//--------------------
	// 1. BUILD HTML PAGE
	//--------------------

	// Add a container for dynamic content from jQuery
	$('body').html('<div id="container"></div>');
	$('#container').css({
		'width': '400px'
		,'margin':'10px auto'
		,'padding': '0px'
	});
	
	// Add the heading
	$('#container').html('<h1>'+heading+'</h1>');
	$('#container').css({
		'text-align':'center'
	});
	
	// Load the images
	$('#container').append('<div id="images"></div>');
	$('#images').css({
		'display':'block'
		,'margin':'0px auto'
	})

	if (n.length==c.length) {
		for (var i=0;i<n.length;i++){
			$('#images').append(
				'<img id="'+i+'" src="'+imgfolder+'/'+n[i]
				+'" cat="'+imgfolder+'/'+c[i]
				+'">'
			);
		}
		$('#images').css({
			'width':'200px'
		});
	} else {
		cosole.log('[ERROR] The two arrays muat have the same length.')
	}
	
	//--------------------------------
	// 2. Connfigure jQuery selectors
	//--------------------------------
	var changetocat=true
			,target;
	$('#container img').click(function(){
		if (changetocat) {
			target=c;
			changetocat=false;
		} else {
			target=n;
			changetocat=true;
		}
		$(this).attr('src', imgfolder+'/'+target[$(this).attr('id')]);
	})

}) //end of $(document)
