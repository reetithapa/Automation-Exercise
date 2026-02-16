#writing
#file = open("C:\\Users\\User\\Desktop\\Python-Selenium\\PythonSeleniumProject1\\Files\\Reeti.txt","w")
#file.write("My name is Reeti Thapa.\n ")
#file.write("I am learning python Programming.")
#file.close()

#reading entire text
file = open("C:\\Users\\User\\Desktop\\Python-Selenium\\PythonSeleniumProject1\\Files\\Reeti.txt","r")
print(file.read())
file.close()

#reading only 10 characters
file = open("C:\\Users\\User\\Desktop\\Python-Selenium\\PythonSeleniumProject1\\Files\\Reeti.txt","r")
print(file.read(10))
file.close()
