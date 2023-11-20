#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <random>

using namespace std;

int leg(int a, int p)
{
    if (a == 0)
        return 0;
    for(int x = 1; x < p; ++x)
    {
        if (a == (x * x) % p)
        {
            return 1;
        }
    }

    return -1;
}


int main()
{
    int n;
    cin >> n;
    int p = n - 1;
    vector<vector<int>> ma(p + 1, vector<int>(p + 1));
    for(int i = 1; i < p + 1; ++i)
    {
        for(int j = 1; j < p + 1; ++j)
        {
            int x = (i-1) - (j-1);
            if (x < 0)
                x += p;
            ma[i][j] = leg(x, p);
        }
    }

    for(int i = 0; i < p + 1; ++i){
        ma[0][i] = 1;
        ma[i][0] = 1;
    }

    for(int i = 1; i < p + 1; ++i){
        ma[i][i] = -1;
    }


    vector<vector<int>> ma2(p + 1, vector<int>(p + 1));
    for(int i = 0; i < p + 1; ++i)
    {
        for(int j = 0; j < p + 1; ++j)
        {
            ma2[i][j] = -1 * ma[i][j];
        }
    }

    for(int i = 0; i < p + 1; ++i)
    {
        for(int j = 0; j < p + 1; ++j)
        {
            if (ma[i][j] == -1)
                ma[i][j] = 0;
            if (ma2[i][j] == -1)
                ma2[i][j] = 0;
        }
    }




   for(int i = 0; i < p + 1; ++i)
    {
        for(int j = 0; j < p + 1; ++j)
        {
            cout<<ma[i][j];
        }
        cout<<endl;

    }
   //cout<<endl;

   for(int i = 0; i < p + 1; ++i)
    {
        for(int j = 0; j < p + 1; ++j)
        {
            cout<<ma2[i][j];
        }
        cout<<endl;

    }



    return 0;
}