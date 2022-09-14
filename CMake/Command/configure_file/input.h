#cmakedefine VAR 3.14
#cmakedefine VAR1 "Good"
#cmakedefine01 VAR3
#cmakedefine01 VAR4
#cmakedefine NAME "@NAME@"
#cmakedefine NEW_NAME "${NEW_NAME}"
#cmakedefine QUOTE  "@QUOTE@"

#include <iostream>

void ${my_print}() {
	std::cout << "print something" << std::endl;
}

