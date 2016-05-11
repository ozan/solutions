module SpaceAge (Planet(..), ageOn) where


data Planet = Earth | Mercury | Venus | Mars | Jupiter | Saturn | Uranus
            | Neptune deriving (Eq, Enum)

earthSeconds :: Double
earthSeconds = 31557600

orbitalPeriods :: [(Planet, Double)]
orbitalPeriods = [
  (Earth, 1),
  (Mercury, 0.2408467),
  (Venus, 0.61519726),
  (Mars, 1.8808158),
  (Jupiter, 11.862615),
  (Saturn, 29.447498),
  (Uranus, 84.016846),
  (Neptune, 164.79132)]

ageOn :: Planet -> Double -> Double
ageOn planet secs =
  case lookup planet orbitalPeriods of
    Just period -> secs / earthSeconds / period
    Nothing -> error "Period not known"
