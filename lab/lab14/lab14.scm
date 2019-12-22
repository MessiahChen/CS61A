; Lab 14: Final Review

(define (compose-all funcs)
  'YOUR-CODE-HERE
  (lambda (x)
    (if (null? funcs)
      x
      ((compose-all (cdr funcs)) ((car funcs) x))
    )
  )
)

(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? curr) #f)
          ((contains? seen-so-far (car curr)) #t)
          (else (pair-tracker (cons-stream (car curr) seen-so-far) (cdr-stream curr)))
    )
  )
  (pair-tracker '() s)
)

(define (contains? lst s)
  'YOUR-CODE-HERE
  (cond
    ((null? lst) #f)
    ((= (car lst) s) #t)
    (else (contains? (cdr-stream lst) s))
  )
)

