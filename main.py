import sys
from bin_to_asm import convert_bin_to_asm
from exe_to_asm import convert_exe_to_asm

print("Select the conversion type:")
print("1. Binary to assembly")
print("2. Executable to assembly")
conversion=input("Enter choice: ")
if conversion=="1":
    file_path=input("Enter the path to the .bin file you want to convert: ")
    output_file=input("Enter the path to the output file where the assembly code will be written: ")
    convert_bin_to_asm(file_path,output_file)
    print("File saved to desired path")
elif conversion=="2":
    file_path=input("Enter the path to the .exe file you want to convert: ")
    output_file=input("Enter the path to the output file where the assembly code will be written: ")
    convert_exe_to_asm(file_path,output_file)
    print("File saved to desired path")
else:
    print("Invalid choice")
    print("The programme will now exit")
    sys.exit()