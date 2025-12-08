def odd_even(start ,end):

    for num in range(start, end):
        if num%2==0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")
odd_even(100,200)

