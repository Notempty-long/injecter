# libcpu/SimpleCpu.py

class SimpleCpu:
    def __init__(self):
        self.registers = [0] * 8  # 8 registers, each 16-bit wide
        self.pc = 0  # Program Counter (16-bit)
        self.flags = {'zero': 0, 'carry': 0, 'overflow': 0}
        self.memory = [0] * 65536  # 64KB of memory
        self.stack_pointer = 0xFF00  # Stack pointer initialization

    def mov(self, reg, value):
        """Move value into register"""
        self.registers[reg] = value

    def add(self, reg1, reg2):
        """Add reg2 to reg1 and update flags"""
        result = self.registers[reg1] + self.registers[reg2]
        self.flags['carry'] = 1 if result > 0xFFFF else 0  # 16-bit overflow check
        self.flags['zero'] = 1 if result == 0 else 0
        self.registers[reg1] = result & 0xFFFF  # 16-bit result

    def sub(self, reg1, reg2):
        """Subtract reg2 from reg1 and update flags"""
        result = self.registers[reg1] - self.registers[reg2]
        self.flags['carry'] = 1 if result < 0 else 0
        self.flags['zero'] = 1 if result == 0 else 0
        self.registers[reg1] = result & 0xFFFF

    def jmp(self, address):
        """Jump to a specific address"""
        self.pc = address

    def execute_instruction(self, instruction):
        """Interpret and execute an instruction"""
        parts = instruction.split()
        cmd = parts[0]

        if cmd == 'MOV':
            reg = int(parts[1][1])  # Extract register number (e.g., A -> 0)
            value = int(parts[2])
            self.mov(reg, value)

        elif cmd == 'ADD':
            reg1 = int(parts[1][1])  # Extract register number (e.g., A -> 0)
            reg2 = int(parts[2][1])
            self.add(reg1, reg2)

        elif cmd == 'SUB':
            reg1 = int(parts[1][1])
            reg2 = int(parts[2][1])
            self.sub(reg1, reg2)

        elif cmd == 'JMP':
            address = int(parts[1])
            self.jmp(address)
