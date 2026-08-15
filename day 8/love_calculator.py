def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    true_array = ['t', 'r', 'u', 'e']
    love_array = ['l', 'o', 'v', 'e']
    true_score = 0
    love_score = 0

    for letter in true_array:
        true_score += name1.count(letter) + name2.count(letter)

    for letter in love_array:
        love_score += name1.count(letter) + name2.count(letter)

    score = int(str(true_score) + str(love_score))
    print(score)

if __name__ == "__main__":
    calculate_love_score("Kanye West", "Kim Kardashian")