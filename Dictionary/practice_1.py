# derek_dictionary = {"f_name" : "Derek" , "l_name" : "Banas" , "address" : "123 church street"}
#
# print("Tutor name is {}".format(derek_dictionary["f_name"]))
#
# # for k,v in derek_dictionary.items():
# #     print(type(derek_dictionary))
# #     print(type(derek_dictionary.items()))
# #     print(k,v)
#
#
# for i in derek_dictionary:
#     print(derek_dictionary)


# list_of_customer = []
# while True:
#     response = str(input("Enter Customer (Yes/No)")).lower().rstrip()
#     if response == "yes":
#         first_name, last_name = str(input("Enter Customer Name")).split()
#         list_of_customer.append({"f_name" : first_name , "l_name" : last_name})
#         continue
#     else:
#         break
# for i in list_of_customer:
#     print(i['f_name'] , i['l_name'])

list_of_customer = []
while True:
    response = str(input("Enter Customer (Yes/No)")).lower().rstrip()
    if response == "yes":
        first_name, last_name = str(input("Enter Customer Name")).split()
        list_of_customer.append({"f_name" : first_name , "l_name" : last_name})
        continue
    else:
        break
for i in list_of_customer:
    print(i['f_name'] , i['l_name'])