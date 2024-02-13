import random
import time

total_count = 1
total_error = 1
correct = 1
each_dic = {}

for i in range(10):
    each_dic[str(i)] = 0

while (True):
    select = input("1 : start \n2 : show\n3 : stop")
    if select == "1":
        classnumber = ""
        for i in range(4):
            classnumber += str(random.randint(0, 9))

        print(classnumber)
        start = time.time()

        user_answer = input()
        totaltime = time.time() - start  # 현재시각-시작시간 = 실행시간
        print("걸린시간 : %.2f" % totaltime)

        temp_error = True
        for i in range(4):
            if(classnumber[i] != user_answer[0]):
                each_dic[classnumber[i]] += 1
                temp_error = False

        if temp_error == True:
            correct =+ 1

        accuracy = (correct % total_count)*100

        print("정확도 : %.2f" %accuracy)
        total_count += 1


    elif (select == "2"):
        print(each_dic)

    elif (select == "3"):
        break
    else:
        pass