class EmptyFileError(Exception):
    pass

def read_file_safely():
    try:
        filename = input("Enter file name to read: ")
        f = open(filename, "r")
        content = f.read()
        if not content.strip():
            raise EmptyFileError("This File is Empty")
    except FileNotFoundError:
        print("❌ FIle not found! PLease check file name and try again.")
    except PermissionError:
        print("❌ You do not have permission to open this file")
    except EmptyFileError as e:
        print("⚠️ ", e)
    else:
        print("\nFile Content:\n")
        print(content)
    finally:
        try:
            f.close()
            print("\n📁 File closed successfully.")
        except:
            print("\n(No file was opened.)")

read_file_safely()
