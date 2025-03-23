# libcpu/assembler.py

def assemble_instruction(instruction):
    """Assemble a single instruction into machine-readable format"""
    # In this case, we're just parsing the instruction string.
    # You can expand this to create a true machine-code assembler.

    parts = instruction.split()
    cmd = parts[0]
    if cmd in ['MOV', 'ADD', 'SUB', 'JMP']:
        return instruction
    else:
        raise ValueError(f"Unsupported instruction: {cmd}")
