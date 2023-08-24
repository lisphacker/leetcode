module Problem121 where

maximizeProfit :: [Int] -> Int
maximizeProfit prices = f prices 10001 0
  where
    f [] _ mp = mp
    f (p:ps) lp mp
      | p - lp > mp = f ps lp (p - lp)
      | p < lp = f ps p mp
      | otherwise = f ps lp mp

i1 = [7, 1, 5, 3, 6, 4] :: [Int]

o1 = 5 :: Int

i2 = [7, 6, 4, 3, 1] :: [Int]

o2 = 0 :: Int
