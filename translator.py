import re
import sys
from enum import Enum
from typing import Union

from isa import write_code, Instruction, Register, Opcode, is_number


class Type(str, Enum):
    string = "string"
    char = "char"
    number = "number"


class Variable:
    value = None
    type_value: Type = None

    def __init__(self, value=None, type_value=None):
        self.type_value = type_value
        self.value = value


START_VARIABLE_ADDRESS: int = 100
START_CODE_ADDRESS: int = 4096

current_variable_address = START_VARIABLE_ADDRESS
current_code_address = START_CODE_ADDRESS
variables: dict = {}

free_registers: list = [Register.R6, Register.R5, Register.R4, Register.R3, Register.R2, Register.R1]

variable_const: dict = {}

last_result = None
ar_var: dict = {}
code = []


def add_code(split_arr: list, op: Opcode) -> Union[Register, str]:
    global current_variable_address, current_code_address, last_result, code
    if split_arr[0][0] == 'r':
        free_registers.append(Register(split_arr[0]))
    if split_arr[1][0] == 'r':
        free_registers.append(Register(split_arr[1]))
    if len(free_registers) > 0:
        mem_to = free_registers[-1]
        free_registers.pop()
    else:
        mem_to = Register.DX
    first = to_register(split_arr[0], 1)
    second = to_register(split_arr[1] ,2)
    code.append(
        Instruction(op, current_code_address, first, second, mem_to))
    current_code_address += 1
    if mem_to == Register.DX:
        code.append(Instruction(Opcode.ST, current_code_address, "#" + str(current_variable_address)))
        current_variable_address += 1
        current_variable_address = current_variable_address + 1
    last_result = mem_to
    return mem_to


def to_register(s: str, number: int) -> Union[Register, str]:
    global current_variable_address, current_code_address, code
    if s[0] == "#":
        register = Register.BX if number == 1 else Register.BX if number == 2 else Register.DX
        code.append(Instruction(Opcode.LD, s, register))
        current_code_address += 1
        return register
    elif is_number(s[0]):
        return s
    if s in variables:
        register = Register.BX if number == 1 else Register.BX if number == 2 else Register.DX
        code.append(
            Instruction(Opcode.LD, current_code_address, "#" + str(variables[s].value), register))
        current_code_address += 1
        return register
    if s is Register:
        return Register(s)


def logic(log_str: str):
    global current_variable_address, current_code_address, code
    log_str = [x.strip() for x in re.split("[>=<!]", log_str) if len(x) != 0]
    arithmetic(log_str[0])
    first = last_result
    arithmetic(log_str[1])
    second = last_result
    code.append(Instruction(Opcode.CMP, current_code_address, first, second))
    current_code_address += 1


def arithmetic(arith_str: str):
    global current_variable_address, last_result, current_code_address, code
    if "read" in arith_str:
        last_result = free_registers[-1]
        return [Instruction(Opcode.READ, free_registers[-1])]
    start: int = -1
    count_s: int = 0
    i = 0
    while i < len(arith_str):
        if arith_str[i] == '(' and start == -1:
            start = i
            count_s += 1
        elif arith_str[i] == '(':
            count_s += 1
        elif arith_str[i] == ')':
            count_s -= 1
            if count_s == 0:
                arithmetic(arith_str[start + 1: i])
                arith_str = arith_str[:start] + last_result + arith_str[i + 1:]
                i = start
                start = -1
        i += 1
    while len(re.findall("[#r]?[0-9\\w.]+\\s*[*/+\\-%]\\s*[#r]?[0-9\\w.]+", arith_str)) > 0:
        if len(re.findall("[#r]?[0-9\\w.]+\\s*[*/%]\\s*[#r]?[0-9\\w.]+", arith_str)) > 0:
            arr = re.findall("[#r-]?[0-9\\w.]+\\s*[*/%]\\s*[#r]?[0-9\\w.]+", arith_str)[0]
            if arr[0] == '-' and arr != arith_str[:len(arr)]:
                arr = arr[1:]
            if (len(re.findall("\\*", arr))) > 0:
                split_arr = [x.strip() for x in re.split("\\*", arr)]
                mem_to = add_code(split_arr, Opcode.MUL)
                arith_str = arith_str.replace(arr, mem_to, 1)
            elif (len(re.findall("/", arith_str))) > 0:
                split_arr = [x.strip() for x in re.split("/", arr)]
                mem_to = add_code(split_arr, Opcode.DIV)
                arith_str = arith_str.replace(arr, mem_to, 1)
            else:
                split_arr = [x.strip() for x in re.split("%", arr)]
                mem_to = add_code(split_arr, Opcode.MOD)
                arith_str = arith_str.replace(arr, mem_to, 1)
        else:
            arr = re.findall("[-#r]?[0-9\\w.]+\\s*[-+]\\s*[#r]?[0-9\\w.]+", arith_str)[0]

            if arr[0] == '-' and arr != arith_str[:len(arr)]:
                arr = arr[1:]
            if (len(re.findall("\\+", arr))) > 0:
                split_arr = [x.strip() for x in re.split("\\+", arr)]
                mem_to = add_code(split_arr, Opcode.ADD)
                arith_str = arith_str.replace(arr, mem_to, 1)
            else:
                split_arr = [x.strip() for x in re.split("-", arr)]
                mem_to = add_code(split_arr, Opcode.SUB)
                arith_str = arith_str.replace(arr, mem_to, 1)
        last_result = mem_to
    if is_number(arith_str):
        if len(free_registers) > 0:
            mem_to = free_registers[-1]
            free_registers.pop()
        else:
            mem_to = "#" + str(current_variable_address)
            current_variable_address = current_variable_address + 1
        code.append(
            Instruction(Opcode.MOV, current_code_address, arith_str, mem_to))
        current_code_address += 1
        last_result = mem_to
    elif arith_str in variables:
        code.append(Instruction(Opcode.LD, current_code_address, "#" + str(variables[arith_str].value), Register.R1))
        last_result = Register.R1
        current_code_address += 1
    return code


