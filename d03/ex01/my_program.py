import sys
from path import Path

sys.path.insert(0, './install_dir')

folder_path = Path('test_folder')
file_path = folder_path / 'test_file.txt'

# Créer le dossier s'il n'existe pas
folder_path.mkdir_p()

# Écrire quelque chose dans le fichier
file_content = "Bonjour, ceci est un test !"
file_path.write_text(file_content)

# Lire et afficher le contenu du fichier
read_content = file_path.read_text()
print(f"Contenu du fichier : {read_content}")

if __name__ == '__main__':
    main()
