# Разрез минимальной плотности
Реализуйте приближённый алгоритм поиска разреза минимальной плотности (алгоритм на основе собственного вектора, соответствующего второму по величине собственному значению лапласиана графа). 
### На вход программы подаются рёбра неориентированного графа в виде:
```
<количество рёбер>
<id начала ребра> <id конца ребра>
<id начала ребра> <id конца ребра>
...
```

id вершин натуральные числа (необязательно последовательные), изолированных вершин нет. Выход программы разделённые пробельными символами и упорядоченные по возрастанию номера вершин, включённых в наименьшую по мощности компоненту разреза. Если есть разные полученные в строгом соответствии с алгоритмом ответы, имеющие одинаковую плотность, то нужно вывести лексикографически минимальный из них. (Минимальный как список чисел, а не как строку, например, из разрезов "1 2 3 112” и “1 2 3 12” нужно вывести именно “1 2 3 12”.)
