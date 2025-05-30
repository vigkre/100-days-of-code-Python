"""Program to create separate invites for the list of names using sample letter format.

This is to test "Files" and "Paths".
"""

with open("Input/Names/invited_names.txt") as names:
    names_to_invite: list[str] = [name.strip("\n") for name in names.readlines()]

with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter_content: str = starting_letter.read()

for name in names_to_invite:
    new_letter = letter_content.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_to_{name}.txt", "w") as invite:
        invite.write(new_letter)

