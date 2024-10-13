# Write a custom context manager using with in Python to manage file resources (opening, processing, and closing files).

class FileManager:
    def __init__(self, file_path, mode):
        """
        Initializes the file manager with the file path and mode
        """
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        """
        Opens the file and returns the file object
        """
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes the file
        """
        if self.file:
            self.file.close()

def process_file(file_manager):
    """
    Processes the file by reading its contents
    """
    with file_manager as file:
        contents = file.read()
        print(f"File contents: {contents}")

def main():
    file_path = "example.txt"
    mode = "r"

    file_manager = FileManager(file_path, mode)
    process_file(file_manager)

if __name__ == "__main__":
    main()