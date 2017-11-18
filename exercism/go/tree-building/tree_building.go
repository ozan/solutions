package tree

import (
	"errors"
	"sort"
)

// Record is an id, parent pair
type Record struct {
	ID, Parent int
}

// Node is a tree node
type Node struct {
	ID       int
	Children []*Node
}

// Build constructs a tree from a slice of records
func Build(records []Record) (*Node, error) {
	nodes := make(map[int]*Node)
	numRecords := len(records)

	if numRecords == 0 {
		return nil, nil
	}

	// sort records by parent, then own id. this will simplify validation as well
	// as parent lookup (when iterating, we will be able to verify that a parent,
	// if valid, has been seen)
	sort.Slice(records, func(i, j int) bool {
		return numRecords*records[i].Parent+records[i].ID < numRecords*records[j].Parent+records[j].ID
	})

	for i, r := range records {
		n := &Node{ID: r.ID}
		if i == 0 {
			switch {
			case r.ID != 0:
				return nil, errors.New("No root node")
			case r.Parent > 0:
				return nil, errors.New("Root node can't have parent")
			}
			// root = n
		} else {
			switch {
			case r.ID >= numRecords:
				return nil, errors.New("ID outside range")
			case r.ID <= r.Parent:
				return nil, errors.New("Cycle")
			case nodes[r.Parent] == nil:
				return nil, errors.New("Invalid parent")
			}
			nodes[r.Parent].Children = append(nodes[r.Parent].Children, n)
		}

		// track location of each node to avoid traversing to locate parent
		nodes[r.ID] = n
	}
	return nodes[0], nil
}
