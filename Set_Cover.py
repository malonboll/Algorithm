import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

c = input("c�� �Է��ϼ��� : ")
r = int(c) * (800**0.5)
def Distance(a1,b1,a2,b2):
    result = ((a1 - a2)**2) + ((b1-b2)**2)
    return result**0.5

def List_Sort(list): #����Ʈ �������� ����
    temp_sorted_list = []
    for i in range(200):
        temp_sorted_list.append(max(list))
    return temp_sorted_list

N = [[0 for i in range(2)]for j in range(200)]
x = random.sample(range(800),200)
y = random.sample(range(800),200)

for i in range(200): # random�� �ߺ����� �ʴ� Node ����
    N[i][0] = x[i]
    N[i][1] = y[i]

pos = {} # ������ ��ġ������ dictioary�� ����
for i in range(200):
   pos[i] = [x[i],y[i]]

print(pos) # ������ ������ ��ġ���� ���

G_list = [] # Graph�� ��带 �߰��ϱ����� G_list��� List�� ����� 0~199���� ����
for i in range(200):
    G_list.append(i)
X=nx.Graph() # X��� �׷��� ���� 
nx.draw_networkx_nodes(X,pos,node_size=30,nodelist=G_list,node_color='g',label = True) # Graph �� Node �߰�
del G_list # G_list ����

label = {} # Graph Label
for i in range(200):
    label[i] = (i)
nx.draw_networkx_labels(X,pos,label,alpja = 1.0) # Graph Node�� Label �� ����

linked_Node = {}
list = []
count = 0
for i in range(200):
    T_list = []
    for j in range(200):
        if(Distance(N[i][0],N[i][1],N[j][0],N[j][1]) <= int(r) and i != j ):
            T_list.append(j)
            count += 1
            nx.draw_networkx_edges(X, pos, edgelist=[(i,j)],alpha=1.0) # node���� ����
    list.append(count)
    count = 0
    linked_Node[i] = T_list
    del T_list

temp_list = list[:] #list�� temp_list�� ����
sorted_list = []# list�� ������������ �����ϱ� ���� ���� sorted_list
Greedy_idx = [] # ����� ��� ���� ū �� ���� ����
for i in range(200): # ����� ��尡 ���� ������ list ���� = sorted_list
    sorted_list.append(max(temp_list))
    Greedy_idx.append(temp_list.index(max(temp_list)))
    temp_list[temp_list.index(max(temp_list))] = -1
del temp_list # temp_list ����
print('     SetCover idx ����     ')
print(Greedy_idx)
print('     idx�� ���� ��       ')
print(sorted_list)

visit = [0 for i in range(200)]
Boom_list = {} # teace
count = 0
count_result = 0
for i in Greedy_idx: # ��� ���
    if(max(visit) != -1):
        if(visit[i] != -1):
            Boom_list[count] = [x[i],y[i]] # trace
            count_result += list[i]
            count += 1
            visit[i] = -1
            for z in linked_Node[i]:
                visit[z] = -1
    else:
        break

print('��� = ',count)


T_list = []#trace
for i in range(count):
    T_list.append(i)
nx.draw_networkx_nodes(X,Boom_list,node_size=1000,nodelist=T_list,node_color='r')

plt.show()
