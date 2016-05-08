#!/usr/bin/env lein-exec

; Given a graph, determine whether the graph is connected. A connected
; graph is such that a path exists between any two given nodes.

; - Your function must return true if the graph is connected and false
; - otherwise.

; - You will be given a set of tuples representing the edges of a graph.
; - Each member of a tuple being a vertex/node in the graph.

; - Each edge is undirected (can be traversed either direction).

(defn connected? [edges]
   (let [bidirectional (concat edges (map reverse edges))
         adjacencies (into {} (for [[k v] (group-by first bidirectional)] [k (map second v)]))]
     (letfn [(traverse [visited]
               (if (= (count adjacencies) (count visited)) true
                   (let [adjacent (into #{} (adjacencies (last visited)))
                         visited-set (into #{} visited)
                         to-traverse (clojure.set/difference adjacent visited-set)]
                     (or (some true? (map #(traverse (conj visited %)) to-traverse)) false))))]
       (or (some true? (map #(traverse (vector %)) (keys adjacencies))) false))))


(assert (= true (connected? #{[:a :a]})))
(assert (= true (connected? #{[:a :b]})))
(assert (= false (connected? #{[1 2] [2 3] [3 1]
               [4 5] [5 6] [6 4]})))
(assert (= true (connected? #{[1 2] [2 3] [3 1]
              [4 5] [5 6] [6 4] [3 4]})))
(assert (= false (connected? #{[:a :b] [:b :c] [:c :d]
               [:x :y] [:d :a] [:b :e]})))
(assert (= true (connected? #{[:a :b] [:b :c] [:c :d]
              [:x :y] [:d :a] [:b :e] [:x :a]})))
