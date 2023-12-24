from art import logo

print(logo)

bid_list = []
bid_dict = {}

name = input("enter your name \n")
amount = int(input("enter your bid amount \n"))

bid_dict["name"] = name
bid_dict["amount"] = amount

while True:
    again = input("Is there other bidder enter 'Y' fro YES and 'N' for NO \n").lower()
    if again == 'n':
        max_bid = 0
        max_bidder = ''
        for bid in bid_list:
            if max_bid < bid["amount"]:
                max_bid = bid["amount"]
                max_bidder = bid["name"]
        print(f"Bid won by {max_bidder} with bidding amount {max_bid}")
        break
    else:
        new_name = input("enter your name \n")
        new_amount = int(input("enter your bid amount \n"))
        new_dic = {"name": new_name, "amount": new_amount}
        bid_list.append(new_dic)
