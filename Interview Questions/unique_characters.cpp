/*
 * Given a string construct a new string containing the occurrences of unique
 * characters in it. You can
 * assume that only a-z & A-Z appear in the string with 'a' being different
 * from 'A'. Also the letters in the output string must be in the order of
 * their occurrence in the input string.
 * e.g. for the string "ThunderBirdFirefox" you must return the string
 * "T1h1u1n1d2e2r3B1i2F1f1o1x1".
 */

#include <sstream>
#include <string>
#include <vector>
#include <iostream>

std::string count(std::string input)
{
    std::vector<char> order;
    unsigned int counts[28 * 2] = {0};

    for(std::string::iterator it = input.begin() ; it != input.end() ; ++it)
    {
        if (counts[*it - 0x41] == 0)
            order.push_back(*it);
        counts[*it - 0x41] ++ ;
    }

    std::ostringstream ss;

    for(std::vector<char>::iterator it = order.begin(); it != order.end() ; ++it)
    {
        ss << *it << counts[*it - 0x41];
    }

    return ss.str();
}

int main(int argc, char** argv)
{
    std::string testInput = "ThunderBirdFirefox";

    std::cout << testInput << std::endl;

    std::cout << count(testInput) << std::endl;


    return 0;
}
