# 100 days of python 
# Blind auction program

import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)



other_bidders = "yes"
blind_bids = {}
name = input("Hi please input you name: ")
bid = int(input("Please input your bid: "))
blind_bids[name] = bid


while other_bidders == "yes":

    other_bidders = input("If there are any other bidder type 'yes' or 'no'").lower()
    if other_bidders == "yes":
        os.system('clear')
        name = input("Hi please input you name: ")
        bid = int(input("Please input your bid: "))
        blind_bids[name] = bid
max_bid = 0

for key in blind_bids:
    if blind_bids[key] > max_bid:
        max_bid = blind_bids[key]
        winner = key
    

print(f"The winner is: {winner}!")
print(f"They bid: {max_bid}")