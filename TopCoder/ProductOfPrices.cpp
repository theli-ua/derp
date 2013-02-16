#include <algorithm>
#include <vector>

using namespace std;

class ProductOfPrices
{
	
	
	public:
	int product(unsigned int N, unsigned int L, unsigned int X0, unsigned int A, unsigned int B)
	{
		vector<unsigned int> places;
		
		places.push_back( X0 % L );
		A %= L;
		B %= L;
		for (int i = 1;  i < N ; ++i)
		{
			places.push_back(((places[i-1]*A)%L + B) % L);
		}
		unsigned int res = 1;
		for (int i = N - 1; i > 0 ; --i)
		{
			unsigned int sum = 0;
			for(int j = i - 1; j >= 0 ; --j)
			{
				if (places[i] > places[j])
					sum += places[i] - places[j];
				else
					sum += places[j] - places[i];
				sum %= 1000000007;
			}
			res = (res * sum) % 1000000007;
		}
				
		return res;
	}
};
