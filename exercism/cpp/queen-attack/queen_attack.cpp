#include "queen_attack.h"

queen_attack::chess_board::chess_board(coord_t white, coord_t black) {
  if (white.first == black.first && white.second == black.second)
    throw std::domain_error("Pieces must be distinct");
  _white = white;
  _black = black;
}

bool queen_attack::chess_board::can_attack() const {
  return _white.first == _black.first || _white.second == _black.second ||
         abs(_white.first - _black.first) == abs(_white.second - _black.second);
}

queen_attack::chess_board::operator std::string() const {
  std::stringstream ss;
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      if (j > 0)
        ss << ' ';
      coord_t coord = {i, j};
      if (coord == _white)
        ss << 'W';
      else if (coord == _black)
        ss << 'B';
      else
        ss << '_';
    }
    ss << '\n';
  }
  return ss.str();
}
