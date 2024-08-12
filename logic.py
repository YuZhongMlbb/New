from random import choice

variant = {
    1 : "камень",
    2 : "ножницы",
    3 : "бумага"
}


def varian_game(user_choice : int):
    computer_choice = choice(list(variant))
    if user_choice == computer_choice:
        return f"ничья, бот выбрал {variant[computer_choice]}"  
    elif user_choice == 1 and computer_choice ==2 or user_choice == 2 and computer_choice == 3 or user_choice == 3 and computer_choice == 1:
        return f"вы выиграли компьютер выбрал {variant[computer_choice]}"
    elif user_choice == 1 and computer_choice == 3 or user_choice == 2 and computer_choice == 1 or user_choice == 3 and computer_choice == 2:
        return f"вы проиграли компьютер выбрал {variant[computer_choice]}"
    else:
        return "введите корректные данные"