class Solution:
    def findRedundantConnection(self, edges):
        chains = {}

        for edge in edges:
            if edge[0] in chains and edge[1] in chains[edge[0]]:
                return edge
            elif edge[0] in chains and edge[1] in chains:
                unioned = chains[edge[0]].union(chains[edge[1]]) 
                chains[edge[0]] = unioned
                chains[edge[1]] = unioned

                for node in chains[edge[0]]:
                    chains[node] = unioned
                for node in chains[edge[1]]:
                    chains[node] = unioned


            elif edge[0] in chains:
                chains[edge[0]].add(edge[1])
                chains[edge[1]] = chains[edge[0]]
            elif edge[1] in chains:
                chains[edge[1]].add(edge[0])
                chains[edge[0]] = chains[edge[1]]
            else:
                newChain = set(edge)
                chains[edge[0]] = newChain
                chains[edge[1]] = newChain

    def solve(self, inputs):
        return self.findRedundantConnection(inputs['edges'])
