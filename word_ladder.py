"""
Given two words beginWord and endWord, and a list of words wordList, create a function that returns the length of the shortest transformation sequence from beginWord to endWord.
"""
def difference(word1, word2):
    counter = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            counter += 1
    return counter

def transformationSequenceLength(beginWord, endWord, wordList):
    if len(wordList) == 0 or endWord not in wordList:
        return 0
    adjList = {}
    for word in wordList:
        adjList[word] = set()
    for i in range(len(wordList)):
        for j in range(i+1, len(wordList)):
            if (difference(wordList[i], wordList[j]) == 1):
                adjList[wordList[i]].add(wordList[j])
                adjList[wordList[j]].add(wordList[i])
    visited = set()
    queue = []
    i = 0
    for word in wordList:
        if difference(beginWord, word) == 1:
            queue.append([word, 1])
            visited.add(word)
    while i < len(queue):
        word = queue[i][0]
        level = queue[i][1]
        i += 1
        if word == endWord:
            return level + 1
        else:
            for transformation in adjList[word]:
                if transformation not in visited:
                    queue.append([transformation, level+1])
                    visited.add(transformation)
    return 0

def transformationSequenceLength2(beginWord, endWord, wordList):
    if len(wordList) == 0 or endWord not in wordList:
        return 0
    lenWord = len(wordList[0])
    forms = {}
    for word in wordList:
        for i in range(lenWord):
            form = word[:i] + '*' + word[i+1:]
            if forms.get(form) is None:
                forms[form] = []
            forms[form].append(word)
    visited = set()
    queue = [[beginWord, 0]]
    i = 0
    while i < len(queue):
        word = queue[i][0]
        level = queue[i][1]
        i += 1
        if word == endWord:
            return level+1
        else:
            for j in range(lenWord):
                form = word[:j] + '*' + word[j+1:]
                if forms.get(form) is not None:
                    for transformation in forms[form]:
                        if transformation not in visited:
                            queue.append([transformation, level+1])
                            visited.add(transformation)
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(transformationSequenceLength(beginWord, endWord, wordList))