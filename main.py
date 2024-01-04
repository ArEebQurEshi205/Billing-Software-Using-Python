from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Billing Software")


        # ----------- Image Section -----------
        # Image 1
        img=Image.open("image/frontImage1.png")
        img=img.resize((400,100),Image.AFFINE)
        self.photoimg=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=400,height=100)
        
        # Image 2
        img_1=Image.open("image/frontImage2.png")
        img_1=img_1.resize((620,100),Image.AFFINE)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=380,y=0,width=620,height=100)

        # Image 3
        img_2=Image.open("image/frontImage3.png")
        img_2=img_2.resize((400,100),Image.AFFINE)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=1000,y=0,width=400,height=100)


        # ------------ Title Section --------

        lbl_title=Label(self.root,text="BILLING SOFTWARE",font=("Arial",26,"bold","italic"),bg="black",fg="white")
        lbl_title.place(x=0,y=103,width=1400,height=45)

        # ------- details frame --------
        Main_Frame=Frame(self.root,bd=9,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=150,width=1360,height=550)
# ---------------------------------------------------------------------------------------------------------#
        # ------- Customer Frame --------
        Cust_Frame=LabelFrame(Main_Frame,text="Customer Details:",font=("Arial Black",12,"bold"),bg="Black",fg="white",bd=8)
        Cust_Frame.place(x=-1,y=3,width=350,height=130)
       
        # -------- Mobile Info Section ---------
        self.lbl_mob=Label(Cust_Frame,text="Mobile Number:",font=("arial",12,"bold"),bg="black",fg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)
        self.entry_mob=ttk.Entry(Cust_Frame,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)
        # ------- Customer Info Section
        self.lblCustName=Label(Cust_Frame,font=('arial',12,'bold'),bg="black",fg="white",text="Customer Name:",bd=4)
        self.lblCustName.grid(row=1,column=0,stick=W,padx=5,pady=2)
        self.txtCustName=ttk.Entry(Cust_Frame,font=('arial',10,'bold'),width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        # -------- Gmail info section 
        self.lblEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg="black",fg="white",text="Email:",bd=4)
        self.lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)
        self.txtEmail=ttk.Entry(Cust_Frame,font=('arial',10,'bold'),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
# ---------------------------------------------------------------------------------------------------------#
        # ------- Product Frame --------
        Product_Frame=LabelFrame(Main_Frame,text="Product:",font=('Arial Black',13,'bold'),bg="black",fg="white",bd=8)
        Product_Frame.place(x=351,y=3,width=560,height=130)

        # ------- Product Category -------
        self.lblCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="black",fg="white",text="Select Category:",bd=4)
        self.lblCategory.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,font=('arial',8,'bold'),width=24,state="readonly")
        self.Combo_Category.grid(row=0,column=1,stick=W,padx=5,pady=2)
        # ------- Product Sub - Category -------
        self.lblSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg="black",fg="white",text="SubCategory:",bd=4)
        self.lblSubCategory.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,state="readonly",font=('arial',8,'bold'),width=24)
        self.ComboSubCategory.grid(row=1,column=1,stick=W,padx=5,pady=2)
        # ------- Product Name -------
        self.lblproduct=Label(Product_Frame,font=('arial',12,'bold'),bg="black",fg="white",text="Product Name:",bd=4)
        self.lblproduct.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.Combo_Product=ttk.Combobox(Product_Frame,state="readonly",font=('arial',8,'bold'),width=24)
        self.Combo_Product.grid(row=2,column=1,stick=W,padx=5,pady=2)
        # ------- Price -------
        self.Price=Label(Product_Frame,font=('arial',12,'bold'),bg="black",fg="white",text="Price:",bd=4)
        self.Price.grid(row=0,column=2,stick=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,state="readonly",font=('arial',5,'bold'),width=24)
        self.ComboPrice.grid(row=0,column=3,stick=W,padx=5,pady=2)
        # ------- Quantity -------
        self.lblQty=Label(Product_Frame,font=('arial',12,'bold'),bg="black",fg="white",text="Quantity:",bd=4)
        self.lblQty.grid(row=1,column=2,stick=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,font=('arial',6,'bold'),width=26)
        self.ComboQty.grid(row=1,column=3,stick=W,padx=5,pady=2)


#-----------------------------------------------------------------------------------------------------------
        # ---------- Right Frame Bill Section ----------------
        RighLabelFrame=LabelFrame(Main_Frame,text="Bill Section",font=("Arial Black",14,"bold"),bg="black",fg="white",bd=6)
        RighLabelFrame.place(x=915,y=45,width=423,height=342)

        scroll_y=Scrollbar(RighLabelFrame,orient=VERTICAL)
        self.textarea=Text(RighLabelFrame,yscrollcommand=scroll_y.set,bg="black",fg="white",font=("Arial Black",10,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # ------------- Bill Counter  Section --------------
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Recipt",font=("Arial Black",14,"bold"),bg="black",fg="white")
        Bottom_Frame.place(x=0,y=390,width=1337,height=139)



if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()