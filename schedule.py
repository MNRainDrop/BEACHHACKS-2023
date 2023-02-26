# #user inputs time they want to sleep
# #output: time spent awake
# def sleepNeeded():
#     sleepInput = int(input("Please enter amount of sleep, you would need."))
#     sleep = 24 - sleepInput
#     return sleep

#view task
#output: String of all values
def selectTask():
    temp = addTask()
    for val in temp:
        print(val, temp[val])


#add tasks to the schedule
#tasks are categorized into classes, homework/projects, hobbies
#output: returns dictionary of all values
def addTask():
    category = str(input("Please input the category it would go under. "))
    print("Task are categorized into class, homework, hobby, chore, work.")
    while (category != "class") and (category != "homework") and (category != "hobby") and (category != "chore") and (category != "work"):
        print("Invalid Input, please enter again one of these categories: class, homework, hobby, chore, work")
        category = str(input("Please input the category it would go under. "))
    if category == "class" or category == "chore" or category == "hobby" or category == "work" :
        return getValue(category)
    elif category == "homework":
        return getValue(category)
        

#auxiliary function
def getValue(category):
    userTask = str(input("Please enter your task name. "))
    day = str(input("Please enter the day when your class will take place. "))
    startTime = int(input("Please enter the start time of your class. "))
    endTime = int(input("Please enter the end time of your class. "))
    date = str(input("Please enter a date for when you will start the task. "))
    taskDict = {"Task": userTask, "Category": category, "Day": day, "startTime": startTime, "endTime": endTime, "Date": date}
    return taskDict

        
# # #user enters true false to be able to delete tasks
# # def deleteTask():
#     # print("would you like to delete task? Y/N")
#     # input= str(input(""))
#     # if input == 'N':
#     #     exit
#     #elif input == 'Y':



# # #edit tasks to be more versatile with time
# # #def editTask():


# bedTime = {}
# #output: holds the value
# def scheduleTask():
#     temp = addTask()
#     for val in temp:

#selectTask()
