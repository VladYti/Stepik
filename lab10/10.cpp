#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <random>
#include <bitset>

using namespace std;

struct kl {
    int x;
    int y;
    int z;
};


string to_binary_string(unsigned int n, int k)
{
    string buffer;
    buffer.reserve(numeric_limits<unsigned int>::digits);
    do
    {
        buffer += char('0' + n % 2);
        n = n / 2;
    } while (n > 0);
    string res = string(buffer.crbegin(), buffer.crend());
    while (res.size() != k)
        res.insert(0, 1, '0');
    return res;
}


int main()
{
    int n, m;
    cin>>n>>m;
    int k = ceil(log2(n));
    double count = (7 * m)/8.0;

    int x, y, z;
    vector<kl> f(m);
    for(int i = 0; i < m; ++i)
    {
        cin>>x>>y>>z;
        f[i].x = x;
        f[i].y = y;
        f[i].z = z;
    }

    //матрица (левая) для кси
    vector<vector<int>> m1(pow(2, k), vector<int>(k));
    //cout<<"k = "<<k<<endl;
    for(int i = 0; i < pow(2, k); ++i)
    {
        string s = to_binary_string(i, k);
        for(int j = 0; j < k; ++j)
        {
            m1[i][j] = s[j] - 48;
        }
    }

    /*for(int i = 0; i < pow(2, k); ++i)
    {

        for(int j = 0; j < k; ++j)
        {
            cout<<m1[i][j]<<' ';
        }
        cout<<endl;
    }*/


    vector<vector<int>> m2(pow(2, k), vector<int>(pow(2, k+1)));
    //по столбцам
    for(int j = 0; j < pow(2, k+1); ++j)
    {
        string s = to_binary_string(j, k+1);  //набор альф для данного столбца i
        for(int i = 0; i < pow(2, k); ++i)
        {
            m2[i][j] = s[0] - 48;
            int b = 0;          //номер столбца для кси из первой матрицы
            for (int t = 1; t < s.size(); ++t)
            {
                int alpha = s[t] - 48;
                m2[i][j] = m2[i][j] ^ (alpha*m1[i][b++]);
            }
        }
    }



    /*for(int i = 0; i < pow(2, k); ++i)
    {

        for(int j = 0; j < pow(2, k  +1); ++j)
        {
            cout<<m2[i][j]<<' ';
        }
        cout<<endl;
    }*/


    //столбцы
    for(int j = 0; j < pow(2, k + 1); ++j)
    {
        int t = 0;  //колво истинных скобок
        for (auto u : f)
        {
            bool res = 0;

            if (u.x < 0)
                res = res || !m2[-u.x - 1][j];
            else
                res = res || m2[u.x - 1][j];

            if (u.y < 0)
                res = res || !m2[-u.y - 1][j];
            else
                res = res || m2[u.y - 1][j];

            if (u.z < 0)
                res = res || !m2[-u.z - 1][j];
            else
                res = res || m2[u.z - 1][j];

            if (res == true)
                t++;

            if (t > count)
            {
                for(int i = 0; i < n; ++i)
                {
                    cout<<m2[i][j];
                }
                return 0;
            }

        }


    }





    return 0;
}
