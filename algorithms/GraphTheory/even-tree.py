'''
[Hint]
Try counting the children.
If the subtree has even number of nodes then the edge leading to this subtree can be removed.
Otherwise, you have to keep on searching until you find a suitable edge or the entire tree exhausted.
As it always can be decomposed into forests of even number of nodes,
you will always end up with an answer greater than 1.
'''

def find_children(node_N):
    children = []
    for m in xrange(M):
        if edges[m][1] == node_N:
            children.append(edges[m][0])
            children += find_children(edges[m][0])
    return children


if __name__ == '__main__':
    # load data
    N, M = map(int, raw_input().split())
    edges = []
    for x in xrange(M):
        u, v = map(int, raw_input().split())
        edges.append([u, v])

    # create tree
    tree = []
    for n in xrange(N):
        tree.append([n+1])
    for n in xrange(N):
        tree[n].append(find_children(n+1))

    # remove edge if the subtree has even number of nodes
    count = 0
    for n in xrange(N):
        if(len(tree[n][1]) % 2):
            count += 1
    print count - 1