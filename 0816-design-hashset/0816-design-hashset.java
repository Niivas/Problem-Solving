class MyHashSet {
    Boolean bool[];
    public MyHashSet() {
        bool = new Boolean[1000001];
    }
    
    public void add(int key) {
        bool[key] = true;
    }
    
    public void remove(int key) {
        bool[key] = false;
    }
    
    public boolean contains(int key) {
        if(bool[key] == null || !bool[key]) return false;
        return true;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */