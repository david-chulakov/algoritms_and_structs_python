import queue


class Node:

    def __init__(self, x, k=-1, l=None, r=None, c=''):
        self.freq = x
        self.key = k
        self.left = l
        self.right = r
        self.code = c


    def __lt__(self, otr):
        return self.freq < otr.freq


def haffman(data: str) -> list:
    freqTable = {}
    nodeList = []
    que = queue.PriorityQueue()
    codeTable = {}

    # frequent label init
    for n in data:
        if n in freqTable:
            freqTable[n] += 1
        else:
            freqTable[n] = 1

    # Huffman tree init
    for k, v in freqTable.items():
        nodeList.append(Node(v, k))
        que.put(nodeList[-1])

    # Huffman tree generate
    while que.qsize() > 1:
        n1 = que.get()
        n2 = que.get()
        n1.code = '1'
        n2.code = '0'
        nn = Node(n1.freq + n2.freq, l=n1, r=n2);
        nodeList.append(nn);
        que.put(nodeList[-1])

    # get Huffman code
    def bl(p, codestr=[]):
        codestr.append(p.code)
        if p.left:
            bl(p.left, codestr.copy())
            bl(p.right, codestr.copy())
        else:
            codeTable[p.key] = ''.join(codestr)

    bl(nodeList[-1])

    # print Huffman code result
    print(str(codeTable))

    return codeTable


if __name__ == '__main__':
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
    haffman('beep boop beer!')

