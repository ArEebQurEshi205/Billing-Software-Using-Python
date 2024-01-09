from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk #pip install pillow
import random

class Bill_App:
    def __init__(self,root):
          self.root=root
          self.root.geometry("1500x800+0+0")
          self.root.title("Billing Software")
#==================================> Variables <=============================================
          self.c_name=StringVar()
          self.c_phon=StringVar()
          self.bill_no=StringVar()
          z=random.randint(1000,9999)
          self.bill_no.set(z)
          self.c_email=StringVar()
          self.search_bill=StringVar()
          self.product=StringVar()
          self.prices=IntVar()
          self.qty=IntVar()
          self.sub_total=StringVar()
          self.tax_input=StringVar()
          self.total=StringVar()   
#--------------------#--------------------#--------Ux Section ------------#--------------------#--------------------      
          #---- Product Categories List -----
          self.Category=["Select Option","BreakFast","Lunch","Dinner"]
        
          # 1) Sub Category Part (BreakFast)
          self.SubCategoryBreakFast=["Eggs","Parathas","Tea","Drinks"]
        
          # Product Name Part
          # i)Eggs Part
          self.Eggs=["Half Fry","Omlete","Cheese Omlete","Cheese Half Fry"]
          self.price_HalfFry=100
          self.price_Omlete=60
          self.price_CheeseOmlete=150
          self.price_CheeseHalfFry=160
          # ii)Parathas Part
          self.Parathas=["Lacha Paratha","Aloo Paratha","Chicken Paratha","Chicken Cheese Paratha"]
          self.price_LachaParatha=50
          self.price_AlooParatha=100
          self.price_ChickenParatha=180
          self.price_ChickenCheeseParatha=260
          # iii)Tea Part
          self.Tea=["Doodh Patti Half","Doodh Patti Full","Green Tea"]
          self.price_DoodhPattiHalf=40
          self.price_DoodhPattiFull=70
          self.price_GreenTea=80
          # iv)Drinks Part
          self.Drinks=["Cola Next 500ml","Cola Next 1liter","FizzUp 500ml","FizzUp 1liter","Red Apple 1.5liter","Pakola Water 1.5liter"]
          self.price_ColaNext500ml= 80
          self.price_ColaNext1liter= 160
          self.price_Fizzup500ml= 80
          self.price_Fizzup1liter= 160
          self.price_RedApple=200
          self.price_PakolaWater= 100 


          # 2) Sub Category Part (Lunch)
          self.SubCategoryLunch=["Salads","Pasta And Noodles"]

          #Product Name Part
          # i) Salads Part
          self.Salads=["Green Salads","Pasta Salads","Specialty Salads"]
          self.price_GreenSalads= 120 
          self.price_PastaSalads= 140 
          self.price_SpecialtySalads= 180 
          # ii) Pasta And Noodles Part
          self.PastaAndNoodles=["Italian Pasta","Asian Noodles","Fusion Creations"]
          self.price_ItalianPasta= 220
          self.Price_AsianNoodles= 250
          self.price_FusionCreations= 280
        
          # 3) Sub Category Part (Dinner)
          self.SubCategoryDinner=["Chicken Dishes","Beef Dishes","Pizza's Varieties","Burgurs"]
          #Product Name Part
          # i) Chicken Dishes
          self.ChickenDishes=["Chicken Qourma","Chicken Nihari","Chicken Karahi","Chicken Biryani","Chicken Puloa"]
          self.price_ChickenQourma= 200
          self.price_ChickenNihari= 240
          self.price_ChickenKarahi= 270
          self.price_ChickenBiryani= 300
          self.price_ChickenPuloa= 280
          # ii) Beef Dishes
          self.BeefDishes=["Beef Qourma","Beef Nihari","Beef Biryani","Beef Puloa"]
          self.price_BeefQourma= 200
          self.price_BeefNihari= 240
          self.price_BeefBiryani= 300
          self.price_BeefPuloa= 280
          # iii) Pizzas Varieties
          self.PizzaVarieties=["Tikka","Fajita","Creamy"]
          self.price_Tikka= 300
          self.price_Fajita= 320
          self.price_Creamy= 240
          # iv) Burgur
          self.Burgurs=["Zinger Burgur","Beef Burgur","Double Zinger Burgur"]
          self.price_ZingerBurgur=250
          self.price_BeefBurgur=280
          self.price_DoubleZingerBurgur= 350


        
