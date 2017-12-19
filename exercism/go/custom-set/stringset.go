package stringset

import (
	"bytes"
)

// Set is simply backed by a map of strings to true
type Set map[string]bool

// New returns an empty set
func New() Set {
	return make(Set)
}

// NewFromSlice returns a set consisting of the elemens in a slice
func NewFromSlice(xs []string) Set {
	set := New()
	for _, x := range xs {
		set[x] = true
	}
	return set
}

// IsEmpty returns true if underlying map has no items
func (s Set) IsEmpty() bool {
	return len(s) == 0
}

// Has tests set membership
func (s Set) Has(k string) bool {
	_, ok := s[k]
	return ok
}

// Subset tests if the first set is a subset of the second
func Subset(s, t Set) bool {
	if len(s) > len(t) {
		return false
	}
	for sx := range s {
		if _, ok := t[sx]; !ok {
			return false
		}
	}
	return true
}

// Disjoint tests that neither set has elements of the other
func Disjoint(s, t Set) bool {
	for sx := range s {
		if _, ok := t[sx]; ok {
			return false
		}
	}
	return true
}

// Equal tests that the two sets are exactly equal
func Equal(s, t Set) bool {
	return len(s) == len(t) && Subset(s, t)
}

// Add adds an item to the set
func (s Set) Add(x string) {
	s[x] = true
}

// Intersection creates a new set of elements in both s and t
func Intersection(s, t Set) Set {
	out := New()
	for x := range s {
		if _, ok := t[x]; ok {
			out[x] = true
		}
	}
	return out
}

// Difference creates a new set of elements in s but not t
func Difference(s, t Set) Set {
	out := New()
	for x := range s {
		if _, ok := t[x]; !ok {
			out[x] = true
		}
	}
	return out
}

// Union creates a new set of elements in both s and t
func Union(s, t Set) Set {
	out := New()
	for x := range s {
		out[x] = true
	}
	for x := range t {
		out[x] = true
	}
	return out
}
func (s Set) String() string {
	var b bytes.Buffer
	b.WriteByte('{')
	comma := false
	for x := range s {
		if comma {
			b.WriteString(", ")
		} else {
			comma = true
		}
		b.WriteByte('"')
		b.WriteString(x)
		b.WriteByte('"')
	}
	b.WriteByte('}')
	return b.String()
}
