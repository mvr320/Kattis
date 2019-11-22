convert "1" 'A'		= "2"
convert "1" 'C'		= "3"
convert "2" 'A'		= "1"
convert "2" 'B'		= "3"
convert "3" 'B'		= "2"
convert "3" 'C'		= "1"
convert i j				= i

solve state [] 			= state
solve state (c:rest) 	= solve ( convert state c ) rest

main = do  
    name <- getLine
    putStrLn $ solve "1" name