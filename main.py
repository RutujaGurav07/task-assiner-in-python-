###############n add task function##################
def addtask():
    def submitadd():
        print("submit")
        task =taskvalue.get()
        status=statusvalue.get()        
        try:
            strr = "insert into task ( task,status)values(%s,%s);"
            mycursor.execute(strr,(task,status))
            con.commit()
            msg= messagebox.askokcancel('Notification','task added sucessesfully',parent=addroot)
            print("task")
        except:
            print("Error occure whlie adding task")
            msg= messagebox.askokcancel('Notification','Error occure while adding task',parent=addroot)
        strr ='select * from task'
        mycursor.execute(strr)                                          
        datas=mycursor.fetchall()
        tasktable.delete(*tasktable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2]]
            tasktable.insert('',END,values=vv)
    
    addroot=Toplevel()
    addroot.geometry('370x200+200+200')
    addroot.grab_set()
    addroot.title("Task assigner")
    addroot.resizable(False,False) 
    print("Task Added")
    
    tasklabel=Label(addroot,text='Enter task :',font=('times',10 ,'bold'),relief=RIDGE,borderwidth=4,bg='white',width=12)
    tasklabel.place(x=10,y=10)
    statuslabel=Label(addroot,text='Enter status :',font=('times',10 ,'bold'),relief=RIDGE,borderwidth=4,bg='white',width=12)
    statuslabel.place(x=10,y=60)

    taskvalue=StringVar()
    taskentry=Entry(addroot,font=('times',10 ,'bold'),bd=5,textvariable=taskvalue)
    taskentry.place(x=120,y=10)

    statusvalue=StringVar()
    statusentry=Entry(addroot,font=('times',10 ,'bold'),bd=5,textvariable=statusvalue)
    statusentry.place(x=120,y=60)
    
    submintbtn=Button(addroot,text='submit',width=20,font=('times',10 ,'bold'),relief=RIDGE,borderwidth=4,bg='white',activebackground ="light blue",command=submitadd)
    submintbtn.place(x=120,y=120)
    addroot.mainloop()

########################### Update task function ###################
def updatetask():
    def update():
        id=idvalue.get()
        task =taskvalue.get()
        status=statusvalue.get()

        try:
            strr = "update task set task = %s , status=%s where task_id = %s "
            mycursor.execute(strr,(task,status,id))
            con.commit()
            msg= messagebox.showinfo('Notification','task modify sucessesfully',parent=addroot)
            print("task")
        except:
            print("Error occure whlie adding task")
            msg= messagebox.showerror('Notification','Error occure while adding task',parent=addroot)
        strr ='select * from task'
        mycursor.execute(strr)                                          
        datas=mycursor.fetchall()
        tasktable.delete(*tasktable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2]]
            tasktable.insert('',END,values=vv)
    

    addroot=Toplevel()
    addroot.geometry('370x200+200+200')
    addroot.grab_set()
    addroot.title("Task assigner")
    addroot.resizable(False,False)
    print("Task Added")
    
    idlabel=Label(addroot,text='update id :',font=('times',10 ,'bold'),relief=RIDGE,borderwidth=4,bg='white',width=12)
    idlabel.place(x=10,y=10)
    
    tasklabel=Label(addroot,text='update task :',font=('times',10 ,'bold'),relief=RIDGE,borderwidth=4,bg='white',width=12)
    tasklabel.place(x=10,y=50)
    
    statuslabel=Label(addroot,text='update status :',font=('times',10 ,'bold'),relief=RIDGE,borderwidth=4,bg='white',width=12)
    statuslabel.place(x=10,y=80)
    
    idvalue=StringVar()
    identry=Entry(addroot,font=('times',10 ,'bold'),bd=5,textvariable=idvalue)
    identry.place(x=120,y=10)
    
    taskvalue=StringVar()
    taskentry=Entry(addroot,font=('times',10 ,'bold'),bd=5,textvariable=taskvalue)
    taskentry.place(x=120,y=50)
    
    statusvalue=StringVar()
    statusentry=Entry(addroot,font=('times',10 ,'bold'),bd=5,textvariable=statusvalue)
    statusentry.place(x=120,y=80)
    
    submintbtn=Button(addroot,text='submit',width=20,font=('times',10 ,'bold'),relief=RIDGE,borderwidth=4,bg='white',activebackground ="light blue",command=update)
    submintbtn.place(x=120,y=120)
    print("Task Updated")
    
    up=tasktable.focus()
    upinfo=tasktable.item(up)
    pp=upinfo['values']
    print (pp)
    if (len(pp) != 0):
        idvalue.set(pp[0])
        taskvalue.set(pp[1])
        statusvalue.set(pp[2])
    
    addroot.mainloop()
################################Delete task ###################    
def deletetask():
    cc=tasktable.focus()
    info=tasktable.item(cc)
    pp=info['values'][0]
    strr='delete from task where task_id = %s '
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification' 'id {} deleted sucessfully',format(pp))  
    strr ='select * from task'
    mycursor.execute(strr)   
    datas=mycursor.fetchall()
    tasktable.delete(*tasktable.get_children())
    for i in datas:
        vv=[i[0],i[1],i[2]]
        tasktable.insert('',END,values=vv)
##################### Show task ####################################### 
def showtask():
    print("Task Added")
    strr ='select * from task'
    mycursor.execute(strr)                                          
    datas=mycursor.fetchall()
    tasktable.delete(*tasktable.get_children())
    for i in datas:
        vv=[i[0],i[1],i[2]]
        tasktable.insert('',END,values=vv)

