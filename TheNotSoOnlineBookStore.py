#The Not So Online Bookstore program

#Completed Milestones/Goals:

# Creates GUI
# Created Homescreen
# Created Sign In and Sign Up pages
# Read in files containing book data
# Displayed Book images correctly when corresponding genre button has been clicked
# Sign In System Completed
# Drop Down Menu Completed
# Sign Up System Completed
# Book Info Display Completed
# Last Seen Completed
# Search Options Completed
# Account Balance System Completed
# Account Delete System Completed
# Quality Of Life Improvements Completed

import random

import tkinter
import tkinter as tk                            #This imports all the needed libraries and software that is being used for the software
from tkinter import *
from tkinter import filedialog

from PIL import ImageTk,Image
from functools import partial
from shutil import copyfile

from Mega_Book_List_Creation import Mega_Book_List           # This reads in two files that create the Mega dictionaries that are then utilsed throughout the code
from Mega_User_List_Creation import Mega_User_List

from Encryption_And_Decryption_Subroutines import Encrypt


class Main_Program():
    def __init__(self,GUI):
        self.GUI = GUI

    def Main_Interface(self):

        def Login():

            for Q in range(0,len(Book_Name_Button_List)):
                Var = Book_Name_Button_List[Q]
                Var.destroy()

                Var2 = Image_Button_List[Q]                                       
                Var2.destroy()
                
            if Z_Index_Position[2] != 0:
                Z_Index_Position[2].destroy()
                Z_Index_Position[3].destroy()

            if Beta_List != "0":
                for x in range(0,len(Beta_List)):                   # This subroutine redirects the user to the Login Screen, whilst removing all images, Search bar and text currently on 
                    Beta_List[x].destroy()                          # the screen
                
            X = Main_Program(self.GUI)
            X.Login_Screen()

            for Q in range(0,len(Book_Name_Button_List)):
                Var = Book_Name_Button_List[Q]
                Var.destroy()

                Var2 = Image_Button_List[Q]
                Var2.destroy()

            if Z_Index_Position[2] != 0:
                Z_Index_Position[2].destroy()
                Z_Index_Position[3].destroy()
                
            Destroy_All()
           
        
        def Destroy_All():

            for x in range(0,len(Genre_Button_List)):                    # Deletes all genre buttons at the top of the page, used by the "Home" and "Sign In" buttons to prevent
                Genre_Button_List[x].destroy()                           # overlap when main program is called again
                                                                         # Theta_List is used to store and thus delete the search button, and search entry bar.
            for x in range(0,len(Theta_List)):
                Theta_List[x].destroy()

            for x in range(0,len(Kappa_List)):
                Kappa_List[x].destroy()
                          
                    
                                    
        def Display_Books(x):
            for n in range(0,len(Kappa_List)):
                Kappa_List[n].destroy()
                
            X = Main_Program(self.GUI)             #Simply singular funtion that directs the user to the relevant subroutine, that presents the books of the chosen genre
            X.Page_Generation(x)                                        

        def Home():
            for Q in range(0,len(Book_Name_Button_List)):
                Var = Book_Name_Button_List[Q]
                Var.destroy()

                Var2 = Image_Button_List[Q]                  #This refreshes the page and rellocates the user back to the home screen
                Var2.destroy()

            if Z_Index_Position[2] != 0:
                Z_Index_Position[2].destroy()
                Z_Index_Position[3].destroy()

            Destroy_All()
            
            X = Main_Program(self.GUI)
            X.Main_Interface()

        def Display_Book_Information(x):

            Destroy_All()

            Last_Saw[0] = True
            X = Main_Program(self.GUI)
            X.Present_Book_Information(x)
            

        def User_Drop_Menu():

            def Destroy_Some():
                for x in range(0,(len(Drop_List)-1)):       #Deletes all the widgets and items on the Drop Down menu
                    Drop_List[x].destroy()

                User_Profile_Pic[3].place_forget()

            def Destroy_Some_More():
                if Z_Index_Position[2] != 0:
                    Z_Index_Position[2].destroy()           #Delete the Images on screen
                    Z_Index_Position[2] = 0

                if Z_Index_Position[3] != 0:
                    Z_Index_Position[3].destroy()
                    Z_Index_Position[3] = 0

                if Book_Name_Button_List:
                    for Q in range(0,len(Book_Name_Button_List)):
                        Var = Book_Name_Button_List[Q]
                        Var.destroy()

                        Var2 = Image_Button_List[Q]
                        Var2.destroy()
                    

            def Sign_Out_Link():
                Destroy_Some()
                Destroy_Some_More()
                Destroy_All()                     # Signs the user out of their account and directs the user back to the main screen
                        
                Logged_In[0] = False
                Z = Main_Program(self.GUI)
                Z.Main_Interface()

            def User_Account_Link():
                Destroy_Some()
                Destroy_Some_More()
                Destroy_All()
                                                                                   #Links the user to the respecive page
                Z = Main_Program(self.GUI)
                Z.User_Account_Interface()

            def User_Account_Bal_Link():
                Destroy_Some()
                Destroy_Some_More()                    # Redirects the user to Account Balance subroutine
                Destroy_All()

                N = Main_Program(self.GUI)
                N.User_Account_Bal_Interface()
                
            def Last_Seen_Link():
                Destroy_Some()
                Destroy_Some_More()          #Redirects the user to their Last Seen Images if they are signed in
                Destroy_All()

                M = Main_Program(self.GUI)
                M.User_Last_Seen_Interface()
                

            if Logged_In[2] == 0:                 #IF Statement used so when the picture is clicked again it closes the drop menu and reopens when clicked again
                Logged_In[2] = 1

                User_Name = User_Dict[Index_Position][3]
                
                Drop_Down_Menu_Label = Label(self.GUI,bg = "grey30", width = 25, height = 40)
                Message_Label = Label(self.GUI, text = User_Name, bg = "grey40", fg = "black",font = ("ComicSans",18,"bold"))

                User_Acc_Button = tk.Button(self.GUI, text = "User Account", bg = "darkorchid4", fg = "gold", font = ("Arial",14), width = 13,command = User_Account_Link, activebackground = "darkorchid4")
                Acc_Bal_Button = tk.Button(self.GUI, text = "Account Balance", bg = "darkorchid4",fg = "gold", font = ("Arial",14),width = 13, command = User_Account_Bal_Link, activebackground = "darkorchid4")
                Last_Seen_Button = tk.Button(self.GUI, text = "Last Seen", bg = "darkorchid4",fg = "gold", font = ("Arial",14),width = 13, command = Last_Seen_Link, activebackground = "darkorchid4")
                Sign_Out_Button = tk.Button(self.GUI,text = "Sign Out", bg = "darkorchid4",fg = "gold", font = ("Arial",14), width = 13,command = Sign_Out_Link, activebackground = "darkorchid4")

                Original = Image.open(User_Dict[Logged_In[1]][1])
                Resized = Original.resize((75,75),Image.ANTIALIAS)
                Photo = ImageTk.PhotoImage(Resized)
                User_Profile_Pic[2] = (Photo)
                Display_User_Image = Label(self.GUI, image = Photo ,bg = "red",activebackground = "darkorchid")
                User_Profile_Pic[3] = Display_User_Image

                Drop_List.append(Drop_Down_Menu_Label)
                Drop_List.append(Message_Label)                        #Creates a drop down menu, containing the following buttons: User Account, Account Balance, Last Seen and Sign Out
                Drop_List.append(User_Acc_Button)
                Drop_List.append(Acc_Bal_Button)
                Drop_List.append(Last_Seen_Button)
                Drop_List.append(Sign_Out_Button)
                Drop_List.append(User_Profile_Pic[3])

                Drop_Down_Menu_Label.place(rely = 0.085, relx = 0.880)
                User_Profile_Pic[3].place(rely = 0.1, relx = 0.885)
                Message_Label.place(relx = 0.885, rely = 0.2)
                User_Acc_Button.place(relx = 0.888, rely = 0.3)
                Acc_Bal_Button.place(relx = 0.888, rely = 0.35)
                Last_Seen_Button.place(relx = 0.888, rely = 0.4)
                Sign_Out_Button.place(relx = 0.888, rely =0.55)

            else:
                Destroy_Some()
                Logged_In[2] = 0

        def Search():                                
                
            Looking_For = Search_Entry.get()               #Destroy's all images and text on screen and redirects the user to the Search Books subroutine
            Destroy_All()

            X = Main_Program(self.GUI)
            X.Search_Books(Looking_For)
            
        

        Search_Button = tk.Button(self.GUI,text = "Search", bg = "goldenrod", fg = "black", font = ("Comic Sans", 20,"bold","italic"),activebackground = "red4",command = Search)
        Search_Button.place(rely = 0.01, relx = 0.15, height = 45)
        Search_Entry = tk.Entry(self.GUI,bg = "white", font = ("Arial",20))
        Search_Entry.place(rely = 0.01, relx = 0.24, height = 45,width = 700)

        Theta_List.append(Search_Button)
        Theta_List.append(Search_Entry)

        Horror_Button = tk.Button(self.GUI,text = "Horror", fg = "black",font = ("Arial",16), activebackground = "red", bg = "darkturquoise", command = partial(Display_Books,"Horror"))
        Fantasy_Button = tk.Button(self.GUI,text = "Fantasy", fg = "black",font = ("Arial",16), activebackground = "red", bg = "darkturquoise", command = partial(Display_Books,"Fantasy"))
        SciFi_Button =  tk.Button(self.GUI,text = "Sci-Fi", fg = "black",font = ("Arial",16), activebackground = "red", bg = "darkturquoise", command = partial(Display_Books,"SciFi"))
        Non_Fiction_Button= tk.Button(self.GUI,text = "Non-Fiction", fg = "black",font = ("Arial",16), activebackground = "red", bg = "darkturquoise", command = partial(Display_Books,"Non-Fiction"))
        Crime_Mystery_Button= tk.Button(self.GUI,text = "Crime/Mystery", fg = "black",font = ("Arial",16), activebackground = "red", bg = "darkturquoise", command =partial(Display_Books,"Crime/Mystery"))
        Political_Fiction_Button= tk.Button(self.GUI,text = "Political Fiction", fg = "black",font = ("Arial",16), activebackground = "red", bg = "darkturquoise", command = partial(Display_Books,"Political Fiction"))
        Historical_Fiction_Button= tk.Button(self.GUI,text = "Historical Fiction", fg = "black",font = ("Arial",16), activebackground = "red", bg = "darkturquoise", command = partial(Display_Books,"Historical"))
        Action_Button= tk.Button(self.GUI,text = "Action", fg = "black",font = ("Arial",16), activebackground = "red", bg = "darkturquoise", command = partial(Display_Books,"Action"))
        Tragedy_Button= tk.Button(self.GUI,text = "Tragedy", fg = "black",font = ("Arial",16), activebackground = "red", bg = "darkturquoise", command = partial(Display_Books,"Tragedy"))
        Random_Book_Button = tk.Button(self.GUI,text = "Random", fg ="black", font = ("Arial",16),activebackground = "red",bg = "medium aquamarine", command = partial(Display_Books,"Random"))

        Drama_Button = tk.Button(self.GUI, text = "Drama", fg = "black", bg = "darkturquoise", activebackground = "red", font = ("Arial",16),command = partial(Display_Books,"Drama"))
        Adventure_Button = tk.Button(self.GUI, text = "Adventure", fg = "black", bg ="darkturquoise", activebackground = "red", font = ("Arial",16),command = partial(Display_Books,"Adventure"))
        Comedy_Button = tk.Button(self.GUI, text = "Comedy", fg = "black", bg = "darkturquoise", activebackground = "red", font = ("Arial",16), command = partial(Display_Books,"Comedy"))
        Thriller_Button = tk.Button(self.GUI, text = "Thriller", fg = "black", bg = "darkturquoise", activebackground = "red", font = ("Arial",16), command = partial(Display_Books,"Thriller"))
        Supernatural_Button = tk.Button(self.GUI, text = "Supernatural", fg = "black", bg = "darkturquoise", activebackground = "red", font = ("Arial",16), command = partial(Display_Books,"Supernatural"))
        Romance_Button = tk.Button(self.GUI, text = "Romance", fg = "black", bg = "darkturquoise", activebackground = "red", font = ("Arial",16), command = partial(Display_Books,"Romance"))
        

        Home_Button = tk.Button(self.GUI, text = "Home", fg = "black", bg = "medium aquamarine", activebackground = "red", font = ("Arial",16,"bold","italic"), command = Home)
        
        Genre_Button_List.append(Horror_Button)
        Genre_Button_List.append(Fantasy_Button)
        Genre_Button_List.append(SciFi_Button)
        Genre_Button_List.append(Non_Fiction_Button)
        Genre_Button_List.append(Crime_Mystery_Button)
        Genre_Button_List.append(Political_Fiction_Button)
        Genre_Button_List.append(Historical_Fiction_Button)
        Genre_Button_List.append(Action_Button)                         # This adds all the genre buttons to a singular list
        Genre_Button_List.append(Tragedy_Button)                        # This list is then used to destroy all the buttons rather than repeat a long statement similar to this
        Genre_Button_List.append(Random_Book_Button)                    # each time
        Genre_Button_List.append(Drama_Button)
        Genre_Button_List.append(Adventure_Button)
        Genre_Button_List.append(Comedy_Button)
        Genre_Button_List.append(Thriller_Button)
        Genre_Button_List.append(Supernatural_Button)
        Genre_Button_List.append(Romance_Button)
        Genre_Button_List.append(Home_Button)
        
        Home_Button.place(relx = 0.0, rely = 0.085)
        Horror_Button.place(relx = 0.1135, rely = 0.145)
        Fantasy_Button.place(relx = 0.05,rely = 0.085)
        SciFi_Button.place(relx = 0.1115, rely= 0.085)
        Action_Button.place(relx = 0.15875, rely = 0.085)
        Tragedy_Button.place(relx = 0.2085, rely = 0.085)
        
        Drama_Button.place(relx = 0.2695, rely = 0.085)
        Adventure_Button.place(relx = 0.32175, rely = 0.085)
        Comedy_Button.place(relx = 0.3945, rely = 0.085)
        Thriller_Button.place(relx = 0.4565, rely = 0.085)                    #Allocation fo all the genre buttons
        Supernatural_Button.place(relx = 0.50825, rely = 0.085)
        Romance_Button.place(relx = 0.59725, rely = 0.085)

        Non_Fiction_Button.place(relx = 0.665, rely = 0.085)
        Crime_Mystery_Button.place(relx = 0.746, rely = 0.085)
        Political_Fiction_Button.place(relx = 0.8465, rely = 0.085)
        Historical_Fiction_Button.place(relx = 0.0, rely = 0.145)
        Random_Book_Button.place(relx = 0.1635, rely = 0.145)
        
                
        if Logged_In[0] == True:                                   

            Index_Position = Logged_In[1]                #Checks if the user is logged in, and if so displays the user's account balance and profile picture

            Photo = [0]

            Original = Image.open(User_Dict[Logged_In[1]][1])
            Resized = Original.resize((55,55),Image.ANTIALIAS)
            Photo[0] = ImageTk.PhotoImage(Resized)
            User_Profile_Pic[0] = Photo[0]
            Display_User_Image = tkinter.Button(self.GUI, image = Photo,bg = "hotpink",activebackground = "darkorchid", command = User_Drop_Menu)
            User_Profile_Pic[1] = Display_User_Image
            
            User_Profile_Pic[1].place(relx = 0.95, rely = 0.005)

            User_Bal = "Balance: "+str(User_Dict[Logged_In[1]][4])+" Coin"
            User_Bal_Label = Label(self.GUI,text = User_Bal, bg = "green4",fg = "Black",font = ("Comic Sans",18,"bold"), width = 25)
            User_Bal_Label.place(relx = 0.70,rely = 0.015)

            Theta_List.append(User_Profile_Pic[1])

            Theta_List.append(User_Bal_Label)
            
        else:
            Sign_In_Button = tk.Button(self.GUI,text = "Sign In",bg = "grey50", fg = "black",font = ("Comic Sans",18,"bold"),command = Login)
            Sign_In_Button.place(rely=0.01,relx = 0.92, height = 45)
            Beta_List.append(Sign_In_Button)                                      # If the user is not logged in, then it will show a sign out button instead of the user's profile picture
            Theta_List.append(Sign_In_Button)


        Original_Ad1 = Image.open("E:\\NEA_USB\\Front_Page_And_Logos\\Ad_Space_JoshsJingles.jpg")                
        Resized_Ad1 = Original_Ad1.resize((300,150),Image.ANTIALIAS)
        Lambda_List[0] = ImageTk.PhotoImage(Resized_Ad1)
        Ad_Space_1 = Label(self.GUI,image = Lambda_List[0],bg = "grey14")
        Kappa_List.append(Ad_Space_1)
        
        Original_Ad2 = Image.open("E:\\NEA_USB\\Front_Page_And_Logos\\Ad_Space_LidjCook.jpg")
        Resized_Ad2 = Original_Ad2.resize((300,150),Image.ANTIALIAS)
        Lambda_List[1] = ImageTk.PhotoImage(Resized_Ad2)
        Ad_Space_2 = Label(self.GUI,image = Lambda_List[1],bg = "grey14")
        Kappa_List.append(Ad_Space_2)

        Original_Ad3 = Image.open("E:\\NEA_USB\\Front_Page_And_Logos\\Ad_Space_HolyFeather.jpg")
        Resized_Ad3 = Original_Ad3.resize((300,150),Image.ANTIALIAS)
        Lambda_List[2] = ImageTk.PhotoImage(Resized_Ad3)
        Ad_Space_3 = Label(self.GUI,image = Lambda_List[2],bg = "grey40")
        Kappa_List.append(Ad_Space_3)

        if Logged_In[0] == "":
            Original_Offer = Image.open("E:\\NEA_USB\\Front_Page_And_Logos\\Offer.jpg")
            Resized_Offer = Original_Offer.resize((900,400),Image.ANTIALIAS)
            Lambda_List[3] = ImageTk.PhotoImage(Resized_Offer)
            Offer_Button = tk.Button(self.GUI,image = Lambda_List[3],bg = "grey10",activebackground = "red4",command = Login)
            Kappa_List.append(Offer_Button)

        App_Description = "Welcome to BookWorm!" + "\n"+ "\n" + "This site is allows you to reserve a book from your local library!"
        Description_Of_App = Message(self.GUI,text = App_Description,bg = "grey20",fg = "goldenrod",font = ("Arial",28,"bold"),width = 250)
        Kappa_List.append(Description_Of_App)

        Creator_Label = Label(self.GUI,text = "Created by Nathan Horder for NEA Coursework 2020-2021",bg = "black",fg = "darkorchid4", font = ("Comic Sans",18,"bold"))
        Kappa_List.append(Creator_Label)
            
        Original_Book1 = Image.open("E:\\NEA_USB\\Book_Images\\TheBeginningAfterTheEndEarlyYearsBook1.jpg")
        Resized_Book1 = Original_Book1.resize((150,200),Image.ANTIALIAS)                                                             # This Section creates the front page of the software
        Lambda_List[4] = ImageTk.PhotoImage(Resized_Book1)                                                                           # This section displays all the relevant images and sizes them
        Book1 = tk.Button(self.GUI,image = Lambda_List[4],bg = "grey14",command = partial(Display_Book_Information,1))
        Kappa_List.append(Book1)

        Original_Book2 = Image.open("E:\\NEA_USB\\Book_Images\\TheTempest.jpg")
        Resized_Book2 = Original_Book2.resize((150,200),Image.ANTIALIAS)
        Lambda_List[5] = ImageTk.PhotoImage(Resized_Book2)
        Book2 = tk.Button(self.GUI,image = Lambda_List[5],bg = "grey14",command = partial(Display_Book_Information,47))
        Kappa_List.append(Book2)

        Original_Book3 = Image.open("E:\\NEA_USB\\Book_Images\\DiaryOfAWimpyKid.jpg")
        Resized_Book3 = Original_Book3.resize((150,200),Image.ANTIALIAS)
        Lambda_List[6] = ImageTk.PhotoImage(Resized_Book3)
        Book3 = tk.Button(self.GUI,image = Lambda_List[6],bg = "grey14", command = partial(Display_Book_Information,53))
        Kappa_List.append(Book3)

        Original_Book4 = Image.open("E:\\NEA_USB\\Book_Images\\OneOfUsIsLying.jpg")
        Resized_Book4 = Original_Book4.resize((150,200),Image.ANTIALIAS)
        Lambda_List[7] = ImageTk.PhotoImage(Resized_Book4)
        Book4 = tk.Button(self.GUI,image = Lambda_List[7],bg = "grey14", command = partial(Display_Book_Information,21))
        Kappa_List.append(Book4)

        Original_Book5 = Image.open("E:\\NEA_USB\\Book_Images\\Stalingrad.jpg")
        Resized_Book5 = Original_Book5.resize((150,200),Image.ANTIALIAS)
        Lambda_List[8] = ImageTk.PhotoImage(Resized_Book5)
        Book5 = tk.Button(self.GUI,image = Lambda_List[8],bg = "grey14", command = partial(Display_Book_Information,19))
        Kappa_List.append(Book5)

        Top_5_Books = Label(self.GUI,text = "Top 5 Recommended Reads!",bg = "purple",fg = "goldenrod",font = ("Arial",18,"bold"))
        Kappa_List.append(Top_5_Books)

        Original_Logo = Image.open("E:\\NEA_USB\\Front_Page_And_Logos\\Bookworm_Logo.jpg")
        Resized_Logo = Original_Logo.resize((400,200), Image.ANTIALIAS)
        Lambda_List[9] = ImageTk.PhotoImage(Resized_Logo)
        BookWorm_Logo = Label(self.GUI,image = Lambda_List[9], bg = "grey14")
        Kappa_List.append(BookWorm_Logo)

        
        Description_Of_App.place(relx = 0.75,rely = 0.45)
        BookWorm_Logo.place(relx = 0.75,rely = 0.20)
        Ad_Space_1.place(relx = 0.015,rely = 0.25)
        Ad_Space_2.place(relx = 0.015,rely = 0.45)
        Ad_Space_3.place(relx = 0.015,rely = 0.65)
        
        if Logged_In[0] == "":
            Offer_Button.place(relx = 0.25,rely = 0.20)
            
        Creator_Label.place(relx = 0.0,rely = 0.95)                   #This part allocates and actually displays the buttons, labels and images defined above
        Top_5_Books.place(relx = 0.25,rely = 0.65)
        Book1.place(relx = 0.25,rely = 0.7)
        Book2.place(relx = 0.35,rely = 0.7)
        Book3.place(relx = 0.45,rely = 0.7)
        Book4.place(relx = 0.55,rely = 0.7)
        Book5.place(relx = 0.65,rely = 0.7)
                


    def Page_Generation(self,Genre):

        def Next_Page():
            
            if Z_Index_Position[0] <= len(Index_List):
                Z = Z_Index_Position[0]
                Z_Index_Position[0] = Z + 10                      # Increases the base index, allowing the next 10 photos to be displayed
                Button_And_Label_Creation()
            else:
                Z_Index_Position[2].destroy()
                Z_Index_Position[2] = 0


        def Last_Page():
            if Z_Index_Position[0] >= 10:
                Z = Z_Index_Position[0]                  # Decreases the base index, allowing the previous 10 photos to be displayed
                Z_Index_Position[0] = Z-10
                Button_And_Label_Creation()

            else:
                Z_Index_Position[3].destroy()
                Z_Index_Position[3] = 0

        def Show_Book_Info(Z):

            for Q in range(0,len(Book_Name_Button_List)):
                Var = Book_Name_Button_List[Q]
                Var.destroy()

                Var2 = Image_Button_List[Q]
                Var2.destroy()

            Z_Index_Position[2].destroy()                  # When an image or button relating to a book is pressed, this is called and redirects the user
            Z_Index_Position[3].destroy()                  #to a page that displays all the information regarding the book (Name, Author, Price, ect)

            for x in range(0,len(Genre_Button_List)):
                Genre_Button_List[x].destroy()

            for x in range(0,len(Theta_List)):
                Theta_List[x].destroy()
                    

            X = Main_Program(self.GUI)
            
            X.Present_Book_Information(Z)
            

        def Button_And_Label_Creation():               #Creates all the images and labels of the books on screen
            
            if Z_Index_Position[2] == 0:

                Next_Page_Button = tk.Button(self.GUI, text = "Next Page", command = Next_Page, fg = "gold", bg = "green4",font = ("Comic sans",18, "bold"), activebackground = "red")
                Z_Index_Position[2] = Next_Page_Button
                Next_Page_Button.place(relx = 0.9,rely = 0.925)

            if Z_Index_Position[3] == 0:
                Last_Page_Button = tk.Button(self.GUI, text = "Previous Page", command = Last_Page, fg = "gold", bg = "green4",font = ("Comic sans",18, "bold"), activebackground = "red")
                Z_Index_Position[3] = Last_Page_Button
                Last_Page_Button.place(relx = 0.01, rely =0.925)
            
            
            for Q in range(0,len(Book_Name_Button_List)):
                Var = Book_Name_Button_List[Q]
                Var.destroy()

                Var2 = Image_Button_List[Q]    #Might make it so it carrys Book_Dict[List[x]][2] across then use a loop to cross reference with the dictionary to find the original index
                Var2.destroy()                 #Then use the index as a new varible to display the relevant information.

            
            
            for x in range(Z_Index_Position[0],len(Index_List)):
                
                Temp = Book_Dict[Index_List[x]][2]
                

                if x <= (Z_Index_Position[0]+4):
                
                    Original = Image.open(Book_Dict[Index_List[x]][1])
                    Resized = Original.resize((150,200), Image.ANTIALIAS)                  #Nested Subroutine for the creation of the images and their name tag buttons
                    Photo = ImageTk.PhotoImage(Resized) 

                    Photo_List.append(Photo)
                    
                    Image_Button = tk.Button(self.GUI, image = Photo,command =partial(Show_Book_Info,x),activebackground = "red4", bg = "red4")
                    Image_Button.place(relx = XCords[x- Z_Index_Position[0]], rely = 0.225)

                    Image_Button_List.append(Image_Button)

                    Book_Name_Button = tk.Button(self.GUI, text = Book_Dict[Index_List[x]][2], bg = "grey50",fg = "black",font = ("Arial",16),command = partial(Show_Book_Info,x),activebackground = "red4")
                    Book_Name_Button.place(relx = LabelXCords[x - Z_Index_Position[0]], rely = 0.485)

                    Book_Name_Button_List.append(Book_Name_Button)

                elif x > (Z_Index_Position[0]+4) and x <= (Z_Index_Position[0]+9):
                    

                    Original = Image.open(Book_Dict[Index_List[x]][1])
                    Resized = Original.resize((150,200), Image.ANTIALIAS)
                    Photo = ImageTk.PhotoImage(Resized)

                    Photo_List.append(Photo)                                                           #Used to limit the number of books displayed to a maximum of 10
                                                                                                       #Limit is required as over 10 books would not all fit on the page
                    Image_Button = tk.Button(self.GUI, image = Photo,command = partial(Show_Book_Info,x),activebackground = "red4", bg = "red4")
                    Image_Button.place(relx = XCords[x-5 - Z_Index_Position[0]], rely = 0.55)

                    Image_Button_List.append(Image_Button)

                    Book_Name_Button = tk.Button(self.GUI, text = Book_Dict[Index_List[x]][2], bg = "grey50",fg = "black",font = ("Arial",16),command = partial(Show_Book_Info,x),activebackground = "red4")
                    Book_Name_Button.place(relx = LabelXCords[x- Z_Index_Position[0]-5], rely = 0.85)

                    Book_Name_Button_List.append(Book_Name_Button)

            
        Length_List = Book_Genre_List

        global Index_List
        Index_List = []
        
        if Genre == "Random":
            
            Index_List = []
            for x in range(0,len(Length_List)):
                Var = random.randint(0,(len(Length_List)-1))     #If  this clicked, it creates a list of randomly chosen books that is then displayed, when the subroutine is later called
                if Var not in Index_List:
                    Index_List.append(Var)
            
        else:
            Index_List = []
            for x in range(0,len(Book_Genre_List)):
                if Genre in Book_Genre_List[x]:
                    Index_List.append(x)

        Image_Location = []
        
        for z in range(0,len(Book_Dict)):
            Var = Book_Dict[z][1]
            Image_Location.append(Var)


        global Photo_List
        Photo_List = []
        

        XCords = [0.05,0.25, 0.45, 0.65, 0.85]
        LabelXCords = [0.025, 0.225,0.425,0.625,0.825]

        if Z_Index_Position[2] != 0:
            Z_Index_Position[2].destroy()
            Z_Index_Position[2] = 0

        if Z_Index_Position[3] !=0:
            Z_Index_Position[3].destroy()
            Z_Index_Position[3] = 0


        Z_Index_Position[0] = 0
        Button_And_Label_Creation()                                     

    def Present_Book_Information(self,x):

        def Return_To_Page():

            for x in range(0,len(Beta_List)):
                Beta_List[x].destroy()

            Last_Saw[0] = "False"

            Alpha = Main_Program(self.GUI)            # A return button that return the user to the main screen.
            Alpha.Main_Interface()

        def Purchase_Book():

            def Purchase_Confirmed(x):

                def Purchase_Completed():
                    Purchase_Complete_Label.destroy()
                    
                    X = Main_Program(self.GUI)                 #Creates a confirmation screen, allowing the user to decide whether to purchase the book or not
                    X.Main_Interface()
 
                if Last_Saw[1] == "False":
                    
                    Funds_After_Purchase = int(int(User_Dict[Logged_In[1]][4]) - int(Book_Dict[x][4])) 

                else:
                    Funds_After_Purchase = int(int(User_Dict[Logged_In[1]][4]) - int(Book_Dict[x][4]))
                    Last_Saw[1] = "False"

                
                    
                User_Dict[Logged_In[1]][4] = Funds_After_Purchase

                for x in range(0,len(Beta_List)):
                    Beta_List[x].destroy()
                

                Old_Data = open("E:\\NEA_USB\\User_Info\\User_Account_Bal.txt","w")
                Old_Data.truncate()
                Old_Data.close()                                                               #Changes users balance and directly modifies the file containing all the user balances

                for Z in range(0,len(User_Dict)):
                    item = str(User_Dict[Z][4]) + "\n"
                    with open("E:\\NEA_USB\\User_Info\\User_Account_Bal.txt","a") as f:
                        f.write(item)
                f.close()

                for X in range(0,len(Gamma_List)):
                   Gamma_List[X].destroy()

                for x in range(0,len(Theta_List)):
                        Theta_List[x].destroy()

                Purchase_Complete_Label = Label(self.GUI, text = "Purchase Completed",bg = "lawngreen",fg = "black",font = ("Arial",18))
                Purchase_Complete_Label.pack()
                self.GUI.after(1000,Purchase_Completed)
                
            def Purchase_Cancelled():

                for x in range(0,len(Gamma_List)):              #Cancels the purchase and erases the confirmation labels
                    Gamma_List[x].destroy()

            
            def Erase_Label():
                Insuffient_Funds_Label.destroy()

            
            if Last_Saw[0] == "False":               
                
                Price = int(Book_Dict[Index_List[x]][4])
                User_Bal = int( User_Dict[Logged_In[1]][4])

            else:
                Price = int(Book_Dict[x][4])
                User_Bal = int(User_Dict[Logged_In[1]][4])
                Last_Saw[0] = "False"
            
            if (User_Bal - Price) > 0 or (User_Bal - Price) == 0:
                
                Confirm_Purchase_Button = tk.Button(self.GUI,text = "Click to Confirm Purchase",bg = "green4",fg = "black",font = ("Arial",18,"bold","italic"),activebackground = "red",command = partial(Purchase_Confirmed,x))
                Cancel_Purchase_Button = tk.Button(self.GUI,text = "Cancel Purchase",bg = "red4",fg = "black",font = ("Comic Sans",20,"bold"),activebackground = "red",command = Purchase_Cancelled)

                Confirm_Purchase_Button.place(rely = 0.325,relx = 0.35)
                Cancel_Purchase_Button.place(rely = 0.425, relx = 0.35)

                Gamma_List.append(Confirm_Purchase_Button)
                Gamma_List.append(Cancel_Purchase_Button)

            else:
                Insuffient_Funds_Label = Label(self.GUI,text = "Insuffient Funds",font = ("Papyrus",24,"bold","italic"),bg = "red4",fg = "white")
                Insuffient_Funds_Label.pack()
                self.GUI.after(1000,Erase_Label)             

        global Last_Saw

        if Logged_In[0] == True:
            Book_Purchase_Button = tk.Button(self.GUI,text = "Purchase",bg = "darkgreen",fg = "black",font = ("Akaya Telivigala",14,"bold","italic"),width = 10,activebackground = "lawngreen",command = Purchase_Book)
            Book_Purchase_Button.place(relx = 0.35, rely = 0.325)
            Beta_List.append(Book_Purchase_Button)
            

        Return_Button = tk.Button(self.GUI,text = "Return",bg = "grey50",fg = "black", font = ("Comic Sans",18,"bold"),activebackground = "red", command = Return_To_Page)
        Return_Button.place(rely = 0.085, relx = 0.0)
        
        
        if Last_Saw[0] == "False":        # This is needed as if it was last seen, it takes a different x value and Index_List is not needed
        
            Original = Image.open(Book_Dict[Index_List[x]][1])
            Resized = Original.resize((400,650),Image.ANTIALIAS)
            Photo = ImageTk.PhotoImage(Resized)
            Photo_List.append(Photo)
            
            Image_Label = Label(self.GUI,image = Photo)                     #Display's the books information
            Beta_List.append(Image_Label)
            Image_Label.place(relx = 0.075,rely = 0.125)

            Book_Name_Label = Label(self.GUI,text = Book_Dict[Index_List[x]][2], bg = "cyan",fg= "black",font = ("Alfa Slab One",24,"bold","italic"),width = 28)
            Book_Name_Label.place(relx = 0.35, rely = 0.15)
            Beta_List.append(Book_Name_Label)

            Book_Description = Message(self.GUI,text = Book_Dict[Index_List[x]][5], bg = "grey50",fg = "black", font = ("Arial",18),width = 900)
            Book_Description.place(rely = 0.45,relx = 0.35)

            Price_Label_Text = "Price: "+Book_Dict[Index_List[x]][4]+ " Coin"

            Book_Price_Label = Label(self.GUI,text = Price_Label_Text,bg = "darkorchid4",fg = "goldenrod",font = ("Akaya Telivigala",18,"bold"))
            Book_Price_Label.place(relx = 0.35, rely = 0.275)

            Author_Text = "Author: "+ Book_Dict[Index_List[x]][3]
            Author_Label = Label(self.GUI,text = Author_Text,bg = "cadetblue", fg = "black",font = ("Alfa Slab One",20,"italic"))
            Author_Label.place(rely = 0.205,relx = 0.35)

        else:

            Original = Image.open(Book_Dict[x][1])
            Resized = Original.resize((400,650),Image.ANTIALIAS)
            Photo = ImageTk.PhotoImage(Resized)
            Photo_List.append(Photo)

            Image_Label = Label(self.GUI,image = Photo)         #Displays book information, if it was last seen
            Beta_List.append(Image_Label)
            Image_Label.place(relx = 0.075,rely = 0.125)

            Book_Name_Label = Label(self.GUI,text = Book_Dict[x][2], bg = "cyan",fg= "black",font = ("Alfa Slab One",24,"bold","italic"),width = 28)
            Book_Name_Label.place(relx = 0.35, rely = 0.15)
            Beta_List.append(Book_Name_Label) 

            Book_Description = Message(self.GUI,text = Book_Dict[x][5], bg = "grey50",fg = "black",font = ("Arial",18),width = 900)
            Book_Description.place(rely = 0.45,relx = 0.35)

            Price_Label_Text = "Price: "+Book_Dict[x][4]+ " Coin"

            Book_Price_Label = Label(self.GUI,text = Price_Label_Text,bg = "darkorchid4",fg = "goldenrod",font = ("Akaya Telivigala",18,"bold"))
            Book_Price_Label.place(relx = 0.35, rely = 0.275)

            Author_Text = "Author: "+ Book_Dict[x][3]
            Author_Label = Label(self.GUI,text = Author_Text,bg = "cadetblue", fg = "black",font = ("Alfa Slab One",20,"italic"))
            Author_Label.place(rely = 0.205,relx = 0.35)
        
        if Logged_In[0] == "True":
            Book_Purchase_Button = tk.Button(self.GUI,text = "Purchase",bg = "darkgreen",fg = "black",font = ("Akaya Telivigala",14,"bold","italic"),width = 10,activebackground = "lawngreen",command = Purchase_Book)
            Book_Purchase_Button.place(relx = 0.35, rely = 0.325)
            Beta_List.append(Book_Purchase_Button)

        Beta_List.append(Author_Label)
        Beta_List.append(Return_Button)
        Beta_List.append(Book_Price_Label)
        Beta_List.append(Book_Description)

        if Logged_In[0] == True:

            Account_Bal_Text = "Balance: "+ str(User_Dict[Logged_In[1]][4])
            Account_Bal_Label = Label(self.GUI,text = Account_Bal_Text,bg = "green3",fg = "black",font = ("Arial",18))
            Account_Bal_Label.place(rely = 0.085,relx = 0.75)
            Theta_List.append(Account_Bal_Label)

            if Last_Saw[0] == "False":
                User_Dict[Logged_In[1]][5] = User_Dict[Logged_In[1]][5]+","+(Book_Dict[Index_List[x]][2])      #If the user is logged in, it prints the user's account balance

            else:
                User_Dict[Logged_In[1]][5] = User_Dict[Logged_In[1]][5]+","+(Book_Dict[x][2])

            Last_Seen_UnOrdered_String = (User_Dict[Logged_In[1]][5])
            Last_Seen_Unordered = Last_Seen_UnOrdered_String.split(",")
            
            for X in range(0,len(Last_Seen_Unordered)):
                if Last_Seen_Unordered[X] == '':
                    Last_Seen_Unordered.remove(Last_Seen_Unordered[X])                         # This bit reads the singular line that contains all last seen for said user into a 
                                                                                               # dictionary
            if len(Last_Seen_Unordered) > 5:
                for X in range(0,(len(Last_Seen_Unordered)-5)):                               
                    Last_Seen_Unordered.pop(X)

            Last_Seen_Length_Update = Last_Seen_Unordered[0]
            for X in range(1,len(Last_Seen_Unordered)):                                            #This part makes sure that the number of last seen books in this list does not exceed 5
                Last_Seen_Length_Update = Last_Seen_Length_Update + "," + Last_Seen_Unordered[X]   # This is to prevent the file from getting infintly large and using all the space on
                                                                                                   # the clients computer, so having it shorten to 5 allows the Last Seen subroutine to work
            User_Dict[Logged_In[1]][5] = Last_Seen_Length_Update                                   # and makes the total file size small instead of infinitly large
            
            Old_Data = open("E:\\NEA_USB\\User_Info\\User_Last_Seen.txt","w")
            Old_Data.truncate()
            Old_Data.close()

            for X in range(0,len(User_Dict)):
                item = User_Dict[X][5]
                with open("E:\\NEA_USB\\User_Info\\User_Last_Seen.txt","a") as f:
                    f.write(item)
                    f.write("\n")
            f.close()     
        
    def Login_Screen(self):

        def Destroy_All():
            Username_Label.destroy()
            Enter_Username.destroy()
            Password_Label.destroy()
            Enter_Password.destroy()
            Login_Button.destroy()                                       #Erases Buttons and Labels on the Login page
            Or_Label.destroy()
            Create_Account_Button.destroy()
            Return_Button.destroy()

        def Check_Username_Password(Username,Password):

            def Incorrect_Username_Password_Noticed():
                Incorrect_Label.destroy()

            Username_Array = []
            Password_Array = []

            for x in range(0,len(User_Dict)):
                Username_Array.append(User_Dict[x][0])
                Password_Array.append(User_Dict[x][2])
            
            if Username in Username_Array:
                Found = False
                for x in range(0,len(Username_Array)):
                    if Username == Username_Array[x] and Password == Password_Array[x]:         #Checks to see if the password and username are in the system and are connected
                        Found = True

                        Logged_In[0] = True
                        
                        Logged_In[1] = x

                        Destroy_All()
                        R = Main_Program(self.GUI)
                        R.Main_Interface()
                        
                if Found == False:
                    Incorrect_Label = tk.Button(self.GUI,text = "Incorrect Username or Password", font = ("Comic Sans","24","bold"),bg = "red4", fg = "black",activebackground = "red", command = Incorrect_Username_Password_Noticed)
                    Incorrect_Label.place(relx = 0.30, rely = 0.125)
                    
            else:
                Incorrect_Label = tk.Button(self.GUI,text = "Incorrect Username or Password", font = ("Comic Sans","24","bold"),bg = "red4", fg = "black",activebackground = "red", command = Incorrect_Username_Password_Noticed)
                Incorrect_Label.place(relx = 0.30, rely = 0.125)
                

        def Retrieve_Login():
            Username = Enter_Username.get()
            Password = Enter_Password.get()
            Check_Username_Password(Username,Password)

        def Sign_Up():
            Destroy_All()
            R = Main_Program(self.GUI)
            R.Account_Creation()

        def Return():
            Destroy_All()
            X = Main_Program(self.GUI)
            X.Main_Interface()

        Username_Label = Label(self.GUI,text = "Enter Username: ", font = ("Arial",18),bg = "Navy",fg = "white")
        Username_Label.place(rely = 0.1, relx = 0.4)
        Enter_Username = tk.Entry(self.GUI,font = ("Arial",18), bg = "grey40")
        Enter_Username.place(rely = 0.15,relx = 0.4)

        Password_Label = Label(self.GUI,text = "Enter Password: ",font = ("Arial",18),bg = "Navy",fg = "white")     # Allows the user to sign into their account or create one
        Password_Label.place(rely =0.2,relx =0.4)                                                                                       
        Enter_Password = tk.Entry(self.GUI, font = ("Arial",18), bg = "grey40", show = "*")
        Enter_Password.place(rely = 0.25,relx =0.4)

        Login_Button = tk.Button(self.GUI,text = "Login", bg = "green",font = ("Arial",16),command = Retrieve_Login, activebackground = "red")
        Login_Button.place (rely = 0.3,relx =0.4)

        Or_Label = Label(self.GUI,text = "or", bg = "blue", fg = "black", font = ("Comic Sans",18))
        Or_Label.place(rely = 0.375,relx = 0.48)

        Create_Account_Button = tk.Button(self.GUI,text = "Create an Account",bg = "grey50",fg = "black", font = ("Comic Sans",18,"bold"),command = Sign_Up, activebackground = "red")
        Create_Account_Button.place(rely = 0.45,relx =0.41)

        Return_Button = tk.Button(self.GUI,text = "Return", bg = "blue", fg = "black", font = ("Arial",18,"bold"), command = Return,activebackground = "red")
        Return_Button.place(rely = 0.085,relx = 0.0)

    def Account_Creation(self):

        def Destroy_All():
            Username_Label_C.destroy()
            Entry_Username_C.destroy()
            Password_Label_C.destroy()
            Entry_Password_C.destroy()                 #Destroys the buttons and labels on the sign up page
            Name_Label_C.destroy()
            Entry_Name_C.destroy()
            Create_Account_Button.destroy()
            Return_Button.destroy()

        def Check_Username():

            Username_List = []
            Create_Username =  Entry_Username_C.get()
            Create_Password = Entry_Password_C.get()
            Create_Name = Entry_Name_C.get()

            for x in range(0,len(User_Dict)):
                Username_List.append(User_Dict[x][0])

            if Create_Username in Username_List:

                Username_Taken = tk.Button(self.GUI,text = "Username already taken",command = Destroy_Username_Taken, bg = "red", fg = "black", font = ("Comicsans",20),activebackground = "red")
                List.append(Username_Taken)
                Username_Taken.place(relx = 0.4, rely = 0.15)
                
            else:
                Index = len(User_Dict)
                New_Info = {Index: [Create_Username,"E:\\NEA_USB\\User_Images\\New_Account_Image.jpg" ,Create_Password, Create_Name,250]}
                User_Dict.update(New_Info)
                
                with open("E:\\NEA_USB\\User_Info\\User_UserNames.txt","a") as f:
                    f.write("\n")
                    f.write(User_Dict[len(User_Dict)-1][0])

                Item_Uno = Encrypt(User_Dict[x][2], Layer1)
                Item_Dos = Encrypt(Item_Uno,Layer2)
                Item = ""
                for z in range(0,len(Item_Dos)):
                    Item = Item + Item_Dos[z]
                    
                Item = Item + "\n"
                
                with open("E:\\NEA_USB\\User_Info\\User_Passwords.txt","a") as f:
                    f.write("\n")
                    f.write(Item)

                with open("E:\\NEA_USB\\User_Info\\User_Names.txt","a") as f:
                    f.write("\n")
                    f.write(User_Dict[len(User_Dict)-1][3])

                with open("E:\\NEA_USB\\User_Info\\User_Account_Bal.txt","a") as f:            # Adds the new accounts information directly to the various text files that make the database
                    f.write("\n")
                    f.write("250")

                with open("E:\\NEA_USB\\User_Info\\User_Photo_Locations.txt","a") as f:
                    f.write("\n")
                    f.write(User_Dict[len(User_Dict)-1][1])

                with open("E:\\NEA_USB\\User_Info\\User_Last_Seen.txt","a") as f:
                    f.write("\n")
                    f.write("Book_Not_Found")

                Logged_In[0] = True
                Logged_In[1] = len(User_Dict)-1
                Destroy_All()
                X = Main_Program(self.GUI)
                X.Main_Interface()   

        def Destroy_Username_Taken():
            List[0].destroy()

        def Return():
            Destroy_All()
            X = Main_Program(self.GUI)
            X.Login_Screen()

        List = []

        Username_Label_C = Label(self.GUI,text = "Create a Username: ", font = ("Arial",18),bg = "navy",fg = "white")
        Username_Label_C.place(rely = 0.1,relx = 0.4)

        Entry_Username_C = tk.Entry(self.GUI,font = ("Arial",18),bg = "grey40",fg = "black")
        Entry_Username_C.place(rely = 0.15,relx = 0.4)

        Password_Label_C = Label(self.GUI,text = "Create a Password: ", font = ("Arial",18),bg = "navy",fg = "white")
        Password_Label_C.place(rely = 0.2,relx = 0.4)

        Entry_Password_C = tk.Entry(self.GUI,font = ("Arial",18),show = "*",bg = "grey40",fg = "black")              # Allows the user to create a account, by entering username
        Entry_Password_C.place(rely = 0.25,relx = 0.4)                                                               # password and name (Password is hidden by "*" for security reasons)
        
        Name_Label_C = Label(self.GUI, text = "Enter your Name: ", font = ("Arail",18), bg = "navy",fg = "white")
        Name_Label_C.place(rely = 0.3, relx = 0.4)

        Entry_Name_C = tk.Entry(self.GUI,font = ("Arial",18),bg = "grey40",fg = "black")
        Entry_Name_C.place(rely = 0.35, relx = 0.4)

        Create_Account_Button = tk.Button(self.GUI,text = "Create Account", bg = "grey50", fg = "black", font = ("Comic Sans", 18, "bold"), command = Check_Username, activebackground = "red")
        Create_Account_Button.place(rely = 0.4, relx = 0.4)

        Return_Button = tk.Button(self.GUI,text = "Return", bg = "blue", fg = "black", font =("Arial",18,"bold"),activebackground = "red",command = Return)
        Return_Button.place(rely = 0.085, relx = 0.0)

    def User_Account_Interface(self):

        def Destroy_All():
            User_Profile_Pic[1].destroy()
            User_Name_Label.destroy()
            Username_Label.destroy()
            Change_Name_Username_Password_Button.destroy()
            Account_Balance_Button.destroy()
            Last_Seen_Button.destroy()
            Return_Button.destroy()
            Erase_Account_Button.destroy()

        def Account_Balance_Link():
            Destroy_All()
            X = Main_Program(self.GUI)
            X.User_Account_Bal_Interface()

        def Last_Seen_Link():
            Destroy_All()
            X = Main_Program(self.GUI)
            X.User_Last_Seen_Interface()

        def Return_Home():
            Destroy_All()
            X = Main_Program(self.GUI)
            X.Main_Interface()

        def Change_Profile_Pic():
            Destroy_All()
            filename = filedialog.askopenfilename(initialdir = "/",title = "Select a Photo to use",filetypes = (("JPG","*.jpg"),("All Files","*.*")))

            if filename != '':
            
                User_Profile_Address = "E:\\NEA_USB\\User_Images\\"+User_Dict[Logged_In[1]][0]+".jpg"

                if User_Dict[Logged_In[1]][1] == "E:\\NEA_USB\\User_Images\\New_Account_Image.jpg":
                    User_Dict[Logged_In[1]][1] = User_Profile_Address

                copyfile(filename,User_Profile_Address)

                Old_Data = open("E:\\NEA_USB\\User_Info\\User_Photo_Locations.txt","w")            # Opens the computer's directory and allows the user to select a new profile picture
                Old_Data.truncate()                                                                # This new picture is then copied to the USB and overwrites the original image
                Old_Data.close()
       
                for x in range(0,len(User_Dict)):
                    item = User_Dict[x][1]+"\n"
                    with open("E:\\NEA_USB\\User_Info\\User_Photo_Locations.txt","a") as f:
                        f.write(item)
                f.close()

            X = Main_Program(self.GUI)
            X.User_Account_Interface()
                
        def Change_Name_Password():
            
            def Confirm_Password_Change():

                def Change_Success():
                    Password_Change_Success.destroy()

                def Change_Failure():
                    Password_Change_Failed.destroy()
                
                Old_Pass = Old_Pass_Entry.get()
                New_Pass = New_Pass_Entry.get()

                if User_Dict[Logged_In[1]][2] == Old_Pass:
                    User_Dict[Logged_In[1]][2] = New_Pass
                
                    Old_Data = open("E:\\NEA_USB\\User_Info\\User_Passwords.txt","w")       # Allows the user to change their passsword, then the system directly changes the password in
                    Old_Data.truncate()                                                     # the database
                    Old_Data.close()

                    for x in range(0,len(User_Dict)):

                        

                        with open("E:\\NEA_USB\\User_Info\\User_Passwords.txt","a") as f:
                            f.write(Item)
                    f.close()

                    Password_Change_Success = Label(self.GUI,text = "Success! Password has been changed", bg = "green2",fg = "black")
                    Password_Change_Success.pack()
                    self.GUI.after(1000,Change_Success)
                else:
                    Password_Change_Failed = Label(self.GUI,text = "Failed, Password is Incorrect",bg = "red",fg ="black", font = ("Arial",22,"bold","italic"))
                    Password_Change_Failed.pack()
                    self.GUI.after(1000,Change_Failure)

            def Change_Name():

                def Change_Success():
                    Name_Change_Success.destroy()
                    

                New_Name = New_Name_Entry.get()

                User_Dict[Logged_In[1]][3] = New_Name
                
                Old_Data = open("E:\\NEA_USB\\User_Info\\User_Names.txt","w")             # Allows thr user to change their screen name, then the sytem directly
                Old_Data.truncate()                                                       # writes the new name into the database
                Old_Data.close()

                for x in range(0,len(User_Dict)):
                    item = User_Dict[x][3] + "\n"
                    with open("E:\\NEA_USB\\User_Info\\User_Names.txt","a") as f:
                        f.write(item)
                f.close()

                Name_Change_Success = tk.Button(self.GUI,text = "Sucess! Name has been changed!",bg = "green2",fg = "black",font = ("Arial",18),command = Change_Success)
                Name_Change_Success.pack()
                self.GUI.after(1000,Change_Success)
                

            def Destroy_Some():
                Password_Change_Label.destroy()
                Old_Pass_Label.destroy()
                Old_Pass_Entry.destroy()
                New_Pass_Label.destroy()
                New_Pass_Entry.destroy()
                Confirm_Password_Change_Button.destroy()
                Name_Change_Label.destroy()
                New_Name_Label.destroy()
                New_Name_Entry.destroy()
                Change_Name_Button.destroy()
                Return_Button.destroy()

            def Return():
                Destroy_Some()
                X = Main_Program(self.GUI)
                X.User_Account_Interface()
                

            Destroy_All()

            Password_Change_Label = Label(self.GUI,text = "Change Password", bg = "dark turquoise",fg = "Black", font = ("Comic sans",22,"bold"))
            Password_Change_Label.place(relx = 0.375,rely = 0.1)

            Old_Pass_Label = Label(self.GUI,text ="Confirm Password: ", bg = "grey40", fg = "black", font = ("Arial",18))
            Old_Pass_Label.place(relx = 0.3, rely = 0.3)

            Old_Pass_Entry = tk.Entry(self.GUI,bg = "grey30",fg = "black", font = ("Arial",18))
            Old_Pass_Entry.place(relx = 0.45,rely = 0.3)

            New_Pass_Label = Label(self.GUI,text = "New Password: ",bg = "grey40",fg = "black",font = ("Arial",18))          # Displays the buttons and entry widgets for 
            New_Pass_Label.place(relx = 0.3, rely = 0.2)                                                                     # changing the name, password and return

            New_Pass_Entry = tk.Entry(self.GUI,bg = "grey30",fg = "black",font = ("Arial",18))
            New_Pass_Entry.place(relx = 0.45,rely = 0.2)

            Confirm_Password_Change_Button = tk.Button(self.GUI, text = "Confirm Password Change",bg = "blue3",fg = "black",font = ("Arial",14),command = Confirm_Password_Change, activebackground = "red")
            Confirm_Password_Change_Button.place(relx = 0.375, rely = 0.4)

            Name_Change_Label = Label(self.GUI,text = "Change Name", bg = "dark turquoise", fg = "black",font = ("Comic Sans",22,"bold"),width = 14)
            Name_Change_Label.place(relx = 0.375 ,rely = 0.55)

            New_Name_Label = Label(self.GUI,text = "New Name: ", bg = "grey40",fg = "black",font = ("Arial",18))
            New_Name_Label.place(relx = 0.325, rely = 0.7)

            New_Name_Entry = tk.Entry(self.GUI, fg = "black",font = ("Arial",18),bg = "grey40")
            New_Name_Entry.place(relx = 0.425, rely = 0.7)

            Change_Name_Button = tk.Button(self.GUI,text = "Name Change",bg = "blue3",fg= "Black", font = ("arial",14),command = Change_Name,activebackground = "red")
            Change_Name_Button.place(relx = 0.4, rely = 0.8)

            Return_Button = tk.Button(self.GUI,text = "Return", bg = "grey50",fg = "Black",font = ("Arial",18),command = Return)
            Return_Button.place( relx = 0, rely = 0.085)

        def Delete_Account():           

            def Cancel():
                Destroy_Other()
                X = Main_Program(self.GUI)
                X.User_Account_Interface()

            def Destroy_Other():
                Confirm_Erase_Label.destroy()
                Confirm_Erase_Entry.destroy()
                Confirm_Erase_Button.destroy()
                Cancel_Button.destroy()

            def Confirm_Password():
                def Erase():
                    Incorrect_Password.destroy()

                def Delete():
                    Success_Label.destroy()
                    X = Main_Program(self.GUI)                             # Deletes the users account after receiving confirmation via the form of correct password
                    X.Main_Interface()                                     # The system then erases all the data concerning the user from the database
                    
                Pass = Confirm_Erase_Entry.get()

                if Pass == User_Dict[Logged_In[1]][2]:

                    del User_Dict[Logged_In[1]]
                    Logged_In[0] = False
                    Logged_In[1] = 0

                    File_Names = ["E:\\NEA_USB\\User_Info\\User_UserNames.txt",
                                  "E:\\NEA_USB\\User_Info\\User_Photo_Locations.txt",
                                  "E:\\NEA_USB\\User_Info\\User_Passwords.txt",
                                  "E:\\NEA_USB\\User_Info\\User_Names.txt",
                                  "E:\\NEA_USB\\User_Info\\User_Account_Bal.txt",
                                  "E:\\NEA_USB\\User_Info\\User_Last_Seen.txt"]

            
                    for y in range(0,6):
                            Old_File = open(File_Names[y],"w")
                            Old_File.truncate()
                            Old_File.close()
                            
                    for x in range(0,len(User_Dict)):

                        for z in range(0,6):

                            if File_Names[z] == "E:\\NEA_USB\\User_Info\\User_Passwords.txt":
                                Item_Uno = Encrypt(User_Dict[x][2], Layer1)
                                Item_Dos = Encrypt(Item_Uno,Layer2)
                                item = ""
                                
                                for n in range(0,len(Item_Dos)):
                                    item = item + Item_Dos[n]
                                    
                                item = item + "\n"

                            else:
                                item = str(User_Dict[x][z])+"\n"
                                
                            with open(File_Names[z],"a") as f:                  
                                f.write(item)
                            f.close()

                    Destroy_Other()
                    Success_Label = Label(self.GUI,text = "Success! Account has been deleted!",bg = "lawngreen",fg = "black",font = ("Comic Sans",22,"bold"))
                    Success_Label.pack()
                    self.GUI.after(1000,Delete)

                else:
                    Incorrect_Password = Label(self.GUI,text = "Incorrect Password",bg = "red2",fg = "black",font = ("Comic Sans",22,"bold"))
                    Incorrect_Password.pack()
                    self.GUI.after(1000,Erase)
                    

            Destroy_All()
            Confirm_Erase_Label = Label(self.GUI,text = "Confirm Password to Delete:", bg = "grey50",fg = "black",font = ("Arial",18))
            Confirm_Erase_Entry = tk.Entry(self.GUI,show = "*",font = ("Arial",18),bg = "grey40",fg = "black")
            Confirm_Erase_Button = tk.Button(self.GUI,text = "Confirm",command = Confirm_Password, bg = "green4",fg ="black",font = ("Arial",18))

            Cancel_Button = tk.Button(self.GUI,text = "Cancel",command = Cancel, bg = "red4",fg = "black",font = ("Arial",18))

            Confirm_Erase_Label.place(rely = 0.15,relx = 0.2750)
            Confirm_Erase_Entry.place(rely = 0.15, relx = 0.5)               # Asks the user for their password to confirm account deletion
            Confirm_Erase_Button.place(rely = 0.25,relx = 0.4)
            Cancel_Button.place(rely = 0.25,relx = 0.5)

  
        Index_Position = Logged_In[1]

        Photo = [0]

        Original = Image.open(User_Dict[Logged_In[1]][1])
        Resized = Original.resize((175,175),Image.ANTIALIAS)
        Photo[0] = ImageTk.PhotoImage(Resized)
        User_Profile_Pic[0] = Photo[0]
        Display_User_Image = tkinter.Button(self.GUI, image = Photo,bg = "grey40",activebackground = "cyan",command = Change_Profile_Pic)
        User_Profile_Pic[1] = Display_User_Image
        
        User_Profile_Pic[1].place(relx = 0.35, rely = 0.1)                 # Displays the information on the User Account settings

        Name = "Name: " + str(User_Dict[Logged_In[1]][3])
        User_Name_Label = Label(self.GUI, text = Name, bg = "midnightblue", fg = "cyan", font = ("Impact",24,"bold"))
        User_Name_Label.place(relx = 0.485, rely = 0.125)

        UserName = "Username: "+ str(User_Dict[Logged_In[1]][0])
        Username_Label = Label(self.GUI, text = UserName, bg = "midnightblue",fg = "cyan",font = ("Impact",24,"bold"))
        Username_Label.place(relx = 0.485, rely = 0.2)

        Change_Name_Username_Password_Button = tkinter.Button(self.GUI,text = "Change Password or Name",bg = "grey50",fg = "black", activebackground = "red",command = Change_Name_Password)
        Change_Name_Username_Password_Button.place(relx = 0.485, rely = 0.275)
            
        Account_Balance_Button = tkinter.Button(self.GUI,text = "View Account Balance", bg = "Grey30",fg = "black", font = ("Arial",18), width = 30,command = Account_Balance_Link)
        Account_Balance_Button.place(relx = 0.35, rely = 0.35)

        Last_Seen_Button = tkinter.Button(self.GUI,text = "Last Viewed", bg = "Grey30",fg = "black",font = ("Arial",18),width = 30,command = Last_Seen_Link)
        Last_Seen_Button.place(relx = 0.35, rely = 0.45)

        Return_Button = tkinter.Button(self.GUI,text = "Return", bg = "Grey50",fg = "black", font = ("Arial",18), activebackground = "red", command = Return_Home, width = 10)
        Return_Button.place(relx = 0, rely =0.085)

        Erase_Account_Button = tk.Button(self.GUI,text = "Delete Account",bg = "red3",fg = "black",font = ("Arial",18,"bold","italic"),width = 28, command = Delete_Account)
        Erase_Account_Button.place(relx = 0.35,rely = 0.55)

    def User_Account_Bal_Interface(self):

        def Destroy_All():
            for x in range(0,len(Label_List)):         
                Label_List[x].destroy()
                Button_List[x].destroy()
                
            Return_Button.destroy()
            Current_Bal_Label.destroy()

        def Purchase_Confirmation(x):

            def Deny():
                Confirm_Purchase.destroy()
                Cancelled_Purchase.destroy()            
                

            def Confirmed(x):

                def Erase():
                    Purchase_Complete_Label.destroy()
                    Destroy_All()
                    X = Main_Program(self.GUI)
                    X.User_Account_Bal_Interface()
                    

                Confirm_Purchase.destroy()
                Cancelled_Purchase.destroy()
                
                Purchase_Complete_Label = Label(self.GUI,text = "Purchase Complete!",bg = "lawngreen",font = ("Impact",18,"bold","italic"),fg = "black")
                Purchase_Complete_Label.place(relx = 0.5, rely =0.085, anchor = N)
                self.GUI.after(1000,Erase)

                Prices_List = [250,600,1500,2250,3000]
                New_User_Bal = int(User_Dict[Logged_In[1]][4]) + Prices_List[x]              # Tells the user they have successfully bought the desired package
                                                                                             # and changes the user's account balance accordingly
                User_Dict[Logged_In[1]][4] = New_User_Bal

                Old_Data = open("E:\\NEA_USB\\User_Info\\User_Account_Bal.txt","w")
                Old_Data.truncate()
                Old_Data.close()

                for x in range(0,len(User_Dict)):
                    item = str(User_Dict[x][4]) + "\n"
                    with open("E:\\NEA_USB\\User_Info\\User_Account_Bal.txt","a") as f:
                        f.write(item)
                f.close()

                #Asks the user to confirm that they are purchasing the package
                
            Confirm_Purchase = tk.Button(self.GUI,text = "Click to Confirm Purchase",bg = "green4",command = partial(Confirmed,x),font = ("Arial",20,"bold"),activebackground = "red4")
            Confirm_Purchase.pack()

            Cancelled_Purchase = tk.Button(self.GUI,text = "Cancel Purchase",bg = "red2",command = Deny, font=("Arial",20,"bold"),activebackground = "red4")
            Cancelled_Purchase.pack()

    
        def Return():
            Destroy_All()
            Return_Button.destroy()

            X = Main_Program(self.GUI)
            X.Main_Interface()

        Label_List = []                 # Displays the different packagees that are available for set prices
        Button_List = []
        Text = ["£2.50 for 250 Coin","£5.00 for 500 + 100 Coin", "£10.00 for 1000 + 500 Coin","£15.00 for 1500 + 750 Coin","£20.00 for 2000 + 1000 Coin", "£0.00 for infinite Coin"]

        Background_Label_Colours = ["red","deeppink","purple","blue","cyan","thistle4"]

        Current_Bal_Text = "Current Balance: "+str(User_Dict[Logged_In[1]][4]) + " Coins"
        Current_Bal_Label = Label(self.GUI,text = Current_Bal_Text,bg = "Darkviolet",fg = "black",font = ("Comic Sans",18,"bold","italic"))
        Current_Bal_Label.place(rely = 0.1,relx = 0.5,anchor = N)

        Y_Coords = [0.2,0.3,0.4,0.5,0.6]

        for x in range(0,5):
            Price_Set_Label = Label(self.GUI,text = Text[x], bg = Background_Label_Colours[x],fg = "black",font = ("Akaya Telivigala",20,"bold"))
            Label_List.append(Price_Set_Label)
            Label_List[x].place(relx = 0.425,rely = Y_Coords[x],anchor = N)

            Price_Set_Button = tk.Button(self.GUI, text = "Purchase",command = partial(Purchase_Confirmation,x), bg = "green4",fg = "black", font = ("Arial",18,"bold","italic"))
            Button_List.append(Price_Set_Button)
            Button_List[x].place(relx = 0.60,rely = Y_Coords[x],anchor = N)

        Return_Button = tk.Button(self.GUI,text = "Return", bg = "grey50",fg = "black",font = ("Arial",18,"bold"),command = Return,activebackground = "red4")
        Return_Button.place(relx = 0, rely =0.085)
        

    def User_Last_Seen_Interface(self):

        def Display_Last_Seen_Books(Last_Seen_List_Original):

            def Show_Book_Info(Z):
                
                if Eta_List[0] != "0":
                    for x in range(0,len(Zeta_Book_Name_List)):
                        Zeta_Book_Name_List[x].destroy()
                        Epsilon_Button_List[x].destroy()
                        Delta_Photo_List = []
                    Eta_List[0] = "0"

                Return_Button.destroy()                    #Deletes everything on the sceen before redirecting towards book information
                Last_Seen_Text_Box.destroy()

                global Last_Saw
                Last_Saw = ["True","True"]


                X = Main_Program(self.GUI)
                X.Present_Book_Information(Z)

            def Return():
                if Eta_List[0] != "0":
                    for x in range(0,len(Zeta_Book_Name_List)):
                        Zeta_Book_Name_List[x].destroy()
                        Epsilon_Button_List[x].destroy()                # Deletes everything on screen and return the user to the main screen
                        Delta_Photo_List = []
                    Eta_List[0] = "0"

                Return_Button.destroy()
                Last_Seen_Text_Box.destroy()

                X = Main_Program(self.GUI)
                X.Main_Interface()

            Last_Seen_List = []
            for x in Last_Seen_List_Original:
                if x not in Last_Seen_List:
                    Last_Seen_List.append(x)
            
            Index_List = []
            for x in range(0,len(Last_Seen_List)):
                for y in range(0,len(Book_Dict)):                     
                    if Book_Dict[y][2] == Last_Seen_List[x]:
                        Index_List.append(y)

            X_Cords = [0.03, 0.23,0.43,0.63,0.83]
            
            Delta_Photo_List.clear()
            Epsilon_Button_List.clear()
            Zeta_Book_Name_List.clear()

            if len(Index_List) < 5:
                
                for x in range(0,len(Index_List)):
                    Original = Image.open(Book_Dict[Index_List[x]][1])
                    Resized = Original.resize((250,350),Image.ANTIALIAS)
                    Photo = ImageTk.PhotoImage(Resized)
                    Delta_Photo_List.append(Photo)

                    Image_Button = tk.Button(self.GUI,image = Photo, bg = "red4",command = partial(Show_Book_Info,Index_List[x]))
                    Epsilon_Button_List.append(Image_Button)
                    Epsilon_Button_List[x].place(relx = X_Cords[x], rely = 0.275)

                    Book_Name_Button = tk.Button(self.GUI,text = Book_Dict[Index_List[x]][2],command = partial(Show_Book_Info,Index_List[x]), font = ("Akaya Telivigala",16,"bold"),bg = "darkturquoise",fg = "black")
                    Zeta_Book_Name_List.append(Book_Name_Button)
                    Zeta_Book_Name_List[x].place(relx = X_Cords[x],rely = 0.725)

                    Eta_List[0]= "1"
                    
            else:                  #Displays the last seen books, in the order they were last seen, if they have seen more than 5 books, then only the most recent 5 are displayed

                for x in range(0,4):
                    Original = Image.open(Book_Dict[Index_List[x]][1])
                    Resized = Original.resize((250,350),Image.ANTIALIAS)
                    Photo = ImageTk.PhotoImage(Resized)
                    Delta_Photo_List.append(Photo)

                    Image_Button = tk.Button(self.GUI,image = Photo, bg = "red4",command = partial(Show_Book_Info,Index_List[x]))
                    Epsilon_Button_List.append(Image_Button)
                    Epsilon_Button_List[x].place(relx = X_Cords[x], rely = 0.275)

                    Book_Name_Button = tk.Button(self.GUI,text = Book_Dict[Index_List[x]][2],command = partial(Show_Book_Info,Index_List[x]))
                    Zeta_Book_Name_List.append(Book_Name_Button)
                    Zeta_Book_Name_List[x].place(relx = X_Cords[x],rely = 0.725)

                    Eta_List[0] = "1"

            Last_Seen_Text_Box = Label(self.GUI,text = "Last Seen:",font = ("Arial",24,"bold","italic"),fg = "midnight blue",bg = "maroon2")
            Last_Seen_Text_Box.place(relx = 0.4,rely = 0.1)

            Return_Button = tk.Button(self.GUI,text = "Return",bg = "grey50",fg = "black",font = ("Arial",18),activebackground = "red4",command = Return)
            Return_Button.place(relx = 0, rely =0.085)
            

        Last_Seen_UnOrdered_String = (User_Dict[Logged_In[1]][5])
        Last_Seen_Unordered = Last_Seen_UnOrdered_String.split(",")
        
        for x in range(0,len(Last_Seen_Unordered)):
            if Last_Seen_Unordered[x] == '':
                Last_Seen_Unordered.remove(Last_Seen_Unordered[x])             
        
        Last_Seen_List = []

        X = len(Last_Seen_Unordered)-1                                      # Sorts and reads in the last seen list, so that it is presented to the user correctly
                                                                            
        while X != -1:
            Last_Seen_List.append(Last_Seen_Unordered[X])
            X = X-1
            
        item = Last_Seen_List[0]
        if item != "Book_Not_Found":
            for x in range(1,len(Last_Seen_List)):
                item =item+","+Last_Seen_List[x] 
            Display_Last_Seen_Books(Last_Seen_List)
        else:
            X = Main_Program(self.GUI)
            X.Main_Interface()

    def Search_Books(self,Looking_For):
                
        def Not_Found_Clicked():
                Not_Found.destroy()        #This is used to let the user know that there is no books containing the words in the search entry

        def Next_Page():
            
            if Z_Index_Position[0] <= len(Listed_Books):
                Z = Z_Index_Position[0]
                Z_Index_Position[0] = Z + 10
                Return_Button.destroy()                # Increases the base index, allowing the next 10 books to be seen
                Display_Books()
            else:
                Z_Index_Position[2].destroy()
                Z_Index_Position[2] = 0
                
        def Last_Page():
            if Z_Index_Position[0] >= 10:
                Z = Z_Index_Position[0]
                Z_Index_Position[0] = Z-10
                Return_Button.destroy()

                if Found == False:
                    Not_Found.destroy()                    # Decreases the base index, allowing the last 10 books to be seen
             
                Display_Books()

            else:
                Z_Index_Position[3].destroy()
                Z_Index_Position[3] = 0

            Return_Button.destroy()

            if Found == False:
                Not_Found.destroy()

        def Show_Book_Info(Z):

            for Q in range(0,len(Book_Name_Button_List)):
                Var = Book_Name_Button_List[Q]
                Var.destroy()

                Var2 = Image_Button_List[Q]
                Var2.destroy()

            Z_Index_Position[2].destroy()
            Z_Index_Position[3].destroy()

            for x in range(0,len(Genre_Button_List)):
                Genre_Button_List[x].destroy()

            global Last_Saw
            Last_Saw = ["True","False"]               # Calls the subroutine that displays the information regarding the individual books

            N = Listed_Books[Z]

            for x in range(0,len(Iota_List)):
                Iota_List[x].destroy()

            if Found == False:
                Not_Found.destroy()
                    
            X = Main_Program(self.GUI)
            X.Present_Book_Information(N)

        def Return():
            for Q in range(0,len(Book_Name_Button_List)):
                Var = Book_Name_Button_List[Q]
                Var.destroy()

                Var2 = Image_Button_List[Q]
                Var2.destroy()

            if Z_Index_Position[2] != 0 and Z_Index_Position[3] != 0:
                
                Z_Index_Position[2].destroy()
                Z_Index_Position[3].destroy()

            for x in range(0,len(Genre_Button_List)):                           # Erases all the information on screen and direct the user to the main screen
                Genre_Button_List[x].destroy()

            for x in range(0,len(Iota_List)):
                Iota_List[x].destroy()

            if Found == False:
                Not_Found.destroy()

            X = Main_Program(self.GUI)
            X.Main_Interface()

        def Display_Books():
            if Z_Index_Position[2] == 0:

                Next_Page_Button = tk.Button(self.GUI, text = "Next Page", command = Next_Page, fg = "gold", bg = "green4",font = ("Comic sans",18, "bold"), activebackground = "red")
                Z_Index_Position[2] = Next_Page_Button
                Next_Page_Button.place(relx = 0.9,rely = 0.925)

            if Z_Index_Position[3] == 0:
                Last_Page_Button = tk.Button(self.GUI, text = "Previous Page", command = Last_Page, fg = "gold", bg = "green4",font = ("Comic sans",18, "bold"), activebackground = "red")
                Z_Index_Position[3] = Last_Page_Button
                Last_Page_Button.place(relx = 0.01, rely =0.925)
            
            for Q in range(0,len(Book_Name_Button_List)):
                Var = Book_Name_Button_List[Q]
                Var.destroy()

                Var2 = Image_Button_List[Q]    # Displays all the books that contrain the search input
                Var2.destroy()                 

            for x in range(Z_Index_Position[0],len(Listed_Books)):
                
                Temp = Book_Dict[Listed_Books[x]][2]
                

                if x <= (Z_Index_Position[0]+4):
                
                    Original = Image.open(Book_Dict[Listed_Books[x]][1])
                    Resized = Original.resize((150,200), Image.ANTIALIAS)                  #Nested Subroutine for the creation of the images and their name tag buttons
                    Photo = ImageTk.PhotoImage(Resized) 

                    Photo_List.append(Photo)
                    
                    Image_Button = tk.Button(self.GUI, image = Photo,command =partial(Show_Book_Info,x),activebackground = "red4", bg = "red4")
                    Image_Button.place(relx = XCords[x- Z_Index_Position[0]], rely = 0.225)

                    Image_Button_List.append(Image_Button)

                    Book_Name_Button = tk.Button(self.GUI, text = Book_Dict[Listed_Books[x]][2], bg = "grey50",fg = "black",font = ("Arial",16),command = partial(Show_Book_Info,x),activebackground = "red4")
                    Book_Name_Button.place(relx = LabelXCords[x - Z_Index_Position[0]], rely = 0.485)

                    Book_Name_Button_List.append(Book_Name_Button)

                elif x > (Z_Index_Position[0]+4) and x <= (Z_Index_Position[0]+9):
                    

                    Original = Image.open(Book_Dict[Listed_Books[x]][1])
                    Resized = Original.resize((150,200), Image.ANTIALIAS)
                    Photo = ImageTk.PhotoImage(Resized)

                    Photo_List.append(Photo)       #Used to limit the number of books displayed to a maximum of 10, Limit is required as over 10 books would not all fit on the page
                                                                                                       
                    Image_Button = tk.Button(self.GUI, image = Photo,command = partial(Show_Book_Info,x),activebackground = "red4", bg = "red4")
                    Image_Button.place(relx = XCords[x-5 - Z_Index_Position[0]], rely = 0.55)

                    Image_Button_List.append(Image_Button)

                    Book_Name_Button = tk.Button(self.GUI, text = Book_Dict[Listed_Books[x]][2], bg = "grey50",fg = "black",font = ("Arial",16),command = partial(Show_Book_Info,x),activebackground = "red4")
                    Book_Name_Button.place(relx = LabelXCords[x- Z_Index_Position[0]-5], rely = 0.85)

                    Book_Name_Button_List.append(Book_Name_Button)

            Return_Button = tk.Button(self.GUI, text = "Return",bg = "grey50",fg = "black",font = ("Arial",16),command = Return)
            Return_Button.place(relx = 0, rely =0.085)
            Iota_List.append(Return_Button)

        Listed_Books = []
        
        Found = False
        for x in range(0,len(Book_Dict)):
            if Looking_For.lower() in Book_Dict[x][2].lower():
                Found = True
                Listed_Books.append(x)

        if Found == False:
            Not_Found = Label(self.GUI,text = "Book Not found, please check spelling",font = ("Arial",18),bg = "red4",fg = "black")
            Not_Found.pack()

        Image_Location = []
        
        for z in range(0,len(Book_Dict)):                       # Creates the list of that contains all the books that contain the search input
            Var = Book_Dict[z][1]                               # Otherwise it lets the user know that the search input is invalid
            Image_Location.append(Var)

        if Found == True:
            global Photo_List
            Photo_List = []

            XCords = [0.05,0.25, 0.45, 0.65, 0.85]
            LabelXCords = [0.025, 0.225,0.425,0.625,0.825]

            if Z_Index_Position[2] != 0:
                Z_Index_Position[2].destroy()
                Z_Index_Position[2] = 0

            if Z_Index_Position[3] !=0:
                Z_Index_Position[3].destroy()
                Z_Index_Position[3] = 0

            Z_Index_Position[0] = 0
            Display_Books()

        Return_Button = tk.Button(self.GUI, text = "Return",bg = "grey50",fg = "black",font = ("Arial",16),command = Return)
        Return_Button.place(relx = 0, rely =0.085)
        Iota_List.append(Return_Button)

        

        
    


