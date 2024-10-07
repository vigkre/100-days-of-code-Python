def calculate_love_score(name1, name2):
    true_count = 0
    love_count = 0
    name3 = name1 + name2
    
    for letter in name3.upper():
       if letter == "T" or letter == "R" or letter == "U" or letter == "E":
           true_count += 1
       if letter == "L" or letter == "O" or letter == "V" or letter == "E":
           love_count += 1

    print(f"{true_count}{love_count}")

calculate_love_score("Virat", "Anushka")