package erratum

// Use opens a resource and calls Frob
func Use(opener ResourceOpener, input string) (out error) {
	resource, err := opener()

	for err != nil {
		if _, ok := err.(TransientError); !ok {
			return err
		}
		resource, err = opener()
	}

	defer resource.Close()
	defer func() {
		if r := recover(); r != nil {
			if frob, ok := r.(FrobError); ok {
				resource.Defrob(frob.defrobTag)
			}
			out = r.(error)
		}
	}()

	resource.Frob(input)
	return
}
