#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <random>

using namespace std;

const int p = /*pow(2, 19) - 1*/61;


//обратное для a в кольце Z_m
int inv(int a, int m)
{
    for(int x = 1; x < m; ++x) {
        if (((a % m) * (x % m)) % m == 1) {
            return x;
        }
    }
    return -1;
}


void print(const vector<vector<int>>& m)
{
    cout<<"////////////////////"<<endl;
    for(int i = 0; i < m.size(); ++i)   {
        for(int j = 0; j < m.size(); ++j)   {
            cout<<m[i][j]<<"  ";
        }
        cout<<endl;
    }
    cout<<"////////////////////"<<endl<<endl;
}


void print(const vector<vector<double>>& m)
{
    cout<<"////////////////////"<<endl;
    for(int i = 0; i < m.size(); ++i)   {
        for(int j = 0; j < m.size(); ++j)   {
            cout<<m[i][j]<<"  ";
        }
        cout<<endl;
    }
    cout<<"////////////////////"<<endl<<endl;
}



//ставит на диагональ [k][k] ненулевой элемент
int swap_rows(vector<vector<double>>& m, int k)
{
    int n = m.size();
    int i = k;
    //for(int i = k; i < n; ++i)
    //{
    if (m[i][i] == 0)
    {
        //ставим на место этой строки строку с ненулевым эл-ом
        for(int j = i + 1; j < n; ++j)
        {
            if (m[j][i] != 0)
            {
                //меняем i и j строчку
                for(int t = 0; t < n; ++t)
                {
                    swap(m[i][t], m[j][t]);
                }
                return 1;
            }
        }
    }
    //}

    return 0;
}


double det(vector<vector<double>>& m)
{
    int n = m.size();
    int countSwaps = 0;
    //диагональ
    for(int j = 0; j < n; ++j)
    {
        countSwaps += swap_rows(m, j);
        if (m[j][j] == 0)
            return 0;
        //строки
        for(int i = j + 1; i < n; ++i)
        {
            double coef = (1/m[j][j]) * m[i][j];
            //столбцы
            for(int k = 0; k < n; ++k)
            {
                m[i][k] = m[i][k] - m[j][k] * coef;
            }
        }
    }

    double res = 1;
    for(int i = 0; i < n; ++i) {
        res *= m[i][i];
    }
    return res * pow(-1, countSwaps);
}




//ставит на диагональ [k][k] ненулевой элемент
int swap_rows(vector<vector<int>>& m, int k)
{
    int n = m.size();
    int i = k;
    //for(int i = k; i < n; ++i)
    //{
    if (m[i][i] == 0)
    {
        //ставим на место этой строки строку с ненулевым эл-ом
        for(int j = i + 1; j < n; ++j)
        {
            if (m[j][i] != 0)
            {
                //меняем i и j строчку
                for(int t = 0; t < n; ++t)
                {
                    swap(m[i][t], m[j][t]);
                }
                return 1;
            }
        }
    }
    //}
    return 0;
}



int det(vector<vector<int>>& m)
{
    int n = m.size();
    int countSwaps = 0;
    //диагональ
    for(int j = 0; j < n; ++j)
    {
        countSwaps += swap_rows(m, j);
        if (m[j][j] == 0)
            return 0;
        //строки
        for(int i = j + 1; i < n; ++i)
        {
            int coef = (inv(m[j][j], p) * m[i][j]) % p;
            //столбцы
            for(int k = 0; k < n; ++k)
            {
                m[i][k] = m[i][k] - (m[j][k] * coef) % p;
                if (m[i][k] < 0)
                    m[i][k] += p;
            }
        }
    }

    int res = 1;
    for(int i = 0; i < n; ++i) {
        res *= m[i][i];
        res = res % p;
    }
    res = res * pow(-1, countSwaps);
    if (res < 0)
        res += p;
    return res;
}


int main()
{
//    srand(time(0));

//    vector<vector<double>> m = {
//      {-9,2,3},
//        {4,5,6},
//        {7,8,9}

//    };

//    m = { {4,1,0,0},
//          {0,0,3,0},
//          {0,0,0,2},
//          {2,0,0,1}};

//    print(m);
//    cout<<det(m)<<endl;
//    print(m);


    int n, x, y, maxv = 0;
    cin >> n;

    vector<vector<int>> input(n, vector<int>(n, 0));
    for(int i = 0; i < n; ++i) {
        cin>>x>>y;
        int m = 0;
        while (m == 0)
            m = rand() % p;
        input[x][y] = m;
        maxv = max(maxv, max(x,y));
    }

    vector<vector<int>> g(maxv + 1, vector<int>(maxv + 1, 0));
    for(int i = 0; i < maxv + 1; ++i) {
        for(int j = 0; j < maxv + 1; ++j) {
            g[i][j] = input[i][j];
        }
    }

    //print(g);
    double d = det(g);
    //print(g);
    //cout<<"det(g) == "<<d<<endl;

    if (d == 0) {
        cout<<"no"<<endl;
    }
    else {
        cout<<"yes"<<endl;
    }



    return 0;
}
