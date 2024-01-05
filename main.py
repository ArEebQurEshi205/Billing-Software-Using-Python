from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.title("Billing Software")


        # ----- ----- Image Section ----- ------
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

        # ----- ----- Title Section ----- -----
        lbl_title=Label(self.root,text="BILLING SOFTWARE",font=("Arial",26,"bold","italic"),bg="black",fg="white")
        lbl_title.place(x=0,y=103,width=1400,height=45)
        
        # ----- ----- Details Frame ----- -----
        Main_Frame=Frame(self.root,bd=9,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=150,width=1360,height=550)

# ---------------------------------------------------------------------------------------------------------#
        # ----- ----- Customer Frame ----- -----
        Cust_Frame=LabelFrame(Main_Frame,text="Customer Details:",font=("Courier New",12,"bold"),bg="Black",fg="white",bd=8)
        Cust_Frame.place(x=-1,y=3,width=355,height=130)       
        # Mobile Info Section 
        self.lbl_mob=Label(Cust_Frame,text="Mobile Number:",font=("Courier New",12,"bold"),bg="black",fg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)
        self.entry_mob=ttk.Entry(Cust_Frame,font=("Courier New",10,"bold"),width=20)
        self.entry_mob.grid(row=0,column=1,padx=5,pady=2)
        # Customer Info Section
        self.lblCustName=Label(Cust_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="Customer Name:",bd=4)
        self.lblCustName.grid(row=1,column=0,stick=W,padx=5,pady=2)
        self.txtCustName=ttk.Entry(Cust_Frame,font=('Courier New',10,'bold'),width=20)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        # Gmail Info Section 
        self.lblEmail=Label(Cust_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="Email:",bd=4)
        self.lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)
        self.txtEmail=ttk.Entry(Cust_Frame,font=('Courier New',10,'bold'),width=20)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
# ---------------------------------------------------------------------------------------------------------#
        # ----- ----- Product Frame ----- -----
        Product_Frame=LabelFrame(Main_Frame,text="Product:",font=('Courier New',13,'bold'),bg="black",fg="white",bd=8)
        Product_Frame.place(x=357,y=3,width=560,height=130)
        # Product Category
        self.lblCategory=Label(Product_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="Select Category:",bd=4)
        self.lblCategory.grid(row=0,column=0,stick=W,padx=5,pady=2)
        self.Combo_Category=ttk.Combobox(Product_Frame,font=('arial',8,'bold'),width=24,state="readonly")
        self.Combo_Category.grid(row=0,column=1,stick=W,padx=5,pady=2)
        # Product Sub-Category
        self.lblSubCategory=Label(Product_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="SubCategory:",bd=4)
        self.lblSubCategory.grid(row=1,column=0,stick=W,padx=5,pady=2)
        self.ComboSubCategory=ttk.Combobox(Product_Frame,state="readonly",font=('arial',8,'bold'),width=24)
        self.ComboSubCategory.grid(row=1,column=1,stick=W,padx=5,pady=2)
        # Product Name 
        self.lblproduct=Label(Product_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="Product Name:",bd=4)
        self.lblproduct.grid(row=2,column=0,stick=W,padx=5,pady=2)
        self.Combo_Product=ttk.Combobox(Product_Frame,state="readonly",font=('arial',8,'bold'),width=24)
        self.Combo_Product.grid(row=2,column=1,stick=W,padx=5,pady=2)
        # Price
        self.Price=Label(Product_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="Price:",bd=4)
        self.Price.grid(row=0,column=2,stick=W,padx=5,pady=2)
        self.ComboPrice=ttk.Combobox(Product_Frame,state="readonly",font=('arial',5,'bold'),width=11)
        self.ComboPrice.grid(row=0,column=3,stick=W,padx=5,pady=2)
        # Quantity 
        self.lblQty=Label(Product_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="Quantity:",bd=4)
        self.lblQty.grid(row=1,column=2,stick=W,padx=5,pady=2)
        self.ComboQty=ttk.Entry(Product_Frame,font=('arial',6,'bold'),width=14)
        self.ComboQty.grid(row=1,column=3,stick=W,padx=5,pady=2)
