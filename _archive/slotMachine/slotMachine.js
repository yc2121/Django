function slotmachine(credit,leave)
{
  startcredit=credit;
  console.log("****** START CREDIT:   "+startcredit);
  won=0;
  trial=0;
  win=0;

  while(credit>0)
  {
    n1=Math.floor(Math.random()*100);
    n2=Math.floor(Math.random()*100);
    n3=Math.floor(Math.random()*100);
    credit--;
    console.log("SlotMachine [ "+n1+"-"+n2+"-"+n3+" ]");
    trial++;
  
    if (n1==n2 && n2==n3)
    {
      //three of a kind, win coins between 50 to 100
      won=Math.floor( (Math.random()*50) )+50;
      console.log("CONGRATIONS, You've won "+won+" credits!");
      win++;
    }
    else
    {
      console.log("May the force bewith you. Better luck next time.");
    }
  
    credit=credit+won;
    console.log("Credit remaining: "+credit);
  
    if (credit>=leave) {
      console.log("****** START CREDIT:   "+startcredit);
      console.log("****** FINISH CREDIT:  "+credit);
      console.log("****** CREDIT WON:     "+won);
      console.log("****** TOTAL GAMES:    "+trial);
      console.log("****** WINNING GAMES:  "+win);
      console.log("****** WIN RATIO:      "+(win/trial));
          return;
    }
  }

  console.log("****** TOTAL GAMES:    "+trial);
  console.log("****** WINNING GAMES:  "+win);
  console.log("****** WIN RATIO:      "+(win/trial));
  console.log("Thanks for trying "+trial+" times. Come again.")

}

slotmachine(2,);
slotmachine(20,40);
slotmachine(200,201);