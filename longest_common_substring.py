def lcs_problem(str1, str2):
    str1_list = list(str1)
    str2_list = list(str2)
    common_chars = []

    for i, char1 in enumerate(str1_list):                                  # first loop through letters in first string
        print(f'i = {i}')
        for j, char2 in enumerate(str2_list):                              # second loop through letters in (remaining) second string
            print(f'Char1 = {char1} & Char2 = {char2}')
            if char2 == char1:                                             # tests if a matched letter has been found
                common_chars.append(char1)                                 # Appends the letter to the end of the list
                str2_list = str2_list[j+1:]                                # changes the second string list to make it only search through 
                break                                                      # the letters after the match has been found
                
        print(common_chars)
                    
    return len(common_chars)


print(lcs_problem('brigfdf','brian'))