dictionary_bids= {
    "Jannet": 123, 
    "Daniel": 321,
    "John": 456,
}

print("Welcome to the secret auction program.")
print("Here are the current bids: ")
for name, bid in dictionary_bids.items():
    print(f"{name}: ${bid}")

