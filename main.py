def format_card(name:str,city:str,age:int)-> str:
    """Возвращает информацию о человеке"""
    return f"Имя: {name}\nгород: {city}\nвозраст: {age}"
assert format_card("Joe", "Moscow", 24) == "Имя: Joe\nгород: Moscow\nвозраст: 24"
print(format_card("Joe", "Moscow", 24))






