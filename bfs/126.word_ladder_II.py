"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:
    1 <= beginWord.length <= 5
    endWord.length == beginWord.length
    1 <= wordList.length <= 500
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the words in wordList are unique.
    The sum of all shortest transformation sequences does not exceed 105.
"""


# Solution 1: pure BFS - TLE
import string
from collections import deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)

        if endWord not in word_set:
            return []

        visited = set()
        queue = deque([[beginWord]])
        res = []

        while queue:
            level_size = len(queue)
            level_visited = set()

            for _ in range(level_size):
                path = queue.popleft()
                word = path[-1]

                if word == endWord:
                    res.append(path)

                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        new_word = word[:i] + c + word[i+1:]
                        
                        if new_word in word_set and new_word not in visited:
                            queue.append(path + [new_word])
                            level_visited.add(new_word)

            if res:
                return res
            
            visited.update(level_visited)

        return []
    
    
# Solution 2: BFS + backtracking
import string
from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        # ==========================================
        # Phase 1: BFS to build the 'parents' graph
        # ==========================================
        
        # parents[child] = [list of parents that lead to child with shortest distance]
        # e.g., parents['cog'] = ['dog', 'log']
        parents = defaultdict(list)
        
        # distance[word] stores the shortest steps from beginWord to 'word'
        # This acts as our 'visited' check.
        distance = {beginWord: 0}
        
        queue = deque([beginWord])
        found = False
        
        while queue:
            # Processing level by level isn't strictly necessary with the 'distance' map,
            # but it can help us break early if we find the endWord.
            curr_word = queue.popleft()
            
            # Optimization: If we pulled endWord from queue, we don't need to expand it further.
            # But we must continue processing other nodes in the queue to finish the graph.
            if curr_word == endWord:
                found = True
                continue
            
            # If we found the shortest path already, and the current node is deeper, 
            # we can stop processing this branch (pruning).
            if found and distance[curr_word] >= distance[endWord]:
                continue

            cur_dist = distance[curr_word]

            for i in range(len(curr_word)):
                for c in string.ascii_lowercase:
                    next_word = curr_word[:i] + c + curr_word[i+1:]

                    if next_word in word_set:
                        # Case 1: First time visiting this node (Unvisited)
                        if next_word not in distance:
                            distance[next_word] = cur_dist + 1
                            parents[next_word].append(curr_word)
                            queue.append(next_word)
                        
                        # Case 2: Visited, but found another path of the SAME shortest length
                        # We add the new parent, but DO NOT add to queue (avoid duplicates)
                        elif distance[next_word] == cur_dist + 1:
                            parents[next_word].append(curr_word)

        # If we never reached the endWord
        if not found:
            return []

        # ==========================================
        # Phase 2: Backtracking (DFS) to reconstruct paths
        # ==========================================
        res = []
        
        # We start from endWord and walk backwards to beginWord
        def backtrack(word, current_path):
            if word == beginWord:
                # We reached the start! Add the path (reversed) to results
                # current_path is [end, ..., start], so we reverse it
                res.append(current_path[::-1])
                return

            # Recursively explore all parents
            for parent in parents[word]:
                current_path.append(parent)
                backtrack(parent, current_path)
                current_path.pop() # Backtrack

        backtrack(endWord, [endWord])
        return res
    