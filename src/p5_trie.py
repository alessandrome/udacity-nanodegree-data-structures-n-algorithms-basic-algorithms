#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[10]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self, char='', is_word=False):
        ## Initialize this node in the Trie
        self.char = char
        self.is_word = is_word
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self._insert_helper(char)
    
    def _insert_helper(self, value):
        if len(value) == 0:
            return
        char = value[0]
        child = None
        if char in self.children:
            child = self.children[char]
        if child:
            return child._insert_helper(value[1:])
        self.children[char] = TrieNode(char)
        
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        self.root.insert(word)

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        string = ''
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node
        


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[87]:


class TrieNode:
    def __init__(self, char='', is_word=False):
        ## Initialize this node in the Trie
        self.char = char
        self.is_word = is_word
        self.children = {}
    
    def insert(self, word):
        ## Add a child node in this Trie
        self._insert_helper(word)
    
    def _insert_helper(self, value):
        if len(value) == 0:
            return
        char = value[0]
        child = None
        if char in self.children:
            child = self.children[char]
        if child:
            return child._insert_helper(value[1:])
        child = TrieNode(char)
        self.children[char] = child
        if len(value) == 1:
            child.is_word = True
        child._insert_helper(value[1:])
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        return_list = []
        for el in list(self.children.values()):
            el._suffixes_helper(return_list, '', el.is_word)
        return return_list
    
    def _suffixes_helper(self, return_list, suffix, is_word):
        suffix += self.char
        list_nodes = list(self.children.values())
        if is_word:
            return_list.append(suffix)
        for el in list_nodes:
            el._suffixes_helper(return_list, suffix, el.is_word)
        return return_list


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[88]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[89]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        #print(prefixNode.suffixes() if prefixNode else None)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:




