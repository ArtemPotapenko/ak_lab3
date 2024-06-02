import sys

from isa import *

memory = []


class ControlUnit:
    class Tick:
        tick_number: int
        registers: dict[Register, Union[int, chr, int]]
        NF: bool
        ZF: bool

        def __init__(self, tick_number: int, registers: dict[Register, Union[int, chr, int]], NF: bool, ZF: bool):
            self.tick_number = tick_number
            self.registers = registers
            self.NF = NF
            self.ZF = ZF

        def __str__(self):
            s = "<tick_number: " + str(self.tick_number) + ";"
            for x in self.registers:
                s += x + ": " + str(self.registers[x]) + ";"
            s += "NF: " + str(self.NF) + ";ZF: " + str(self.ZF) + ">"
            return s

    input_list: list[Union[int, chr]] = []
    max_tick = None
    memory: list[int]
    tick_number = 0
    instruction_count = 0
    ticks: list[Tick] = []
    start: int = 4096
    registers: dict[Register, Union[int, chr, int]] = {}

    def __init__(self):
        for reg in Register:
            self.registers[Register(reg)] = 0
        self.registers[Register.SP] = 8191

    flags: dict[Flags, bool] = {Flags.NF: False, Flags.ZF: False}
    code: list[Instruction] = []

    def tick(self):
        self.tick_number += 1
        self.ticks.append(
            self.Tick(self.tick_number, self.registers.copy(), self.flags[Flags.NF], self.flags[Flags.ZF]))

    def set_flag(self, result: int):
        self.flags[Flags.NF] = result < 0
        self.flags[Flags.ZF] = result == 0

    def parse(self, instr: list[Instruction]):
        ip = self.start
        input_index: int = 0
        while ip < len(instr):
            self.instruction_count += 1
            self.registers[Register.IP] = ip

            self.tick()
            if self.tick == self.max_tick:
                return

            self.registers[Register.CR] = instr[ip]

            self.tick()
            if self.tick == self.max_tick:
                return

            if instr[ip].op == Opcode.ADD:
                first = self.registers[instr[ip].first] if instr[ip].first in Register else instr[ip].first
                second = self.registers[instr[ip].second] if instr[ip].second in Register else instr[ip].second
                self.registers[instr[ip].third] = first + second

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.set_flag(first + second)

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.SUB:
                first = self.registers[instr[ip].first] if instr[ip].first in Register else instr[ip].first
                second = self.registers[instr[ip].second] if instr[ip].second in Register else instr[ip].second
                self.registers[instr[ip].third] = first - second

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.set_flag(first - second)

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.MUL:
                first = self.registers[instr[ip].first] if instr[ip].first in Register else instr[ip].first
                second = self.registers[instr[ip].second] if instr[ip].second in Register else instr[ip].second
                self.registers[instr[ip].third] = first * second

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.set_flag(first * second)

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.DIV:
                first = self.registers[instr[ip].first] if instr[ip].first in Register else instr[ip].first
                second = self.registers[instr[ip].second] if instr[ip].second in Register else instr[ip].second
                self.registers[instr[ip].third] = first // second

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.set_flag(first // second)

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.MOD:
                first = self.registers[instr[ip].first] if instr[ip].first in Register else instr[ip].first
                second = self.registers[instr[ip].second] if instr[ip].second in Register else instr[ip].second
                self.registers[instr[ip].third] = first % second

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.set_flag(first % second)

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.CMP:
                first = self.registers[instr[ip].first] if instr[ip].first in Register else instr[ip].first
                second = self.registers[instr[ip].second] if instr[ip].second in Register else instr[ip].second
                first = ord(first) if type(first) == str else first
                second = ord(second) if type(second) == str else second
                self.set_flag(first - second)

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.LD:

                first = instr[ip].first

                if not (is_number(instr[ip].first)):
                    adr = int(self.registers[instr[ip].first]) if instr[ip].first in Register else int(
                        instr[ip].first[1::])
                    self.registers[Register.DR] = adr

                    self.tick()
                    if self.tick == self.max_tick:
                        return

                    first = memory[adr]

                self.registers[instr[ip].second] = first

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.ST:
                first = self.registers[instr[ip].first] if instr[ip].first in Register else instr[ip].first
                second = self.registers[instr[ip].second] if instr[ip].second in Register else int(
                    instr[ip].second[1::])
                self.registers[Register.DR] = second

                self.tick()
                if self.tick == self.max_tick:
                    return

                memory[second] = first

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.JMP:
                arg = self.registers[instr[ip].first] if instr[ip].first in Register else int(instr[ip].first)
                ip = int(arg)
                continue
            if instr[ip].op == Opcode.PRINT:
                arg = self.registers[instr[ip].first] if instr[ip].first in Register else instr[ip].first if is_number(
                    instr[ip].first) else instr[ip].first
                if type(arg) == int:
                    print(chr(arg), end='')
                else:
                    print(arg, end='')
                self.tick()
                if self.tick == self.max_tick:
                    return
            if instr[ip].op == Opcode.PUSH:
                first = self.registers[instr[ip].first] if instr[ip].first in Register else instr[ip].first
                self.registers[Register.DR] = self.registers[Register.SP]

                self.tick()
                if self.tick == self.max_tick:
                    return

                memory[self.registers[Register.DR]] = first

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.registers[Register.SP] -= 1

                self.tick()
                if self.tick == self.max_tick:
                    return
            if instr[ip].op == Opcode.POP:

                self.registers[Register.SP] += 1

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.registers[Register.DR] = self.registers[Register.SP]

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.registers[instr[ip].first] = memory[self.registers[Register.DR]]

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.JNL:
                if not (self.flags[Flags.NF]):
                    arg = self.registers[instr[ip].first] if instr[ip].first in Register else int(instr[ip].first)
                    ip = int(arg)
                    continue
            if instr[ip].op == Opcode.JG:
                if not (self.flags[Flags.NF]) and not (self.flags[Flags.ZF]):
                    arg = self.registers[instr[ip].first] if instr[ip].first in Register else int(instr[ip].first)
                    ip = int(arg)
                    continue
            if instr[ip].op == Opcode.JE:
                if self.flags[Flags.ZF]:
                    arg = self.registers[instr[ip].first] if instr[ip].first in Register else int(instr[ip].first)
                    ip = int(arg)
                    continue
            if instr[ip].op == Opcode.JNE:
                if not (self.flags[Flags.ZF]):
                    arg = self.registers[instr[ip].first] if instr[ip].first in Register else int(instr[ip].first)
                    ip = int(arg)
                    continue
            if instr[ip].op == Opcode.JNG:
                if not (self.flags[Flags.NF]) or self.flags[Flags.ZF]:
                    arg = self.registers[instr[ip].first] if instr[ip].first in Register else int(instr[ip].first)
                    ip = int(arg)
                    continue
            if instr[ip].op == Opcode.JL:
                if self.flags[Flags.NF]:
                    arg = self.registers[instr[ip].first] if instr[ip].first in Register else int(instr[ip].first)
                    ip = int(arg)
                    continue
            if instr[ip].op == Opcode.READ:
                self.registers[instr[ip].first] = self.input_list[input_index]
                input_index += 1

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.HLT:

                self.tick()
                if self.tick == self.max_tick:
                    return

                break
            if instr[ip].op == Opcode.INC:
                self.registers[Register.DR] = memory[int(instr[ip].first[1::])]
                self.tick()
                if self.tick == self.max_tick:
                    return

                self.registers[Register.R1] = memory[int(instr[ip].first[1::])]
                self.tick()
                if self.tick == self.max_tick:
                    return

                self.registers[Register.R1] = memory[int(instr[ip].first[1::])] + 1

                self.tick()
                if self.tick == self.max_tick:
                    return

                memory[int(instr[ip].first[1::])] = self.registers[Register.R1]
                self.tick()
                if self.tick == self.max_tick:
                    return

            ip += 1


def main(source, ticks_file, input_file):
    global memory
    memory = [Instruction(Opcode.NOPE, 0)] * 8192
    instr_list: list[Instruction] = read_code(source)
    for x in instr_list:
        if x.op == Opcode.WORD:
            memory[x.memory] = ord(x.first)
        else:
            memory[x.memory] = x
    cu = ControlUnit()
    with open(input_file, encoding="utf-8") as file:
        s = file.read()
        for i in range(len(s)):
            cu.input_list.append(s[i])
        cu.input_list.append('\0')
    cu.parse(memory)
    with open(ticks_file, "w") as file:
        for x in cu.ticks:
            file.write(str(x) + "\n")
        file.write("\n")
        file.write("\n")
        file.write("ticks: " + str(cu.tick_number) + "\n" + "instructions: " + str(cu.instruction_count))


if __name__ == "__main__":
    assert len(sys.argv) == 4, "Wrong arguments: machine.py <input_file> <target_file> <input>"
    main(sys.argv[1], sys.argv[2], sys.argv[3])
