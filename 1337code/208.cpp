#include<string.h>
#include<unordered_map>

class Trie {
public:

    Trie() {
        
    }
    
    void insert(string word) {
        
    }
    
    bool search(string word) {
        
    }
    
    bool startsWith(string prefix) {
        
    }

    class Node {
    public:
        int val;
        unordered_map<char, Node> children;

        Node(int val, unordered_map<char) {
            
        }
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */