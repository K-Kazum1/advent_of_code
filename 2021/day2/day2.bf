>+>,            Read first byte and increment read counter
    [           While the byte isn't 0
                Read more bytes and increment read counter
                until a 32 (ascii space) is read
        [,<+>>++++[-<-------->]<]
                Read another byte (no increment read counter)
                and subtract 48 (ascii zero) from it
                This is the number
        ,+>+++++++[-<------->]
                Begin a "switch statement" on the read counter
                Fallthrough flag is initialized
        <<---<+>Subtract 3 from the read counter
        [--     If not zero then subtract 2 more
            [---If not zero then subtract 3 more
                "forward" case
                Clear the fallthrough flag
                Add number*aim to depth
                Add number to hposition
                <->>[->>[-<+>>+<]<[->+<]>>>+<<<<]
            <]
            <   Check fallthrough flag
            [->>If it's set then clear it
                "down" case
                Add the number to the aim
                [->>+<<]
            <<]
         >
        ]
        <       Check fallthrough flag
        [->>    If it's set then clear it
                "up" case
                Subtract the number from the aim
            [->>-<<]
         <<]
                Consume newline and read a new byte
    >+>,,]      and increment read counter and loop
                Multiply depth by hposition
                and print (raw number not ascii)
>>>[->[->+>+<<]>[-<+>]<<]>>>.
