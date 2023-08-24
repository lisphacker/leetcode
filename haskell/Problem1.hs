module Problem1 where

import           Data.List (sortOn)

twoSum :: [Int] -> Int -> Maybe (Int, Int)
twoSum n t =
  let n' = zip n [0 ..]
      n'' = sortOn (fst) n'
      r = reverse n''
   in twoSum' n'' r t
  where
    twoSum' _ [] _ = Nothing
    twoSum' [] _ _ = Nothing
    twoSum' ((n, ni):ns) ((r, ri):rs) t
      | n + r == t = Just (ni, ri)
      | n + r < t = twoSum' ns ((r, ri) : rs) t
      | otherwise = twoSum' ((n, ni) : ns) rs t

nums = [2, 7, 11, 15] :: [Int]

target = 9 :: Int
