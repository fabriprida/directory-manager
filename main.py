import os
import subprocess

def get_file_extension(file_path):
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

def open_pdf_in_preview(pdf_file):
    try:
        # Use the open command to open the PDF file in Preview
        #Queremos ejecutar el comando 'open', luego con '-a' decimos que lo que viene a continuación es la aplicación con la cual queremos abrir 
        #el archivo, luego indicamos que la aplicación sea 'Preview' y por último le pasamos el archivo. 
        #El check = True es para que tira la excepción en caso de fallar.
        subprocess.run(['open', '-a', 'Preview', pdf_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def delete_files():
    files = os.listdir('/Users/fabrizioprida/Downloads')
    files.sort()
    
    for file in files: 
        print('--------------------------------------------------------')
        file_extension = get_file_extension(file)
        full_path = os.path.join('/Users/fabrizioprida/Downloads', file)

        if (file_extension == '.pdf'):
            print('¿Desea ver el contenido del archivo: ' + file + ' (y/n)')
            response_for_opening = input()
            if (response_for_opening == 'y'):
                 open_pdf_in_preview(full_path)
            elif (response_for_opening == 'n'):
                pass
            else: 
                raise Exception("Se ingresó una respuesta inválida")
        
        print('¿Desea borrar el archivo: ' + file + '? (y/n)')
        response_for_deletion = input()
        if (response_for_deletion == 'y'):
            os.remove(full_path)
        elif (response_for_deletion == 'n'):
            print('¿Desea cambiar el nombre del archivo: ' + file + '? (y/n)')
            response_for_renaming = input()
            if (response_for_renaming == 'y'):
                print('Introduzca el nuevo nombre: ')
                new_name = input()
                new_path = '/Users/fabrizioprida/Downloads/' + new_name + file_extension
                os.rename(full_path, new_path)
                print('Se cambió el nombre del archivo ' + file + ' por: ' + os.path.basename(new_path))
        else: 
            raise Exception("Se ingresó una respuesta inválida")





        

delete_files()
