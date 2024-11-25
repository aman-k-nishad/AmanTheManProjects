
def guesser(start_of_range, end_of_range):
    tracker = False
    while tracker == False:
        range_of_num = end_of_range - start_of_range 
        secret_num = start_of_range + range_of_num//2
        guess = input(f"Is your number {secret_num}? (y/n)")
        if guess == y:
            print(f"Success! Secret number is {secret_num}.")
            exit()
        else:
            halver = input(f"Is your number greater than {secret_num}? (y/n)")
            if halver == "y":
                start_of_range = secret_num
            else:
                end_of_range = secret_num

def main():
    print("Think of a number and give a range in which that number lies")
    start = int(input("Start of range:"))
    end = int(input("End of range"))
    guesser(start,end)

main()