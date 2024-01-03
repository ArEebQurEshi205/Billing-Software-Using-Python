from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        # ----------- Image Section -----------
        # Image 1
        img=Image.open("image/frontImage1.png")
        img=img.resize((400,120),Image.AFFINE)
        self.photoimg=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=400,height=120)
        
        # Image 2
        img_1=Image.open("image/frontImage2.png")
        img_1=img_1.resize((620,120),Image.AFFINE)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=380,y=0,width=620,height=120)

        # Image 3
        img_2=Image.open("image/frontImage3.png")
        img_2=img_2.resize((400,120),Image.AFFINE)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=400,height=120)


        # ------------ Title Section --------

        lbl_title=Label(self.root,text="BILLING SOFTWARE",font=("Arial",26,"bold","italic"),bg="black",fg="white")
        lbl_title.place(x=0,y=122,width=1400,height=45)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=169,width=1530,height=620)
# ---------------------------------------------------------------------------------------------------------#
        # ------- Customer Frame --------
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="black")
        Cust_Frame.place(x=7,y=2,width=350,height=140)
       
        # -------- Mobile Info Section ---------
        self.lbl_mob=Label(Cust_Frame,text="Mobile Number:",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)
        self.entry_mob=ttk.Entry(Cust_Frame,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)
        # ------- Customer Info Section
        self.lblCustName=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Customer Name:",bd=4)
        self.lblCustName.grid(row=1,column=0,stick=W,padx=5,pady=2)
        self.txtCustName=ttk.Entry(Cust_Frame,font=("arial",10,"bold"),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        # -------- Gmail info section 
        self.lblEmail=Label(Cust_Frame,font=("arial",12,"bold"),bg="white",text="Email:",bd=4)
        self.lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)
        self.txtEmail=ttk.Entry(Cust_Frame,font=("arial",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
# ---------------------------------------------------------------------------------------------------------#
        # ------- Product Frame --------
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="black")
        Product_Frame.place(x=367,y=2,width=550,height=140)

        # ------- Product Category -------
        self.lblCategory=Label(Product_Frame,font=("times new roman",12,"bold"),bg="white",text="Select Category:",bd=4)
        self.lblCategory.grid(row=2,column=0,stick=W,padx=5,pady=2)





if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()