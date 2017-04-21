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

using namespace std;

string count(string input)
{
    vector<char> order;
    unsigned int counts[28 * 2] = {0};

    for(string::iterator it = input.begin() ; it != input.end() ; ++it)
    {
        if (counts[*it - 0x41] == 0)
            order.push_back(*it);
        counts[*it - 0x41] ++ ;
    }

    ostringstream ss;

    for(vector<char>::iterator it = order.begin(); it != order.end() ; ++it)
    {
        ss << *it << counts[*it - 0x41];
    }

    return ss.str();
}

int main()
{
    string testInput = "ThunderBirdFirefox";

    cout << testInput << endl;

    cout << count(testInput) << endl;

    return 0;
}
