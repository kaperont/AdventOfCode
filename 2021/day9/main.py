import numpy as np

class vertex:
    value = 10000
    lowest_neighbor = 10000
    found = False

    def __init__(self, value):
        self.value = value
        self.lowest_neighbor = 10000

    def update_lowest_neighbor(self, lowpoint):
        self.lowest_neighbor = lowpoint


input = open("input.txt", "r").readlines()

graph = []

for line in input:
    l = list(line)
    l.pop(-1)
    row = []
    for num in l:
        v = vertex(int(num))
        row.append(v)
    graph.append(row)

#print(graph)
    
i = 0
for row in graph:
    j = 0
    for col in row:
        if i==0 and j==0:

            if col.value < graph[i][j+1].value and col.value < graph[i+1][j].value:
                graph[i][j].lowest_neighbor = col.value
            elif graph[i][j+1].value < graph[i+1][j].value:
                graph[i][j].lowest_neighbor = graph[i][j+1].value
            elif graph[i+1][j].value < graph[i][j+1].value:
                graph[i][j].lowest_neighbor = graph[i+1][j].value
            elif graph[i][j+1].value == graph[i+1][j].value:
                graph[i][j].lowest_neighbor = graph[i][j+1].value

            print(graph[i][j].value, graph[i][j].lowest_neighbor)
        
        elif i==0 and j==99:

            if col.value < graph[i][j-1].value and col.value < graph[i+1][j].value:
                graph[i][j].lowest_neighbor = col.value
            elif graph[i][j-1].value < graph[i+1][j].value:
                graph[i][j].lowest_neighbor = graph[i][j-1].value
            elif graph[i+1][j].value < graph[i][j-1].value:
                graph[i][j].lowest_neighbor = graph[i+1][j].value
            elif graph[i][j-1].value == graph[i+1][j].value:
                graph[i][j].lowest_neighbor = graph[i][j-1].value

            print(graph[i][j].value, graph[i][j].lowest_neighbor)

        elif i==0 and j!=0:

            if col.value < graph[i][j+1].value and col.value < graph[i][j-1].value and col.value < graph[i+1][j].value:
                graph[i][j].lowest_neighbor = col.value
            elif graph[i][j+1].value < graph[i+1][j].value and graph[i][j+1].value < graph[i][j-1].value:
                graph[i][j].lowest_neighbor = graph[i][j+1].value
            elif graph[i][j-1].value < graph[i+1][j].value and graph[i][j-1].value < graph[i][j+1].value:
                graph[i][j].lowest_neighbor = graph[i][j-1].value
            elif graph[i+1][j].value < graph[i][j+1].value and graph[i+1][j].value < graph[i][j-1].value:
                graph[i][j].lowest_neighbor = graph[i+1][j].value
            elif graph[i][j+1].value == graph[i+1][j].value and graph[i][j+1].value == graph[i][j-1].value:
                graph[i][j].lowest_neighbor = graph[i][j+1].value

            print(graph[i][j].value, graph[i][j].lowest_neighbor)
        j += 1
    i += 1