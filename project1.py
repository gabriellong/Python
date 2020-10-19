# import json
# from pprint import pprint
# data = '''
# {
#   "car_data": {
#     "owner_1": {
#       "Name": "Alyx",
#       "Brand": "Ford",
#       "Model": "Mustang"
#     },
#     "owner_2": {
#       "Name": "Gordon",
#       "Brand": "BMW",
#       "Model": "M4"
#     },
#     "owner_3": {
#       "Name": "Kleiner",
#       "Brand": "Ford",
#       "Model": "Mustang"
#     }
#   }
# }
# '''
# 
# json_car_data = json.loads(data)
# 
# carbrand_list = ['Ford','BMW']
# cars_dict = dict.fromkeys(carbrand_list, [])
# 
# for key in cars_dict: 
#     for owner in json_car_data['car_data']:
#         Name = json_car_data['car_data'][owner]['Name']
#         Brand = json_car_data['car_data'][owner]['Brand']
#         if Brand == key:
#             print(f'{Name} owns a {key}')
#             cars_dict[key].append(Name)
#         else:
#             print(f'{Name} does not own a {key}')
#             
# 
# pprint(cars_dict)
# 
# for owner in json_car_data['car_data']:
#     Name = print(json_car_data['car_data'][owner]['Name'])
#     Brand = print(json_car_data['car_data'][owner]['Brand'])
#     print(json_car_data['car_data'][owner]['Name'] + json_car_data['car_data'][owner]['Brand'])
# 
# for owner in json_car_data['car_data']:
#     print(json_car_data['car_data'][owner]['Name'])
# 
# pprint(cars_dict)
# 
# # for owner in dict_1.keys() & dict_2.keys():
# #     dict_2[k] = dict_1[k]
# # 
# # print(dict_2)
# # 
# 
# pprint(json_car_data)
# 
# for k,v in cars_dict.items():
#      cars_dict[k] = json_car_data.get(k,v)
# 
# pprint(cars_dict)
# 
# 









import json
from pprint import pprint
data = '''
{
  "car_data": {
    "owner_1": {
      "Name": "Alyx",
      "Brand": "Ford",
      "Model": "Mustang"
    },
    "owner_2": {
      "Name": "Gordon",
      "Brand": "BMW",
      "Model": "M4"
    },
    "owner_3": {
      "Name": "Kleiner",
      "Brand": "Ford",
      "Model": "Mustang"
    }
  }
}
'''

json_car_data = json.loads(data)
pprint(type(json_car_data))
carbrand_list = ["Ford","BMW"]
cars_dict = dict.fromkeys(carbrand_list, [])
# # pprint(cars_dict)
# 
# # Print the type of data variable
# print("Type:", type(json_car_data)) 
#   
# # Print the data of dictionary 
# print("\nowner_1:", json_car_data['car_data']['owner_1']) 
# print("\nowner_2:", json_car_data['car_data']['owner_2'])
# print("\nowner_3:", json_car_data['car_data']['owner_3'])
# 
# pprint(type(json_car_data))

cars_dict.update(json_car_data)
 
 
pprint(json_car_data)
 
for key in cars_dict: 
       or owner in json_car_data['car_data']:
           Name = json_car_data['car_data'][owner]['Name']
         Brand = json_car_data['car_data'][owner]['Brand']
         if Brand == key:
               print(f'{Name} owns a {Brand}')
             cars_dict[key].append(Name)



         else:
               print(f'{Name} does not own a {key}')

             continue



 pprint(cars_dict)
 # cars_dict.update(json_car_data)
 pprint(cars_dict)

# for key in cars_dict: 
#     for owner in json_car_data['car_data']:
#         Name = json_car_data['car_data'][owner]['Name']
#         Brand = json_car_data['car_data'][owner]['Brand']
#         if Brand == key:
#           print(f'{Name} owns a {Brand}')
#         else:
#           print(f'{Name} does not own a {Brand}')
#           
# 
# 
# for k,v in json_car_data.items():
#     cars_dict[k] = json_car_data.get(k,v)
#  
# pprint(cars_dict)
# 
# pprint(json_car_data)
# 
# 
# 
# result = []
# for items in json_car_data:
#     my_dict={}
#     my_dict['Name']=item.get('Name').
#     my_dict['Brand']=item.get('Brand')
#     print my_dict
#     result.append(my_dict)
# 
# pprint(json_car_data["car_data"]["owner_1"])
# 
# 
# 
# 
# pprint(json_car_data["car_data"]["owner_1"]["Brand"]["Name"])
# 
# 
# # data='''
# # {
# #    "store":{
# #       "book":[
# #          {
# #             "category":"reference",
# #             "author":"Nigel Rees",
# #             "title":"Sayings of the Century",
# #             "price":8.95
# #          },
# #          {
# #             "category":"fiction",
# #             "author":"Evelyn Waugh",
# #             "title":"Sword of Honour",
# #             "price":12.99
# #          }
# #       ],
# #       "bicycle":{
# #          "color":"red",
# #          "price":19.95
# #       }
# #    },
# #    "expensive":10
# }
# '''
# data1 = json.loads(data)
# 
# 
# 
# 
# 
# 
# print(data1['store']['bicycle']['price'])# 


