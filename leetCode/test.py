def top_color(image):
    flat = sorted([x for p in image for x in p ])
    





image = [['red','red','blue'],['blue','blue','white'],['white','white','red', 'red']]
print top_color(image)





# def top_color(image):
#     d = {}
#     for i in range(len(image)):
#         for j in range(len(image[0])):
#             if image[i][j] in d.keys():
#                 d[image[i][j]] += 1
#             else:
#                 d[image[i][j]] = 1
#
#     res = []
#     for key,value in d.items():
#         res.append([key,value])
#     res = sorted(res, key=lambda x: x[1])
#     x = set()
#     for i in range(len(res)-2,-1,-1):
#         if res[i][1] == res[i+1][1]:
#             x.add(res[i+1][0])
#             x.add(res[i][0])
#         else:
#             x.add(res[i+1][0])
#             break
#     return x
