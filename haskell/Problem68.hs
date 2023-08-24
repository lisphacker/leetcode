module Problem68 where

justify :: Int -> [String] -> [String]
justify mw words = justify' words [] 0 []
  where
    justify' [] cws _ lines = lines ++ [makeRJLine cws]
    justify' (w:ws) cws cwsl lines
      | cwsl + 1 + length w > mw =
        justify' ws [w] (length w) (lines ++ [makeFJLine cws])
      | otherwise = justify' ws (w : cws) (cwsl + 1 + length w) lines
    makeRJLine ws =
      let line = (unwords . reverse) ws
       in line ++ replicate (mw - length line) ' '
    makeFJLine ws
      | null (tail ws) = makeRJLine ws
      | otherwise =
        let ls = map length ws
            tlen = sum ls
            numWords = length ws
            spToAdd = mw - tlen - (numWords - 1)
            spBwWords = div spToAdd (numWords - 1)
            extras = rem spToAdd (numWords - 1)
         in makeFJLine' (reverse ws) spBwWords extras
    makeFJLine' [] spBwWords extras = ""
    makeFJLine' (w:ws) spBwWords extras
      | null ws = w
      | extras > 0 =
        w ++
        " " ++
        replicate (spBwWords + 1) ' ' ++ makeFJLine' ws spBwWords (extras - 1)
      | otherwise =
        w ++
        " " ++ replicate spBwWords ' ' ++ makeFJLine' ws spBwWords (extras - 1)

i1 = ["This", "is", "an", "example", "of", "text", "justification."] :: [String]

mw1 = 16 :: Int

o1 = ["This    is    an", "example  of text", "justification.  "] :: [String]

i2 = ["What", "must", "be", "acknowledgment", "shall", "be"] :: [String]

mw2 = 16 :: Int

o2 = ["What   must   be", "acknowledgment  ", "shall be        "] :: [String]

i3 =
  [ "Science"
  , "is"
  , "what"
  , "we"
  , "understand"
  , "well"
  , "enough"
  , "to"
  , "explain"
  , "to"
  , "a"
  , "computer."
  , "Art"
  , "is"
  , "everything"
  , "else"
  , "we"
  , "do"
  ] :: [String]

mw3 = 20 :: Int

o3 =
  [ "Science  is  what we"
  , "understand      well"
  , "enough to explain to"
  , "a  computer.  Art is"
  , "everything  else  we"
  , "do                  "
  ] :: [String]
