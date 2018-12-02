def pollard_rho(n):
	if is_prime(n):
		return -1

	# the polynomial x^2 + 1 fails to find factor 2	
	if n%2 == 0:
		return 2

	# note precision issues here
	# it's recommended to only use integers
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