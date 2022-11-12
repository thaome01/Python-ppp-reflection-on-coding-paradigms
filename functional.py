def flatten_and_sort(array):
    arr=[]
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)



# How does this solution ensure data immutability?
# Is this solution a pure function? Why or why not?
# Yes this is a pure function because it only writes properties of locals if they do not alias non-locals.
# Is this solution a higher order function? Why or why not?
# Yes this is a higher order function because i am describing the result you want rather than explicity the steps required to get there.
# Would it have been easier to solve this problem using a different programming style?
# Yes
# Why in particular is functional programming a helpful paradigm when solving this problem?
# Less line of code and it breaks into smaller code.