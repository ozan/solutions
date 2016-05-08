#!/usr/bin/env lein-exec

; Reversi is normally played on an 8 by 8 board. In this problem, a 4 by
; 4 board is represented as a two-dimensional vector with black, white,
; and empty pieces represented by 'b, 'w, and 'e, respectively. Create a
; function that accepts a game board and color as arguments, and returns
; a map of legal moves for that color. Each key should be the
; coordinates of a legal move, and its value a set of the coordinates of
; the pieces flipped by that move.

; Board coordinates should be as in calls to get-in. For example, [0 1]
; is the topmost row, second column from the left.

(defn ar [board player]
  (let [deltas [[-1 -1] [-1  0] [-1  1]
                [ 0 -1]         [ 0  1]
                [ 1 -1] [ 1  0] [ 1  1]]
        other? #(or (and (= player 'w) (= % 'b))
                    (and (= player 'b) (= % 'w)))
        get-at (fn [[i j]] (-> board (get i) (get j)))
        step #(map (comp (partial apply +) vector) %1 %2)
        get-flips (fn [start delta]
                    (let [places (iterate (partial step delta) start)
                          [flips more] (split-with (comp other? get-at) (rest places))]
                      (if (= player (get-at (first more))) flips)))
        ]
    (into {} (for [[i row] (map-indexed vector board)
                   [j piece] (map-indexed vector row)
                   :when (= piece 'e)]
               (let [flips (mapcat (partial get-flips [i j]) deltas)]
                 (if (not (empty? flips)) (vector [i j] (into #{} flips))))))))


(assert (= {[1 3] #{[1 2]}, [0 2] #{[1 2]}, [3 1] #{[2 1]}, [2 0] #{[2 1]}}
   (ar '[[e e e e]
         [e w b e]
         [e b w e]
         [e e e e]] 'w)))
(assert (= {[3 2] #{[2 2]}, [3 0] #{[2 1]}, [1 0] #{[1 1]}}
   (ar '[[e e e e]
         [e w b e]
         [w w w e]
         [e e e e]] 'b)))
(assert (= {[0 3] #{[1 2]}, [1 3] #{[1 2]}, [3 3] #{[2 2]}, [2 3] #{[2 2]}}
   (ar '[[e e e e]
         [e w b e]
         [w w b e]
         [e e b e]] 'w)))
(assert (= {[0 3] #{[2 1] [1 2]}, [1 3] #{[1 2]}, [2 3] #{[2 1] [2 2]}}
   (ar '[[e e w e]
         [b b w e]
         [b w w e]
         [b w w w]] 'b)))
