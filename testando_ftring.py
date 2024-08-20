

age = "23"
age2 = ""

car1 = (f", Caracteristica 1: {age}\n    " if age else "")
car2 = (f", Caracteristica 2: {age2}\n    " if age2 else "")
car3 = (f", Caracteristica 3: {age}\n    " if age else "")
car4 = (f", Caracteristica 4: {age}\n" if age else "")

teste = f"""
    {car1}{car2}{car3}{car4}
"""

print(teste)