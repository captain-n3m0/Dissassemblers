import subprocess

def convert_exe_to_asm(exe_path, output_file):
    # Run objdump command to disassemble the binary code into assembly language
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
exe_path = 'example.exe'  # Path to the .exe file you want to convert
output_file = 'output.asm'  # Path to the output file where the assembly code will be written
convert_exe_to_asm(exe_path, output_file)
