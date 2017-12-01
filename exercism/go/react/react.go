package react

// ReactorGraph implements Reactor
type ReactorGraph struct{}

// New creates a new reactor
func New() *ReactorGraph {
	return &ReactorGraph{}
}

// CreateInput creates a new InputNode
func (r *ReactorGraph) CreateInput(value int) InputCell {
	return &Node{value: value, dependencies: make([]*Node, 0)}
}

// CreateCompute1 creates a Node dependant on the given single node
func (r *ReactorGraph) CreateCompute1(a Cell, f func(int) int) ComputeCell {
	n := &Node{a: a.(*Node), f1: f, value: f(a.Value())}
	a.(*Node).addDependency(n)
	return n
}

// CreateCompute2 creates a Node dependant on the given two nodes
func (r *ReactorGraph) CreateCompute2(a Cell, b Cell, f func(int, int) int) ComputeCell {
	n := &Node{a: a.(*Node), b: b.(*Node), f2: f, value: f(a.Value(), b.Value())}
	a.(*Node).addDependency(n)
	b.(*Node).addDependency(n)
	return n
}

// Node implements Cell, InputCell and OutputCell
type Node struct {
	value        int
	dependencies []*Node
	a, b         *Node
	f1           func(int) int
	f2           func(int, int) int
	callbacks    []func(int)
}

func (n *Node) addDependency(m *Node) {
	n.dependencies = append(n.dependencies, m)
}

// Value gets the value of a Node
func (n *Node) Value() int {
	return n.value
}

// SetValue sets the value of a Node
func (n *Node) SetValue(value int) {
	priorValues := map[*Node]int{n: n.value}
	n.value = value
	queue := append([]*Node{}, n.dependencies...)

	// update values of all dependencies in a BFS manner, tracking prior values
	for len(queue) > 0 {
		next := queue[0]
		queue = append(queue[1:], next.dependencies...)
		priorValues[next] = next.value
		if next.f1 != nil {
			next.value = next.f1(next.a.Value())
		} else if next.f2 != nil {
			next.value = next.f2(next.a.Value(), next.b.Value())
		}
	}

	// for any changed value, also trigger callbacks
	for m := range priorValues {
		if priorValues[m] != m.value {
			for _, f := range m.callbacks {
				if f != nil {
					f(m.value)
				}
			}
		}
	}
}

// AddCallback adds a callback to the node which is called when a value is set
func (n *Node) AddCallback(f func(int)) Canceler {
	n.callbacks = append(n.callbacks, f)
	return CallbackCanceler{n, len(n.callbacks) - 1}
}

// CallbackCanceler cancels callbacks
type CallbackCanceler struct {
	node *Node
	idx  int
}

// Cancel cancels the callback
func (cc CallbackCanceler) Cancel() {
	cc.node.callbacks[cc.idx] = nil
}
