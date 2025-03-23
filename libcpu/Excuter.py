# libcpu/executer.py

class Executer:
    def __init__(self, cpu):
        self.cpu = cpu

    def execute(self, instruction):
        """Execute a single instruction"""
        self.cpu.execute_instruction(instruction)
