class MyCalendarThree {
    
    TreeMap<Integer,Integer> tm;
    int maxi = 0;

    public MyCalendarThree() {
        tm = new TreeMap<>();
    }
    
    public int book(int start, int end) {
        //add by 1 from the map -> for start
        tm.put(start,tm.getOrDefault(start,0)+1);
        
        //remove by 1 from the map -> end
        tm.put(end,tm.getOrDefault(end,0)-1);
        
        int cnt = 0;
        // iterate the cnt
        for (int val:tm.values()){
            cnt += val;
            // max element till now
            maxi = Math.max(cnt,maxi);
        }
        
        
        return maxi;
    }
}