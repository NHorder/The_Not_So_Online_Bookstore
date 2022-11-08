
def Mega_User_List():
    from Encryption_And_Decryption_Subroutines import Decrypt
    
    User_Usernames_List = []
    Read_File = open("E:\\NotSoOnlineBookStore_USB\\User_Info\\User_UserNames.txt")
    for line in Read_File.readlines():
        User_Usernames_List.append(line.strip("\n"))
    Read_File.close

    User_Passwords_List = []
    Read_File = open("E:\\NotSoOnlineBookStore_USB\\User_Info\\User_Passwords.txt")
    for line in Read_File.readlines():
        User_Passwords_List.append(line.strip("\n"))
    Read_File.close

    User_Names_List = []
    Read_File = open("E:\\NotSoOnlineBookStore_USB\\User_Info\\User_Names.txt")
    for line in Read_File.readlines():
        User_Names_List.append(line.strip("\n"))
    Read_File.close

    User_Account_Bal_List = []
    Read_File = open("E:\\NotSoOnlineBookStore_USB\\User_Info\\User_Account_Bal.txt")
    for line in Read_File.readlines():
        User_Account_Bal_List.append(line.strip("\n"))
    Read_File.close

    User_Photo_Locations_List = []
    Read_File = open("E:\\NotSoOnlineBookStore_USB\\User_Info\\User_Photo_Locations.txt")
    for line in Read_File.readlines():
        User_Photo_Locations_List.append(line.strip("\n"))
    Read_File.close()

    User_Last_Seen_List = []
    Read_File = open("E:\\NotSoOnlineBookStore_USB\\User_Info\\User_Last_Seen.txt")
    for line in Read_File.readlines():
        User_Last_Seen_List.append(line.strip("\n"))
        
    Read_File.close()

    Dict = {}
    M5 = []

    Layer1 = "\/z.x,cmvnbasdfghjkl;'#][poiuytrewq=1-023948576¬?>!<£|~$@%:^}&{*+(_)QPWOEIRUTYAMSNDBFVGCHXJZKL"
    Layer2 = "`1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik,9ol.0p;/-[=]#\?~>@}<:{+_¬|!)(£*$&$^%ZMXNCBVAPSODIFUGYHTRJEKWLQ"

    ListX = Decrypt(User_Passwords_List,Layer2)
    ListY = Decrypt(ListX,Layer1)
    #print(ListY)
    
    
    

    for x in range(0,len(User_Usernames_List)):
        N0 = User_Usernames_List[x]
        N1 = User_Photo_Locations_List[x]
        N2 = ListY[x]
        N3 = User_Names_List[x]
        N4 = User_Account_Bal_List[x]
        N5 = User_Last_Seen_List[x]

        

        M5 = [N0,N1,N2,N3,N4,N5]

        for y in range (2,102):
            Dict[x] = M5

    return Dict
