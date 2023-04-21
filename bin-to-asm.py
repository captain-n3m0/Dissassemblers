from capstone import Cs, CS_ARCH_X86, CS_MODE_64, CS_MODE_32, CS_MODE_16

def convert_bin_to_asm(bin_path, output_file):
    # Load the binary file
    with open(bin_path, 'rb') as f:
        binary = f.read()

    # Initialize Capstone disassembler
    md = Cs(CS_ARCH_X86, CS_MODE_64)  # Set the architecture and mode according to your binary

    # Disassemble the binary code into assembly instructions
    asm_code = ''
    for insn in md.disasm(binary, 0x0):
        asm_code += f'0x{insn.address:x}: {insn.mnemonic} {insn.op_str}\n'

    # Write the assembly code to the output file
    with open(output_file, 'w') as f:
        f.write(asm_code)

    print(f'Successfully converted {bin_path} to {output_file}.')

# Example usage
bin_path = 'example.bin'  # Path to the .bin file you want to convert
output_file = 'output.asm'  # Path to the output file where the assembly code will be written
convert_bin_to_asm(bin_path, output_file)
