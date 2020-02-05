from tkinter import *
import pymysql
import pymysql.cursors
from tkinter import messagebox
""""****************************************MANAGE  STOCKS************************************************"""

def stock_1():
    def stock_insert():
        pid=product_id.get()
        pq=product_quantity.get()
        try:
                
              conn= pymysql.connect(host='localhost',user='root',password='',db="ims")
              a=conn.cursor()
              a.execute("update product set productQty='"+pq+"' where productid='"+pid+"'")
              conn.commit()
              messagebox.showinfo('submitted')
        except:
          conn.rollback()
          messagebox.showinfo('Not submit')
          conn.close()
    top=Toplevel()
    top.title('NEW Window')
    Mframe=Frame(top,bg="yellow",width=1000,height=800,relief='raise',bd=10)
    Mframe.pack(padx=50,pady=20)

    lb2=Label(Mframe,text="Product_id",width=15)
    lb2.grid(row=1,column=0,padx=10,pady=10)
    product_id=StringVar()
    tb2=Entry(Mframe,textvariable=product_id)
    tb2.grid(row=1,column=1)

    lb2=Label(Mframe,text="Product_Quantity",width=15)
    lb2.grid(row=2,column=0,padx=10,pady=10)
    product_quantity=StringVar()
    tb2=Entry(Mframe,textvariable=product_quantity)
    tb2.grid(row=2,column=1)
        
    b1 = Button(top, text='close', command=top.destroy)
    b1.pack()
    b2 = Button(top, text='Insert', command=stock_insert)
    b2.pack()

def stock_2():
    top=Toplevel()
    top.geometry("720x320")
    top.title('NEW Window')
    top.config(background='gray')
    sb = Scrollbar(top)  
    sb.pack(side = RIGHT, fill = Y)
    mylist = Listbox(top,yscrollcommand = sb.set)  
    
    
    def stock_display():
        conn = pymysql.connect(host='localhost', user='root', password='', db='ims')
        a = conn.cursor()

        a.execute("select productid,productname,productQty from product")
        results = a.fetchall()
        
        count = a.rowcount

      

        if count > 0:
            for row in results:
              
                 
                
                L = Label(top,text=("pid=",row[0],",pname=",row[1],",qty=",row[2]),font = "Verdana 20 bold",width=50,relief= RAISED)
                L.pack(pady=0,padx=0)
            
              
            
           
                     
        else:
            messagebox.showinfo("record not found")
        conn.close()
    b1=Button(top,text='close',width=20,height=2,bg='skyblue',command=top.destroy)
    b1.pack()
    
    b2=Button(top,text='view stock details',width=20,height=2,command=stock_display)
    b2.pack()
    #l=Label(top,text='Pid  pname qty',font = "Verdana 20 bold")
    #l.pack()
   

def verify1():
    def verifiable():
        p_id=product_id.get()
        try:
            conn= pymysql.connect(host='localhost',user='root',password='',db='ims')
            a=conn.cursor()
            a.execute("select * from product where productid='"+p_id+"'")
            result=a.rowcount
            print(result)
            if result>0:
                 stock_1()
            else:
                 messagebox.showinfo("Id not Found")
        except Exception as e:
             messagebox.showinfo(e)
    top=Toplevel()
    top.title('NEW Window')
    Mframe=Frame(top,bg="yellow",width=1000,height=800,relief='raise',bd=10)
    Mframe.pack(padx=50,pady=20)

    lb2=Label(Mframe,text="Product_id",width=15)
    lb2.grid(row=1,column=0,padx=10,pady=10)
    product_id=StringVar()
    tb2=Entry(Mframe,textvariable=product_id)
    tb2.grid(row=1,column=1)

    b2 = Button(top, text='search', command=verifiable)
    b2.pack()


