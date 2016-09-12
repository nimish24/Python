__author__ = 'Nimish'

def pair_sum(arr,k):

    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = k-num

        if target not in seen:
            seen.add(num)

        else:
            output.add( ( min(num,target), max(num,target)  ) )
    print len(output)
    # "map()" takes a function and sequence as arguments and applies function to all elements of the sequence and returns a list
    print '\n'.join(map(str,list(output)))

pair_sum([1,2,3,5,7,9,6,4],6)