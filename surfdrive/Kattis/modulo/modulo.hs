import qualified Data.Set as Set

{-solve [] = []
solve (a:rest) = (a `mod` 3):(solve rest)-}

solve arr = [Set.size (solveset arr)]
solveset [] = Set.empty
solveset (a:rest) = Set.insert (a `mod` 42) (solveset rest)

readInput = (map read) . words
writeOutput = unlines . (map show)

main = interact (writeOutput . solve . readInput)


{-solve [] = Set.empty
solve (a:rest) = Set.insert a (solve rest)
-}

	{-putStrLn("Hello")
-}	{-putStrLn (show (Set.size (Set.insert '1' Set.empty) ) )-}
	{-Set.toList(solve(map read . words))-}
	{-putStrLn "Hello World!"-}
{-interact (writeOutput (solve (readInput)))-}
{-interact (solve . readInput)-}
	{-interact (solve . readInput)
-}