# Start of the program
# Creates the interface that the program is built upon
# Reads all the external files in, the outcome is two "Mega" dictionaries, 1 contains user information, the other book information.

GUI = Tk(className = " Book Worm: The Not So Online Bookstore")
GUI.geometry("1080x1080")
GUI.configure(bg = "grey14")

Top_Bar = Label(GUI,text ="",bg = "grey40",font = ("Arial",40),width = 1080)
Top_Bar.pack()

my_Canvas = Canvas(GUI,width = 200, height = 63,bg = "navy")
my_Canvas.place(rely = 0, relx = 0, anchor = NW)

Original = Image.open("E:\\NEA_USB\\Front_Page_And_Logos\\Bookworm_Logo.jpg")
Resized = Original.resize((201,64),Image.ANTIALIAS)
Photo = ImageTk.PhotoImage(Resized)

my_Canvas.create_image(0,0,anchor = NW,image = Photo)

global Logged_In
Logged_In = ["","",0]

global Book_Genre_List
Book_Genre_List = []
Read_File = open("E:\\NEA_USB\\Books_Info\\Book_Genre.txt")           #"Book_Genre_List" is a global list as it is used later to display and sort the books
for line in Read_File.readlines():                                    # The other lists are not global as only the genre and its index is required to sort and display book data
    Book_Genre_List.append(line.strip("\n"))                          