def string(s: str) -> list[Instruction]:
    global current_variable_address, current_code_address, free_registers, last_result
    if s.startswith("read(") and s[-1] == ")":
        k: int = int(s.split("(", 1)[1].split(")", 1)[0])
        last_result = current_variable_address
        for i in range(k):
            code.append(Instruction(Opcode.READ, current_code_address, Register.R1))
            current_code_address += 1
            code.append(Instruction(Opcode.ST, current_code_address, Register.R1, "#" + str(current_variable_address)))
            current_code_address += 1
            current_variable_address += 1
        code.append(Instruction(Opcode.ST, current_code_address, '\0', "#" + str(current_variable_address)))
        current_code_address += 1
        current_variable_address += 1
    if s[0] == "\"" and s[-1] == "\"":
        last_result = current_variable_address
        for x in s[1:-1]:
            variable_const[current_variable_address] = x
            current_variable_address += 1
        variable_const[current_variable_address] = '\0'
        current_variable_address += 1
    return code


def get_log_opcode(s: str) -> Opcode:
    if ">=" in s:
        return Opcode.JNL
    if "<=" in s:
        return Opcode.JNG
    if "==" in s:
        return Opcode.JE
    if "!=" in s:
        return Opcode.JNE
    if ">" in s:
        return Opcode.JG
    if "<" in s:
        return Opcode.JL
    raise Exception


