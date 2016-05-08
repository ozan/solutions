#!/usr/bin/env lein-exec

; As in Problem 73, a tic-tac-toe board is represented by a two
; dimensional vector. X is represented by :x, O is represented by :o,
; and empty is represented by :e. Create a function that accepts a game
; piece and board as arguments, and returns a set (possibly empty) of
; all valid board placements of the game piece which would result in an
; immediate win.

; Board coordinates should be as in calls to get-in. For example, [0 1]
; is the topmost row, center position.

(defn win-tic-tac-toe [player, board]
  (let [winning-combinations [
                              [[0 0] [0 1] [0 2]]  ; horizontal
                              [[1 0] [1 1] [1 2]]
                              [[2 0] [2 1] [2 2]]
                              [[0 0] [1 0] [2 0]]  ; vertical
                              [[0 1] [1 1] [2 1]]
                              [[0 2] [1 2] [2 2]]
                              [[0 0] [1 1] [2 2]]  ; diagonal
                              [[2 0] [1 1] [0 2]]
                              ]
        ]
    (->> winning-combinations
         (map (fn [row] (group-by (fn [[i j]] (-> board (get i) (get j))) row)))
         (filter (fn [plays] (and (= 1 (count (get plays :e))) (= 2 (count (get plays player))))))
         (map (fn [plays] (first (get plays :e))))
         set)))


(assert (= (win-tic-tac-toe :x [[:o :e :e]
                                [:o :x :o]
                                [:x :x :e]])
   #{[2 2] [0 1] [0 2]}))
(assert (= (win-tic-tac-toe :x [[:x :o :o]
                                [:x :x :e]
                                [:e :o :e]])
   #{[2 2] [1 2] [2 0]}))
(assert (= (win-tic-tac-toe :x [[:x :e :x]
                                [:o :x :o]
                                [:e :o :e]])
   #{[2 2] [0 1] [2 0]}))
(assert (= (win-tic-tac-toe :x [[:x :x :o]
                                [:e :e :e]
                                [:e :e :e]])
   #{}))
(assert (= (win-tic-tac-toe :o [[:x :x :o]
                                [:o :e :o]
                                [:x :e :e]])
   #{[2 2] [1 1]}))
