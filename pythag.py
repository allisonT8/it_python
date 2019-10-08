from math import sqrt
from banner import banner
banner("PYTHAGOREAN CALCULATOR", "By.Allison.T")
print("We will help you find the missing side of a right triangle. The lengths of the two legs are 'a' and 'b' and lengths of the hypotenuse is 'c'.")

go_again = True
while go_again:
    formula = input('Which side (a, b, c) do you wish to calculate? side: ')
    if formula == 'c':
        side_a = int(input('Input the length of side a: '))
        side_b = int(input('Input the length of side b: '))

        side_c = sqrt(side_a * side_a + side_b * side_b)

        print('The length of side c is: ' )
        print(side_c)

    elif formula == 'a':
        side_b = int(input('Input the length of side b: '))
        side_c = int(input('Input the length of side c: '))

        side_a = sqrt((side_c * side_c) - (side_b * side_b))

        print('The length of side a is' )
        print(side_a)

    elif formula == 'b':
        side_a = int(input('Input the length of side a: '))
        side_c = int(input('Input the length of side c: '))

        side_c = sqrt(side_c * side_c - side_a * side_a)

        print('The length of side b is')
        print(side_c)

    go_again = False
    if input("Would you like to calculate another triangle (Y/N)? ") == "y":
            print("")
            go_again = True


print("Thank you for using the Pythagorean Calculator.")