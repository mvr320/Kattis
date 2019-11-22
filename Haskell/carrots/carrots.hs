split (a:b:rest) = b

main = do  
    line <- getLine
    putStrLn $ split (words line)
