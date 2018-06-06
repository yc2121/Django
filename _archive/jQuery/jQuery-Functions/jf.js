$(document).ready(function(){

  console.log('DOM ready for jQuery');

  var flagged = false;
  var c='black',hc='white',bg='white', hbg='lightgreen';
  var imgsrc=['HTML.png','JavaScript.png','nodejs.png','python.png'];

  $(document).on('click','#click', function(){
    console.log('Clicked the "click" button.');
    if (flagged) {
       $('#displayarea').css({'color':c,'background-color':bg});
        flagged=false;      
    } else {
      $('#displayarea').css({'color':hc,'background-color':hbg});
      flagged=true;      
    }
  });

  $(document).on('click','#show-hide', function(){
    console.log('Clicked the "show-hide" button.');
    $('#displayarea').html(
      '<img id="shownit" class=".added" src="Python.png">'+
      '<img id="hideit" class=".added" src="JavaScript.png" display="none"><p>Something else hidden? ('+flagged+')</p>');

      if (flagged) {
        $('#hideit').hide(function(){
          $(this).css('visibility','hidden');         
        });
        flagged=false;      
      } else {
        $('#hideit').show(function(){
          $(this).css('visibility','visible');
        });
        flagged=true;      
      }
  });

  $(document).on('click','#toggle', function(){

    console.log('Clicked the "toggle" button.');
    var p='<img class="added" src="python.png">';
    var n='<img class="added" src="nodejs.png">';

    if (flagged) {
      $('#displayarea').html(p+n);
      flagged=false;      
    } else {
      $('#displayarea').html(n+p);
      flagged=true; 
    }

  });  

  $(document).on('click','#slideDown-Up', function(){

    console.log('Clicked the "slideDown-Up" button.');
    $(function(){
    });

    if (flagged) {
      $('.added').slideUp('slow');
      $('.added').remove();
      flagged=false;      
    } else {
      $('#displayarea').append('<img class="added" visibility="hidden" src="JavaScript.png">')
      $('.added').slideDown('slow');
      flagged=true; 
    }

  });  

  $(document).on('click','#html-remove', function(){
    console.log('Clicked the "#html-remove" button.');   
    if (flagged) {
      $('.added').remove();
      flagged=false;      
    } else {
      $('#displayarea').html('<img class="added" src="HTML.png">');
      flagged=true;      
    }
  });
  
})

