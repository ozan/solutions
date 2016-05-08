#!/usr/bin/env lein-exec

; Every node of a tree is connected to each of its children as well as
; its parent. One can imagine grabbing one node of a tree and dragging
; it up to the root position, leaving all connections intact.

(defn tp [n tree]
  (let [get-parents (fn f [[x & kids]]
                      (concat (map #(vector (first %) x) kids)
                               (mapcat f kids)))
        parent-of (into {} (get-parents tree))
        path-up-from (fn f [n] (let [parent (parent-of n)]
                                 (if parent (cons (parent-of n) (f (parent-of n))))))
        path-to-n (reverse (path-up-from n))
        upshift-targets (concat (rest path-to-n) (list n))
        upshift (fn [new-root [old-root & kids]]
                  (let [branch-to-shift (first (filter #(= new-root (first %)) kids))
                        other-branches (remove #(= new-root (first %)) kids)]
                    (if (nil? branch-to-shift) (cons old-root kids)
                      (concat branch-to-shift (list (cons old-root other-branches))))))
        ]
    (loop [targets upshift-targets
           current-tree tree]
      (if (empty? targets) current-tree
        (recur (rest targets) (upshift (first targets) current-tree))))))


(assert (= '(n)
   (tp 'n '(n))))
(assert (= '(a (t (e)))
   (tp 'a '(t (e) (a)))))
(assert (= '(e (t (a)))
   (tp 'e '(a (t (e))))))
(assert (= '(a (b (c)))
   (tp 'a '(c (b (a))))))
(assert (= '(d
      (b
        (c)
        (e)
        (a
          (f
            (g)
            (h)))))
  (tp 'd '(a
            (b
              (c)
              (d)
              (e))
            (f
              (g)
              (h))))))
(assert (= '(c
      (d)
      (e)
      (b
        (f
          (g)
          (h))
        (a
          (i
          (j
            (k)
            (l))
          (m
            (n)
            (o))))))
   (tp 'c '(a
             (b
               (c
                 (d)
                 (e))
               (f
                 (g)
                 (h)))
             (i
               (j
                 (k)
                 (l))
               (m
                 (n)
                 (o)))))))

