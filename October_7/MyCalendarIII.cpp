class MyCalendarThree {
public:
    map<int,int> mp;  //
    MyCalendarThree() {
        
    }
    
    int book(int start, int end) {
        int temp = 0;
        int result = 0;
        // for event start => increase the value by 1 of key in map.
        mp[start]++;
        // for event end => decrease the value by 1 of key in map.         
        mp[end]--;           
        
        for(auto m : mp){
            temp += m.second;
            // record  the maximum overlapping intervals               
            result = max(result, temp);
        }
        return result;
    }
};