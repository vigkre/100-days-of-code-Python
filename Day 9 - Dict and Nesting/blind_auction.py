from art import logo

print(logo)

bidders = {"name": [], "price": []}


# TODO-1: Ask the user for input
def collect_bidders():
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))

    # TODO-2: Save data into dictionary {name: price}
    bidders["name"].append(bidder_name)
    bidders["price"].append(bid_amount)

    # TODO-3: Whether if new bids need to be added
    other_bidders = input("Are there any other bidders? Type 'yes or 'no'. \n").lower()
    if other_bidders == "yes":
        print("\n" * 20)
        collect_bidders()
    elif other_bidders == "no":
        compare_bids()
    else:
        print("You provided wrong input. Try again!")


# TODO-4: Compare bids in dictionary
def compare_bids():
    highest_bid = 0
    winner = ""
    for index, price in enumerate(bidders["price"]):
        if price > highest_bid:
            highest_bid = price
            winner = bidders["name"]
    print(
        f"""The winner is {winner} with a bid of ${highest_bid}"""
    )


collect_bidders()


# Solution from the course

# from art import logo
# print(logo)


# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")


# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#     if should_continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         print("\n" * 20)

