package tournament

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"sort"
	"strings"
)

type results struct {
	win  uint
	loss uint
	draw uint
}

type teamResults struct {
	team string
	res  results
}

func (r *results) score() uint {
	return 3*r.win + r.draw
}

type teamResultList []teamResults

// Tally writes a tally of the results read from reader
func Tally(r io.Reader, w io.Writer) error {
	m := make(map[string]*results)
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		ss := strings.Split(scanner.Text(), ";")
		if len(ss) == 1 {
			continue
		}
		if len(ss) != 3 {
			return errors.New("Result line should have 3 parts")
		}
		a, b, res := ss[0], ss[1], ss[2]
		if m[a] == nil {
			m[a] = &results{}
		}
		if m[b] == nil {
			m[b] = &results{}
		}
		switch res {
		case "win":
			m[a].win++
			m[b].loss++
		case "loss":
			m[a].loss++
			m[b].win++
		case "draw":
			m[a].draw++
			m[b].draw++
		default:
			return errors.New("Invaild result type")
		}
	}
	ranking := make(teamResultList, len(m))
	i := 0
	for k, v := range m {
		ranking[i] = teamResults{k, *v}
		i++
	}
	sort.Sort(sort.Reverse(ranking))
	fmt.Fprintf(w, "Team                           | MP |  W |  D |  L |  P\n")
	for _, tr := range ranking {
		fmt.Fprintf(w, "%-30s | %2d | %2d | %2d | %2d | %2d\n", tr.team, tr.res.win+tr.res.loss+tr.res.draw, tr.res.win, tr.res.draw, tr.res.loss, tr.res.score())
	}
	return nil
}

func (l teamResultList) Len() int { return len(l) }
func (l teamResultList) Less(i, j int) bool {
	delta := int(l[i].res.score()) - int(l[j].res.score())
	if delta == 0 {
		return l[i].team > l[j].team
	}
	return delta < 0
}
func (l teamResultList) Swap(i, j int) { l[i], l[j] = l[j], l[i] }
