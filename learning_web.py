has_account = True
email_verified = False

can_login = has_account and email_verified

email_id = "g@example.com"
is_email_valid = '@' in email_id

user_age = 17
is_age_valid = user_age >= 18 

can_login_final = has_account and email_verified and is_email_valid and is_age_valid

print("Initial Login:", can_login)
print("Is Email Valid:", is_email_valid)
print("Is Age Valid:", is_age_valid)
print("Final Login:", can_login_final)

identity_check = has_account is True
print("Identity Check (has_account is True):",identity_check)
