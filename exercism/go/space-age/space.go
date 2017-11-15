package space

// Planet is a string
type Planet string

var yearSeconds = map[Planet]float64{
	"Earth":   31557600.0,
	"Mercury": 7600543.82,
	"Venus":   19414149.05,
	"Mars":    59354032.69,
	"Jupiter": 374355659.12,
	"Saturn":  929292362.88,
	"Uranus":  2651370019.33,
	"Neptune": 5200418560.03,
}

// Age returns age on given planet
func Age(seconds float64, planet Planet) float64 {
	n := seconds / yearSeconds[planet]
	return float64(int(n*100+.5)) / 100
}
