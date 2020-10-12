email = input("What is your email addr? ").strip()
user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
print("My username is {u} and domain name is {d}. Also, "
      "my email addr is {e}".format(u=user_name,d=domain_name,
                                    e=email))
