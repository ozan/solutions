#!/usr/bin/env lein-exec

; Create a function of two integer arguments: the start and end,
; respectively. You must create a vector of strings which renders a 45°
; rotated square of integers which are successive squares from the start
; point up to and including the end point. If a number comprises
; multiple digits, wrap them around the shape individually. If there are
; not enough digits to complete the shape, fill in the rest with
; asterisk characters. The direction of the drawing should be clockwise,
; starting from the center of the shape and working outwards, with the
; initial direction being down and to the right.


(defn make-square [start end]
  (let [square-range (fn square-range [n end] (if (> n end) [] (cons n (square-range (* n n) end))))
        pad-asterisks (fn [n] (repeat (-> n Math/sqrt Math/ceil (Math/pow 2) (- n)) \*))
        rotate (fn [matrix] (reverse (apply (partial map vector) matrix)))
        numerals (mapcat str (square-range start end))
        padding (pad-asterisks (count numerals))
        chars (concat numerals padding)
        populate (fn populate [spiral chars iterations]
                          (if (empty? chars) (if (= 0 (mod iterations 4))
                                               spiral
                                               (populate (rotate spiral) chars (inc iterations)))
                            (let [rotated (rotate spiral)
                                  [head tail] (split-at (count (first rotated)) chars)]
                              (populate (conj rotated head) tail (inc iterations))
                              )
                            ))
        spiral (populate [[(first chars)]] (rest chars) 0)
        spiral-size (count spiral)
        left-padded (map-indexed (fn [i row] (concat (repeat i \space)
                                                     row
                                                     (repeat (- (dec spiral-size) i) \space)))
                                 spiral)
        diamond-shaped (map reverse (apply (partial map vector) left-padded))
        spaced (map #(interpose \space %) diamond-shaped)
        unskewed (map-indexed (fn [i row]
                                (let [n (- (dec spiral-size) i)
                                      m (- i (dec spiral-size))]
                                  (take (count row)
                                  (concat (repeat m \space) (drop n row) (repeat \space)))))
                              spaced)
        ]
     (map clojure.string/join unskewed)))


(assert (= (make-square 2 2) ["2"]))
(assert (= (make-square 2 4) [" 2 "
                              "* 4"
                              " * "]))
(assert (= (make-square 3 81) [" 3 "
                               "1 9"
                               " 8 "]))
(assert (= (make-square 4 20) [" 4 "
                               "* 1"
                               " 6 "]))
(assert (= (make-square 2 256) ["  6  "
                                " 5 * "
                                "2 2 *"
                                " 6 4 "
                                "  1  "]))
(assert (= (make-square 10 10000) ["   0   "
                                   "  1 0  "
                                   " 0 1 0 "
                                   "* 0 0 0"
                                   " * 1 * "
                                   "  * *  "
                                   "   *   "]))
