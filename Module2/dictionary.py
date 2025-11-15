contact_info = {
    "Alice": "432-543",
    "Bob": "769 650"
}

alice_phone = contact_info["Alice"]
print(alice_phone)

contact_info["Alice"] = "123-456"
print(contact_info)

contact_info["Eva"] = "956 777"
print(contact_info)

del contact_info["Bob"]
print(contact_info)

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)

contact_information = {

    "Alice" : {
        "phone_number" : "123-444",
        "email": "alice@gmail.com",
        "birthday" : "20/11/2000"
    },

"Bob" : {
        "phone_number" : "543-477",
        "email": "bob@gmail.com",
        "birthday" : "10/07/2000"
    }
}

print(contact_information)
print(contact_information["Bob"])

