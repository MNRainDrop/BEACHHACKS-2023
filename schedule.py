#user inputs time they want to sleep
def sleepNeeded():
    sleepInput = int(input("Please enter amount of sleep, you would need."))
    sleep = 24 - sleepInput
    return sleep

#def sleepNeeded(input: int):
    #pause

#view task
#def selectTask():
    #print("due date:", due, "start time", start, "end time", end, "category")


#add tasks to the schedule
#tasks are categorized into classes, homework/projects, hobbies
#param: due date: str, start time, end time, category:
#output: 
def addTask():
    userTask = str(input("Please enter your task name. "))
    print("Task are categorized into class, homework, hobby, chore, work.")
    category = str(input("Please input the category it would go under. "))
    while (category != "class") or (category != "homework") or (category != "hobby") or (category != "chore") or (category != "work"):
        print("Invalid Input, please enter again one of these categories: class, homework, hobby, chore, work")
        category = str(input("Please input the category it would go under. "))
        if category == "class" or category == "chore" or category == "hobby" or category == "work" :
            day = str(input("Please enter the day when your class will take place. "))
            startTime = int(input("Please enter the start time of your class. "))
            endTime = int(input("Please enter the end time of your class. "))
            date = str(input("Please enter a date for when you will start the task. "))
            taskDict = {"Task": userTask, "Category": category, "Day": day, "startTime": startTime, "endTime": endTime, "Date": date}
            return taskDict
        elif category == "homework":
            day = str(input("Please enter the day when your class will take place. "))
            startTime = int(input("Please enter the start time of your class. "))
            endTime = int(input("Please enter the end time of your class. "))
            date = str(input("Please enter a date for when you will start the task. "))
            taskDict = {"Task": userTask, "Category": category, "Day": day, "startTime": startTime, "endTime": endTime, "Date": date}
            return taskDict
        
        

#user enters true false
#be able to delete tasks
def deleteTask():
    print("would you like to delete task? Y/N")
    complete = False
    moved = False


#edit tasks to be more versatile with time
#def editTask():


#def scheduleTask():
addTask()