Read_File.close

global Book_Dict, User_Dict
Book_Dict = Mega_Book_List()
User_Dict = Mega_User_List()

#Globalises the variables so that they can be used anywhere within the system
# Some of these global variables are needed so that images can actually be displayed rather than being garbage collected (When garbage collected, the image is blank and disables the button)

global Book_Name_Button_List, Image_Button_List, Incorrect_Counter, Drop_List, Z_Index_Position, Genre_Button_List, Beta_List, Gamma_List, Delta_Photo_List,Epsilon_Button_List, Zeta_Book_Name_List, Eta_List, Last_Saw, Theta_List, Iota_List
Book_Name_Button_List = []
Image_Button_List = []
Incorrect_Counter = 0
Drop_List = []
Z_Index_Position = [0,0,0,0,0]  # Used to store the base index when displaying 10 books, this allows the "Next Page" and "Last Page" buttons to work and display the next/previous books
Genre_Button_List = []
Beta_List = []                  # Beta List is used to delete the buttons and labels when a book is clicked for more information
Gamma_List = []                 # Gamma List is used to delete the purchase cancelation and confirmation buttons.
Delta_Photo_List = []           # Delta_Photo_List is used in the User_Last_Seen_Interface to prevent garbage collection of the photos used.
Epsilon_Button_List = []        # Epsilon_Button_List is used in the User_Last_Seen_Interface to prevent the image on the button being garbage collected
Zeta_Book_Name_List = []        # Zeta_Book_Name_List is used in the User_Last_Seen_Interface to store the buttons on the page that are not located in Delta_Photo_List or Epsilon_Button_List
Eta_List = ["0"]                # Eta_List is used in the User_Last_Seen_Interface to show that Delta_Photo_List, Epsilon_Button_List and Zeta_Book_Name list had variables within that needed to be destroyed or deleted.
Theta_List = []                 # Used to erase Search Bar Buttons and entries, and the user account bal label
Iota_List = []                  # Used to erase the return button in next page for the search bar
Kappa_List = []                 # Used to store the buttons and labels used on the front page
Lambda_List = [0,0,0,0,0,0,0,0,0,0]                # Used to store the images of the buttons and labels on the front page

Last_Saw = ["False","False"]

global Photo_List
Photo_List = []

global Layer1,Layer2
Layer1 = "\/z.x,cmvnbasdfghjkl;'#][poiuytrewq=1-023948576¬?>!<£|~$@%:^}&{*+(_)QPWOEIRUTYAMSNDBFVGCHXJZKL"
Layer2 = "`1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik,9ol.0p;/-[=]#\?~>@}<:{+_¬|!)(£*$&$^%ZMXNCBVAPSODIFUGYHTRJEKWLQ"

User_Profile_Pic = ["","","",""]           #Needed so when signed in the actual picture isnt garbage collected

B = Main_Program(GUI)
B.Main_Interface()                        #Calls the "Main_Program" class, which all the buttons and features are apart of
GUI.mainloop()

#Extra Notes

#Created for AQA A Level Computer Science NEA Coursework
#Created by Nathan Horder
