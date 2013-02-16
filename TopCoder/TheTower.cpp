#include <algorithm>
#include <vector>
using namespace std;

class TheTower {

public:
vector<int> count(vector<int>x, vector<int>y)
{
	int i = 0;
	vector<int> result;
	result.push_back(0);
	int maxX,minX;
	maxX = x[0],minX=x[0];
	int maxY,minY;
	maxY = y[0]; minY = y[0];
	for (i = 1 ; i < x.size() ; ++i)
	{
		maxX = max(maxX, x[i]);
		minX = min(minX, x[i]);
		maxY = max(maxY, y[i]);
		minY = min(minY, y[i]);
		
		
		int count= 0;
		result.push_back(1000000);
		for(int _x = minX; _x <= maxX; ++_x)
		{
			for (int _y = minY ; _y <= maxY ; ++_y)
			{
				count =0;
				for(int j = 0 ; j <= i ; ++j)
				{
					count += abs(_x - x[j]);
					count += abs(_y - y[j]);
				}
				result[i] = min(result[i], count);
			}			
		}
	}
	return result;
}
};
