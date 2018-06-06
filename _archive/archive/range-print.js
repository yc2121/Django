function rangeprint(start,end,skip)
{
  console.log("From "+start+" to "+end+" with each skip of "+skip)
  for (var i=start; i<end; i=i+skip)
  {
    console.log(i);
  }
}

rangeprint(1,10,2);
rangeprint(3,15,3);
rangeprint(45,32,10);
rangeprint(66,178,23);
