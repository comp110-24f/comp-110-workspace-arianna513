def check_first_letter(word: str, letter: str) -> str:
    """Checks if first letter is a match"""
    if word[0] == letter[0]:
        return "match!"
     else:
        return "no match!"
    