#--------------------#--------------------#-------- UI Section ------------#--------------------#--------------------
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
          self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=("Courier New",10,"bold"),width=20)
          self.entry_mob.grid(row=0,column=1,padx=5,pady=2)
          # Customer Info Section
          self.lblCustName=Label(Cust_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="Customer Name:",bd=4)
          self.lblCustName.grid(row=1,column=0,stick=W,padx=5,pady=2)
          self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('Courier New',10,'bold'),width=20)
          self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
          # Gmail Info Section 
          self.lblEmail=Label(Cust_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="Email:",bd=4)
          self.lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)
          self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('Courier New',10,'bold'),width=20)
          self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)
# ------  ---------------------------------------------------------------------------------------------------#
          # ----- ----- Product Frame ------ -----
          Product_Frame=LabelFrame(Main_Frame,text="Product:",font=('Courier New',13,'bold'),bg="black",fg="white",bd=8)
          Product_Frame.place(x=357,y=3,width=560,height=130)
          # Product Category
          self.lblCategory=Label(Product_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="Select Category:",bd=4)
          self.lblCategory.grid(row=0,column=0,stick=W,padx=5,pady=2)
          self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=('arial',8,'bold'),width=24,state="readonly")
          self.Combo_Category.current(0)
          self.Combo_Category.grid(row=0,column=1,stick=W,padx=5,pady=2)
          self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)
          # Product Sub-Category
          self.lblSubCategory=Label(Product_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="SubCategory:",bd=4)
          self.lblSubCategory.grid(row=1,column=0,stick=W,padx=5,pady=2)
          self.ComboSubCategory=ttk.Combobox(Product_Frame,values=[""],state="readonly",font=('arial',8,'bold'),width=24)
          self.ComboSubCategory.grid(row=1,column=1,stick=W,padx=5,pady=2)
          self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)
          # Product Name 
          self.lblproduct=Label(Product_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="Product Name:",bd=4)
          self.lblproduct.grid(row=2,column=0,stick=W,padx=5,pady=2)
          self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=('arial',8,'bold'),width=24)
          self.ComboProduct.grid(row=2,column=1,stick=W,padx=5,pady=2)
          self.ComboProduct.bind("<<ComboboxSelected>>",self.price)
          # Price
          self.Price=Label(Product_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="Price:",bd=4)
          self.Price.grid(row=0,column=2,stick=W,padx=5,pady=2)
          self.ComboPrice=ttk.Combobox(Product_Frame,state="readonly",textvariable=self.prices,font=('arial',9,'bold'),width=7)
          self.ComboPrice.grid(row=0,column=3,stick=W,padx=0,pady=2)
          # Quantity 
          self.lblQty=Label(Product_Frame,font=('Courier New',12,'bold'),bg="black",fg="white",text="Quantity:",bd=4)
          self.lblQty.grid(row=1,column=2,stick=W,padx=5,pady=2)
          self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',9,'bold'),width=7)
          self.ComboQty.grid(row=1,column=3,stick=W,padx=5,pady=2)
# ------  -------------------------#----------------------#----------------------------# ------------------------#
          # ----- ----- Middle Frame ----- ----- 
          MiddleFrame=Frame(Main_Frame,bd=10,bg="black")
          MiddleFrame.place(x=2,y=137,width=915,height=247)
          # Middle Image 1
          middleimg=Image.open("image/dashboard image.png")
          middleimg=middleimg.resize((905,237),Image.AFFINE)
          self.photomiddleimg=ImageTk.PhotoImage(middleimg)
          lbl_middleimg=Label(MiddleFrame,image=self.photomiddleimg)
          lbl_middleimg.place(x=-4.5,y=-4.5,width=905,height=237)
#-------  ----------------------------------------------------------------------------------------------------
          # --------- Search Section --------
          Search_Frame=Frame(Main_Frame,bd=2,bg="black")
          Search_Frame.place(x=923,y=2,width=413,height=38.5)  
          # Bill No Search Frame
          self.lblBill=Label(Search_Frame,font=('Courier New',13,'bold'),bg="black",fg="white",text="Bill No:")
          self.lblBill.grid(row=0,column=0,sticky=W,padx=9,pady=4)
          # Bill No Search Bar
          self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',11,'bold'),width=19)
          self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=5,pady=5)  
          # Bill No Button
          self.BtnSearch=Button(Search_Frame,text="Search",font=('arial black',8,'bold'),bg="white",fg="black",width=10,cursor="hand2")
          self.BtnSearch.grid(row=0,column=2,padx=15,pady=1)  
