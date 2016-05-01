using System.Collections.Generic;

namespace Exercism
{
    public class SpaceAge
    {
        public long Seconds { get; private set; }

        enum Planet {
            Earth,
            Mercury,
            Venus,
            Mars,
            Jupiter,
            Saturn,
            Uranus,
            Neptune
        };

        int earthSeconds = 31557600;

        Dictionary<Planet, double> secondsPerYear;

        public SpaceAge(long seconds)
        {
            Seconds = seconds;
            secondsPerYear = new Dictionary<Planet, double> {
                { Planet.Earth, 1.0 * earthSeconds },
                { Planet.Mercury, 0.2408467 * earthSeconds },
                { Planet.Venus, 0.61519726 * earthSeconds },
                { Planet.Mars, 1.8808158 * earthSeconds },
                { Planet.Jupiter, 11.862615 * earthSeconds },
                { Planet.Saturn, 29.447498 * earthSeconds },
                { Planet.Uranus, 84.016846 * earthSeconds },
                { Planet.Neptune, 164.79132 * earthSeconds }
            };
        }

        public double OnEarth() { return ageOnPlanet(Planet.Earth); }
        public double OnMercury() { return ageOnPlanet(Planet.Mercury); }
        public double OnVenus() { return ageOnPlanet(Planet.Venus); }
        public double OnMars() { return ageOnPlanet(Planet.Mars); }
        public double OnJupiter() { return ageOnPlanet(Planet.Jupiter); }
        public double OnSaturn() { return ageOnPlanet(Planet.Saturn); }
        public double OnUranus() { return ageOnPlanet(Planet.Uranus); }
        public double OnNeptune() { return ageOnPlanet(Planet.Neptune); }

        private double ageOnPlanet(Planet planet)
        {
            return Seconds / secondsPerYear[planet];
        }
    }
}
