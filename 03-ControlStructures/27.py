my_list = []

fb_account = input("Does this person have a facebook account? y/n ")
t_account = input("Does this person have a twitter account? y/n ")
ig_account = input("Does this person have an instagram account? y/n ")

if fb_account == "y":
    my_list.append (fb_account)
    facebook = True
else:
    facebook = False

if t_account == "y":
    my_list.append(t_account)
    twitter = True
else:
    twitter = False

if ig_account == "y":
    my_list.append(ig_account)
    instagram = True
else:
    instagram = False

x = len(my_list)

if x >= 2:
    print(f"Facebook: {facebook}")
    print(f"Twitter: {twitter}")
    print(f"Instagram: {instagram}")
    print("This person can be a good influencer!!")