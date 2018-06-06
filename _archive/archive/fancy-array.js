var foo = ["James", "Jill", "Jane", "Jack"];

function fancy_array(array,s) {
  console.log('===========');
  for(var i=0; i<array.length; i++) {
      console.log(i+s+array[i]);
  }
}

fancy_array(foo,'->');
fancy_array(foo,'::');
fancy_array(foo,'=>');
fancy_array(foo,'----');