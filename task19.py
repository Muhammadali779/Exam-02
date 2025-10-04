def find_longest_name(names: list) -> str:
    longest_name = ""
    
    for name in names:
        if len(name) > len(longest_name):
            longest_name = name
            
    return longest_name

print(find_longest_name(['Ali', 'Diyor', 'Jasurbek', 'Muhammad']))
