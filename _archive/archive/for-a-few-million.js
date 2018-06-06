var penny=0;
for(var i=0; i<30; i++) {
  // console.log("day "+(i+1)+" gets "+2**i);
  penny=penny+2**i;
  // console.log("total = "+penny);
}
console.log("The reward for a penny lover becomes $"+ penny/100 +"!!!");

console.log("***** HOW LONG TO REACH INFINITY *****");
var total=0, i=0, all=0;
while((total/100)<Infinity) 
{
  total=total+2**i;
  i++;
  console.log("Day "+i+" Total Penny Count = "+total);
}
all=total/100;
console.log(i +" days for the reward to reach the '" + all + "'number in JavaScript.");
