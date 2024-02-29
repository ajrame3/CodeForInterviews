'''
Intuition
We need to track the number of people that reach each node and divide that by the number of seats per 
car, this will tell us the number of cars required to take us to the node that is closer to node0

Approach
DFS

Imagine you are at a leaf node, you move towards 0. There will be only 1 person in the car (you)
Now let's say you're somewhere in the middle of the tree, with a car of size 5. You have 3 children 
nodes. Let's say each child node brings 1 car of 3 people. So a total of 3 * 3 = 9 people. 
Including you there are 10 people now. Now you have 3 cars from the child nodes and one car of your own.
You actually need just 10 / 5 = 2 cars. You take 2 cars and move towards 0
'''

def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)
    self.ans = 0
        
    def dfs(i, prev, people = 1):
        for x in graph[i]:
            if x == prev: continue
            people += dfs(x, i)
        self.ans += (int(ceil(people / seats)) if i else 0)
        return people
        
    dfs(0, 0)
    return self.ans