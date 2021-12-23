from factorial import factorial
from exp_root import root, exponentiation
from logarithm import logarithm






def main():
    while 1:
        print("Menu")
        print("Enter 1 for factorial")
        print("Enter 2 for exp2")
        print("Enter 3 for exp3")
        print("Enter 4 for log")
        print("Enter 5 for ln")
        print("Enter 6 for lg")
        print("Enter 7 for root2")
        print("Enter 8 for root3")
        inp = input()
        if inp == '1':
            print("You choose factorial")
            j = int(input("Enter x"))
            result = factorial.fact(j) 
            print("Factorial of:", j,"is", result)
        elif inp == '2':
            print("You choose exp2")
            j = int(input("Enter x"))
            result = exponentiation.exp2(j) 
            print("exp2 of:", j,"is", result)
        elif inp == '3':
            print("You choose exp3")
            j = int(input("Enter x"))
            result = exponentiation.exp3(j) 
            print("exp3 of:", j,"is", result)
        elif inp == '4':
            print("You choose log")
            j = int(input("Enter a"))
            i = int(input("Enter b"))
            result = logarithm.log(j, i) 
            print("log of:", j, i,"is", result)
        elif inp == '5':
            print("You choose ln")
            j = int(input("Enter a"))
            result = logarithm.ln(j) 
            print("ln of:", j,"is", result)
        elif inp == '6':
            print("You choose lg")
            j = int(input("Enter a"))
            result = logarithm.lg(j) 
            print("Factorial of:", j,"is", result)
        elif inp == '7':
            print("You choose root2")
            j = int(input("Enter x"))
            result = root.root2(j) 
            print("root2 of:", j,"is", result)
        elif inp == '8':
            print("You choose root3")
            j = int(input("Enter x"))
            result = root.root3(j) 
            print("root3 of:", j,"is", result)
        
        print("-----------------------------------")
        answer = input("Якщо бажаєте повторити тестування вкажіть '1'. \nЯкщо бажаєте закінчити роботу програми вкажіть '2':  ")
        if answer =='1':
            print("-----------------------------------")
            continue
        elif answer=='2':
            print("Робота програми закінчена")
            break
        else:
            print('Перевірте введені дані та спробуйте ще раз.')       
        
if __name__ == '__main__':
    main()