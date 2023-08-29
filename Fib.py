def fib(n):
	pred,curv=1,0
	k=0
	while k<n:
		pred,curv=curv,pred+curv
		k=k+1
	return curv

def print_sums(n):
        """It is just a little hard to think"""
        
        print(n)
        def next_sum(k):
                return print_sums(n+k)
        return next_sum

