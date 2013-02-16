#include <vector>
#include <algorithm>

using namespace std;

class ProductOfDigits{
	private:
	int factorise(vector<int>& digits, int N, int Max)
	{
		if ( N < 10 )
		{
			digits.push_back(N);
			return digits.size();
		}
		for (int i = Max; i > 1 ; --i)
		{
			if (N % i == 0)
			{
				digits.push_back(i);
				return factorise(digits, N / i , i - 1);
			}
		}
		return -1;
	}
	public:
	int smallestNumber(int N)
	{
		vector<int> digits;
		return factorise(digits, N , 9);
	}
};			
