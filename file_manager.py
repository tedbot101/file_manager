import os
import base64

def file_manager_single_encode(hide_file):

    # Encoding the data content
    data = open(hide_file, "rb").read()
    encoded_data = base64.b64encode(data)
    encoded_data = encoded_data.decode('ascii')

    # Encoding the file name
    if "\\" in hide_file:
        hide_file = hide_file.split('\\')
    else:
        hide_file = hide_file.split('/')

    hide_file = hide_file[-1]
    encoded_name = base64.b64encode(hide_file.encode('utf-8'))
    encoded_name = encoded_name.decode('ascii')

    # Saving the encrypted file
    encoded_file = open(data_folder+encoded_name,"w+")
    encoded_file.write(encoded_data)
    encoded_file.close()

    del_original_file = input('\nDo you want to delete original file ?(Y/N)')

    if del_original_file == 'y' or del_original_file == 'Y':
         os.system('del '+hide_file)
    else:
        print ('\n')

def bulk():
    bulk_path = cwd+"/folder/"
    bulk_entires = os.listdir(bulk_path)
    for i in bulk_entires:

        # Encoding content of the file
        data = open(bulk_path+i, "rb").read()
        encoded_data = base64.b64encode(data)
        encoded_data = encoded_data.decode('ascii')

        # Encoding the file name
        encoded_name = base64.b64encode(i.encode('utf-8'))
        encoded_name = encoded_name.decode('ascii')

        # Saving the encrypted file
        encoded_file = open(data_folder+encoded_name,"w+")
        encoded_file.write(encoded_data)
        encoded_file.close()
    
    os.system('del '+bulk_path+'*')

def file_manager_decode():
    decoded_names = []
    original_names = []
    for k in os.listdir(data_folder):
        x = base64.b64decode(k).decode('ascii')
        decoded_names.append(x)
        original_names.append(k)
    
    for o,p in enumerate(decoded_names):
        print ('No : ',o,'   File Name : ',p)
            
    no = int(input ('Enter the file you want to decrypt : '))
    file = original_names[no]

    
    data = open(data_folder+file,'rb').read()
    decoded_data = base64.b64decode(data)
    decoded_data = decoded_data.decode('utf-8')

    # Saving the decrypted file
    decoded_file = open(decrypeted+decoded_names[no],"w+")
    decoded_file.write(decoded_data)
    decoded_file.close()

def app_option():
    launch = True
    while launch:
        try:
            option = int(input("""\n

            Hello young fella, want to hide your unspeakable videos and pictures?

            Option 1 : Encrpt and single file
            Option 2 : Bulk Encrypt  # Copy and paste the files you want to encrypt in "folder"
            Option 3 : Decrypt an encrypted file
            Option 4 : Clear decrypted items # Warning this option will delete ONLY the files inside the "decrypted" folder 
            Option 0 : Exit

            Enter your option : """))

            # Hide file option
            if option == 1:     
                hide_file = input("\n\nEnter the path of your file : ")
                file_manager_single_encode(hide_file)
                print ('Operation Succeeded')

            if option == 2:
                bulk()
                print ('\nOperation Succeeded')

            if option == 3:
                file_manager_decode()
                print ('\nOperation Succeeded')

            if option == 4:
                os.system('del '+option_del+'*')
                print ('\nOperation Succeeded')

            if option == 0:
                launch = False

            else:
                print('\n\nNot a valid option my dude')
        except ValueError:
            app_option()


cwd = os.getcwd()
data_folder = cwd+"/data/"
decrypeted = cwd+"/decrypted/"
option_del = cwd+"\\decrypted\\"
#current_entries = os.listdir(bulk)


if __name__ == "__main__":
    app_option()

       