################################### Search task #####################################
def searchtask():
    def search():
        id = idvalue.get()
        task =taskvalue.get()
        status=statusvalue.get()
        if (id !=''):
            strr='select * from task where task_id = %s '
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            tasktable.delete(*tasktable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2]]
                tasktable.insert('',END,values=vv)

        elif (task !=''):
            # print("it work")
            strr='select * from task where task = %s'
            mycursor.execute(strr,(task))
            datas = mycursor.fetchall()
            tasktable.delete(*tasktable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2]]
                tasktable.insert('',END,values=vv)
        elif (status !=''):
            strr='select * from task where status = %s '
            mycursor.execute(strr,(status))
            datas = mycursor.fetchall()
            tasktable.delete(*tasktable.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2]]
                tasktable.insert('',END,values=vv)

    searchroot=Toplevel()
    searchroot.geometry('370x200+200+200')
    searchroot.grab_set()
    searchroot.title("Task assigner")
    searchroot.resizable(False,False)
    print("Task Added")
    idlabel=Label(searchroot,text='Enter id :',font=('times',10 ,'bold'),relief=RIDGE,borderwidth=4,bg='white',width=12)
    idlabel.place(x=10,y=10)
    tasklabel=Label(searchroot,text='Enter task :',font=('times',10 ,'bold'),relief=RIDGE,borderwidth=4,bg='white',width=12)
    tasklabel.place(x=10,y=50)
    statuslabel=Label(searchroot,text='Enter status :',font=('times',10 ,'bold'),relief=RIDGE,borderwidth=4,bg='white',width=12)
    statuslabel.place(x=10,y=80)
    
    idvalue=StringVar()
    identry=Entry(searchroot,font=('times',10 ,'bold'),bd=5,textvariable=idvalue)
    identry.place(x=120,y=10)

    taskvalue=StringVar()
    taskentry=Entry(searchroot,font=('times',10 ,'bold'),bd=5,textvariable=taskvalue)
    taskentry.place(x=120,y=50) 

    statusvalue=StringVar()
    statusentry=Entry(searchroot,font=('times',10 ,'bold'),bd=5,textvariable=statusvalue)
    statusentry.place(x=120,y=80)
    
    submintbtn=Button(searchroot,text='search',width=20,font=('times',10 ,'bold'),relief=RIDGE,borderwidth=4,bg='white',activebackground ="light blue",command=search)
    submintbtn.place(x=120,y=120)
    searchroot.mainloop()
    print("Task seached")
      
def timefunction():
    time_string=time.strftime("%H:%M:%S")
    date_String =time.strftime('%d/%m/%y')
    clock.config(text='Date:'+date_String+"\n"+'Time:'+time_string)
    clock.after(200,timefunction)

###################################
from tkinter import *
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
import time
import pymysql

root = Tk()
root.title ("Task assigner")
root.config(bg="gray")
root.geometry('900x500+100+100')
root.resizable(False,False)
try:
    con=pymysql.connect(host="localhost",user= "taskassigner",password="password",database='taskassigner')
    mycursor=con.cursor()
    print("connected")
except:
    print("data is incorrect")  
############################################## Frame #################################################
DataEntryFrame =Frame(root,bg='white',relief=GROOVE,borderwidth=2)
DataEntryFrame.place(x=30,y=60,width=400,height=400)    
showEntryFrame =Frame(root,bg='white',relief=GROOVE,borderwidth=2)
showEntryFrame.place(x=460,y=60,width=400,height=400)    
########################## dataentryframe ####################################################
addbtn=Button(DataEntryFrame ,text='Add task',font=('times',10 ,'bold'),width=20,relief=RIDGE,borderwidth=4,bg='white',activebackground ="light blue",command =addtask )
addbtn.pack(side=TOP,expand =True)
updatebtn=Button(DataEntryFrame ,text='Update task',font=('times',10 ,'bold'),width=20,relief=RIDGE,borderwidth=4,bg='white',activebackground ="light blue",command =updatetask)
updatebtn.pack(side=TOP,expand =True)
deletebtn=Button(DataEntryFrame ,text='Delete task',font=('times',10 ,'bold'),width=20,relief=RIDGE,borderwidth=4,bg='white',activebackground ="light blue",command = deletetask)
deletebtn.pack(side=TOP,expand =True)
searchbtn=Button(DataEntryFrame ,text='Search task',font=('times',10 ,'bold'),width=20,relief=RIDGE,borderwidth=4,bg='white',activebackground ="light blue",command =searchtask)
searchbtn.pack(side=TOP,expand =True)
showbtn=Button(DataEntryFrame ,text='Show task',font=('times',10 ,'bold'),width=20,relief=RIDGE,borderwidth=4,bg='white',activebackground ="light blue",command =showtask)
showbtn.pack(side=TOP,expand =True)

########################################## clock ################################################
clock =Label(root,font=('times',10 ,'bold'),relief=RIDGE,borderwidth=4,bg='white',width=20)
clock.place(x=10,y=10)
timefunction()
###################################### showEntryFrame###################################

scroll_x =Scrollbar(showEntryFrame ,orient=HORIZONTAL)
scroll_y =Scrollbar(showEntryFrame ,orient=VERTICAL)
tasktable= Treeview(showEntryFrame,columns=('id','task','status'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=tasktable.xview)
scroll_y.config(command=tasktable.yview)
tasktable.heading('id',text='id')
tasktable.heading('task',text='task')
tasktable.heading('status',text='status')
tasktable['show']='headings'
tasktable.pack(fill=BOTH,expand =1)
root.mainloop()