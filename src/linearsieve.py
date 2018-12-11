def linear_sieve(n):
	sp = (n+1)*[0]
	primes = []

	sp[1] = 1
	for i in range(2, n+1):
		if sp[i] == 0:
			sp[i] = i
			primes.append(i)

		for p in primes:
			if p > sp[i]:
				break
			a = p*i
			if a > n:
				break
			sp[a] = i

	return sp
