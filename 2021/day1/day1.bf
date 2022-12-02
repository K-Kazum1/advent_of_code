,>>,>>,>>,  get in1 in2 in3 in4
>>>>+<<<<   set a flag to use later
[           loop while in4 is not 0
            dupe in1 to accum1
  <<<<<<[->+>>>>>>+<<<<<<<]
  >[-<+>]   move in1 back
            add in2 to accum1
  >[->+>>>>+<<<<<]
  >[-<+>]   move in2 back
            add in3 to accum1
  >[->+>>+<<<]
  >[-<+>]   move in3 back
            dupe in2 to accum2
  <<<[->+>>>>>+<<<<<<]
  >[-<+>]   move in2 back
            add in3 to accum2
  >[->+>>>+<<<<]
  >[-<+>]   move in3 back
            add in4 to accum2
  >[-<+>>>+<<]
            subtract accum2 from accum1
            the position of the tape tells
            which one was smaller
  >>[-<-[<]>>]
            find the flag and increment the
            counter if accum1 was smaller
            and clear accum2
  >[>+<<<[-]>]
  <<[-]     clear accum1
  <<<<<<<[-]clear in1
  >>[-<<+>>]move in2 to in1
  >>[-<<+>>]move in3 to in2
  >[-<+>]   move in4 to in3
  >,        get new in4
]
>>>>>.      print counter
