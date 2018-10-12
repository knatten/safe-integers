## Safe integers for C++

Header only library for safe integers in C++. The library is found in `include/safe_integers.h`.

### The problem
Using raw integers is dangerous. Just a few examples:
 - Signed integer overflow is undefined behavior
 - Dividing by zero is undefined behavior

### The solution
 This library allows you to avoid raw integers entirely in your code base. Notice:
 - There is no mention of `int` or any other integer type in the library
 - There are no integer literals in the library either
 - There is no ZERO in the library, so it's impossible to divide by zero

### Demo
```cpp
cout << ONE << endl;
cout << FIFTYTWO - TWELVE << endl;
```

### Excerpt from the library:
```cpp
constexpr auto ONE = +!!"";
constexpr auto TWO = ONE + ONE;
constexpr auto THREE = TWO + ONE;
//(...)
constexpr auto SIXHUNDREDANDTHIRTYNINETHOUSANDNINEHUNDREDANDNINETYNINE = SIXHUNDREDANDTHIRTYNINETHOUSANDNINEHUNDREDANDNINETYEIGHT + ONE;
constexpr auto SIXHUNDREDANDFORTYTHOUSAND = SIXHUNDREDANDTHIRTYNINETHOUSANDNINEHUNDREDANDNINETYNINE + ONE;
// SIXHUNDREDANDFORTYTHOUSAND ought to be enough for anybody
```

### Credits
Based on ideas by [moonette](https://twitter.com/willkirkby/status/1041657267198849024) and [Ólafur Waage](https://twitter.com/olafurw/status/1050647090731175936)


### Just to be on the safe side:
Yes, this is a joke.

