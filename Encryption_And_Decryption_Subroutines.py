#Decryption and Encyrption of User Passwords

#Encrypts the Password List
def Encrypt(List,Layer):
    Encrypted_List_Layer1 = []

    for n in range(0,len(List)):
        Item = List[n]
        Cipher_Text = ""
        for x in range (0,len(Item)):
            for y in range(0,len(Layer)):
                if Item[x] == Layer[y]:

                    try:
                        Cipher_Text = Cipher_Text + Layer[y+1]

                    except IndexError:
                        Cipher_Text = Cipher_Text + Layer[0]

        Encrypted_List_Layer1.append(Cipher_Text)

    return Encrypted_List_Layer1


#Decrypt the Password List

def Decrypt(Encrypted_List,Layer):
    Decrypted_Text = ""
    List2 = []

    for n in range(0,(len(Encrypted_List))):
        Item = Encrypted_List[n]
        
        Decrypted_Text = ""
        
        for x in range(0,len(Item)):
            
            for y in range(0,len(Layer)):
                
                if Item[x] == Layer[y]:
                    
                    try:
                        Decrypted_Text = Decrypted_Text + Layer[y-1]

                    except IndexError:
                        Decrypted_Text = Decrypted_Text + Layer[0]
        List2.append(Decrypted_Text)

    return List2

