def longest_cont_sublist(vals):
    # Type checking function input
    if type(vals) != list:
        print('Type Error')
        return
    
    vals.sort()

    n = 0
    m = 1
    lengths = []

    while n < len(vals) - 1:
        # resets the max value
        max_value = 1
        # loops the remainder of the list
        for i, num in enumerate(vals[m:]):
            if num == vals[n+i] + 1:
                # increases the max value if the next value is continuous
                max_value += 1
                lengths.append(max_value)  # appends the max_val
                # it doesn't matter that different values are here because only the max of all values counts
            else:
                # breaks out of the loops and resets it with new n values
                print('Loop needs to restart with...')
                print(f'{vals[n+i+1]} as the value and ')
                print(f'{vals[n+i+2:]} as the list')
                n = n + i
                break

        n += 1
        m = n+1

    print(lengths)
    return max(lengths)

print(longest_cont_sublist([1,2,3,5,6,7,8,11,13,17,18,19]))