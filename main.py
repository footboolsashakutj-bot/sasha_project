def repeat_text(text,times):
    """повторяет текст times раз"""
    if times >= 0:
        return text * times
assert repeat_text("hello", 2) == "hellohello"
print(repeat_text("hello", 2))
print(repeat_text("lol", 3))