# -------------------------------#----------------------#----------------------------# ------------------------#
        # ----- ----- Middle Frame ----- ----- 
        MiddleFrame=Frame(Main_Frame,bd=10,bg="black")
        MiddleFrame.place(x=2,y=137,width=915,height=247)
        # Middle Image 1
        middleimg=Image.open("image/dashboard image.png")
        middleimg=middleimg.resize((905,237),Image.AFFINE)
        self.photomiddleimg=ImageTk.PhotoImage(middleimg)
        lbl_middleimg=Label(MiddleFrame,image=self.photomiddleimg)
        lbl_middleimg.place(x=-4.5,y=-4.5,width=905,height=237)
#-----------------------------------------------------------------------------------------------------------
        # --------- Search Section --------
        Search_Frame=Frame(Main_Frame,bd=2,bg="black")
        Search_Frame.place(x=923,y=2,width=413,height=38.5)  
        # Bill No Search Frame
        self.lblBill=Label(Search_Frame,font=('Courier New',13,'bold'),bg="black",fg="white",text="Bill No:")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=9,pady=4)
        # Bill No Search Bar
        self.txt_Entry_Search=ttk.Entry(Search_Frame,font=('arial',11,'bold'),width=19)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=5,pady=5)  
        # Bill No Button
        self.BtnSearch=Button(Search_Frame,text="Search",font=('arial black',8,'bold'),bg="white",fg="black",width=10,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2,padx=15,pady=1)  
# --------------------------------------#---------------------------------#----------------------------------#      
        # ---------- Right Frame Bill Section ----------------
        RighLabelFrame=LabelFrame(Main_Frame,text="Bill Section:",font=("Courier New",14,"bold"),bg="black",fg="white",bd=6)
        RighLabelFrame.place(x=921,y=45,width=415,height=340)

        scroll_y=Scrollbar(RighLabelFrame,orient=VERTICAL)
        self.textarea=Text(RighLabelFrame,yscrollcommand=scroll_y.set,bg="black",fg="white",font=("Courier New",10,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
# ------------------------------------------------------------------------------------------------------------
        # ------------- Bill Counter  Section --------------
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Recipt",font=("Courier New",15,"bold"),bg="black",fg="white")
        Bottom_Frame.place(x=2,y=390,width=1335,height=139)
        # Sub total Section 
        self.lblSubTotal=Label(Bottom_Frame,font=('Courier New',14,'bold'),bg="black",fg="white",text="Sub Total:",bd=5)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=20,pady=2)
        self.EntrySubTotal=ttk.Entry(Bottom_Frame,font=('arial',13,'bold'),width=17)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        # Tax total Section 
        self.lbl_tax=Label(Bottom_Frame,font=('Courier New',14,'bold'),bg="black",fg="white",text="Gov Tax:",bd=5)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=20,pady=2)
        self.txt_tax=ttk.Entry(Bottom_Frame,font=('arial',13,'bold'),width=17)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        # Total Section 
        self.lbl_Total=Label(Bottom_Frame,font=('Courier New',14,'bold'),bg="black",fg="white",text="Total:",bd=5)
        self.lbl_Total.grid(row=2,column=0,sticky=W,padx=20,pady=2)
        self.txt_Total=ttk.Entry(Bottom_Frame,font=('arial',13,'bold'),width=17)
        self.txt_Total.grid(row=2,column=1,sticky=W,padx=5,pady=2)
# ------------------------------------------------------------------------------------------------------------
        # ------ ---------Bill Section Button --------- ------
        Btn_Frame=Frame(Bottom_Frame,bd=5,bg="white")
        Btn_Frame.place(x=400,y=17)
        # Button 1
        self.BtnAddToCart=Button(Btn_Frame,height=2,text="Add To Cart",font=('arial black',10,'bold'),bg="black",fg="white",width=15,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)
        # Button 2
        self.Btngenerate_bill=Button(Btn_Frame,height=2,text="Generate Bill",font=('arial black',10,'bold'),bg="black",fg="white",width=15,cursor="hand2")
        self.Btngenerate_bill.grid(row=0,column=1)
        # Button 3
        self.BtnSave=Button(Btn_Frame,height=2,text="Save Bill",font=('arial black',10,'bold'),bg="black",fg="white",width=15,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)
        # Button 4
        self.BtnPrint=Button(Btn_Frame,height=2,text="Print",font=('arial black',10,'bold'),bg="black",fg="white",width=15,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)
        # Button 5
        self.BtnClear=Button(Btn_Frame,height=2,text="Clear",font=('arial black',10,'bold'),bg="black",fg="white",width=15,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)
        # Button 6
        self.BtnExit=Button(Btn_Frame,height=2,text="Exit",font=('arial black',10,'bold'),bg="black",fg="white",width=15,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)


        





if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()