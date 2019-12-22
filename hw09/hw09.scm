
; Tail recursion

(define (replicate x n)
    (define (replicate-tail x n sofar)
      (if (zero? n)
        sofar
        (replicate-tail x (- n 1) (cons x sofar))
      )
    )
    (replicate-tail x n nil)
)

(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (if (zero? n)
  start
  (accumulate combiner (combiner (term n) start) (- n 1) term)
  )
)

(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
  (if (zero? n)
  start
  (accumulate combiner (combiner (term n) start) (- n 1) term)
  )
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (cons-stream 3 (map-stream (lambda (x) (+ x 3)) multiples-of-three))
)


(define (nondecreastream s)
    (define (help-sequence s)
      (if (or (null? (cdr-stream s)) (> (car s) (car (cdr-stream s))))
        (cons (car s) nil)
        (cons (car s) (help-sequence (cdr-stream s)))
      )
    )
    (define (help-rest s n)
      (cond ((zero? n) (nondecreastream s))
            ((null? (cdr-stream s)) nil)
            (else (help-rest (cdr-stream s) (- n 1)))
      )
    )
    (if (null? s)
      nil
     (cons-stream (help-sequence s)
                  (help-rest s (length (help-sequence s)))
     )
    )
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))
