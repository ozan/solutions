namespace space_age {
class space_age {
  long _seconds;

public:
  space_age(long seconds) { _seconds = seconds; }
  int seconds() const { return _seconds; }
  float on_earth() const;
  float on_mercury() const;
  float on_venus() const;
  float on_mars() const;
  float on_jupiter() const;
  float on_saturn() const;
  float on_uranus() const;
  float on_neptune() const;
};
}
