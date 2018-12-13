def linear_sieve(n):
	sp = (n+1)*[0] # zero-initialize a (n+1)-element array
	primes = [] # initialize an empty list

	sp[1] = 1
	for i in range(2, n+1):
		if sp[i] == 0:
			sp[i] = i
			primes.append(i)

		for p in primes:
			a = p*i
			if p > sp[i] or a > n:
				break
			sp[a] = i

	return sp
