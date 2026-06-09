def calc_volume(length=float, width=float, height=float):

    length = input("Enter the length: ")

    width = input("Enter the width: ")

    height = input("Enter the heigth: ")

    calc_volume =(int(length) * int(width) * int(height))

    print("The volume of the rectangular prism is ",  int(calc_volume))

    

calc_volume()