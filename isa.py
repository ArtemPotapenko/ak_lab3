from enum import Enum
import json
from typing import Union


def is_number(arg: str) -> bool:
    try:
        int(arg)
        return True
    except ValueError:
        return False


def is_char(arg: str) -> bool:
    return (
        isinstance(arg, str)
        and len(arg) == 3
        and (arg[0] == "'" or arg[0] == '"')
        and (arg[2] == "'" or arg[2] == '"')
    )


def is_register(arg: str) -> bool:
    return len(arg) == 2 and arg[0] == "r" and arg[1] in "123456"


class Register(str, Enum):
    R1 = "r1"
    R2 = "r2"
    R3 = "r3"
    R4 = "r4"
    R5 = "r5"
    R6 = "r6"

    # arguments
    BX = "bx"
    CX = "cx"
    DX = "dx"

    IP = "ip"
    CR = "cr"
    DR = "dr"
    SP = "sp"


class Flags(str, Enum):
    NF = "neg flag"
    ZF = "zero flag"


class Opcode(str, Enum):
    # I/O
    READ = "read"
    PRINT = "print"

    # Arithmetic
    MOD = "mod"
    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"
    INC = "inc"

    # loop/if
    JMP = "jmp"
    JE = "je"
    JNG = "jng"
    JNL = "jnl"
    JG = "jg"
    JL = "jl"
    JNE = "jne"
    CMP = "cmp"

    # memory
    LD = "ld"
    ST = "st"
    WORD = "word"

    # stack

    PUSH = "push"
    POP = "pop"

    HLT = "hlt"
    NOPE = "nope"

    def __str__(self) -> str:
        return str(self.value)


# Инструкции машинного кода. Аргументы могут быть пустыми
instr_agr = Union[chr, str, int, Register, None]


class Instruction:
    memory = None

    def __init__(
        self,
        op: Opcode,
        memory,
        first: instr_agr = None,
        second: instr_agr = None,
        third: instr_agr = None,
    ):
        self.op = op
        self.first = first
        self.second = second
        self.third = third
        self.memory = memory

    def __str__(self):
        return (
            str(self.op)
            + " "
            + str(self.first)
            + " "
            + str(self.second)
            + " "
            + str(self.third)
            + " "
            + str(self.memory)
        )


def create_instr(json_dict: dict) -> Instruction:
    return Instruction(
        Opcode(json_dict["opcode"]),
        int(json_dict["memory"]),
        set_from_json(json_dict["first"]),
        set_from_json(json_dict["second"]),
        set_from_json(json_dict["third"]),
    )


def write_code(filename: str, code: list[Instruction]):
    with open(filename, "w", encoding="utf-8") as file:
        buf = []

        for instr in code:
            buf.append(
                json.dumps(
                    {
                        "memory": instr.memory,
                        "opcode": instr.op,
                        "first": instr.first,
                        "second": instr.second,
                        "third": instr.third,
                    }
                )
            )
        file.write("[" + ",\n ".join(buf) + "]")


def set_from_json(json_string: str | None):
    if json_string is None:
        return None
    if is_char(json_string):
        return json_string[1]
    if is_number(json_string):
        return int(json_string)
    if is_register(json_string):
        return Register(json_string)
    return json_string


def read_code(filename: str) -> list[Instruction]:
    with open(filename, encoding="utf-8") as file:
        json_list = json.loads(file.read().replace("\\n", "\n"))
    code: list[Instruction] = []
    for json_instr in json_list:
        code.append(create_instr(json_instr))
    return code
