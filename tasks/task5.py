# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    numbers = input("Введите числа: ") 
    numbers_list = list(map(int, numbers.split())) 
    squares = [x**2 for x in numbers_list]
    print("Результат:", ' '.join(map(str, squares)))

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()