# libcpu/AdvanceCpu.py

import psutil

class AdvanceCpu:
    def __init__(self):
        # Get total physical memory in bytes
        total_memory = psutil.virtual_memory().total
        
        # Subtract the used memory (for other processes or system overhead)
        available_memory = psutil.virtual_memory().available

        # Dynamically allocate memory based on available memory
        # For this example, we take 75% of available memory (You can adjust this as needed)
        allocated_memory = int(available_memory * 0.75)  # Take 75% of available memory

        # Set memory allocation (divide by 8 because 1 item represents 8 bytes)
        self.memory = [0] * (allocated_memory // 8)  # 64-bit values (8 bytes per item)
        
        # Initialize registers and other CPU components
        self.registers = [0] * 16  # 16 registers, each 64-bit wide
        self.pc = 0  # Program Counter (64-bit)
        self.flags = {'zero': 0, 'carry': 0, 'overflow': 0, 'sign': 0, 'parity': 0}
        self.stack_pointer = 0x8000000000000000  # Stack pointer initialization

    def mov(self, reg, value):
        """Move value into register"""
        self.registers[reg] = value

    def add(self, reg1, reg2):
        """Add reg2 to reg1 and update flags"""
        result = self.registers[reg1] + self.registers[reg2]
        self.flags['carry'] = 1 if result > 0xFFFFFFFFFFFFFFFF else 0  # 64-bit overflow check
        self.flags['zero'] = 1 if result == 0 else 0
        self.registers[reg1] = result & 0xFFFFFFFFFFFFFFFF  # 64-bit result

    def sub(self, reg1, reg2):
        """Subtract reg2 from reg1 and update flags"""
        result = self.registers[reg1] - self.registers[reg2]
        self.flags['carry'] = 1 if result < 0 else 0
        self.flags['zero'] = 1 if result == 0 else 0
        self.registers[reg1] = result & 0xFFFFFFFFFFFFFFFF

    def cmp(self, reg1, reg2):
        """Compare two registers (set flags accordingly)"""
        result = self.registers[reg1] - self.registers[reg2]
        self.flags['zero'] = 1 if result == 0 else 0
        self.flags['carry'] = 1 if result < 0 else 0

    def jmp(self, address):
        """Jump to a specific address"""
        self.pc = address

    def execute_instruction(self, instruction):
        """Interpret and execute an instruction"""
        parts = instruction.split()
        cmd = parts[0]

        if cmd == 'MOV':
            reg = int(parts[1][1])  # Extract register number (e.g., RAX -> 0)
            value = int(parts[2])
            self.mov(reg, value)

        elif cmd == 'ADD':
            reg1 = int(parts[1][1])
            reg2 = int(parts[2][1])
            self.add(reg1, reg2)

        elif cmd == 'SUB':
            reg1 = int(parts[1][1])
            reg2 = int(parts[2][1])
            self.sub(reg1, reg2)

        elif cmd == 'CMP':
            reg1 = int(parts[1][1])
            reg2 = int(parts[2][1])
            self.cmp(reg1, reg2)

        elif cmd == 'JMP':
            address = int(parts[1])
            self.jmp(address)
