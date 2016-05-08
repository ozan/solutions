#!/usr/bin/env lein-exec

; A tic-tac-toe board is represented by a two dimensional vector. X is
; represented by :x, O is represented by :o, and empty is represented by
; :e. A player wins by placing three Xs or three Os in a horizontal,
; vertical, or diagonal row. Write a function which analyzes a tic-tac-
; toe board and returns :x if X has won, :o if O has won, and nil if
; neither player has won.

(defn winner [board]
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
        played-combinations (map #(for [[i j] %] (-> board (get i) (get j))) winning-combinations)
        wins (filter #(and (apply = %) (not= :e (first %))) played-combinations)]
    (if (empty? wins) nil (ffirst wins))))


(assert (= nil (winner [[:e :e :e]
                        [:e :e :e]
                        [:e :e :e]])))
(assert (= :x (winner [[:x :e :o]
                       [:x :e :e]
                       [:x :e :o]])))
(assert (= :o (winner [[:e :x :e]
                       [:o :o :o]
                       [:x :e :x]])))
(assert (= nil (winner [[:x :e :o]
                        [:x :x :e]
                        [:o :x :o]])))
(assert (= :x (winner [[:x :e :e]
                       [:o :x :e]
                       [:o :e :x]])))
(assert (= :o (winner [[:x :e :o]
                       [:x :o :e]
                       [:o :e :x]])))
(assert (= nil (winner [[:x :o :x]
                        [:x :o :x]
                        [:o :x :o]])))
