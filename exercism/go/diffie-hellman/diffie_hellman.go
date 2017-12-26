package diffiehellman

import (
	"crypto/rand"
	"math/big"
)

// PrivateKey returns a random bigint in range (2, p)
func PrivateKey(p *big.Int) *big.Int {
	two := big.NewInt(2)
	r, _ := rand.Int(rand.Reader, big.NewInt(0).Sub(p, two))
	return r.Add(r, two)
}

// PublicKey returns g^a (mod p)
func PublicKey(private, p *big.Int, g int64) *big.Int {
	return modexp(big.NewInt(g), private, p)
}

// NewPair simply return a private and public key for given primes
func NewPair(p *big.Int, g int64) (*big.Int, *big.Int) {
	a := PrivateKey(p)
	return a, PublicKey(a, p, g)
}

// SecretKey calculates the shared secret from public and private keys
func SecretKey(private1, public2, p *big.Int) *big.Int {
	return modexp(public2, private1, p)
}

func modexp(base, exp, modulus *big.Int) *big.Int {
	// To do fast modular exponentiation, use the property that
	// a * b (mod p) == (a (mod p)) * (b (mod p)) (mod p)
	// and split exponent into powers of 2
	total := big.NewInt(1)
	part := big.NewInt(0).Mod(base, modulus)
	for i := 0; i < exp.BitLen(); i++ {
		if exp.Bit(i) == uint(1) {
			total.Mul(total, part)
			total.Mod(total, modulus)
		}
		part.Mul(part, part)
		part.Mod(part, modulus)
	}
	return total
}
