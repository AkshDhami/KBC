# print("Where are you from?")

# list = ["surat", "rajkot", "ahemdabad", "baroda"]
# for i in list:
#     print(i)

# city = input("Enter Your ans: ")

# if "surat" in city:
#     print("you are win to 100000")

#     print("next question")

#     print("what is the largest state in india?")
#     list2 = ["gujrat", "panjab", "MH", "MP"]
#     for j in list2:
#         print(j)

#     state = input("Enter your ans: ")
#     if "MH" in state:
#         print("you are win to 200000")
#     else:   
#         print("incorrect ans")
#         print("end game")

# else:   
#     print("incorrect ans")
#     print("end game")

Questions = [
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],

    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ],
    [
        "Which state is big in india?", "Gujrat", "Rajsthan", "MH", "MP", 3
    ]
    ]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
i = 0
for i in range(0, len(Questions)):
    Question = Questions[i]
    
    print(f"Question for Rs. {levels[i]}")
    print(Question[0])
    print(f"A. {Question[1]}      B. {Question[2]}")
    print(f"C. {Question[3]}          D. {Question[4]}")
    reply = int(input("Enter your answer: "))
    if(reply == Question[-1]):
        print(f"Correct answer, you have won RS.{levels[i]}")
        if(i==4):
            money = 10000
        elif(i==9):
            money = 320000
        elif(i==14):
            money = 10000000
    else:
        print("Your answer is wrong!")
        break

print(f"Your take money is {money}")