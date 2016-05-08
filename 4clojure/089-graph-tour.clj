#!/usr/bin/env lein-exec

; Starting with a graph you must write a function that returns true if
; it is possible to make a tour of the graph in which every edge is
; visited exactly once.

; The graph is represented by a vector of tuples, where each tuple
; represents a single edge.

; The rules are:

; - You can start at any node.
; - You must visit each edge exactly once.
; - All edges are undirected.

(defn can-tour? [edges]
  (let [vertices (into #{} (flatten edges))
        get-adjacent (fn [start edges]
                       (for [[a b] edges :when (or (= a start) (= b start))]
                         (let [[head tail] (split-with (partial not= [a b]) edges)]
                           [(if (= a start) b a) (concat head (rest tail))])))
        tour? (fn tour? [[start remaining]]
               (if (empty? remaining) true
                 (some tour? (get-adjacent start remaining))))]
    (boolean (some tour? (map vector vertices (repeat edges))))))


(assert (= true (can-tour? [[:a :b]])))
(assert (= false (can-tour? [[:a :a] [:b :b]])))
(assert (= false (can-tour? [[:a :b] [:a :b] [:a :c] [:c :a]
               [:a :d] [:b :d] [:c :d]])))
(assert (= true (can-tour? [[1 2] [2 3] [3 4] [4 1]])))
(assert (= true (can-tour? [[:a :b] [:a :c] [:c :b] [:a :e]
              [:b :e] [:a :d] [:b :d] [:c :e]
              [:d :e] [:c :f] [:d :f]])))
(assert (= false (can-tour? [[1 2] [2 3] [2 4] [2 5]])))
