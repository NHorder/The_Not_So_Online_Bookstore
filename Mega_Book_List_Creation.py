
def Mega_Book_List():
    Book_Genre_List = []
    Read_File = open("E:\\NotSoOnlineBookStore_USB\\Books_Info\\Book_Genre.txt")           #"Book_Genre_List" is a global list as it is used later to display and sort the books
    for line in Read_File.readlines():                                    # The other lists are not global as only the genre and its index is required to sort and display book data
        Book_Genre_List.append(line.strip("\n"))                          
    Read_File.close

    Book_Photo_List = []
    Read_File = open("E:\\NotSoOnlineBookStore_USB\\Books_Info\\Book_Photo_Dictionary.txt")
    for line in Read_File.readlines():
        Book_Photo_List.append(line.strip("\n"))
    Read_File.close

    Book_Name_List = []
    Read_File = open("E:\\NotSoOnlineBookStore_USB\\Books_Info\\Book_Name.txt")
    for line in Read_File.readlines():                                               #Reads all the external ".txt" files in that contains the information of the books
        Book_Name_List.append(line.strip("\n"))
    Read_File.close

    Book_Author_List = []
    Read_File = open("E:\\NotSoOnlineBookStore_USB\\Books_Info\\Book_Author.txt")
    for line in Read_File.readlines():
        Book_Author_List.append(line.strip("\n"))
    Read_File.close

    Book_Coin_List = []
    Read_File = open("E:\\NotSoOnlineBookStore_USB\\Books_Info\\Book_Coin.txt")
    for line in Read_File.readlines():
        Book_Coin_List.append(line.strip("\n"))
    Read_File.close()

    Read_Descriptions_List = []
    Read_File2 = open("E:\\NotSoOnlineBookStore_USB\\Books_Info\\Book_Decriptions.txt",encoding = "utf8")
    for line in Read_File2.readlines():
        Read_Descriptions_List.append(line.strip("\n"))
    Read_File.close()

    global Book_Dict
    Book_Dict = {}
    L5 = []
    for x in range(0,100):
        T1 = Book_Genre_List[x]
        T2 = Book_Photo_List[x]                #Small loop used to make the "Mega" dictionary for information on the books.
        T3 = Book_Name_List[x]
        T4 = Book_Author_List[x]
        T5 = Book_Coin_List[x]
        T6 = Read_Descriptions_List[x]

        L5 = [T1,T2,T3,T4,T5,T6]

        for y in range (2,102):
            Book_Dict[x] = L5

    return Book_Dict


