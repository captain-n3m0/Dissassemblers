import subprocess

def convert_exe_to_asm(exe_path, output_file):
    # Run objdump command to disassemble the binary code into assembly language
    print("Select the disassembly style:")
    print("1. Intel")
    print("2. AT&T")
    style_choice = int(input("Enter your choice: "))
    if style_choice == 1:
        cmd = ['objdump', '-d', '-M', 'intel', exe_path]
    elif style_choice == 2:
        cmd = ['objdump', '-d', '-M', 'att', exe_path]
    else:
        print("Invalid choice. Defaulting to Intel style.")
        cmd = ['objdump', '-d', '-M', 'intel', exe_path]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    if process.returncode == 0:
        # Write the assembly code to the output file
        with open(output_file, 'w') as f:
            f.write(output.decode())
        print(f'Successfully converted {exe_path} to {output_file}.')
    else:
        print(f'Error converting {exe_path} to assembly code: {error.decode()}')

# Example usage
exe_path = input("Enter the path to the .exe file you want to convert: ")
output_file = input("Enter the path to the output file where the assembly code will be written: ")
convert_exe_to_asm(exe_path, output_file)
