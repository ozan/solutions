package cryptopals

import (
	"bufio"
	"fmt"
	"os"
	"reflect"
	"testing"
)

func TestChallenge1(t *testing.T) {
	expected := "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
	actual := EncodeBase64(DecodeHex("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))
	if actual != expected {
		t.Errorf("Expected \"%s\" (%d bytes) to be \"%s\" (%d bytes)", actual, len(actual), expected, len(expected))
	}
}

func TestHexRoundtrip(t *testing.T) {
	s := []byte("hello!")
	if string(DecodeHex(EncodeHex(s))) != string(s) {
		t.Errorf("Failled to roundtrip %s with hex", s)
	}
}

func TestBase64Roundtrip(t *testing.T) {
	s := []byte("hello!")
	if string(DecodeBase64(EncodeBase64(s))) != string(s) {
		t.Errorf("Failed to roundtrip %s with b64", s)
	}
}

func TestFixedXOR(t *testing.T) {
	expected := DecodeHex("746865206b696420646f6e277420706c6179")
	actual := FixedXOR(DecodeHex("1c0111001f010100061a024b53535009181c"), DecodeHex("686974207468652062756c6c277320657965"))
	if !reflect.DeepEqual(expected, actual) {
		t.Errorf("Expected \"s\" to be \"%s\"", EncodeHex(actual), expected)
	}
}

func TestDecryptFixedXOR(t *testing.T) {
	expectedKey := byte(88)
	key, plaintext, _ := DecryptFixedXOR(DecodeHex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))
	if key != expectedKey {
		t.Errorf("Incorrect key: %d", key)
	} else {
		fmt.Printf("Solution 3: %s\n", plaintext)
	}
}

func TestDetectSingleCharacterXOR(t *testing.T) {
	f, err := os.Open("4.txt")
	if err != nil {
		panic(err)
	}
	var bestKey byte
	var best string
	bestScore := -1

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		text := scanner.Text()
		key, plaintext, score := DecryptFixedXOR(DecodeHex(text))
		if score > bestScore {
			bestScore = score
			best = plaintext
			bestKey = key
		}
	}

	expectedKey := byte(53)
	if bestKey != expectedKey {
		t.Errorf("Incorrect key: %d", bestKey)
	} else {
		fmt.Printf("Solution 4: %s\n", best)
	}
}

func TestRepeatingKeyXOR(t *testing.T) {
	input := []byte("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
	actual := RepeatingKeyXOR(input, []byte("ICE"))
	expected := "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
	if EncodeHex(actual) != expected {
		t.Errorf("Expected %s to be %s", actual, expected)
	}
}

func TestHammingDistance(t *testing.T) {
	if HammingDistance([]byte("this is a test"), []byte("wokka wokka!!!")) != 37 {
		t.Errorf("Hamming distance function is incorrect")
	}
}

func TestDecryptVigenere(t *testing.T) {
	f, err := os.Open("6.txt")
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(f)
	cipherText := make([]byte, 0)
	for scanner.Scan() {
		cipherText = append(cipherText, DecodeBase64(scanner.Text())...)
	}
	key, plainText := DecryptVigenere(cipherText)
	if string(key) != "Terminator X: Bring the noise" {
		t.Errorf("Failed to decrypt vigenere")
	} else {
		fmt.Printf("Solution 6: %s...\n", string(plainText[:25]))
	}
}

// TODO add roundtrip benchmarking tests
