function copyNumOnly (arr)
{
  var newArr=[];
  for(i=0;i<arr.length;i++)
  {
    if(typeof arr[i] === "number")
    {
      newArr.push(arr[i]);
    }
  }
  return newArr;
}

foo=['one',2,true,4];
console.log(copyNumOnly(foo));