"""*********************************************PRODUCTDS DETAILS******************************************************"""
def open_1():
    def insert():
        pid=product_id.get()
        pn=product_name.get()
        pp=product_price.get()
        sp=sale_price.get()
        pq=product_quantity.get()
        try:
          conn= pymysql.connect(host='localhost',user='root',password='',db='ims')
          a=conn.cursor()
          a.execute("insert into product values('"+pid+"','"+pn+"','"+pp+"','"+sp+"','"+pq+"')")
          conn.commit()
          messagebox.showinfo('submitted')
        except:
          conn.rollback()
          messagebox.showinfo('Not submit')
        conn.close()
    top=Toplevel()
    top.title('NEW Window')
    Mframe=Frame(top,bg="yellow",width=1000,height=800,relief='raise',bd=10)
    Mframe.pack(padx=50,pady=20)

    lb1=Label(Mframe,text="Product_id",width=15)
    lb2=Label(Mframe,text="Product_name",width=15)
    lb3=Label(Mframe,text="Product_price",width=15)
    lb4=Label(Mframe,text="Sale_price",width=15)
    lb5=Label(Mframe,text="Product_quantity",width=15)

    lb1.grid(row=3,column=0,padx=10,pady=10)
    lb2.grid(row=4,column=0,padx=10,pady=10)
    lb3.grid(row=5,column=0,padx=10,pady=10)
    lb4.grid(row=6,column=0,padx=10,pady=10)
    lb5.grid(row=7,column=0,padx=10,pady=10)
    
    

    product_id=StringVar()
    product_name=StringVar()
    product_price=StringVar()
    sale_price=StringVar()
    product_quantity=StringVar()
    
    tb1=Entry(Mframe,textvariable=product_id)
    tb2=Entry(Mframe,textvariable=product_name)
    tb3=Entry(Mframe,textvariable=product_price)
    tb4=Entry(Mframe,textvariable=sale_price)
    tb5=Entry(Mframe,textvariable=product_quantity)
    
    

    tb1.grid(row=3,column=1)
    tb2.grid(row=4,column=1)
    tb3.grid(row=5,column=1)
    tb4.grid(row=6,column=1)
    tb5.grid(row=7,column=1)
    
    
    
    
    b1=Button(top,text='close',command=top.destroy)
    b1.pack()
    b2=Button(top,text='Insert',command=insert)
    b2.pack()
   
    

def open2():
    top=Toplevel()
    top.geometry("720x320")
    top.title('NEW Window')
    top.config(background='gray')
    sb = Scrollbar(top)  
    sb.pack(side = RIGHT, fill = Y)
    mylist = Listbox(top,yscrollcommand = sb.set)  
    
    
    def display():
        conn = pymysql.connect(host='localhost', user='root', password='', db='ims')
        a = conn.cursor()

        a.execute("select * from product")

        results = a.fetchall()

        count = a.rowcount

        #print(results)

        print(count)

        if count > 0:
            for row in results:
                print()
                L = Label(top,text=("pid=",row[0],",pname=",row[1],",pprice=",row[2],",sprice=",row[3],",qty=",row[4]),padx=5,pady=10,font="Verdana 20 bold",width=70,relief= RAISED)
                L.pack(pady=0,padx=0)
              
            
           
                     
        else:
            messagebox.showinfo("record not found")
        conn.close()
    b1=Button(top,text='close',width=20,height=2,bg='skyblue',command=top.destroy)
    b1.pack()
    
    b2=Button(top,text='show product details',width=20,height=2,command=display)
    b2.pack()
    #l=Label(top,text="pid     pn     pp    sp      qty",font='Verdana 20 bold',width=30,relief=SUNKEN)
    #l.pack(padx=0,pady=0)

def open3():
    def delete():
          pid=product_id.get()
          try:
               conn = pymysql.connect(host='localhost', user='root', password='', db='ims')
               a = conn.cursor()
               a.execute("delete  from product where productid='"+pid+"'")
               conn.commit()
               messagebox.showinfo('deleted')
          except:
               conn.rollback()
               messagebox.showinfo('Not deleted')
               conn.close()


    top=Toplevel()
    top.geometry("720x320")
    top.title('NEW Window')
    top.config(background='gray')      
    lb1=Label(top,text="Enter Product_id to delete product",padx=5,pady=10,font=50,width=30,relief= RAISED)
    lb1.pack()
    product_id=StringVar()
    
    tb1=Entry(top,textvariable=product_id,font=50,width=20,relief=RAISED)
    tb1.pack(padx=1,pady=1)
        
   
    
    b2=Button(top,text='DELETE PRODUCT DETAILS',width=20,height=2,command=delete)
    b2.pack()
    b1=Button(top,text='close',width=20,height=2,bg='skyblue',command=top.destroy)
    b1.pack()

