#include <sstream>
#include <string>
#include <utility>

namespace queen_attack {
typedef std::pair<int, int> coord_t;
class chess_board {
  coord_t _white;
  coord_t _black;

public:
  chess_board() {
    _white = coord_t{0, 3};
    _black = coord_t{7, 3};
  }
  chess_board(coord_t white, coord_t black);

  coord_t white() const { return _white; };
  coord_t black() const { return _black; };

  explicit operator std::string() const;

  bool can_attack() const;
};
}