# ------  --------------------------------#---------------------------------#----------------------------------#      
          # ---------- Right Frame Bill Section ----------------
          RighLabelFrame=LabelFrame(Main_Frame,text="Bill Section:",font=("Courier New",14,"bold"),bg="black",fg="white",bd=6)
          RighLabelFrame.place(x=921,y=45,width=415,height=340)

          scroll_y=Scrollbar(RighLabelFrame,orient=VERTICAL)
          self.textarea=Text(RighLabelFrame,yscrollcommand=scroll_y.set,bg="black",fg="white",font=("Courier New",10,"bold"))
          scroll_y.pack(side=RIGHT,fill=Y)
          scroll_y.config(command=self.textarea.yview)
          self.textarea.pack(fill=BOTH,expand=1)
# ------  ------------------------------------------------------------------------------------------------------
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
# ------  ------------------------------------------------------------------------------------------------------
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
          self.welcome()

        # ============================> Function Declaration <==============================

#  ------------------------------------------ BIll Recipt ------------------------------------------------
    def welcome(self):
          self.textarea.delete(1.0,END)
          self.textarea.insert(END,"\t Welcome Our Restaurant")
          self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
          self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
          self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
          self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

          self.textarea.insert(END,"\n===============================================")
          self.textarea.insert(END,f"\n Prodcut\t\t\tQTY\tPrice")
          self.textarea.insert(END,"\n===============================================")


# -------------------- FUnction of  Categories Section ----------------------------------------------------
    def Categories(self,event=""):
          # 1) BreakFAst
          if self.Combo_Category.get()=="BreakFast":
                self.ComboSubCategory.config(value=self.SubCategoryBreakFast)
                self.ComboSubCategory.current(0)
          # 2) Lunch      
          if self.Combo_Category.get()=="Lunch":
                self.ComboSubCategory.config(value=self.SubCategoryLunch)
                self.ComboSubCategory.current(0)
          # 2) Dinner
          if self.Combo_Category.get()=="Dinner":
                self.ComboSubCategory.config(value=self.SubCategoryDinner)
                self.ComboSubCategory.current(0)
# -------------------------------------- Function of Sub Categories Section ---------------------------------
                # --- ---- Breakfast  Sub Categories name
    def Product_add(self,event=""):
        # 1) Eggs
          if self.ComboSubCategory.get()=="Eggs":
                self.ComboProduct.config(value=self.Eggs)
                self.ComboProduct.current(0)
        # 2) Parathas
          if self.ComboSubCategory.get()=="Parathas":
                self.ComboProduct.config(value=self.Parathas)
                self.ComboProduct.current(0)
        # 3) Tea
          if self.ComboSubCategory.get()=="Tea":
                self.ComboProduct.config(value=self.Tea)
                self.ComboProduct.current(0)
        # 4) Drinks
          if self.ComboSubCategory.get()=="Drinks":
                self.ComboProduct.config(value=self.Drinks)
                self.ComboProduct.current(0)            

                # --- --- Lunch Sub Categories name
        # 4) Salads" 
          if self.ComboSubCategory.get()=="Salads":  
                self.ComboProduct.config(values=self.Salads)
                self.ComboProduct.current(0)  
        # 5 )"Pasta And Noodles
          if self.ComboSubCategory.get()=="Pasta And Noodles":
                self.ComboProduct.config(values=self.PastaAndNoodles)
                self.ComboProduct.current(0) 

                # --- --- Dinner Sub Categories name 
        # 6) Chicken Dishes
          if self.ComboSubCategory.get()=="Chicken Dishes":
                self.ComboProduct.config(values=self.ChickenDishes)
                self.ComboProduct.current(0)
        # 7) Beef Dishes
          if self.ComboSubCategory.get()=="Beef Dishes":
                self.ComboProduct.config(values=self.BeefDishes)
                self.ComboProduct.current(0)
        # 8) Pizza's Varieties
          if self.ComboSubCategory.get()=="Pizza's Varieties":
                self.ComboProduct.config(values=self.PizzaVarieties)
                self.ComboProduct.current(0)
        # 7) Burgers
          if self.ComboSubCategory.get()=="Burgurs":
                self.ComboProduct.config(values=self.Burgurs)
                self.ComboProduct.current(0)
