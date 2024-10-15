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

# Solution from course
def calculate_love_score(name1: str, name2:str):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e
    
    
    score = int(str(first_digit) + str(second_digit))
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")