import random

def get_answer(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return "Number"

def play():
    backend = 0
    score=0
    prev_no=0
    while True:
        no=random.randint(1, 101)
        backend =prev_no+ no
        print("Number on screen:", no)
        guess = input("Your guess (fizz/buzz/fizzbuzz/Number): ").strip()
        correct = get_answer(backend)
        score += 1
        if guess.lower() == correct.lower():
            print("Correct!")
            prev_no = no
        else:
            print("Wrong! Answer was:", correct)
            print("Hidden number was:", backend)
            cont = input("Do you want to continue? (yes/no): ").strip().lower()
            if cont != "yes":
                print("Your final score is:", score)
                score = 0
                backend = 0
                prev_no = 0
                break
    print("Your final score is:", score)
play()