#pragma once

#include <iostream>

using namespace std;

enum DAY { SUN, MON, TUE, WEN, THR, FRI, STU};

class Example{

    public:

        void say_hello();

        DAY get_cur_day();

};

