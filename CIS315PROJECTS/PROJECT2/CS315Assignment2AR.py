from collections import defaultdict

def addEdge(G, u, v):
    G[u].append(v)

def findAllPaths(G, u, v, path=[]):
    path = path + [u]
    if u == v:
        return [path]
    paths = []
    for node in G[u]:
        if node not in path:
            new_paths = findAllPaths(G, node, v, path)
        for new_path in new_paths:
            paths.append(new_path)
    return paths

def findLongestPath(G, u, v, path=[]):
    path = path + [u]
    if u == v:
        return path
    longest = None
    for node in G[u]:
        if node not in path:
            new_path = findLongestPath(G, node, v, path)
            if new_path:
                if not longest or len(new_path) > len(longest):
                    longest = new_path
    return longest


def findShortestPath(G, u, v, path=[]):
    path = path + [u]
    if u == v:
        return path
    shortest = None
    for node in G[u]:
        if node not in path:
            new_path = findShortestPath(G, node, v, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    return shortest


def solve():
    G = defaultdict(list)
    V = int(input())
    E = int(input())
    for _ in range(E):
        edges = input().strip().split()
        u = edges[0]
        v = edges[1]
        addEdge(G, u, v)

    all_paths = findAllPaths(G, str(1), str(V))

    SP = len(findShortestPath(G, str(1), str(V))) - 1
    LP = len(findLongestPath(G, str(1), str(V))) - 1

    SPNUM = 0
    LPNUM = 0

    for p in all_paths:
        if len(p) == SP+1:
            SPNUM += 1
        if len(p) == LP+1:
            LPNUM += 1
    print("Shortest path: ", SP)
    print("Number of short paths:", SPNUM)
    print("Longest path: ", LP)
    print("Number of long paths", LPNUM)


if __name__ == "__main__":
    solve()