def verify2():
    def verifiable():
        p_id=product_id.get()
        try:
            conn= pymysql.connect(host='localhost',user='root',password='',db='ims')
            a=conn.cursor()
            a.execute("select * from product where productid='"+p_id+"'")
            result=a.rowcount
            print(result)
            if result>0:
                 open3()
            else:
                 messagebox.showinfo("Id not found")
        except Exception as e:
             messagebox.showinfo(e)
    top=Toplevel()
    top.title('NEW Window')
    Mframe=Frame(top,bg="yellow",width=1000,height=800,relief='raise',bd=10)
    Mframe.pack(padx=50,pady=20)

    lb2=Label(Mframe,text="Product_id",width=15)
    lb2.grid(row=1,column=0,padx=10,pady=10)
    product_id=StringVar()
    tb2=Entry(Mframe,textvariable=product_id)
    tb2.grid(row=1,column=1)

    b2 = Button(top, text='search', command=verifiable)
    b2.pack()

"""*******************************************SALE DETAILS***********************************************************"""

def open_s1():
    def insertsale():
        sid=sale_id.get()
        pid=product_id.get()
        
        sp=sale_price.get()
        date=sale_date.get()
        #sp=sale_price.get()
        sq=sale_quantity.get()
        try:
          conn= pymysql.connect(host='localhost',user='root',password='',db='ims')
          a=conn.cursor()
          a.execute("insert into sale values('"+sid+"','"+pid+"','"+sp+"','"+date+"','"+sq+"')")
          conn.commit()
          messagebox.showinfo('submitted')
        except:
        #e.getMessage()
          conn.rollback()
          messagebox.showinfo('Not submit')
        conn.close()
    top=Toplevel()
    top.title('NEW Window')
    Mframe=Frame(top,bg="yellow",width=1000,height=800,relief='raise',bd=10)
    Mframe.pack(padx=50,pady=20)

    lb1=Label(Mframe,text="product_id",width=15)
    lb2=Label(Mframe,text="Sale_id",width=15)
    lb3=Label(Mframe,text="Sale_price",width=15)
    lb4=Label(Mframe,text="Sale_Date",width=15)
    lb5=Label(Mframe,text="Sale_quantity",width=15)

    lb1.grid(row=3,column=0,padx=10,pady=10)
    lb2.grid(row=4,column=0,padx=10,pady=10)
    lb3.grid(row=5,column=0,padx=10,pady=10)
    lb4.grid(row=6,column=0,padx=10,pady=10)
    lb5.grid(row=7,column=0,padx=10,pady=10)
    
    

    sale_id=StringVar()
    product_id=StringVar()
    sale_price=StringVar()
    sale_date=StringVar()
    sale_quantity=StringVar()
    
    tb1=Entry(Mframe,textvariable=sale_id)
    tb2=Entry(Mframe,textvariable=product_id)
    tb3=Entry(Mframe,textvariable=sale_price)
    tb4=Entry(Mframe,textvariable=sale_date)
    tb5=Entry(Mframe,textvariable=sale_quantity)
    
    

    tb1.grid(row=3,column=1)
    tb2.grid(row=4,column=1)
    tb3.grid(row=5,column=1)
    tb4.grid(row=6,column=1)
    tb5.grid(row=7,column=1)
    
    
    
    
    b1=Button(top,text='close',command=top.destroy)
    b1.pack()
    b2=Button(top,text='Insert',command=insertsale)
    b2.pack()

