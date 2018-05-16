import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

c = input("c를 입력하세요 : ")
r = int(c) * (800**0.5)
def Distance(a1,b1,a2,b2):
    result = ((a1 - a2)**2) + ((b1-b2)**2)
    return result**0.5

def List_Sort(list): #리스트 내림차순 정렬
    temp_sorted_list = []
    for i in range(200):
        temp_sorted_list.append(max(list))
    return temp_sorted_list

N = [[0 for i in range(2)]for j in range(200)]
x = random.sample(range(800),200)
y = random.sample(range(800),200)

for i in range(200): # random의 중복되지 않는 Node 생성
    N[i][0] = x[i]
    N[i][1] = y[i]

pos = {} # 점들의 위치정보를 dictioary에 저장
for i in range(200):
   pos[i] = [x[i],y[i]]

print(pos) # 생성된 점들의 위치정보 출력

G_list = [] # Graph에 노드를 추가하기위해 G_list라는 List를 만들어 0~199까지 저장
for i in range(200):
    G_list.append(i)
X=nx.Graph() # X라는 그래프 생성 
nx.draw_networkx_nodes(X,pos,node_size=30,nodelist=G_list,node_color='g',label = True) # Graph 에 Node 추가
del G_list # G_list 삭제

label = {} # Graph Label
for i in range(200):
    label[i] = (i)
nx.draw_networkx_labels(X,pos,label,alpja = 1.0) # Graph Node에 Label 을 붙임

linked_Node = {}
list = []
count = 0
for i in range(200):
    T_list = []
    for j in range(200):
        if(Distance(N[i][0],N[i][1],N[j][0],N[j][1]) <= int(r) and i != j ):
            T_list.append(j)
            count += 1
            nx.draw_networkx_edges(X, pos, edgelist=[(i,j)],alpha=1.0) # node끼리 연결
    list.append(count)
    count = 0
    linked_Node[i] = T_list
    del T_list

temp_list = list[:] #list를 temp_list에 복사
sorted_list = []# list를 내림차순으로 정렬하기 위한 변수 sorted_list
Greedy_idx = [] # 연결된 노드 수가 큰 수 부터 저장
for i in range(200): # 연결된 노드가 많은 순으로 list 정렬 = sorted_list
    sorted_list.append(max(temp_list))
    Greedy_idx.append(temp_list.index(max(temp_list)))
    temp_list[temp_list.index(max(temp_list))] = -1
del temp_list # temp_list 삭제
print('     SetCover idx 순서     ')
print(Greedy_idx)
print('     idx에 따른 값       ')
print(sorted_list)

visit = [0 for i in range(200)]
Boom_list = {} # teace
count = 0
count_result = 0
for i in Greedy_idx: # 결과 계산
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

print('결과 = ',count)


T_list = []#trace
for i in range(count):
    T_list.append(i)
nx.draw_networkx_nodes(X,Boom_list,node_size=1000,nodelist=T_list,node_color='r')

plt.show()
