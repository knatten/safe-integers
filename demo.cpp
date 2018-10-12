#include "include/safe_integers.h"
#include <iostream>
#include <cassert>

using std::cout;
using std::endl;

int main() {
    assert(ONE + FIVE == SIX);
    assert(ONETHOUSAND - THIRTEEN == NINEHUNDREDANDEIGHTYSEVEN);
}
