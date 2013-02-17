#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int levenshtein(string A, string B)
{
    int* memo = new int[(1 + A.size())*( 1 + B.size())];
    int l1 = A.size(), l2 = B.size();
    for(int i = 0; i < l1 ; ++i)
        memo[i] = i;
    for(int i = 1; i < l2 ; ++i)
        memo[ i * l1 ] = i;

    for(int x = 1; x <= l1; ++x)
    {
        for(int y = 1; y <= l2; ++y)
        {
            int equal = 0;
            if(A[x - 1] != B[y - 1])
            {
                equal = 1;
            }
            memo[y*l1 +x] = min( 1 + memo[(y-1)*l1 + x], 
                    min( 1 + memo[(x-1) + y*l1], equal + memo[(y-1)*l1 + (x-1)] ) );
        }
    }
    unsigned int res = memo[l1*l2 -1];
    delete[] memo;
    return res;
}

int LCS(string A, string B)
{
    int* memo = new int[(1 + A.size())*( 1 + B.size())];
    int l1 = A.size(), l2 = B.size();
    for(int i = 0; i < l1 ; ++i)
        memo[i] = 0;
    for(int i = 1; i < l2 ; ++i)
        memo[ i * l1 ] = 0;

    for(int x = 1; x <= l1; ++x)
    {
        for(int y = 1; y <= l2; ++y)
        {
            int equal = 1;
            if(A[x - 1] != B[y - 1])
            {
                equal = 0;
            }
            memo[y*l1 +x] = max( memo[(y-1)*l1 + x], 
                    max( memo[(x-1) + y*l1], equal + memo[(y-1)*l1 + (x-1)] ) );
        }
    }
    unsigned int res = memo[l1*l2 -1];
    delete[] memo;
    return res;
}

int main(int argc, char** argv)
{
    cout << "tennis vs penis distance: " << levenshtein("tennis","penis") << endl;
    cout << "ACGTACGTACGT vs AGTACCTACCGT distance: " << levenshtein("ACGTACGTACGT","AGTACCTACCGT") << endl;
    cout << "ACGTACGTACGT vs AGTACCTACCGT LCS len: " << LCS("ACGTACGTACGT","AGTACCTACCGT") << endl;
    cout << "ABCBDAB vs BDCABA LCS len: " << LCS("ABCBDAB","BDCABA") << endl;
}
