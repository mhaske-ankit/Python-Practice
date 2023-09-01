import os
os.chdir("/home/m_ankit/Python.practice/rename files/")
print(os.getcwd())

for f in os.listdir():
                      
    f_name, f_ext = (os.path.splitext(f))         
                        
    f_course, f_title, f_number =(f_name.split('-')) 

    f_course = f_course.strip()
    f_title = f_title.strip()
    f_number = f_number.strip()[1:].zfill(2)
    new_file=('{}-{}-{}{}'.format(f_number, f_title, f_course, f_ext))

    os.rename(f, new_file)