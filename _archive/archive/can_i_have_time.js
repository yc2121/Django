var HOUR=2, MINUTE=2, PERIOD='';
var filler1, filler2;

if (HOUR >= 0 && HOUR <= 12) {
	PERIOD = 'AM';
	filler2= 'morning'
}
else if (HOUR > 12 && HOUR <= 24) {
	PERIOD = 'PM';
	if (HOUR > 12 && HOUR <= 15) {
		filler2='afternoon';
	}
	else {
		filler2='evening';
	}
	HOUR = HOUR - 12;
}
else {
  console.log ('bad data of HOUR');
}

if (MINUTE >= 0 && MINUTE <= 30) {
  filler1 = 'just after';
}
else if (MINUTE > 30 && MINUTE <=60) {
	filler1 = 'almost';
}
else {
  console.log ('bad data of MINUTE');
}

console.log ("It's "+filler1+' '+HOUR+' in the '+ filler2+'.');
