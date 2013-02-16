#include <vector>
#include <algorithm>

using namespace std;


class TheSimpleGame {
	public:
	int count( int n , vector<int> x , vector<int> y)
	{
		int moves = 0;
		for (int i = 0 ; i < x.size() ; ++i)
		{
			moves += min(abs(1 - x[i]), abs(n - x[i]));
			moves += min(abs(1 - y[i]), abs(n - y[i]));
		}
		return moves;
	}
};