def open_s2():
    def update():
          sid=sale_id.get()
          pid=product_id.get()
          sp=sale_price.get()
          date=sale_date.get()
          sqty=sale_quantity.get()
          try:
           conn = pymysql.connect(host='localhost', user='root', password='', db='ims')
           a = conn.cursor()
           a.execute("update sale set productid='"+pid+"',price='"+sp+"',date='"+date+"',saleqty='"+sqty+"' where saleid='"+sid+"'")
           conn.commit()
           messagebox.showinfo('updated')
          except:
           conn.rollback()
           messagebox.showinfo('Not updated')
          conn.close()
    top=Toplevel()
    top.title('NEW Window')
    Mframe=Frame(top,bg="yellow",width=1000,height=800,relief='raise',bd=10)
    Mframe.pack(padx=50,pady=20)

    lb1=Label(Mframe,text="Sale_id",width=15)
    lb2=Label(Mframe,text="Product_id",width=15)
    lb3=Label(Mframe,text="Sale_price",width=15)
    lb4=Label(Mframe,text="Sale_Date",width=15)
    lb5=Label(Mframe,text="Sale_quantity",width=15)

    lb1.grid(row=3,column=0,padx=10,pady=10)
    lb2.grid(row=4,column=0,padx=10,pady=10)
    lb3.grid(row=5,column=0,padx=10,pady=10)
    lb4.grid(row=6,column=0,padx=10,pady=10)
    lb5.grid(row=7,column=0,padx=10,pady=10)
    
    

    sale_id=StringVar()
    product_id=StringVar()
    sale_price=StringVar()
    sale_date=StringVar()
    sale_quantity=StringVar()
    
    tb1=Entry(Mframe,textvariable=sale_id)
    tb2=Entry(Mframe,textvariable=product_id)
    tb3=Entry(Mframe,textvariable=sale_price)
    tb4=Entry(Mframe,textvariable=sale_date)
    tb5=Entry(Mframe,textvariable=sale_quantity)



    tb1.grid(row=3,column=1)
    tb2.grid(row=4,column=1)
    tb3.grid(row=5,column=1)
    tb4.grid(row=6,column=1)
    tb5.grid(row=7,column=1)

    
    b2=Button(top,text='UPDATE PRODUCT DETAILS',width=20,height=2,command=update)
    b2.pack()
    b1=Button(top,text='close',width=20,height=2,bg='skyblue',command=top.destroy)
    b1.pack()


"********************************************UPDATE SALE DETAILS***********************************************"
def verify3():
    def verifiable():
        sid=sale_id.get()
        try:
            conn= pymysql.connect(host='localhost',user='root',password='',db='ims')
            a=conn.cursor()
            a.execute("select * from sale where saleid='"+sid+"'")
            result=a.rowcount
            print(result)
            if result>0:
                 open_s2()
            else:
                messagebox.showinfo("Id not Found")
        except Exception as e:
             messagebox.showinfo(e)
    top=Toplevel()
    top.title('NEW Window')
    Mframe=Frame(top,bg="yellow",width=1000,height=800,relief='raise',bd=10)
    Mframe.pack(padx=50,pady=20)

    lb2=Label(Mframe,text="sale_id",width=15)
    lb2.grid(row=1,column=0,padx=10,pady=10)
    sale_id=StringVar()
    tb2=Entry(Mframe,textvariable=sale_id)
    tb2.grid(row=1,column=1)

    b2 = Button(top, text='search',command=verifiable)
    b2.pack()


def open_s3():
    top=Toplevel()
    top.geometry("720x320")
    top.title('NEW Window')
    top.config(background='gray')
    sb = Scrollbar(top)  
    sb.pack(side = RIGHT, fill = Y)
    mylist = Listbox(top,yscrollcommand = sb.set)  
    
    
    def display():
        conn = pymysql.connect(host='localhost', user='root', password='', db='ims')
        a = conn.cursor()

        a.execute("select * from sale")

        results = a.fetchall()
        
        count = a.rowcount

        #print(results)

        print(count)

        if count > 0:
            for row in results:
                print()
                L = Label(top,text=("Pid=",row[0],",Sid=",row[1],",Sprice=",row[2],",SDate=",row[3],",Sqty=",row[4]),padx=5,pady=10,font="Verdana 20 bold",width=70,relief= RAISED)
                L.pack(pady=0,padx=0)
              
            
           
                     
        else:
            messagebox.showinfo("record not found")
        conn.close()
    b1=Button(top,text='close',width=20,height=2,bg='skyblue',command=top.destroy)
    b1.pack()
    
    b2=Button(top,text='show sale details',width=20,height=2,command=display)
    b2.pack()
    #l=Label(top,text='pid   pn   pp sp   qty',font='Verdana 20 italic')
    #l.pack()
   




