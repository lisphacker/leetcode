module Problem3 where

f :: String -> Int
f s = f' s 0 0
  where
    f' [] s _ = 0
    f' (x:xs) l m
      | x `elem` xs = f' xs 0 m
      | otherwise = f' xs (l + 1) (max (l + 1) m)

i1 = "abcabcbb" :: String

i2 = "bbbbb" :: String

i3 = "pwwkew" :: String
