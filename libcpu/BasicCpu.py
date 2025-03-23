# libcpu/BasicCpu.py

class BasicCpu:
    def __init__(self):
        self.registers = [0] * 8  # 8 registers, each 32-bit wide
        self.pc = 0  # Program Counter (32-bit)
        self.flags = {'zero': 0, 'carry': 0, 'overflow': 0, 'sign': 0, 'parity': 0}

    def mov(self, reg, value):
        """Move value into register"""
        self.registers[reg] = value

    def add(self, reg1, reg2):
        """Add reg2 to reg1 and update flags"""
        result = self.registers[reg1] + self.registers[reg2]
        self.flags['carry'] = 1 if result > 0xFFFFFFFF else 0  # 32-bit overflow check
        self.flags['zero'] = 1 if result == 0 else 0
        self.registers[reg1] = result & 0xFFFFFFFF  # 32-bit result

    def sub(self, reg1, reg2):
        """Subtract reg2 from reg1 and update flags"""
        result = self.registers[reg1] - self.registers[reg2]
        self.flags['carry'] = 1 if result < 0 else 0
        self.flags['zero'] = 1 if result == 0 else 0
        self.registers[reg1] = result & 0xFFFFFFFF

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

        # Check if the instruction has enough parts
        if len(parts) < 2:
            print(f"Error: Invalid instruction '{instruction}', not enough parts.")
            return

        cmd = parts[0]

        if cmd == 'MOV':
            if len(parts) != 3:
                print(f"Error: Invalid MOV instruction format '{instruction}'.")
                return
            reg = int(parts[1][1])  # Extract register number (e.g., EAX -> 0)
            value = int(parts[2])
            self.mov(reg, value)

        elif cmd == 'ADD':
            if len(parts) != 3:
                print(f"Error: Invalid ADD instruction format '{instruction}'.")
                return
            try:
                reg1 = int(parts[1][1])  # Extract first register number
                reg2 = int(parts[2][1])  # Extract second register number
                self.add(reg1, reg2)
            except ValueError:
                print(f"Error: Invalid register format in ADD instruction '{instruction}'.")
                return

        elif cmd == 'SUB':
            if len(parts) != 3:
                print(f"Error: Invalid SUB instruction format '{instruction}'.")
                return
            try:
                reg1 = int(parts[1][1])  # Extract first register number
                reg2 = int(parts[2][1])  # Extract second register number
                self.sub(reg1, reg2)
            except ValueError:
                print(f"Error: Invalid register format in SUB instruction '{instruction}'.")
                return

        elif cmd == 'CMP':
            if len(parts) != 3:
                print(f"Error: Invalid CMP instruction format '{instruction}'.")
                return
            try:
                reg1 = int(parts[1][1])  # Extract first register number
                reg2 = int(parts[2][1])  # Extract second register number
                self.cmp(reg1, reg2)
            except ValueError:
                print(f"Error: Invalid register format in CMP instruction '{instruction}'.")
                return

        elif cmd == 'JMP':
            if len(parts) != 2:
                print(f"Error: Invalid JMP instruction format '{instruction}'.")
                return
            try:
                address = int(parts[1])
                self.jmp(address)
            except ValueError:
                print(f"Error: Invalid address format in JMP instruction '{instruction}'.")
                return
