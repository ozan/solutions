#!/usr/bin/env lein-exec

; Following on from Recognize Playing Cards, determine the best poker
; hand that can be made with five cards. The hand rankings are listed
; below for your convenience.

; Straight flush: All cards in the same suit, and in sequence
; Four of a kind: Four of the cards have the same rank
; Full House: Three cards of one rank, the other two of another rank
; Flush: All cards in the same suit
; Straight: All cards in sequence (aces can be high or low, but not both at once)
; Three of a kind: Three of the cards have the same rank
; Two pair: Two pairs of cards have the same rank
; Pair: Two cards have the same rank
; High card: None of the above conditions are met

(defn classify [card-reprs]
  (let [suits {\D :diamond \S :spade \H :heart \C :club}
        ranks {\2 0 \3 1 \4 2 \5 3 \6 4 \7 5 \8 6 \9 7 \T 8 \J 9 \Q 10 \K 11 \A 12}
        recognize (fn [[suit rank]] {:suit (get suits suit) :rank (get ranks rank)})
        cards (map recognize card-reprs)
        card-ranks (sort (map :rank cards))
        card-suits (map :suit cards)
        is-flush (apply = card-suits)
        is-straight-high (= card-ranks (range (first card-ranks) (inc (last card-ranks))))
        is-straight-low (= card-ranks [0 1 2 3 12])
        is-straight (or is-straight-high is-straight-low)
        counts (->> card-ranks (group-by identity) vals (map count) sort)]
    (cond
      (and is-flush is-straight) :straight-flush
      (= counts [1 4]) :four-of-a-kind
      (= counts [2 3]) :full-house
      is-flush :flush
      is-straight :straight
      (= counts [1 1 3]) :three-of-a-kind
      (= counts [1 2 2]) :two-pair
      (= counts [1 1 1 2]) :pair
      :else :high-card)))


(assert (= :high-card (classify ["HA" "D2" "H3" "C9" "DJ"])))
(assert (= :pair (classify ["HA" "HQ" "SJ" "DA" "HT"])))
(assert (= :two-pair (classify ["HA" "DA" "HQ" "SQ" "HT"])))
(assert (= :three-of-a-kind (classify ["HA" "DA" "CA" "HJ" "HT"])))
(assert (= :straight (classify ["HA" "DK" "HQ" "HJ" "HT"])))
(assert (= :straight (classify ["HA" "H2" "S3" "D4" "C5"])))
(assert (= :flush (classify ["HA" "HK" "H2" "H4" "HT"])))
(assert (= :full-house (classify ["HA" "DA" "CA" "HJ" "DJ"])))
(assert (= :four-of-a-kind (classify ["HA" "DA" "CA" "SA" "DJ"])))
(assert (= :straight-flush (classify ["HA" "HK" "HQ" "HJ" "HT"])))
