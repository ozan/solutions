package linkedlist

import "errors"

type Node struct {
	Val  interface{}
	next *Node
	prev *Node
}

type List struct {
	first *Node
	last  *Node
}

var ErrEmptyList = errors.New("Invalid operation on empty list")

func (e *Node) Next() *Node {
	return e.next
}

func (e *Node) Prev() *Node {
	return e.prev
}

func NewList(vs ...interface{}) *List {
	l := List{}
	for _, v := range vs {
		l.PushBack(v)
	}
	return &l
}

func (l *List) PushFront(v interface{}) {
	n := Node{v, l.first, nil}
	if l.first != nil {
		l.first.prev = &n
	}
	if l.last == nil {
		l.last = &n
	}
	l.first = &n
}

func (l *List) PushBack(v interface{}) {
	n := Node{v, nil, l.last}
	if l.last != nil {
		l.last.next = &n
	}
	if l.first == nil {
		l.first = &n
	}
	l.last = &n
}

func (l *List) PopFront() (interface{}, error) {
	if l.first == nil {
		return nil, ErrEmptyList
	}
	m, n := l.first, l.first.next
	m.next, l.first = nil, n
	if n != nil {
		n.prev = nil
	}
	if m == l.last {
		l.last = nil
	}
	return m.Val, nil
}

func (l *List) PopBack() (interface{}, error) {
	if l.last == nil {
		return nil, ErrEmptyList
	}
	m, n := l.last.prev, l.last
	n.prev, l.last = nil, m
	if m != nil {
		m.next = nil
	}
	if n == l.first {
		l.first = nil
	}
	return n.Val, nil
}

func (l *List) Reverse() {
	rev := List{}
	for {
		n, err := l.PopBack()
		if err != nil {
			break
		}
		rev.PushFront(n)
	}
	for {
		n, err := rev.PopFront()
		if err != nil {
			break
		}
		l.PushFront(n)
	}
}

func (ll *List) First() *Node {
	return ll.first
}

func (ll *List) Last() *Node {
	return ll.last
}
