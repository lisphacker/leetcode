module Problem3 where

import           Data.Set (empty, insert, member, singleton)

f :: String -> String
f s =
  let (start, len) = f' s 0 0 0 0 0 empty
   in take len $ drop start s
  where
    f' [] start len _ _ _ _ = (start, len)
    f' (c:cs) start len s l i set
      | member c set && l > len = f' cs s l i 1 (i + 1) (singleton c)
      | member c set && l <= len = f' cs start len i 1 (i + 1) (singleton c)
      | not (member c set) && l > len =
        f' cs s l s (l + 1) (i + 1) (insert c set)
      | not (member c set) && l <= len =
        f' cs start len s (l + 1) (i + 1) (insert c set)

i1 = "abcabcbb" :: String

i2 = "bbbbb" :: String

i3 = "pwwkew" :: String
