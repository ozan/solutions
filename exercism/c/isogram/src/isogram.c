#include <stdbool.h>
#include "isogram.h"

bool isIsogram(char* str) {
    int bs = 0;  // bit set
    char c;
    while ((c = *str++) != '\0') {
        if (c >= 'A' && c <= 'Z')
            c -= 'A';
        else if (c >= 'a' && c <= 'z')
            c -= 'a';
        else continue;
        if ((bs & (1 << c)) > 0) return false;
        bs |= (1 << c);
    }
    return true;
}
