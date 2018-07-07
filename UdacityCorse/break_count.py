#Python2
# برنامج أخذ الإستراحة
import time
import webbrowser

break_time = 3
break_count = 0
print('Time star: ', time.ctime())
while break_count < break_time:
    time.sleep(10)
    print('Time now: ', time.ctime())
    webbrowser.open('https://classroom.udacity.com/courses/ud004-track-1mac/lessons/8537c23f-4f42-49d3-90c6-d4b608c80027/concepts/10157285980923')
    break_count +=1
    
