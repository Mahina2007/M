# #backend + mobile app
# #savol - kegan/kemagan student_id

# def find_absent_students(students: list):
#    absent_student = None
#    for date in students:
        
    
# attendance = [
#     {
#         "date": "10-10-2025",
#         "lesson": "python",
#         "students": [
#             {
#                 "name": "ALi",
#                 "absent": True
#             },
#             {
#                 "name": "Vali",
#                 "absent": False
#             }
#         ]
#     },
#     {
#         "date": "11-10-2025",
#         "lesson": "python",
#         "students": [
#             {
#                 "student_id": "10",
#                 "name": "ALi",
#                 "absent": False
#             },
#             {
#                 "student_id": "11",
#                 "name": "Vali",
#                 "absent": False
#             }
#         ]
#     }
# ]
# # def find_max_goal_team(groups: list) -> dict | None:
# #     """
# #     This function helps to find max goal team and return as a dict
# #     or None if there is no any team
# #     :param groups: list of teams as a dict
# #     :return: team dict or None
# #     """
# #     max_goal_team = None
# #     for group in groups:
# #         if max_goal_team is None:
# #             max_goal_team = group
# #         else:
# #             if group['goals'] > max_goal_team['goals']:
# #                 max_goal_team = group
# #     return max_goal_team


# # teams = [
# #     {
# #         "name": "Real madrid",
# #         "goals": 10
# #     },
# #     {
# #         "name": "Barcelona",
# #         "goals": 1
# #     },
# #     {
# #         "name": "Man city",
# #         "goals": 12
# #     }
# # ]

# # result = find_max_goal_team(groups=teams)
# # print(result)

# def find_top_film(films: list, top_film: str) -> list | None:
    
#     results = list()
#     for film in films:
#         for f in films["film"]:
#               if film["rating"] == rating:
#                   if film["rating"] > film["rating"]:
#                       results.append({
#                           "film" : films["film"],
#                           "rating" : films["rating"]
                          
#                     })
                      
                   
#             # if student["student_id"] == student_id:
#             #     if student["absent"]:
#             #         results.append({
#             #             "name": student["name"],
#             #             "date": date["date"],
#             #             "lesson": date["lesson"]
#                     })

#     return results


# films = [
#     {

#         "film": "home alone 1",
#         "rating": "4.9"
#     },
        
#     {
#         "film": "Kelinlar qo'zg'oloni",
#         "rating": "0.5",
                
#     }
# ]
    

# result = find_top_film(films=students, student_id="11")
# for res in result:
#     print(f"Name: {res['name']} Date: {res['date']} Lesson: {res['lesson']}")


# def find_max_goal_team(groups: list) -> dict | None:
#     """
#     This function helps to find max goal team and return as a dict
#     or None if there is no any team
#     :param groups: list of teams as a dict
#     :return: team dict or None
#     """
#     max_goal_team = None
#     for group in groups:
#         if max_goal_team is None:
#             max_goal_team = group
#         else:
#             if group['goals'] > max_goal_team['goals']:
#                 max_goal_team = group
#     return max_goal_team


# teams = [
#     {
#         "name": "Real madrid",
#         "goals": 10
#     },
#     {
#         "name": "Barcelona",
#         "goals": 1
#     },
#     {
#         "name": "Man city",
#         "goals": 12
#     }
# ]

# result = find_max_goal_team(groups=teams)
# print(result)


# def find_absent_dates(attendance: list, student_id: str) -> list | None:
#     """

#     :param attendance:
#     :param student_id:
#     :return:
#     """
#     results = list()
#     for date in attendance:
#         for student in date["students"]:
#             if student["student_id"] == student_id:
#                 if student["absent"]:
#                     results.append({
#                         "name": student["name"],
#                         "date": date["date"],
#                         "lesson": date["lesson"]
#                     })

#     return results


# students = [
#     {
#         "date": "10-10-2025",
#         "lesson": "python",
#         "students": [
#             {
#                 "student_id": "10",
#                 "name": "ALi",
#                 "absent": True
#             },
#             {
#                 "student_id": "11",
#                 "name": "Vali",
#                 "absent": True
#             }
#         ]
#     },
#     {
#         "date": "11-10-2025",
#         "lesson": "python",
#         "students": [
#             {
#                 "student_id": "10",
#                 "name": "ALi",
#                 "absent": False
#             },
#             {
#                 "student_id": "11",
#                 "name": "Vali",
#                 "absent": True
#             }
#         ]
#     }
# ]
# result = find_absent_dates(attendance=students, student_id="11")
# for res in result:
#     print(f"Name: {res['name']} Date: {res['date']} Lesson: {res['lesson']}")
    
"""
Do'kon mahsulotlari - Eng ko'p sotilgan mahsulotni topish.
"""


def find_best_selling_product(products: list) -> dict | None:
    """

    :param products:
    :return:
    """
    collected_products = dict()
    for product in products:
        if product['name'] in collected_products.keys():
            collected_products[product['name']] += product["quantity"]
        else:
            collected_products[product['name']] = product["quantity"]

    best_product = None
    for name, quantity in collected_products.items():
        if best_product is None:
            best_product = (name, quantity)
        elif quantity > best_product[1]:
            best_product = (name, quantity)
    return best_product


orders = [
    {
        "name": "Olma",
        "quantity": 10
    },
    {
        "name": "Olma",
        "quantity": 12
    },
    {
        "name": "Behi",
        "quantity": 21
    },
    {
        "name": "Nok",
        "quantity": 18
    },
    {
        "name": "Behi",
        "quantity": 18
    },
]


result = find_best_selling_product(products=orders)
print(result)
    
