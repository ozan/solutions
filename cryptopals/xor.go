package cryptopals

var frequency = [256]byte{
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	255, 0, 4, 0, 1, 0, 0, 4, 3, 3, 1, 0, 11, 20, 22, 2, 8, 7, 5, 3, 2, 2, 2, 2, 2, 2, 6, 2, 2, 0, 2, 2,
	0, 5, 3, 6, 5, 4, 2, 3, 3, 5, 3, 1, 3, 5, 3, 3, 4, 0, 4, 6, 5, 1, 1, 4, 1, 0, 0, 0, 0, 0, 0, 2,
	0, 77, 15, 31, 37, 127, 20, 23, 41, 73, 1, 10, 47, 24, 74, 86, 23, 1, 63, 65, 95, 31, 13, 19, 3, 17, 1, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
}

// FixedXOR returns a byte array of the pairwise xor of the given byte arrays
func FixedXOR(xs, ys []byte) []byte {
	out := make([]byte, len(xs))
	for i := 0; i < len(xs); i++ {
		out[i] = xs[i] ^ ys[i]
	}
	return out
}

// DecryptFixedXOR attempts to decrypt the given single byte xor encrypted byte slice,
// returning the likely key and plaintext string
func DecryptFixedXOR(bs []byte) (byte, string, int) {
	bestScore := -1
	decrypted := make([]byte, len(bs))
	var best string
	var i, bestI byte
	for i = 0; i < 128; i++ {
		score := 0
		for j := 0; j < len(bs); j++ {
			score += int(frequency[bs[j]^i])
			decrypted[j] = bs[j] ^ i
		}
		if score > bestScore {
			bestScore = score
			best = string(decrypted)
			bestI = i
		}
	}
	return bestI, best, bestScore
}

// RepeatingKeyXOR returns a byte array of the pairwise xor of the given byte arrays
func RepeatingKeyXOR(input, key []byte) []byte {
	out := make([]byte, len(input))
	for i := 0; i < len(input); i++ {
		out[i] = input[i] ^ key[i%len(key)]
	}
	return out
}

// HammingDistance returns the number of bits differing between two given byte slices
func HammingDistance(xs, ys []byte) int {
	count := 0
	for i := 0; i < len(xs); i++ {
		d := xs[i] ^ ys[i]
		for j := 0; j < 8; j++ {
			count += int(d & 1)
			d >>= 1
		}
	}
	return count
}

// DecryptVigenere breaks repeating key xor
func DecryptVigenere(cipherText []byte) (key, plainText []byte) {
	keyLength := 1
	lowestDistance := 8.0 // 8.0 is max distance, as we will normalize by num bytes

	nSamples := 20
	for n := 2; n <= 40; n++ {
		dist := 0
		for i := 0; i < nSamples; i++ {
			dist += HammingDistance(cipherText[n*(i*2):n*(i*2+1)], cipherText[n*(i*2+1):n*(i*2+2)])
		}
		normed := float64(dist) / float64(n*nSamples)
		if normed < lowestDistance {
			lowestDistance = normed
			keyLength = n
		}
	}

	// Now that we have a proposed keyLength, treat the cipherText as that many
	// interleaved fixed xor ciphers
	key = make([]byte, keyLength)
	plainText = make([]byte, len(cipherText))
	blockWidth := len(cipherText)/keyLength + 1
	block := make([]byte, blockWidth)
	for i := 0; i < keyLength; i++ {
		for j := 0; j < blockWidth; j++ {
			if j*keyLength+i < len(cipherText) {
				block[j] = cipherText[j*keyLength+i]
			}
		}
		keyPart, plain, _ := DecryptFixedXOR(block)
		key[i] = keyPart
		for j := 0; j < blockWidth; j++ {
			if j*keyLength+i < len(plainText) {
				plainText[j*keyLength+i] = plain[j]
			}
		}
	}

	return key, plainText
}
