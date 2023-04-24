from capstone import Cs, CS_ARCH_X86, CS_MODE_64, CS_MODE_32, CS_MODE_16

def convert_bin_to_asm(bin_path, output_file):
    # Load the binary file
    with open(bin_path, 'rb') as f:
        binary = f.read()

    # Initialize Capstone disassembler
    print("Select the architecture mode:")
    print("1. 64-bit")
    print("2. 32-bit")
    print("3. 16-bit")
    mode_choice = int(input("Enter your choice: "))
    if mode_choice == 1:
        md = Cs(CS_ARCH_X86, CS_MODE_64)
    elif mode_choice == 2:
        md = Cs(CS_ARCH_X86, CS_MODE_32)
    elif mode_choice == 3:
        md = Cs(CS_ARCH_X86, CS_MODE_16)
    else:
        print("Invalid choice. Defaulting to 64-bit mode.")
        md = Cs(CS_ARCH_X86, CS_MODE_64)

    # Disassemble the binary code into assembly instructions
    asm_code = ''
    for insn in md.disasm(binary, 0x0):
        asm_code += f'0x{insn.address:x}: {insn.mnemonic} {insn.op_str}\n'

    # Write the assembly code to the output file
    with open(output_file, 'w') as f:
        f.write(asm_code)

    print(f'Successfully converted {bin_path} to {output_file}.')

# Example usage
bin_path = input("Enter the path to the .bin file you want to convert: ")
output_file = input("Enter the path to the output file where the assembly code will be written: ")
convert_bin_to_asm(bin_path, output_file)
