"use strict";
// **** jQuery *****
$(document).ready(function(){
	$('body').on(function(){
		console.log("document ready for jQuery");
		var
			topitem=['First Name','Last Name','Email Address','Contat #']
			;
		$('*').css({
			'margin':'0px'
			,'padding':'0px'
		})
		$('body').append('<div id="top"></div>');
		$('top').append('<ul></ul>');
		$('ul').css({
			'margin':'0px'
			,'padding':'0px'
			,'display':'none'
		});
		$('ul').append('<li></li>');
		for (var i=0;i<topitem.legth;i++){
			$('li').append(topitem[i]);
		}
		$('li').css({
			'border':'1px solid black'
			,'border-left':'none'
			,'border-right':'none'
			,'display':'inline'
			,'width':'80px'
		})

		$('top').css({
			'display':'inline-block'
		});

		
		$('body').html('<div id="mid"></div>');
		$('body').append('<h1>Add User</h1>');
		
		$('body').html('<inpout type="button" value="Add User"');
		
	})




});

// **** JavaScript *****
function sampleFunction (arr) {

  for(var i=0;i<arr.length;i++)
  {
    console.log(arr[i]);
  }  

  console.log("The input array of objects: "+arr);

}

var myLoc = { 'city': 'Dallas' };
var foo=[ true, null, ('version'+2.0), {'a_key':'a_value'}, myLoc ];

sampleFunction(foo);