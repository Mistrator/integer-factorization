def pollard_rho(n):
	# Miller-Rabin, for example, can be used
	if is_prime(n):
		return -1

	# the polynomial x^2 + 1 fails to find factor 2	
	if n%2 == 0:
		return 2

	# pay attention to floating-point precision issues
	# it's recommended to implement these with integers
	if is_square(n):
		return sqrt(n)

	for s in range(1, n):
		t = f(s)
		h = f(f(s))

		while gcd(h-t, n) == 1:
			t = f(t)
			h = f(f(h))

		res = gcd(h-t, n)
		if res != n:
			return res

	# n is composite, but we failed to find a factor
	return -1
