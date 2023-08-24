module Problem4 where

import qualified Data.Vector as V

{-
Given two sorted arrays A and B, how do we partition them into A1.A2 and B1.B2 such that
  1. |len(A1 + B1) - len(A2 + B2)| <= 1
  2. Forall x1 in (A1 + B1) and x2 in (A2 + B2) | x1 < x2
-}
median :: V.Vector Int -> V.Vector Int -> Double
median a b = _

a1_1 = V.fromList [1, 3] :: V.Vector Int

a2_1 = V.fromList [2] :: V.Vector Int

a1_2 = V.fromList [1, 2] :: V.Vector Int

a2_2 = V.fromList [3, 4] :: V.Vector Int
