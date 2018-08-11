#include <stdlib.h>
#include "queen_attack.h"

#define pr p.row
#define pc p.column
#define qr q.row
#define qc q.column

attack_status_t can_attack(position_t p, position_t q) {
    if ((pr == qr && pc == qc) || pr >= 8 || pc >= 8 || qr >= 8 || qc >= 8) return INVALID_POSITION;
    return pr == qr || pc == qc || abs(pr - qr) == abs(pc - qc);
}
