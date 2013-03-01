#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N;
    cin >> N;
    vector<int> sums, deadlines;
    sums.resize(N);
    deadlines.resize(N);
    vector<int> tasksM;
    vector<int> tasksD;
    tasksM.reserve(N);
    tasksD.reserve(N);

    for(int l = 0 ; l < N ; l ++)
    {
        int M,D;

        cin >> D;
        cin >> M;

        auto it = upper_bound(tasksD.begin(),tasksD.end(),D);

        int pos = it - tasksD.begin();
        tasksD.insert(it, D);
        tasksM.insert(tasksM.begin() + pos, M);

        int i = pos;
        if (i == 0)
        {
            sums[0] = M;
            deadlines[0] = max(0, M - D);
            ++i;
        }
        while(i <= l)
        {
            sums[i] = sums[i-1] + tasksM[i];
            deadlines[i] = max(deadlines[i-1],sums[i] - tasksD[i]);
            ++i;
        }

        cout << deadlines[l] << endl;
            
    }
    return 0;
}

