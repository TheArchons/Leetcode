class MyHashMap {
public:
    int hashMap[1000001];
    MyHashMap() {
        for (int i = 0; i < 1000001; i++) {
            hashMap[i] = -1;
        }
    }
    
    void put(int key, int value) {
        hashMap[key] = value;
    }
    
    int get(int key) {
        return hashMap[key];
    }
    
    void remove(int key) {
        hashMap[key] = -1;
    }
};