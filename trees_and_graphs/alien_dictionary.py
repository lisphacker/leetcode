from itertools import groupby
from typing import List, Dict, Set, Tuple

Graph = Dict[str, Set[str]]
Ordering = List[str]

class Solution:
    def compute_orderings(self, words: List[str], orderings: List[Ordering]):
        ordering = []
        seen = set()
        last = None
        non_empty_words = []
        for word in words:
            if len(word) == 0:
                continue
            non_empty_words.append(word)
            s = word[0]
            if s != last:
                if s in seen:
                    print(words, word, s, seen)
                    raise Exception('Invalid ordering')
                else:
                    ordering.append(s)
                    seen.add(s)
                
            last = s
                        
        if len(ordering) > 0:
            orderings.append(ordering)
            
        groups = groupby(non_empty_words, lambda w: w[0])
        for s, group in groups:
            words3 = [s[1:] for s in group]
            self.compute_orderings(words3, orderings)
            
    def compute_graph(self, orderings: List[Ordering]) -> Tuple[Graph, Graph]:
        forward_graph = dict()
        backward_graph = dict()

        for ordering in orderings:
            if len(ordering) == 1:
                i = ordering[0]
                if i not in forward_graph:
                    forward_graph[i] = set()
            else:
                for i, j in zip(ordering, ordering[1:]):
                    if i in forward_graph:
                        forward_graph[i].add(j)
                    else:
                        forward_graph[i] = set([j])

                    if j in backward_graph:
                        backward_graph[j].add(i)
                    else:
                        backward_graph[j] = set([i])

        return forward_graph, backward_graph
        
    def flatten_graph(self, 
                      forward_graph: Graph, backward_graph: Graph,
                      unordered_alphabets: List[str],
                      alphabets: Set[str]) -> str:

        for j, ii in backward_graph.items():
            if len(ii) > 1:
                ii = list(ii)
                for i1, i2 in zip(ii, ii[1:]):
                    forward_graph[i1].remove(j)
                    forward_graph[i1].add(i2)

        no_changes = False
        while not no_changes:
            no_changes = True
            for i, jj in forward_graph.items():
                if len(jj) > 1:
                    jj = list(jj)
                    for j1, j2 in zip(jj, jj[1:]):
                        forward_graph[i].remove(j2)
                        if j1 in forward_graph:
                            forward_graph[j1].add(j2)
                        else:
                            forward_graph[j1] = {j2}
                    no_changes = False

        return forward_graph

    def search_ordering_rec(self, 
                            forward_graph: Graph,
                            a: str,
                            ordering: Ordering, 
                            used: Set[str], 
                            alphabets: List[str]) -> Ordering:
        if a in used:
            return None
        
        ordering.append(a)
        used.add(a)
        
        if len(ordering) == len(alphabets):
            for b in forward_graph.get(a, set()):
                # print(a, b, used)
                if b in used:
                    used.remove(a)
                    ordering.pop()
                    return None
            return ordering
        
        if a in forward_graph:
            for bs in forward_graph[a]:
                for b in bs:
                    o = self.search_ordering_rec(forward_graph, b, ordering, used, alphabets)
                    if o is not None:
                        return o
        used.remove(a)
        ordering.pop()
        
        return None
    
    def search_ordering(self,
                        forward_graph: Graph, 
                        unordered_alphabets: List[str], 
                        alphabets: List[str]) -> str:
        init_ordering = [a for a in unordered_alphabets]
        for a in forward_graph:
            ordering = self.search_ordering_rec(forward_graph, a, init_ordering, set(), alphabets)
            if ordering is not None:
                return ''.join(ordering)
            
        return ''.join(init_ordering)
        
    def traverse(self, graph: Graph, i: str, acc: List[str], used: Set[str]):
        print('traverse ', 'i=', i, ', used=', used, ', acc=', acc)
        if i in used:
            return

        acc.append(i)
        used.add(i)
         
        for jj in graph.get(i, {}):
            for j in jj:
                self.traverse(graph, j, acc, used)

    def generate_final_ordering(self, 
                                forward_graph: Graph, 
                                backward_graph: Graph, alphabets: Set[str]) -> str:
        start_letters = alphabets - backward_graph.keys()
        if len(start_letters) == len(alphabets):
            return "" # To work around error in judger
        
        out_list = []
        used = set()
        
        for start_letter in start_letters:
            self.traverse(forward_graph, start_letter, out_list, used)
        return ''.join(out_list)

        
        
    def alienOrder(self, words: List[str]) -> str:
        alphabets = set(''.join(words))
        
        orderings = []
        try:
            self.compute_orderings(words, orderings)
        except:
            return ''

        forward_graph, backward_graph = self.compute_graph(orderings)
        
        ordered_alphabets = set()
        for i in forward_graph:
            ordered_alphabets.add(i)
            for j in forward_graph[i]:
                ordered_alphabets.add(j)
        unordered_alphabets = alphabets - ordered_alphabets
        
        print('Orderings', orderings)
        print('Forward graph', forward_graph)
        print('Backward graph', backward_graph)
        print('Unordered alphabets', unordered_alphabets)
        print('')
        
        self.flatten_graph(forward_graph, backward_graph, [s for s in unordered_alphabets], alphabets)
        
        print('Flattened forward graph', forward_graph)
        
        #return self.search_ordering(forward_graph, [s for s in unordered_alphabets], alphabets)
        return self.generate_final_ordering(forward_graph, backward_graph, alphabets)
        
'''
Test cases
['ac', ad', 'bc', bd']
'''