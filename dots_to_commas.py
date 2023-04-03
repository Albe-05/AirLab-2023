import os

#!!!!!
#risolve il problema dei file csv non letti da excel perché i divisore dei decimali era '.' excel vuole ','

dir_path = input('Inserisci il percorso della cartella con i file da sistemare (C:\\cartella\\esempio\\...)--> ').replace('\\', '\\\\')

def fileList():    
    files = [f.name for f in os.scandir(dir_path) if f.is_file()] #reads all file
    [print(filename) for filename in files] # prints
    return files

def dotToCommas(filename):
    with open(filename, 'r') as f: # open file
        text = f.read().replace('.', ',')
    with open(filename, 'w') as f: # rewrites file
        f.write(text)
    print(f"fatto: {filename}")

for file in fileList():
    dotToCommas(f'{dir_path}\\{file}')