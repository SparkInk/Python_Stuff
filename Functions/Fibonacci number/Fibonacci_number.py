#it's for python3
#It shows you a series of Fibonacci number
def fib(j):      # here j is a number up to 
	a = 0    # you want to display the series   
	b = 1
	while a < j:
		print(a, b, end = " ")
		a = a + b   # this step is changing possitions 
		b = a + b   # of the parameters a and b in the series
