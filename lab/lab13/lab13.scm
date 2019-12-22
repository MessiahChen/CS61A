(define quine
    'your-code-here)

scm> (switch (+ 1 1) ((1 (print 'a))
                      (2 (print 'b))
                      (3 (print 'c))))
b

(define-macro (switch expr cases)
  (cons 'cond
    (map (lambda (case)
                 (cons `(equal? ,expr (quote ,(car case)))
                        (cdr case)
                 )
         )
         cases
    )
  )
)
