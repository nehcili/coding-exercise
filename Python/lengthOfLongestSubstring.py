# Goal: write a function lengthOfLongestSubstring
# that find the length of the longest substring in a string without repetition
# 
# for example:
# lengthOfLongestSubstring('abc') == 3
# lengthOfLongestSubstring('1111111') == 1
# lengthOfLongestSubstring('112123123412345') == 5

# check : list, int, int, char --> int
# returns the index, between start and end,
# where lst[index-1] == c
# however, it returns start if there is no element, i.e. start = end
# or if there is no element in in lst[start:end] that matches c
# assuming lst has no repeated entries and start <= end
def check(lst, start, end, c):
    i = start

    while i < end:
        if lst[i] == c:
            return i + 1
        i += 1
    
    return start
        
# lengthOfLongestSubstring : string --> int
# returns the length of the longest substring in s without repetition
def lengthOfLongestSubstring(s):
    start, end = 0, 1
    
    try:
        c = s[start]
        # the variable maxlen will be returned as a final answer, 
        # now initalized at 1
        maxlen = 1 
    except IndexError:
        return 0
    
    while True:
        try:
            c = s[end]
        except IndexError:
            if end - start > maxlen:
                maxlen = end - start
            return maxlen
        
        # find the index of the element in s[start:end] that matches c
        # if not such element, return start
        new_start = check(s, start, end, c)
        
        # if there is repetition in s[start:end]
        # move start to new_start
        # and modify maxlen to the new, if any, maxlen
        if new_start != start:
            maxlen = end - start if (end - start) > maxlen else maxlen
            start = new_start
        
        end += 1
            
# tests   
# def test_check():
#     print(check("abcdezg", 2, 7, '1'))
#     print(lengthOfLongestSubstring('12345'))
#     print(lengthOfLongestSubstring('11111'))
#     print(lengthOfLongestSubstring('11211'))
#     print(lengthOfLongestSubstring('112123123412345'))