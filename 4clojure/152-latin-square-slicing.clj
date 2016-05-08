#!/usr/bin/env lein-exec

; A Latin square of order n is an n x n array that contains n different
; elements, each occurring exactly once in each row, and exactly once in
; each column. For example, among the following arrays only the first
; one forms a Latin square:

; A B C    A B C    A B C
; B C A    B C A    B D A
; C A B    C A C    C A B

; Let V be a vector of such vectors1 that they may differ in length2. We will say that an arrangement of vectors of V in consecutive rows is an alignment (of vectors) of V if the following conditions are satisfied:

; - All vectors of V are used.
; - Each row contains just one vector.
; - The order of V is preserved.
; - All vectors of maximal length are horizontally aligned each other.
; - If a vector is not of maximal length then all its elements are aligned with elements of some subvector of a vector of maximal length.

; Let L denote a Latin square of order 2 or greater. We will say that L
; is included in V or that V includes L iff there exists an alignment of
; V such that contains a subsquare that is equal to L.

; For example, if V equals [[1 2 3][2 3 1 2 1][3 1 2]] then there are
; nine alignments of V (brackets omitted):

  ;       1              2              3

  ;     1 2 3          1 2 3          1 2 3
  ; A   2 3 1 2 1    2 3 1 2 1    2 3 1 2 1
  ;     3 1 2        3 1 2        3 1 2

  ;     1 2 3          1 2 3          1 2 3
  ; B   2 3 1 2 1    2 3 1 2 1    2 3 1 2 1
  ;       3 1 2        3 1 2        3 1 2

  ;     1 2 3          1 2 3          1 2 3
  ; C   2 3 1 2 1    2 3 1 2 1    2 3 1 2 1
  ;         3 1 2        3 1 2        3 1 2

; Alignment A1 contains Latin square [[1 2 3][2 3 1][3 1 2]], alignments
; A2, A3, B1, B2, B3 contain no Latin squares, and alignments C1, C2, C3
; contain [[2 1][1 2]]. Thus in this case V includes one Latin square of
; order 3 and one of order 2 which is included three times.

; Our aim is to implement a function which accepts a vector of vectors V
; as an argument, and returns a map which keys and values are integers.
; Each key should be the order of a Latin square included in V, and its
; value a count of different Latin squares of that order included in V.
; If V does not include any Latin squares an empty map should be
; returned. In the previous example the correct output of such a
; function is {3 1, 2 1} and not {3 1, 2 3}.

(defn squares [vecs]
  (let [max-count (apply max (map count vecs))
        positions #(range (inc (- max-count (count %))))
        alignments (fn [v] (map #(concat
                                   (repeat % nil)
                                   v
                                   (repeat (- max-count (count v) %) nil))
                                (positions v)))
        cartesian-product (fn f [colls]
                            (if (empty? colls)
                              '(())
                              (for [x (first colls)
                                    more (f (rest colls))]
                                (cons x more))))
        all-planes (cartesian-product (map alignments vecs))
        transpose #(apply map vector %)
        get-slices-of (fn [n plane]
                        (map #(take n (drop % plane))
                             (range (inc (- (count plane) n)))))
        get-squares-of (fn [n plane]
                         (map transpose (mapcat (comp (partial get-slices-of n) transpose)
                                                (get-slices-of n plane)))
                         )
        candidate-sizes (range 2 (inc (min (count vecs) max-count)))
        all-candidates (mapcat (fn [n] (mapcat (partial get-squares-of n) all-planes))
                               candidate-sizes)
        is-latin? (fn [square]
                    (and (every? (partial apply distinct?) square)
                         (every? (partial apply distinct?) (transpose square))
                         (= (count square) (count (set (flatten square))))
                         (not (contains? (set (flatten square)) nil))))

        ]
     (frequencies (map count (distinct (filter is-latin? all-candidates))))))


(assert (= (squares '[[A B C D]
                     [A C D B]
                     [B A D C]
                     [D C A B]])
   {}))
(assert (= (squares '[[A B C D E F]
                      [B C D E F A]
                      [C D E F A B]
                      [D E F A B C]
                      [E F A B C D]
                      [F A B C D E]])
   {6 1}))
(assert (= (squares '[[A B C D]
                      [B A D C]
                      [D C B A]
                      [C D A B]])
   {4 1, 2 4}))
(assert (= (squares '[[B D A C B]
                      [D A B C A]
                      [A B C A B]
                      [B C A B C]
                      [A D B C A]])
   {3 3}))
(assert (= (squares [  [2 4 6 3]
                     [3 4 6 2]
                       [6 2 4]  ])
   {}))
(assert (= (squares [[1]
                     [1 2 1 2]
                     [2 1 2 1]
                     [1 2 1 2]
                     []       ])
   {2 2}))
(assert (= (squares [[3 1 2]
                     [1 2 3 1 3 4]
                     [2 3 1 3]    ])
   {3 1, 2 2}))
(assert (= (squares [[8 6 7 3 2 5 1 4]
                     [6 8 3 7]
                     [7 3 8 6]
                     [3 7 6 8 1 4 5 2]
                           [1 8 5 2 4]
                           [8 1 2 4 5]])
   {4 1, 3 1, 2 7}))
