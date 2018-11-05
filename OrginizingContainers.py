import sys

def organizingContainers(container):

    c=0
    lis=[]
    li=[]
    for e in range(n):
        for i in range(n):
            c+=container[e][i]
        lis.append(c)
        c=0
    for e in range(n):
        for i in range(n):
            c+=container[i][e]
        li.append(c)
        c=0
    for d in li:
        if d not in lis:
            c=1
    if c==0:
        return "Possible"
    else:
        return "Impossible"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
           container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
           container.append(container_t)
        result = organizingContainers(container)
        print(result)
# https://www.hackerrank.com/challenges/organizing-containers-of-balls/submissions/code/65154408
