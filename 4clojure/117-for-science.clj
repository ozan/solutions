#!/usr/bin/env lein-exec

; A mad scientist with tenure has created an experiment tracking mice in
; a maze. Several mazes have been randomly generated, and you've been
; tasked with writing a program to determine the mazes in which it's
; possible for the mouse to reach the cheesy endpoint. Write a function
; which accepts a maze in the form of a collection of rows, each row is
; a string where:

; - spaces represent areas where the mouse can walk freely
; - hashes (#) represent walls where the mouse can not walk
; - M represents the mouse's starting point
; - C represents the cheese which the mouse must reach

; The mouse is not allowed to travel diagonally in the maze (only
; up/down/left/right), nor can he escape the edge of the maze. Your
; function must return true iff the maze is solvable by the mouse.

(defn can-navigate? [maze]
  (let [transpose (fn [coll] (apply mapcat (comp list str) coll))
        reachable? (fn [s] (re-find #"(C@|@C)" s))
        walk (fn [s]
               (reduce (fn [s [x y]] (str (subs s 0 x) (apply str (repeat (- y x) \@)) (subs s y (count s)))) s
                       (let [matcher (re-matcher #"[ ]*[M@]+[ ]*" s)]
                         (loop [r [] match (re-find matcher)]
                           (if match
                             (recur (conj r [(.start matcher) (.end matcher)]) (re-find matcher))
                             r)))))
        search (fn [m]
                 (let [n (->> (map walk m) transpose (map walk) transpose)]
                   (if (= m n)
                     m
                     (recur n))))
        m (search maze)]
    (boolean (or (some reachable? m) (some reachable? (transpose m))))))


(assert (= true  (can-navigate? ["M   C"])))
(assert (= false (can-navigate? ["M # C"])))
(assert (= true  (can-navigate? ["#######"
                                 "#     #"
                                 "#  #  #"
                                 "#M # C#"
                                 "#######"])))
(assert (= false (can-navigate? ["########"
                                 "#M  #  #"
                                 "#   #  #"
                                 "# # #  #"
                                 "#   #  #"
                                 "#  #   #"
                                 "#  # # #"
                                 "#  #   #"
                                 "#  #  C#"
                                 "########"])))
(assert (= false (can-navigate? ["M     "
                                 "      "
                                 "      "
                                 "      "
                                 "    ##"
                                 "    #C"])))
(assert (= true  (can-navigate? ["C######"
                                 " #     "
                                 " #   # "
                                 " #   #M"
                                 "     # "])))
(assert (= true  (can-navigate? ["C# # # #"
                                 "        "
                                 "# # # # "
                                 "        "
                                 " # # # #"
                                 "        "
                                 "# # # #M"])))