def translate(source: str) -> list[Instruction]:
    global current_variable_address, current_variable_address, current_code_address, jmp_code, code
    source = source.replace("\n", "")
    code_list: list[str] = [x.strip() for x in source.strip().split(";")]
    var_start, for_start = 0, 0
    search = ""
    count_skob = 0
    for_max = 0
    rec_code: str = ""
    for code_str in code_list:
        code_str = code_str.strip()
        if search == "for":
            rec_code += code_str + ";"
            if "}" in code_str:
                count_skob -= code_str.count("}")
                if count_skob == 0:
                    rec_code = rec_code[:-2]
                    translate(rec_code)
                    rec_code = ""
                    search = ""
                    count_skob = 0
                    code.append(Instruction(Opcode.INC, current_code_address, "#" + str(for_max)))
                    code.append(Instruction(Opcode.JMP, current_code_address + 1, for_start))
                    current_code_address += 2
                    code[for_start - START_CODE_ADDRESS] = Instruction(Opcode.JNL, for_start,
                                                                       current_code_address)

            if "{" in code_str:
                count_skob += code_str.count("{")
            if count_skob == 0:
                code_str = code_str.split("}")[1].strip()
            else:
                continue
        if search == "if":
            rec_code += code_str + ";"
            if "}" in code_str:
                count_skob -= code_str.count("}")
                if count_skob == 0:
                    rec_code = rec_code[:-2]
                    translate(rec_code)
                    code[jmp_code - START_CODE_ADDRESS].first = current_code_address

            if "{" in code_str:
                count_skob += code_str.count("{")
            if count_skob == 0:
                code_str = code_str.split("}", 1)[1].strip()
            else:
                continue
        if code_str[:6] == "print(":
            if '"' in code_str:
                s = code_str.split('"', 2)[1]
                code.append(Instruction(Opcode.LD, "#" + str(current_variable_address), Register.R1))
                current_code_address += 1
                for x in s:
                    variable_const[current_variable_address] = x
                    current_variable_address += 1
                variable_const[current_variable_address] = '\0'
                current_variable_address += 1
            else:
                arithmetic(code_str[6:-1])
                code.append(Instruction(Opcode.PRINT, current_code_address, last_result))
                current_code_address += 1
        elif code_str[:2] == "if":
            s = code_str.split("(", 1)[1].split(")", 1)[0]
            logic(s.strip())
            code.append(
                Instruction(get_log_opcode(code_str), current_code_address, current_code_address + 2))
            current_code_address += 1
            jmp_code = current_code_address
            search = "if"
            code.append(Instruction(Opcode.JMP, current_code_address, None))
            count_skob = code_str.count("{")
            current_code_address += 1
            rec_code = code_str.split("{", 1)[1] + ";"
        elif code_str[:6] == "number":
            if code_str[6] == " ":
                s = code_str[7:].strip()
                arr = [x.strip() for x in s.split("=")]
                arithmetic(arr[1])
                code.append(
                    Instruction(Opcode.ST, current_code_address, last_result, "#" + str(current_variable_address)))
                current_code_address += 1
                if last_result is Register:
                    free_registers.append(last_result)
                variables[arr[0]] = Variable(current_variable_address, Type.number)
                current_variable_address += 1
            else:
                raise "Compile Exception"
        elif code_str[:3] == "for":

            a = code_str.split("(", 1)
            b = a[1].split(")", 1)
            if a[0].strip() == "for":
                args = [x.strip() for x in b[0].split(",")]
                if variables.get(args[0]) is None:
                    variables[args[0]] = Variable(current_variable_address, Type.number)
                    current_variable_address += 1
                second = to_register(args[1], 2)
                code.append(Instruction(Opcode.ST, current_code_address, second, "#" + str(variables[args[0]].value)))
                current_code_address += 1
                first = to_register(args[0], 1)
                third = to_register(args[2], 3)
                code.append(
                    Instruction(Opcode.CMP, current_code_address, first, third))
                current_code_address += 1
                for_start = current_code_address
                code.append(None)
                current_code_address += 1
                search = "for"
                if b[1].strip()[0] == "{":
                    count_skob = code_str.count("{")
                    b[1] = b[1].strip()[1:]
                var_start = variables[args[0]]
                rec_code = b[1] + ";"
        elif code_str[:6] == "string":
            if code_str[6] == " ":
                s = [x.strip() for x in code_str[7:].split("=")]
                variables[s[0]] = Variable(current_variable_address, Type.string)
                current_variable_address += 1
                string(s[1].strip())
                code.append(Instruction(Opcode.ST, current_code_address, last_result, "#" + str(variables[s[0]].value)))
                current_code_address += 1
            else:
                raise "Compile Exception"
        elif code_str[:4] == "char":
            ok = False
            if code_str[4] == " ":
                s = [x.strip() for x in code_str[5:].split("=")]
                if len(s) == 2:
                    if s[1][0] == "'" and s[1][2] == "'":
                        code.append(
                            Instruction(Opcode.ST, current_code_address, s[1], "#" + str(current_variable_address)))
                        variables[s[0]] = Variable(current_variable_address, Type.char)
                        current_variable_address += 1
                        current_code_address += 1
                        ok = True
            assert ok, "Compile exception"
        if code_str.strip() == "new_line()":
            code.append(Instruction(Opcode.PRINT, current_code_address, '\n'))
            current_code_address += 1
        else:
            if "=" in code_str:
                var, val = [x.strip() for x in code_str.split("=")]
                if var in variables:
                    if variables[var].type_value == Type.number:
                        arithmetic(val)
                        code.append(
                            Instruction(Opcode.ST, current_code_address, last_result, "#" + str(variables[var].value)))
                        current_variable_address += 1
                        current_code_address += 1
                    if variables[var].type_value == Type.string:
                        string(val)
                        code.append(
                            Instruction(Opcode.ST, current_code_address, last_result, "#" + str(variables[var].value)))
                        current_code_address += 1
                        for x in val:
                            variable_const[current_variable_address] = x
                            current_variable_address += 1
                        variable_const[current_variable_address] = '\0'
                        current_variable_address += 2
    return code


def main(source: str, target: str):
    with open("input.txt", encoding="utf-8") as f:
        source = f.read()
    translate(source)
    code.append(Instruction(Opcode.HLT, current_code_address))
    for x in variable_const:
        code.append(Instruction(Opcode.WORD, x, variable_const[x]))
    write_code("output.txt", code)
    print("source LoC:", len(source.split(";")), "code instr:", len(code))


if __name__ == "__main__":
    #    assert len(sys.argv) == 3, "Wrong arguments: translator.py <input_file> <target_file>"
    #   main(sys.argv[1], sys.argv[2])
    main(None, None)
