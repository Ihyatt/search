import time

class Search(object):
    """Initializes searches"""

    def less_than(self,items, key):
        """
        Finds the largest item which is less than the key.
        It returns FoundLess if a match is found, NotFound
        if no match is found 
        """
        lesser = None
        index = None

        for i in range(0, len(items)):
            
            if items[i] < key and lesser is None:
                lesser = items[i]
                index = i 
            elif items[i] > lesser and items[i] < key:
                lesser = items[i]
                index = i 

        if lesser == None:
            return 'NotFound'

        return 'FoundLess', str(index)
        #returns a tuple


    def less_than_equals(self, items, key):
        """
        Finds the item which is equal to the key, or the
        largest item which is less than the key. Returns
        FoundExact if an item that exactly matches the key
        is found, FoundLess if a non-exact match is found
        and NotFound if no match is found.
        """

        if key in items:
            return self.equals(items, key)

        return self.less_than(items, key)


    def equals(self, items,key):
        """
        Finds an item which is equal to the key. Returns
        FoundExact if an item if found, NotFound otherwise.
        """

        for i in range(0, len(items)):
            if items[i] == key:
                return 'FoundExact', str(i)
                #returns a tuple

        return 'NotFound'


    def greater_than_equals(self, items,key):
        """
        Finds the item which is equal to the key, or the
        smallest item which is greater than the key. Returns
        FoundExact if an item that exactly matches the key
        is found, FoundGreater if a non-exact match is found
        and NotFound if no match is found.
        """
        if key in items:
            return self.equals(items, key)

        return self.greater_than(items,key)



    def greater_than(self, items,key):
        """
        Finds the smallest item which is greater than the
        key. Returns FoundGreater if a match if found, NotFound
        if no match is found.
        
        """

        greater = None
        index = None

        for i in range(0, len(items)):
            if items[i] > key and greater is None:
                greater = items[i]
                index = i
            elif items[i] < greater and items[i] > key:
                greater = items[i]
                index = i 

        if greater == None:
            return 'NotFound'

        return 'FoundGreater', str(index)
        #returns a tuple



def test_time(items,key,func):
    """
    Method to test the time it takes for a given funtion to run
    """
    test = Search() #initialize instance of Search()
    start_time = None
  
    #conditional statments will check which function to run
    if func == 'less_than':
        start_time = time.time() #Start the clock! ie begin counting seconds
        print test.less_than(items, key)#display output of function

    elif func == 'less_than_equals':
        start_time = time.time() 
        print test.less_than_equals(items, key)

    elif func == 'equals':
        start_time = time.time()
        print test.equals(items, key)

    elif func == 'greater_than_equals':
        start_time = time.time() 
        print test.greater_than_equals(items,key)

    elif func == 'greater_than':
        start_time = time.time() 
        print test.greater_than(items,key)

    print("--- %s seconds ---" % (time.time() - start_time)) #prints length of time a function takes to run in terms of seconds

 


#####################################################################
if __name__ == "__main__":  

    """Only run one function at a time"""
       
    test_time([0, 2, 4, 6, 8], 0,'less_than')
    # test_time([0, 2, 4, 6, 8], -1,'less_than_equals')
    # test_time([0, 2, 4, 6, 8], 1,'equals')
    # test_time([0, 2, 4, 6, 8], 2,'greater_than_equals')
    # test_time([0, 2, 4, 6, 8], 2,'greater_than')









