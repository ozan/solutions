package flatten

// Flatten returns a flattened version of the given slice
func Flatten(given interface{}) []interface{} {
	out := []interface{}{}
	if slice, ok := given.([]interface{}); ok {
		for _, x := range slice {
			out = append(out, Flatten(x)...)
		}
		return out
	}
	if given != nil {
		out = []interface{}{given}
	}
	return out
}
