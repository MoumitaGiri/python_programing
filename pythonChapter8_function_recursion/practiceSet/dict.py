# data = { "emp1":
#         {
#             "name" : "moumita",
#             "id"   : "girim",
#             "dept" : "QA",
#             "task" : ['a','b','c']
#         },
#         "emp2":
#         {
#             "name" : "raja",
#             "id"   : "girim",
#             "dept" : "DEV",
#             "task" : ['a','b','c', 'd']
#         }
#     }

# print(data["emp2"]["task"])
# print(data["emp1"]["task"])

data1 = [
        {
            "name" : "moumita",
            "id"   : "girim",
            "dept" : "QA",
            "task" : ['1','b','c']
        },
        {
            "name" : "raja",
            "id"   : "girim",
            "dept" : "DEV",
            "task" : ['19','45','27', '30']
        }
    ]

print(data1[0]["task"])
print(data1[1]["task"])
count = 0
y = data1[0]["task"]
for i in y:
    print(i)
    if(int(i) > 0):
        count += 1
    print(count)

    # count = count + 1