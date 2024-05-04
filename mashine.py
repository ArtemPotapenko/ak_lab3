from isa import *

input_list: list[Union[int, chr]] = []
input_index: int = 0
start: int = 0

registers: dict[Register, Union[float, chr]] = {}
flags: dict[Flags, bool] = {Flags.NF: False, Flags.ZF: False}
memory: list[int]


def set_flag(result: float):
    global flags
    flags[Flags.NF] = result < 0
    flags[Flags.ZF] = result == 0


def parse(instr: list[Instruction]):
    global input_list, input_index
    ip = start
    while ip < len(instr):
        if instr[ip].op == Opcode.ADD:
            first = registers[instr[ip].first] if instr[ip].first is Register else float(instr[ip].first)
            second = registers[instr[ip].second] if instr[ip].second is Register else float(instr[ip].second)
            registers[instr[ip].third] = first + second
            set_flag(first + second)
        if instr[ip].op == Opcode.SUB:
            first = registers[instr[ip].first] if instr[ip].first is Register else float(instr[ip].first)
            second = registers[instr[ip].second] if instr[ip].second is Register else float(instr[ip].second)
            set_flag(first - second)
        if instr[ip].op == Opcode.MUL:
            first = registers[instr[ip].first] if instr[ip].first is Register else float(instr[ip].first)
            second = registers[instr[ip].second] if instr[ip].second is Register else float(instr[ip].second)
            registers[instr[ip].third] = first * second
            set_flag(first * second)
        if instr[ip].op == Opcode.DIV:
            first = registers[instr[ip].first] if instr[ip].first is Register else float(instr[ip].first)
            second = registers[instr[ip].second] if instr[ip].second is Register else float(instr[ip].second)
            registers[instr[ip].third] = first / second
            set_flag(first / second)
        if instr[ip].op == Opcode.MOD:
            first = registers[instr[ip].first] if instr[ip].first is Register else float(instr[ip].first)
            second = registers[instr[ip].second] if instr[ip].second is Register else float(instr[ip].second)
            registers[instr[ip].third] = first % second
            set_flag(first % second)
        if instr[ip].op == Opcode.CMP:
            first = registers[instr[ip].first] if instr[ip].first is Register else float(instr[ip].first) if is_number(
                instr[ip].first) else instr[ip]
            second = registers[instr[ip].second] if instr[ip].second is Register else float(instr[ip].second) if is_number(
                instr[ip].first) else instr[ip]
            set_flag(first - second)
        if instr[ip].op == Opcode.LD:
            first = memory[instr[ip].first[1::]] if instr[ip].first[0] == "#" else instr[ip] if instr[ip].first[
                                                                                                    0] == "'" else float(
                instr[ip].first)
            registers[instr[ip].second] = first
        if instr[ip].op == Opcode.ST:
            first = registers[instr[ip].first] if instr[ip].first is Register else instr[ip] if instr[ip].first[
                                                                                                    0] == "'" else float(
                instr[ip].first)
            memory[int(instr[ip].second)] = first
        if instr[ip].op == Opcode.JMP:
            arg = registers[instr[ip].first] if instr[ip].first is Register else int(instr[ip].first)
            ip = int(arg)
            continue
        if instr[ip].op == Opcode.PRINT:
            arg = registers[instr[ip].first] if instr[ip].first is Register else instr[ip].first if is_number(
                instr[ip].first) else instr[ip].first[1]
            print(arg, end='')
        if instr[ip].op == Opcode.JNL:
            if not (flags[Flags.NF]):
                arg = registers[instr[ip].first] if instr[ip].first is Register else int(instr[ip].first)
                ip = int(arg)
                continue
        if instr[ip].op == Opcode.JG:
            if not (flags[Flags.NF]) and not (flags[Flags.ZF]):
                arg = registers[instr[ip].first] if instr[ip].first is Register else int(instr[ip].first)
                ip = int(arg)
                continue
        if instr[ip].op == Opcode.JE:
            if flags[Flags.ZF]:
                arg = registers[instr[ip].first] if instr[ip].first is Register else int(instr[ip].first)
                ip = int(arg)
                continue
        if instr[ip].op == Opcode.JNE:
            if not (flags[Flags.ZF]):
                arg = registers[instr[ip].first] if instr[ip].first is Register else int(instr[ip].first)
                ip = int(arg)
                continue
        if instr[ip].op == Opcode.JNG:
            if flags[Flags.NF] or flags[Flags.ZF]:
                arg = registers[instr[ip].first] if instr[ip].first is Register else int(instr[ip].first)
                ip = int(arg)
                continue
        if instr[ip].op == Opcode.JL:
            if flags[Flags.NF] or not (flags[Flags.ZF]):
                arg = registers[instr[ip].first] if instr[ip].first is Register else int(instr[ip].first)
                ip = int(arg)
                continue
        if instr[ip].op == Opcode.READ:
            registers[instr[ip].first] = input_list[input_index]
            input_index += 1
        if instr[ip].op == Opcode.HLT:
            break
        if instr[ip].op == Opcode.INC:
            registers[instr[ip].first] += 1
        ip += 1
