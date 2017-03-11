def gauss_update(mu, sig_sq, nu, r_sq):
	mu_bar = 1./(sig_sq + r_sq) * (r_sq * mu + sig_sq * nu)
	sig_sq_bar = 1./(1./sig_sq + 1./r_sq)
	
	return [mu_bar, sig_sq_bar]
	
