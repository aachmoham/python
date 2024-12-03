inp = input(
    "\nGive a password:"
    "\n- Minimum 8 characters."
    "\n- A capital letter, A lower letter, number and a speciaal character.\n> "
)
special_chars = "@#$%^&*()_+-=!"
has_upper = False
has_lower = False 
has_digit = False
has_special = False

for i in range(len(inp)):
    if inp[i].isupper(): 
        has_upper = True
    if inp[i].islower(): 
        has_lower = True
    if inp[i].isdigit(): 
        has_digit = True
    if inp[i] in special_chars: 
        has_special = True

if len(inp) < 8:
    print("Password is short")
if not has_upper or not has_lower or not has_digit or not has_special:
    print("Password misses the requirements")
else:
    print("That's a strong password!")
