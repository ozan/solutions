#!/usr/bin/env lein-exec

; The game of life is a cellular automaton devised by mathematician John
; Conway.

; The 'board' consists of both live (#) and dead ( ) cells. Each cell
; interacts with its eight neighbours (horizontal, vertical, diagonal),
; and its next state is dependent on the following rules:

; 1) Any live cell with fewer than two live neighbours dies, as if
; caused by under-population. 2) Any live cell with two or three live
; neighbours lives on to the next generation. 3) Any live cell with more
; than three live neighbours dies, as if by overcrowding. 4) Any dead
; cell with exactly three live neighbours becomes a live cell, as if by
; reproduction.

; Write a function that accepts a board, and returns a board
; representing the next generation of cells.


(defn next-gen [board]
  (let [alive \#
        dead \space
        offsets [[-1 -1] [ 0 -1] [ 1 -1]
                 [-1  0]         [ 1  0]
                 [-1  1] [ 0  1] [ 1  1]]
        rules {alive #{2 3}
               dead #{3}}]
    (letfn [(calc-dimensions [matrix]
                             [[0 (dec (count matrix))] [0 (dec (count (first matrix)))]])

            (valid-coordinate? [[[min-row max-row] [min-col max-col]] [row col]]
                               (and (<= min-col col max-col)
                                    (<= min-row row max-row)))

            (alive? [matrix [x y]]
                    (let [row (nth matrix x)
                          val (nth row y)]
                      (= alive val)))

            (alive-neighbor-count [[i j] matrix]
                                  (let [dimensions (calc-dimensions matrix)]
                                    (->> (map #(map + % [i j]) offsets)
                                         (filter #(valid-coordinate? dimensions %))
                                         (map #(alive? matrix %))
                                         (filter true?)
                                         count)))

            (gen-cells [matrix]
                       (for [[i row] (map-indexed vector matrix)
                             [j cell] (map-indexed vector row)]
                         (vector i j cell)))

            (calc-next-val [matrix [x y cell]]
                           (let [neighbor-count (alive-neighbor-count [x y] matrix)
                                 is-alive (get rules cell)]
                             (if (is-alive neighbor-count) alive dead)))

            (calc-next-generation [board]
                                  (let [matrix (map seq board)]
                                    (->> (gen-cells matrix)
                                         (map #(calc-next-val matrix %))
                                         (partition (count (first board)))
                                         (map clojure.string/join))))
            ]
      (calc-next-generation board))))


(assert (= (next-gen ["      "
        " ##   "
        " ##   "
        "   ## "
        "   ## "
        "      "])
   ["      "
    " ##   "
    " #    "
    "    # "
    "   ## "
    "      "]))

(assert (= (next-gen ["     "
        "     "
        " ### "
        "     "
        "     "])
   ["     "
    "  #  "
    "  #  "
    "  #  "
    "     "]))

(assert (= (next-gen ["      "
        "      "
        "  ### "
        " ###  "
        "      "
        "      "])
   ["      "
    "   #  "
    " #  # "
    " #  # "
    "  #   "
    "      "]))