root=Tk()
root.geometry("1280x1080")
root.title("INVENTORY")
#root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())


#root.configure(bg="orange")

scroll=Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)
scroll.activate()
topframe=Frame(root,bg="yellow",width=1500,height=200,relief='raise',bd=10)
topframe.pack(side=TOP)
lb=Label(topframe,text="INVENTORY  MANAGEMENT  SYSTEM",font=('italic',40,'bold'),width=41,fg='black')
lb.grid(row=0,column=1)

frame=Frame(root,bg="yellow",width=700,height=200,relief='raise',bd=10)
frame.pack(side=TOP)
lb1=Label(frame,text="STOCK",font=('italic',40,'bold'),width=41,fg='black',bg='orange')
lb1.grid(row=2,column=1)


b1=Button(root,text='UPDATE PRODUCTS QUANTITY IN STOCK',bg='skyblue',width=35,height=2,command=verify1,font=('italic',15,'bold'),bd=5,fg='black',relief=SOLID,activebackground="orange")
b1.pack()
b1.place(x=100,y=200)
b9=Button(root,text='VIEW STOCK DETAILS',bg='skyblue',width=20,height=2,command=stock_2,font=('italic',15,'bold'),bd=5,fg='black',relief=SOLID,activebackground="orange")
b9.pack()
b9.place(x=600,y=200)

#frame=Frame(root,bg="yellow",width=1500,height=200,relief='raise',bd=10)
#frame.pack(side=TOP)
lb1=Label(text="PRODUCTS",font=('italic',40,'bold'),width=41,fg='black',bg='orange')
lb1.pack()
lb1.place(x=10,y=280)


b3=Button(root,text='ADD NEW PRODUCT',bg='skyblue',width=25,height=2,command=open_1,font=('italic',15,'bold'),bd=5,relief=SOLID,activebackground="orange")

b3.pack()
b3.place(x=100,y=365)
b4=Button(root,text='SHOW PRODUCTS',bg='skyblue',command=open2,width=20,height=2,font=('italic',15,'bold'),bd=5,fg='black',relief=SOLID,activebackground="orange")
b4.pack()
b4.place(x=500,y=365)
b5=Button(root,text='DELETE PRODUCT',bg='skyblue',command=verify2,width=20,height=2,font=('italic',15,'bold'),bd=5,fg='black',relief=SOLID,activebackground="orange")
b5.pack()
b5.place(x=850,y=365)

#frame=Frame(root,bg="yellow",width=1500,height=200,relief='raise',bd=10)
#frame.pack(side=TOP)
lb1=Label(text="SALES",font=('italic',40,'bold'),width=41,fg='BLACK',bg='orange')
lb1.pack()
lb1.place(x=10, y=470)



b6=Button(root,text='ADD SALE DETAILS',bg='skyblue',command=open_s1,width=20,height=2,font=('italic',15,'bold'),bd=5,fg='black',relief=SOLID,activebackground="orange")
b6.pack()
b6.place(x=100,y=560)
b7=Button(root,text='UPDATE SALE DETAILS',bg='skyblue',command=verify3,height=2,font=('italic',15,'bold'),bd=5,width=35,fg='black',relief=SOLID,activebackground="orange")
b7.pack()
b7.place(x=400,y=560)
b8=Button(root,text='VIEW SALE DETAILS',bg='skyblue',command=open_s3,width=20,height=2,font=('italic',15,'bold'),bd=5,fg='black',relief=SOLID,activebackground="orange")
b8.pack()
b8.place(x=900,y=560)
#b=Button(root,text='open window2',command=open_n)
#b.pack()

root.configure(background='gray')
root.mainloop()

