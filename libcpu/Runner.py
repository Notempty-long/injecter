# libcpu/runner.py

from libcpu.SimpleCpu import SimpleCpu
from libcpu.BasicCpu import BasicCpu
from libcpu.AdvanceCpu import AdvanceCpu
from libcpu.assembler import assemble_instruction
from libcpu.Excuter import Executer

def run():
    print("Starting CPU Emulator")

    # Initialize different CPUs
    simple_cpu = SimpleCpu()
    basic_cpu = BasicCpu()
    advance_cpu = AdvanceCpu()

    # Example instruction set to execute
    instructions = [
        "MOV A 10",
        "ADD A B",
        "JMP 100",
        "MOV A 5",
    ]
    
    # Choose a CPU to run the instructions on
    cpu = basic_cpu  # Example: Using BasicCpu
    
    # Execute instructions
    executer = Executer(cpu)
    for instruction in instructions:
        assembled_instruction = assemble_instruction(instruction)
        executer.execute(assembled_instruction)
        
    print("Emulation complete!")
