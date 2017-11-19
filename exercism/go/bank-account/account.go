package account

import (
	"sync"
)

// Account holds a value and a mutex
type Account struct {
	value  int64
	mutex  sync.Mutex
	closed bool
}

// Open creates and returns an account
func Open(initialDeposit int64) *Account {
	if initialDeposit < 0 {
		return nil
	}
	return &Account{value: initialDeposit}
}

// Balance returns the available balance
func (a *Account) Balance() (int64, bool) {
	a.mutex.Lock()
	defer a.mutex.Unlock()
	// the balance of a closed account cannot be checked
	if a.closed {
		return 0, false
	}
	return a.value, true
}

// Deposit perhaps allows an amount to be deposited
func (a *Account) Deposit(amount int64) (int64, bool) {
	a.mutex.Lock()
	defer a.mutex.Unlock()
	// a closed account cannot be deposited to, nor can a balance go negative
	if a.closed || amount+a.value < 0 {
		return 0, false
	}
	a.value += amount
	return a.value, true
}

// Close closes the account if not closed already
func (a *Account) Close() (int64, bool) {
	a.mutex.Lock()
	defer a.mutex.Unlock()
	// a closed account cannot be re-closed
	if a.closed {
		return 0, false
	}
	a.closed = true
	return a.value, true
}
