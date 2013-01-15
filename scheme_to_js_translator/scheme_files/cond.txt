"""
special forms: 
	define
	lambda
	let
	set
	cond
	else
	if
	equal?
	eq?
	length
	cons x y : [x] + y 
		y is a list
	car x : x[0]
		x is a list
	cdr x : x[1:]
		x is a list
	list? : type(x)
	symbol? : type(x) === type(' ')
	null? : x == []
	append
	list

(define (abs x)
	(cond ((> x 0) x)
		  ((= x 0) 0)
		  ((< x 0) (- x))))

function abs(x) {
	if (x > 0) { return x; }
	else if (x == 0) { return 0; } 
	else if (x < 0) { return -x; }	
};

(define (abs x)
	(cond ((< x 0) (- x))
		   (else x)))

function abs (x) {
	if (x < 0) { return -x; }	
	else { return x; }
};

(define (abs x)
	(if (< x 0)
		(- x)
		x))

function abs (x) {
	if (x < 0) { return -x} 
	else { return x; }
}

(cond (<p_i> <e_i>)
	  (<p_j> <e_j>)
		...        )

"""
