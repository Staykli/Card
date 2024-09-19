import os

file_path = 'path/to/your/file'

# Перевірка, чи файл існує
if not os.path.exists(file_path):
    print("File does not exist")
else:
    # Перевірка прав доступу
    if os.access(file_path, os.R_OK):
        print("Read access granted")
    else:
        print("Read access denied")

    if os.access(file_path, os.W_OK):
        print("Write access granted")
    else:
        print("Write access denied")

    if os.access(file_path, os.X_OK):
        print("Execute access granted")
    else:
        print("Execute access denied")