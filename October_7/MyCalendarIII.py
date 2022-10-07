import bisect

class MyCalendarThree:

    def __init__(self):
        
        # [1] two lists for start and end points 
        #     that will be maintained sorted
        self.ss = []
        self.ee = []
        
        self.k_max = 0

    def book(self, s: int, e: int) -> int:
       
        # [2] insert start and end points into corresponding 
        #     lists while maintaining sort order
        bisect.insort_left(self.ss, s)
        bisect.insort_left(self.ee, e)
        
        # [3] calculate the number 'k_cur' of intervals 
        #     that remain open at point 's'
        opened = bisect.bisect_right(self.ss, s)
        closed = bisect.bisect_right(self.ee, s)
        k_cur = opened - closed
        self.k_max = max(self.k_max, k_cur)

        # [4] two-pointer iteration over start and end points 
        #     to update the number of intervals 'k_cur' that  
        #     remain open at each iteration
        while True:
            
            # [5] no need to continue if:
            #     - either all starting points were accounted for
            #     - or next starting point lies to the righe of 'e'
            if opened >= len(self.ss): break
            if self.ss[opened] >= e  : break
            
            if self.ss[opened] < self.ee[closed]:
                opened += 1
            else:
                closed += 1
            
            k_cur = opened - closed        
            self.k_max = max(self.k_max, k_cur)

        return self.k_max