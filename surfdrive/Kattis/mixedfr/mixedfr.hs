{- verwerkt t n arr | t > n -> putStr "boos" -}

verwerk (t:n:rest) 
	| (t < n) -> do
		putStr "0 "
		putStr $ t
		putStr " / "
		putStrLn n
	| (t=="0" && n=="0" -> putStr ""
	verwerk(arr)
	
{-
			False -> do
				let tt = read t :: Int
				let nn = read n :: Int
				putStr $ show ( (quot) tt nn )
				putStr " "
				putStr $ show ( (mod) tt nn )
				putStr " / "
				putStrLn n
	-}


{- verwerk ("0":"0":rest) = putStr ""
verwerk (t:n:arr) = do
	let tt = read t :: Int
	let nn = read n :: Int
	putStr $ show ( (quot) tt nn )
	putStr " "
	putStr $ show ( (mod) tt nn )
	putStr " / "
	putStrLn n
	verwerk(arr) -}
	
main = do  
	test <- getContents
	verwerk ( words test )