#include <algorithm>
#include <vector>
using namespace std;

class StrengthOrIntellect
{

	public:
	int numberOfMissions(vector<int> str, vector<int> intel, vector<int> points)
	{
		int res = 0;
		int curS = 1, curI = 1;
		int pointsAvail = 0;
		
		while (res < str.size())
		{
			int minI = -1;
			int minS = -1;
			for(int i = 0 ; i < str.size(); ++i)
			{
				if (points[i] != -1)
				{
					if(minI == -1 || intel[i] < minI)
						minI = i;
					if(minS == -1 || str[i] < minS)
						minS = i;
				}
			}
			
			if( str[minS] - curS < intel[minI] - curI )
			{
				int needPoints = 	str[minS] - curS;
				if (needPoints < 0)
					needPoints = 0;
				if (needPoints > pointsAvail)
					break;
				pointsAvail -= needPoints;
				pointsAvail += points[minS];
				curS += needPoints;
			}
			else
			{
				int needPoints = 	intel[minI] - curI;
				if (needPoints < 0)
					needPoints = 0;
				if (needPoints > pointsAvail)
					break;
				pointsAvail -= needPoints;
				pointsAvail += points[minI];
				curI += needPoints;
			}
			res ++;
		}
		return res;
	}
};
