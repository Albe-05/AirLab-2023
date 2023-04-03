import os

#fornisce il totale di linee di tutti i file in un cartella, utile per avere il numero totale di misurazioni

dir_path = input('inserisci il percorso della cartella con i file da sistemare (C:\\cartella\\esempio\\...)--> ').replace('\\', '\\\\')
num_lines = 0

def totLines(filename):
    global num_lines
    with open(filename, 'r') as f:
        num_lines += sum(1 for line in f)

def fileList():    
    files = [f.name for f in os.scandir(dir_path) if f.is_file()] #reads all file
    [print(filename) for filename in files] # prints
    return files

for file in fileList():
    totLines(f'{dir_path}\\{file}')

print(num_lines)