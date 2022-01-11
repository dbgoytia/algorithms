def shortcut( s:str ) -> str:
    vowels = ['a','e','i','o','u']
    res = ''
    for letter in s:
        if letter not in vowels:
            res += letter
    return res