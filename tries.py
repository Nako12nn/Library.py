#simple number 
def is_smpl_num(n):
    if n == 0 or n < 0:
        print("Can't divide by Zero")
    elif n % n == 0 and n % 2 !=0 and n % 5 != 0 and n % 3 !=0:
        return f"Number {n} is simple"
    else:
        return f"Number {n} is not simple"
 



print(is_smpl_num(9))
