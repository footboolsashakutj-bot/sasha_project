def count_char(text: str, simbol: str) -> int:
    """Сколько данного символа в тексте"""
    count = 0
    for char in text:
        if char == simbol:
            count += 1
    return count
assert count_char("banana","a")==3
print(count_char("banana","a"))
print(count_char("banana","b"))







