def safe_div(a: int, b: int) -> int:
    """Проверка чтобы В не был нулем"""
    assert b != 0
    """Деление а на в"""
    return a // b
assert safe_div(2, 2) ==1
assert safe_div(4, 2) ==2
print(safe_div(4, 2))
print(safe_div(4, 3))






