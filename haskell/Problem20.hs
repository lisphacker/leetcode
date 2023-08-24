module Problem20 where

f :: String -> Bool
f s = f' s 0 0 0 []
  where
    f' "" c p s [] = c == 0 && p == 0 && s == 0
    f' "" _ _ _ _ = False
    f' (x:xs) c p s st
      | x == '{' = f' xs (c + 1) p s (x : st)
      | x == '(' = f' xs c (p + 1) s (x : st)
      | x == '[' = f' xs c p (s + 1) (x : st)
      | x == '}' = f'' xs '{' (c - 1) p s st
      | x == ')' = f'' xs '(' c (p - 1) s st
      | x == ']' = f'' xs '[' c p (s - 1) st
    f'' xs open c p s st
      | null st = False
      | head st /= open = False
      | otherwise = f' xs c p s (tail st)

i1 = "()" :: String

i2 = "()[]{}" :: String

i3 = "(]" :: String
