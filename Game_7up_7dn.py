import random

wins = 0
matches = 0

while True:
    print("\nChoose one of the following:")
    print("a. 7 Up")
    print("b. 7")
    print("c. 7 Down")
    
    user_choice = input("Enter your choice (a/b/c): ").strip().lower()
    
    if user_choice not in ['a', 'b', 'c']:
        print("Invalid choice. Please try again.")
        continue
    
    random_number = random.randint(2, 12)
    matches += 1
    
    won = False
    
    if user_choice == 'a' and random_number > 7:
        won = True
    elif user_choice == 'b' and random_number == 7:
        won = True
    elif user_choice == 'c' and random_number < 7:
        won = True
    
    print(f"\nRandom number: {random_number}")
    
    if won:
        print("You WON!")
        wins += 1
    else:
        print("You LOST!")
    
    print(f"Matches played: {matches}, Matches won: {wins}")
    
    continue_choice = input("\nDo you want to Continue playing? (y/n): ").strip().lower()
    if continue_choice == 'n':
        print(f"\nFinal Stats - Total Matches: {matches}, Total Wins: {wins}")
        break