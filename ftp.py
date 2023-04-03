import ftplib
import os

#credenziali server ftp
url = '' #indirizzo server
username = ''
password = ''
serverDirForData = '' #directory dove salvari i dati acquisiti sul server

def send(fileName, filePath):
    """send file to server

    Args:
        fileName (str): Nome del file da inviare
        filePath (str): Percorso locale '/path/to/local/'
    """    
    # Set up the FTP connection
    ftp = ftplib.FTP(url)
    ftp.login(username, password)

    # Set the working directory on the FTP server
    ftp.cwd(serverDirForData)

    # Open the local file you want to send
    with open(filePath + fileName, 'rb') as file:
        # Send the file to the FTP server
        ftp.storbinary(f'STOR {fileName}', file)
        file.close()

    # Close the FTP connection
    ftp.quit()
    
def sendFiles():
    """sends all the file from a determined folder
    """    
    #path = os.getcwd() #directory del programma
    path = '/home/pi/Desktop/AirLab' # DA INSERIRE PERCORSO CORRETTO

    # Get a list of all files in the directory
    file_list = os.listdir(path)

    # Print the list of files
    print(file_list)

    for file in file_list:
        send(file, path)
        print(f'{file} sent')
        
if __name__ == "__main__":
    sendFiles()