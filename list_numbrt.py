# num = [1,2,3,4,5,6,7,8,9,10]
# for item in num:
#     print(item)
#
#
# i = 0
# while i < len(num):
#     print(num[i])
#     i =i+1

lucky_number =[42,8,15,16,23,42]
friend = ["Kevin","Karen","Jim","Jim","Oscar"]
friend.append("Creed") #add creed to list#
friend.extend(lucky_number) #add lucky list to friend#
friend.insert(1,"Harry")
friend.remove("Oscar")
friend.pop()
lucky_number.sort()
print(lucky_number)
print(friend)
print(friend.index("Kevin"))
print(friend.count("Jim"))
