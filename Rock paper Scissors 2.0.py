import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r','p', 's'])
    print(f"Computer selected: {computer}")
    if (user == computer):
        return 'Tie'

# r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost...'

def is_win(user, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (user == 'r' and opponent == 's') or (user == 's' and opponent == 'p') \
      or (user == 'p' and opponent == 'r'):
       return True

print (play())
