(define-macro (switch expr cases)
    'YOUR-CODE-HERE
    (cons 'cond
          (map (lambda (case) (cons `(equal? ,expr ',(car case)) (cdr case)))
               cases)
    )
)

(define (flatmap f x)
  'YOUR-CODE-HERE)

(define (expand lst)
  'YOUR-CODE-HERE)

(define (interpret instr dist)
  'YOUR-CODE-HERE)

(define (apply-many n f x)
  (if (zero? n)
      x
      (apply-many (- n 1) f (f x))))

(define (dragon n d)
  (interpret (apply-many n expand '(f x)) d))
