def decodeMorse(morse_code):
    decrypted_message = ""
    encrypted_words = morse_code.split('   ') # Sepparate by words
    for i in range (0, len(encrypted_words)):
        encrypted_letters = encrypted_words[i].split(' ') # Sepparate by character
        started = False # Only add space after we started writing something
        for letter in encrypted_letters:
            if letter != '': 
                started = True
                decrypted_message += MORSE_CODE[letter]

        if i + 1 < len(encrypted_words) and started:
            decrypted_message += ' ' # Append a space at the end of each word
    return decrypted_message

MORSE_CODE = dict # This was already given in code kata.