# -------------------- FUnction of  Price Section ----------------------------------------------------
    def price(self,event=""):
          # ================>BreakFast Section Price set Code<==============
          # 1) Eggs
          # i) Half Fry Price set section
          if self.ComboProduct.get()=="Half Fry":
                self.ComboPrice.config(value=self.price_HalfFry)
                self.ComboPrice.current(0)
                self.qty.set(1) 
          # ii) Omlete Price set section
          if self.ComboProduct.get()=="Omlete":
                self.ComboPrice.config(value=self.price_Omlete)
                self.ComboPrice.current(0)
                self.qty.set(1)                   
          # ii) CheeseOmlete Price set section 
          if self.ComboProduct.get()=="Cheese Omlete":
                self.ComboPrice.config(value=self.price_CheeseOmlete)
                self.ComboPrice.current(0)
                self.qty.set(1)                  
          # ii) Cheese HAlfFry Price set section 
          if self.ComboProduct.get()=="Cheese Half Fry":
                self.ComboPrice.config(value=self.price_CheeseHalfFry)
                self.ComboPrice.current(0)
                self.qty.set(1)                 
          
          # 2) Parathas
          # i) Lacha Paratha
          if self.ComboProduct.get()=="Lacha Paratha":
                self.ComboPrice.config(value=self.price_LachaParatha)
                self.ComboPrice.current(0)
                self.qty.set(1)  
          # ii) Aloo Paratha
          if self.ComboProduct.get()=="Aloo Paratha":
                self.ComboPrice.config(value=self.price_AlooParatha)
                self.ComboPrice.current(0)
                self.qty.set(1)  
          # iii) Chicken Paratha
          if self.ComboProduct.get()=="Chicken Paratha":
                self.ComboPrice.config(value=self.price_ChickenParatha)
                self.ComboPrice.current(0)
                self.qty.set(1)  
          # iv) Chicken Cheese Paratha
          if self.ComboProduct.get()=="Chicken Cheese Paratha":
                self.ComboPrice.config(value=self.price_ChickenCheeseParatha)
                self.ComboPrice.current(0)
                self.qty.set(1)  
        
          # 3) Tea 
          # i) Doodh Patti Half
          if self.ComboProduct.get()=="Doodh Patti Half":
                self.ComboPrice.config(value=self.price_DoodhPattiHalf)
                self.ComboPrice.current(0)
                self.qty.set(1)  
          # ii) Doodh patti Full
          if self.ComboProduct.get()=="Doodh Patti Full":
                self.ComboPrice.config(value=self.price_DoodhPattiFull)
                self.ComboPrice.current(0)
                self.qty.set(1)  
          # iii) Green Tea
          if self.ComboProduct.get()=="Green Tea":
                self.ComboPrice.config(value=self.price_GreenTea)
                self.ComboPrice.current(0)
                self.qty.set(1)  
        
          # 4)Drinks
          # i) Cola Next 500ml
          if self.ComboProduct.get()=="Cola Next 500ml":
                self.ComboPrice.config(value=self.price_ColaNext500ml)
                self.ComboPrice.current(0)
                self.qty.set(1)  
          # ii) Cola Next 1liter
          if self.ComboProduct.get()=="Cola Next 1liter":
                self.ComboPrice.config(value=self.price_ColaNext1liter)
                self.ComboPrice.current(0)
                self.qty.set(1)  
          # iii) FizzUp 500ml
          if self.ComboProduct.get()=="FizzUp 500ml":
                self.ComboPrice.config(value=self.price_Fizzup500ml)
                self.ComboPrice.current(0)
                self.qty.set(1)  
          # iv) FizzUp 1liter
          if self.ComboProduct.get()=="FizzUp 1liter":
                self.ComboPrice.config(value=self.price_Fizzup1liter)
                self.ComboPrice.current(0)
                self.qty.set(1)  
          # v) Red Apple 1.5liter
          if self.ComboProduct.get()=="Red Apple 1.5liter":
                self.ComboPrice.config(value=self.price_RedApple)
                self.ComboPrice.current(0)
                self.qty.set(1)  
          # vi) Pakola Water 1.5liter
          if self.ComboProduct.get()=="Pakola Water 1.5liter":
                self.ComboPrice.config(value=self.price_PakolaWater)
                self.ComboPrice.current(0)
                self.qty.set(1)  
          # ====================> LUnch Section Price set Code <==================
          # 1) Salads
          # i) Green Salads 
          if self.ComboProduct.get()=="Green Salads":
                self.ComboPrice.config(value=self.price_GreenSalads)
                self.ComboPrice.current(0)
                self.qty.set(1)       
          # ii) Pasta Salads
          if self.ComboProduct.get()=="Pasta Salads":
                self.ComboPrice.config(value=self.price_PastaSalads)
                self.ComboPrice.current(0)
                self.qty.set(1)
          # iii) Specialty Salads
          if self.ComboProduct.get()=="Specialty Salads":
                self.ComboPrice.config(value=self.price_SpecialtySalads)
                self.ComboPrice.current(0)
                self.qty.set(1)
                
          # 2) Pasta And Noodles
          # i) Italian Pasta 
          if self.ComboProduct.get()=="Italian Pasta":
                self.ComboPrice.config(value=self.price_ItalianPasta)
                self.ComboPrice.current(0)
                self.qty.set(1)
          # ii) Asian Noodles 
          if self.ComboProduct.get()=="Asian Noodles":
                self.ComboPrice.config(value=self.Price_AsianNoodles)
                self.ComboPrice.current(0)
                self.qty.set(1)
          # iii) Fusion Creations
          if self.ComboProduct.get()=="Fusion Creations":
                self.ComboPrice.config(value=self.price_FusionCreations)
                self.ComboPrice.current(0)
                self.qty.set(1) 
         
          # ================>Dinner Section Price set Code<==============
          # 1) Chicken Dishes
          # i) Chicken Qourma
          if self.ComboProduct.get()=="Chicken Qourma":
                self.ComboPrice.config(value=self.price_ChickenQourma)
                self.ComboPrice.current(0)
                self.qty.set(1)  
          # ii) Chicken Nihari 
          if self.ComboProduct.get()=="Chicken Nihari":
                self.ComboPrice.config(value=self.price_ChickenNihari)
                self.ComboPrice.current(0)
                self.qty.set(1) 
          # iii) Chicken Karahi 
          if self.ComboProduct.get()=="Chicken Karahi":
                self.ComboPrice.config(value=self.price_ChickenKarahi)
                self.ComboPrice.current(0)
                self.qty.set(1) 
          # iv) Chicken Biryani 
          if self.ComboProduct.get()=="Chicken Biryani":
                self.ComboPrice.config(value=self.price_ChickenBiryani)
                self.ComboPrice.current(0)
                self.qty.set(1) 
          # v Chicken Puloa    
          if self.ComboProduct.get()=="Chicken Puloa":
                self.ComboPrice.config(value=self.price_ChickenPuloa)
                self.ComboPrice.current(0)
                self.qty.set(1)             
          
          # 2) Beef Dishes
          # i) Beef Qourma
          if self.ComboProduct.get()=="Beef Qourma":
                self.ComboPrice.config(value=self.price_BeefQourma)
                self.ComboPrice.current(0)
                self.qty.set(1)  
          # ii) Beef Nihari 
          if self.ComboProduct.get()=="Beef Nihari":
                self.ComboPrice.config(value=self.price_BeefNihari)
                self.ComboPrice.current(0)
                self.qty.set(1) 
          # iii) Beef Biryani 
          if self.ComboProduct.get()=="Beef Biryani":
                self.ComboPrice.config(value=self.price_BeefBiryani)
                self.ComboPrice.current(0)
                self.qty.set(1) 
          # iv) Beef Puloa      
          if self.ComboProduct.get()=="Beef Puloa":
                self.ComboPrice.config(value=self.price_BeefPuloa)
                self.ComboPrice.current(0)
                self.qty.set(1) 

          # 3) Pizza's Varieties::
          # i) Tikka
          if self.ComboProduct.get()=="Tikka":
                self.ComboPrice.config(value=self.price_Tikka)
                self.ComboPrice.current(0)
                self.qty.set(1)   
          # ii) Fajita 
          if self.ComboProduct.get()=="Fajita":
                self.ComboPrice.config(value=self.price_Fajita)
                self.ComboPrice.current(0)
                self.qty.set(1) 
          # iii) Creamy 
          if self.ComboProduct.get()=="Creamy":
                self.ComboPrice.config(value=self.price_Creamy)
                self.ComboPrice.current(0)
                self.qty.set(1) 
          # 4) Burgurs
          # i) Zinger Burgur 
          if self.ComboProduct.get()=="Zinger Burgur":
                self.ComboPrice.config(value=self.price_ZingerBurgur)
                self.ComboPrice.current(0)
                self.qty.set(1) 
          # ii) Beef Burgur 
          if self.ComboProduct.get()=="Beef Burgur":
                self.ComboPrice.config(value=self.price_BeefBurgur)
                self.ComboPrice.current(0)
                self.qty.set(1) 
          # iii) Double Zinger Burgur
          if self.ComboProduct.get()=="Double Zinger Burgur":
                self.ComboPrice.config(value=self.price_DoubleZingerBurgur)
                self.ComboPrice.current(0)
                self.qty.set(1)  
                
                  
        
        

if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()