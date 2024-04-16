import os
import subprocess


class DirectoryManager:
    def __init__(self, dir_path) -> None:
        self.dir_path = dir_path


    def process_directory(self):
        """
        Process directory showing options for each file.

        """
        files = os.listdir(self.dir_path)
        files.sort()
        
        for file in files: 
            
            file_extension = self.get_file_extension(file)
            full_path = os.path.join(self.dir_path, file)
            self.process_file(file, full_path, file_extension)
            
        print('--------------------------------------------------------')
        print('Se procesaron todos los archivos.')
        print('--------------------------------------------------------')


    def process_file(self, file, full_path, file_extension):
        print('--------------------------------------------------------')
        print('Seleccione una opción para el archivo ' + file + ': ')
        print('1. Eliminar el archivo.')
        print('2. Renombrar el archivo.')
        print('3. Pasar al siguiente archivo.')
        if (file_extension == '.pdf'):
            print('4. Abrir el archivo en Preview')
        
        response = input()
        if (response == '1'):
            self.process_file_deletion(file, full_path)
        elif (response == '2'):
            self.process_file_renaming(file, full_path)
        elif (response == '3'):
            return 
        elif (file_extension == '.pdf' and response == '4'):
            self.process_file_opening(file, full_path, file_extension)
        else: 
            print('Opción inválida.')
            return
        

    def process_file_renaming(self, file_name, full_path):
        """
        Rename file.
        
        Args:
            file_name (str): Basename of the file to be renamed.
            full_path (str): Full path of the file to be renamed, including basename.
        """

        print('Introduzca el nuevo nombre junto a su extensión: ')
        new_name = input()
        new_path = self.dir_path + '/' + new_name
        os.rename(full_path, new_path)
        print('--Se cambió el nombre del archivo ' + file_name + ' por: ' + os.path.basename(new_path) + '\n')
        if (self.other_action_required(file_name)):
            self.process_file(new_name, new_path, self.get_file_extension(new_path))
        else: 
            return


    def process_file_opening(self, file_name, full_path, file_extension):
        """
        Open .pdf file on MacOS Preview.
        
        Args:
            file_name (str): Basename of the file to open.
            full_path (str): Full path of the file to open, including basename.
            file_extension (str): File extension of the file to open.
        """
        print('--Abriendo archivo...\n')
        self.open_pdf_in_preview(full_path)
        if (self.other_action_required(file_name)):
            self.process_file(file_name, full_path, file_extension)
        else: 
            return
    

    def process_file_deletion(self, file_name, full_path):
        """
        Delete file
        
        Args:
            file_name (str): Basename of the file to open.
            full_path (str): Full path of the file to open, including basename.
        """
        os.remove(full_path)
        print('--Se eliminó el archivo ' + file_name + '\n')


    def open_pdf_in_preview(self, file_path):
        """
        Open pdf file using 'Preview' app for MacOS
        
        Args:
            file_path (str): Path to the file.
        """
        try:
            #Ejecutamos el comando 'open', con la aplicación (-a) 'Preview', indicando el path del archivo a abrir. check = True para lanzar excepción si falla.
            subprocess.run(['open', '-a', 'Preview', file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    
    def other_action_required(self, file_name):
        """
        After renaming or opening file with Preview, decide whether to process file again or move to the next one.
        
        Args:
            file_path (str): Path to the file.
        
        Returns:
            bool: Process file again.
        """
        print('¿Quiere realizar otra acción sobre el archivo ' + file_name + '? (y/n)')
        response = input()
        if (response == 'y'):
            return True 
        elif (response == 'n'):
            return False 
        else: 
            Exception('Respuesta inválida al preguntar por otra acción.')


    def get_file_extension(self, file_path):
        """
        Get the file extension from a file path.
        
        Args:
            file_path (str): Path to the file.
            
        Returns:
            str: File extension (including the dot).
        """
        # Get the base name of the file
        base_name = os.path.basename(file_path)
        
        # Split the file name and extension
        _, extension = os.path.splitext(base_name)
        
        return extension


    