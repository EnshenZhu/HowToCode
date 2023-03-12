import pandas as pd


class TreeNode:
    def __init__(self, distance_val=0, left=None, right=None, selfIdx=None, parentNodeIdx=None):
        self.distance_val = distance_val
        self.leftNodeIdx = left
        self.rightNodeIdx = right

        self.selfIdx = selfIdx
        self.parentNodeIdx = parentNodeIdx


# The following is the O(n) Find and O(1) Union

def FindNode(x, allNode_Map):
    if x.parentNodeIdx == x.selfIdx:
        return x.selfIdx

    parentNode = allNode_Map[x.parentNodeIdx]
    return FindNode(parentNode, allNode_Map)


def UnionNode(targetIdx, x, y):
    x.parentNodeIdx = targetIdx
    y.parentNodeIdx = targetIdx

    # query out the target parent node
    # x_parentNode = allNode_Map[x_parentNodeIdx]
    # y_parentNode = allNode_Map[y_parentNodeIdx]

    # allNode_Map[x_parentNodeIdx].parentNodeIdx < - targetIdx
    # allNode_Map[y_parentNodeIdx].parentNodeIdx < - targetIdx


def pipeline(data):
    df = pd.DataFrame(data=data)
    # print(df)

    dp_num = df.shape[0] + 1
    allNode_Map = {}
    for idx in range(-dp_num + 1, dp_num):
        allNode_Map[idx] = TreeNode(selfIdx=idx, parentNodeIdx=idx)

    tracker = 0
    for idx in range(-1, -dp_num, -1):
        the_dist = df.iloc[tracker, 0]
        the_pointA_idx = df.iloc[tracker, 1]
        the_pointB_idx = df.iloc[tracker, 2]

        NodeObj = allNode_Map[idx]

        NodeObj.distance_val = the_dist

        the_pointA = allNode_Map[the_pointA_idx]
        the_pointB = allNode_Map[the_pointB_idx]

        NodeObj.leftNodeIdx = FindNode(the_pointA, allNode_Map)
        NodeObj.rightNodeIdx = FindNode(the_pointB, allNode_Map)

        leftNode = allNode_Map[NodeObj.leftNodeIdx]
        rightNode = allNode_Map[NodeObj.rightNodeIdx]

        UnionNode(targetIdx=idx, x=leftNode, y=rightNode)

        tracker += 1

    return allNode_Map


if __name__ == "__main__":
    d = {"distance": [10, 10, 20, 30], "A": [0, 2, 0, 1], "B": [1, 3, 2, 4]}

    allNode_Map = pipeline(d)

    # print(allNode_Map[-1].leftNodeIdx)
    # print(allNode_Map[-1].rightNodeIdx)
    # print(allNode_Map[-1].selfIdx)
    print(allNode_Map[-3].leftNodeIdx)
    print(allNode_Map[-3].rightNodeIdx)
    print(allNode_Map[-3].parentNodeIdx)

    # print(allNode_Map[-1].leftNodeIdx)
    # print(allNode_Map[-1].rightNodeIdx)
    # print(allNode_Map[-1].parentNodeIdx)

    # print(allNode_Map[-2].leftNodeIdx)
    # print(allNode_Map[-2].rightNodeIdx)
    #
    # print(allNode_Map[-3].leftNodeIdx)
    # print(allNode_Map[-3].rightNodeIdx)
    # print(allNode_Map[-3].distance_val)