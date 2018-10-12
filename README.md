## Safe integers for C++

### The problem
Using raw integers is dangerous. Just a few examples:
 - Signed integer overflow is undefined behavior
 - Dividing by zero is undefined behavior

### The solution
 This library allows you to avoid raw integers entirely in your code base. Notice:
 - There is no mention of `int` or any other integer type in the library
 - There are no integer literals in the library either
 - There is no ZERO in the library, so it's impossible to divide by zero
