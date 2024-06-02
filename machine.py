import sys

from isa import (
    Register,
    Flags,
    Opcode,
    Instruction,
    Union,
    is_number,
    read_code,
    registers_name,
)


class DataPath:
    input_list: list[Union[int, chr]] = []
    memory: list[int]
    registers: dict[Register, Union[int, chr, int]] = {}
    flags: dict[Flags, bool]

    def set_flag(self, result: int):
        self.flags[Flags.NF] = result < 0
        self.flags[Flags.ZF] = result == 0

    def __init__(self):
        for reg in Register:
            self.registers[Register(reg)] = 0
        self.registers[Register.SP] = 8191
        self.memory = [Instruction(Opcode.NOPE, 0)] * 8192
        self.input_list = []
        self.flags = {Flags.NF: False, Flags.ZF: False}


class ControlUnit:
    class Tick:
        tick_number: int

        def __init__(
                self,
                tick_number: int,
                registers: dict[Register, Union[int, chr, int]],
                NF: bool,
                ZF: bool,
        ):
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

    max_tick = None
    tick_number = 0
    instruction_count = 0
    ticks: list[Tick] = []
    start: int = 4096

    def __init__(self, data: DataPath):
        self.data = data
        self.ticks = []
        self.tick_number = 0
        self.start = 4096
        self.instruction_count = 0

    def tick(self):
        self.tick_number += 1
        self.ticks.append(
            self.Tick(
                self.tick_number,
                self.data.registers.copy(),
                self.data.flags[Flags.NF],
                self.data.flags[Flags.ZF],
            )
        )

    def parse(self, instr: list[Instruction]):
        ip = self.start
        input_index: int = 0
        while ip < len(instr):
            self.instruction_count += 1
            self.data.registers[Register.IP] = ip

            self.tick()
            if self.tick == self.max_tick:
                return

            self.data.registers[Register.CR] = instr[ip]

            self.tick()
            if self.tick == self.max_tick:
                return

            if instr[ip].op == Opcode.ADD:
                first = (
                    self.data.registers[instr[ip].first]
                    if instr[ip].first in registers_name
                    else instr[ip].first
                )
                second = (
                    self.data.registers[instr[ip].second]
                    if instr[ip].second in registers_name
                    else instr[ip].second
                )
                self.data.registers[instr[ip].third] = first + second

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.data.set_flag(first + second)

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.SUB:
                first = (
                    self.data.registers[instr[ip].first]
                    if instr[ip].first in registers_name
                    else instr[ip].first
                )
                second = (
                    self.data.registers[instr[ip].second]
                    if instr[ip].second in registers_name
                    else instr[ip].second
                )
                self.data.registers[instr[ip].third] = first - second

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.data.set_flag(first - second)

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.MUL:
                first = (
                    self.data.registers[instr[ip].first]
                    if instr[ip].first in registers_name
                    else instr[ip].first
                )
                second = (
                    self.data.registers[instr[ip].second]
                    if instr[ip].second in registers_name
                    else instr[ip].second
                )
                self.data.registers[instr[ip].third] = first * second

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.data.set_flag(first * second)

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.DIV:
                first = (
                    self.data.registers[instr[ip].first]
                    if instr[ip].first in registers_name
                    else instr[ip].first
                )
                second = (
                    self.data.registers[instr[ip].second]
                    if instr[ip].second in registers_name
                    else instr[ip].second
                )
                self.data.registers[instr[ip].third] = first // second

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.data.set_flag(first // second)

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.MOD:
                first = (
                    self.data.registers[instr[ip].first]
                    if instr[ip].first in registers_name
                    else instr[ip].first
                )
                second = (
                    self.data.registers[instr[ip].second]
                    if instr[ip].second in registers_name
                    else instr[ip].second
                )
                self.data.registers[instr[ip].third] = first % second

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.data.set_flag(first % second)

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.CMP:
                first = (
                    self.data.registers[instr[ip].first]
                    if instr[ip].first in registers_name
                    else instr[ip].first
                )
                second = (
                    self.data.registers[instr[ip].second]
                    if instr[ip].second in registers_name
                    else instr[ip].second
                )
                first = ord(first) if isinstance(first, str) else first
                second = ord(second) if isinstance(second, str) else second
                self.data.set_flag(first - second)

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.LD:
                first = instr[ip].first

                if not (is_number(instr[ip].first)):
                    adr = (
                        int(self.data.registers[instr[ip].first])
                        if instr[ip].first in registers_name
                        else int(instr[ip].first[1::])
                    )
                    self.data.registers[Register.DR] = adr

                    self.tick()
                    if self.tick == self.max_tick:
                        return

                    first = self.data.memory[adr]

                self.data.registers[instr[ip].second] = first

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.ST:
                first = (
                    self.data.registers[instr[ip].first]
                    if instr[ip].first in registers_name
                    else instr[ip].first
                )
                second = (
                    self.data.registers[instr[ip].second]
                    if instr[ip].second in registers_name
                    else int(instr[ip].second[1::])
                )
                self.data.registers[Register.DR] = second

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.data.memory[second] = first

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.JMP:
                arg = (
                    self.data.registers[instr[ip].first]
                    if instr[ip].first in registers_name
                    else int(instr[ip].first)
                )
                ip = int(arg)
                continue
            if instr[ip].op == Opcode.PRINT:
                arg = (
                    self.data.registers[instr[ip].first]
                    if instr[ip].first in registers_name
                    else instr[ip].first
                    if is_number(instr[ip].first)
                    else instr[ip].first
                )
                if isinstance(arg, int):
                    print(chr(arg), end="")
                else:
                    print(arg, end="")
                self.tick()
                if self.tick == self.max_tick:
                    return
            if instr[ip].op == Opcode.PUSH:
                first = (
                    self.data.registers[instr[ip].first]
                    if instr[ip].first in registers_name
                    else instr[ip].first
                )
                self.data.registers[Register.DR] = self.data.registers[Register.SP]

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.data.memory[self.data.registers[Register.DR]] = first

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.data.registers[Register.SP] -= 1

                self.tick()
                if self.tick == self.max_tick:
                    return
            if instr[ip].op == Opcode.POP:
                self.data.registers[Register.SP] += 1

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.data.registers[Register.DR] = self.data.registers[Register.SP]

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.data.registers[instr[ip].first] = self.data.memory[self.data.registers[Register.DR]]

                self.tick()
                if self.tick == self.max_tick:
                    return

            if instr[ip].op == Opcode.JNL:
                if not (self.data.flags[Flags.NF]):
                    arg = (
                        self.data.registers[instr[ip].first]
                        if instr[ip].first in registers_name
                        else int(instr[ip].first)
                    )
                    ip = int(arg)
                    continue
            if instr[ip].op == Opcode.JG:
                if not (self.data.flags[Flags.NF]) and not (self.data.flags[Flags.ZF]):
                    arg = (
                        self.data.registers[instr[ip].first]
                        if instr[ip].first in registers_name
                        else int(instr[ip].first)
                    )
                    ip = int(arg)
                    continue
            if instr[ip].op == Opcode.JE:
                if self.data.flags[Flags.ZF]:
                    arg = (
                        self.data.registers[instr[ip].first]
                        if instr[ip].first in registers_name
                        else int(instr[ip].first)
                    )
                    ip = int(arg)
                    continue
            if instr[ip].op == Opcode.JNE:
                if not (self.data.flags[Flags.ZF]):
                    arg = (
                        self.data.registers[instr[ip].first]
                        if instr[ip].first in Register
                        else int(instr[ip].first)
                    )
                    ip = int(arg)
                    continue
            if instr[ip].op == Opcode.JNG:
                if not (self.data.flags[Flags.NF]) or self.data.flags[Flags.ZF]:
                    arg = (
                        self.data.registers[instr[ip].first]
                        if instr[ip].first in registers_name
                        else int(instr[ip].first)
                    )
                    ip = int(arg)
                    continue
            if instr[ip].op == Opcode.JL:
                if self.data.flags[Flags.NF]:
                    arg = (
                        self.data.registers[instr[ip].first]
                        if instr[ip].first in registers_name
                        else int(instr[ip].first)
                    )
                    ip = int(arg)
                    continue
            if instr[ip].op == Opcode.READ:
                self.data.registers[instr[ip].first] = self.data.input_list[input_index]
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
                self.data.registers[Register.DR] = self.data.memory[int(instr[ip].first[1::])]
                self.tick()
                if self.tick == self.max_tick:
                    return

                self.data.registers[Register.R1] = self.data.memory[int(instr[ip].first[1::])]
                self.tick()
                if self.tick == self.max_tick:
                    return

                self.data.registers[Register.R1] = self.data.memory[int(instr[ip].first[1::])] + 1

                self.tick()
                if self.tick == self.max_tick:
                    return

                self.data.memory[int(instr[ip].first[1::])] = self.data.registers[Register.R1]
                self.tick()
                if self.tick == self.max_tick:
                    return

            ip += 1


def main(source, ticks_file, input_file):
    instr_list: list[Instruction] = read_code(source)
    dp: DataPath = DataPath()

    for x in instr_list:
        if x.op == Opcode.WORD:
            dp.memory[x.memory] = ord(x.first)
        else:
            dp.memory[x.memory] = x
    cu = ControlUnit(dp)
    with open(input_file, encoding="utf-8") as file:
        s = file.read()
        for i in range(len(s)):
            cu.data.input_list.append(s[i])
        cu.data.input_list.append("\0")
    cu.parse(cu.data.memory)
    with open(ticks_file, "w") as file:
        for x in cu.ticks:
            file.write(str(x) + "\n")
        file.write("\n")
        file.write("\n")
        file.write(
            "ticks: "
            + str(cu.tick_number)
            + "\n"
            + "instructions: "
            + str(cu.instruction_count)
        )


if __name__ == "__main__":
    assert (
            len(sys.argv) == 4
    ), "Wrong arguments: machine.py <input_file> <target_file> <input>"
    main(sys.argv[1], sys.argv[2], sys.argv[3])
