import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)  # 재귀함수 리미트하여 메모리 초과 방지

n = int(input())
# 딕셔너리로 트리 구현
tree = {}
for i in range(n):
    root, left, right = map(str, input().split())  # 루트, 왼쪽자식, 오른쪽 자식
    tree[root] = (left, right)  # {'A': ('B', 'C')}

def preorder(v):  # 전위순회
    if v != ".":
        print(v, end="")
        preorder(tree[v][0])
        preorder(tree[v][1])


def inorder(v):  # 중위순회
    if v != ".":  # .이 아니면
        inorder(tree[v][0])
        print(v, end="")
        inorder(tree[v][1])


def postorder(v):  # 후위순회
    if v != ".":  # .이 아니면
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end="")

#루트노드 'A'
preorder('A')
print("")
inorder('A')
print("")
postorder('A')