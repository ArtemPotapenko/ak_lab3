
# Лабораторная работа #3 АК
***
#### Потапенко Артем P3234
Базовый Вариант: `alg -> asm | risc | neum | hw | tick -> instr | struct | stream | mem | cstr | prob2 | cache`


## Язык программирования
***
* Алгоритмический язык программирования, синтаксис совпадает с синтаксисом С.
* Все символы от '#' до конца строки будут расценены как комментарии
* Каждое выражение должно заканчиваться знаком `;`. 
* Поддерживаются математические выражения.
* Стратегия вычисления: последовательная
* Все переменные объявляются в глобальной зоне видимости 
Статическая типизация, существует 3 типа данных:
* `number` - целое число
* `char` - символ, в памяти хранится как число в кодировке Unicode 
* `string` - строка, ссылка на последовательность символов

### BNF

```BNF
<program> ::= <statement_list>

<statement_list> ::= <statement> | <statement> <statement_list>

<statement> ::= <declaration> 
    | <assignment> 
    | <while_loop> 
    | <for_loop>
    | <if_statement> 
    | <print_statement>
    | <read_statement>
<declaration> ::= 
    | "char" <identifier> "=" <char> ";"
    | "string" <identifier> "=" <string> ";"
    | "number" <identifier> "=" <string> ";" 
<assignment> ::= <identifier> "=" <expression> ";"
    | <identifier> "=" <identifier> ";"
   
<while_loop> ::= "while" "(" <condition> ")" "{" <statement_list> "}"
<for_loop> ::= "for" "(" <identifier>, <expression>, <expression> ")" "{" <
<if_statement> ::= "if" "(" <condition> ")" "{" <statement_list> "}"

<print_statement> ::= "print" "(" <expression> | <identifier> | <string> | <character>")" ";"

<read_statement> ::= "read" "(" <identifier> ")" ";"

<condition> ::= <expression> <comparison_op> <expression>

<expression> ::= <factor> 
    | <expression> "+" <expression> | 
    | <expression> "-" <expression>
    | <expression> "*" <expression>
    | <expression> "/" <expression>
    | <expression> "%" <expression>
    | "(" <expression> ")"


<factor> ::= <number> | <identifier>

<comparison_op> ::= "<" | "<=" | ">" | ">=" | "==" | "!="

<identifier> ::= <letter> {<letter> | <digit>}

<number> ::= <digit> {<digit>}

<string> ::= "\"" {<character>} "\""

<char> ::= "\'" <character> "\'"

<character> ::= <letter> | <digit> | <special_char>
```
* Функции используются только встроенные:
*  read и print:
  * print:
    * Выводит результат математического выражения
    * Выводит переменную типа `string` как строку
    * Выводит данный символ
  * read:
    * Считывание одного символа в переменную типа `char`
    * Считывание строки не длинее, чем аргумент функции.
* Цикл `while` и условный переход `if` в качестве аргумента принимают `condition`
  * `condition` проверяет на равенство или неравенство два математических выражения, поддерживаемые сравнения:
    * `==, !=, >, <, <=, >=`
  * `break` или `else` не предусмотрены
* Цикл `for` принимает 3 аргeумента: переменная, начальная точка, конечная точка.
* Поддерживаются математические выражения, поддерживаемые операции:
  * `+, -, *, /, %`
  * Любые правильные скобочные последовательности
* Литералы:
  * Целые числа
  * Строки `"<string>"`
  * Символы `'<character>'`


## Организация памяти

Модель памяти: `neum` -  архитектура Фон Неймана

### Модель  памяти

| Address | Instruction      |
|---------|------------------|
| 0       | instruction/data |
| 1       | instruction/data |
| ...     |
| 8191    | instruction/data |

* ячейки `0-99` используются для ввода-ввывода
* ячейки `100-4095` используется для данных
* ячейки `4096 - ..` используется для команд
* ячейки `.. - 8191` используем для стека
### Pегистры

* Общего назначения: `R1`, `R2`, `R3`, `R4`, `R5`, `R6`
* Аргументы команд: `BX`, `CX`, `DX` (используется для работы с памятью)
* Специализированные: `IP`, `DR`, `CR`, `SP`


## Система команд


| Операнд  | Описание                         | Аргумент1             | Аргумент2      | Аргумент2 | Кол-во тактов |
|----------|----------------------------------|-----------------------|----------------|-----------|---------------|
| `READ`   | Чтение символа                   | Регистр               | -              | -         | 3             |
| `PRINT`  | Вывод символа                    | Регистр/символ        | -              | -         | 3             |
 | `MOD`    | Нахождение остатка от деления    | Регистр/число         | Регистр/число  |           | 4             |
 | `ADD`    | Сложение                         | Регистр/число         | Регистр/число  | Регистр   | 4             |
 | `MUL`    | Умножение                        | Регистр/число         | Регистр/число  | Регистр   | 4             |
 | `DIV`    | Целочисленное деление            | Регистр/число         | Регистр/число  | Регистр   | 4             |
 | `INC`    | Инкремент                        | ячейка памяти | -              | -         | 6             |
 | `JMP`    | Безусловный переход              | Число                 | -              | -         | 2             |
 | `JE`     | Переход, если равно              | Число                 | -              | -         | 2             |
 | `JNG`    | Переход, если меньше или равно   | Число                 | -              | -         | 2             |
 | `JNL`    | Переход, если больше или равно   | Число                 | -              | -         | 2             |
 | `JG`     | Переход, если больше             | Число                 | -              | -         | 2             |
 | `JL`     | Переход, если меньше             | Число                 | -              | -         | 2             |
 | `JNE`    | Переход, если не равно          | Число                 | -              | -         | 2             |
 | `CMP`    | Установить флаги сравнения чисел | Регистр/число         | Регистр/число  | -         | 3             |
 | `ST`     | Загрузить в память               | Регистр/число         | Ячейка/регистр | -         | 4             |
| `LD`     | Загрузить в регистры             | Регистр/число/ячейка | Регистр        | -         | 3-4           |
| `PUSH`   | Загрузить в стек                 | Регистр/число         | -              | -         | 5             |
 | `POP`    | Выгрузить из стека               | Регистр               | -              | -         | 5             |
 | `HLT`    | Остановка                        | -                     | -              | -         | 3             |
 
### Кодирование инструкций

Каждая инструкция представлена в виде Json объекта (по варианту)
* Пример
```json
{"memory": 4124, "opcode": "add", "first": "r1", "second": 48, "third": "r1"}
```
Если аргумента в инструкйии нет, ему присваивается значение `null`

Реализация [isa](isa.py)

## Транслятор

Реализозация [translator](stranslator.py)

Сценарий использования:
* `translator.py <input_file> <target_file>`, где: 
  * `<input_file>` - Код программы
  * `<target_file>` - Название файла для машинного кода


## Модель процессора

Сценарий использования:
*`machine.py <machine_code_file> <tick_file> <input_file>`, где
  * `<machine_code_file>`  -- файл со скомпилированным кодом   

Реализация: [machine](src/machine.py)

### Datapath
![datapath](resources/datapath.svg)


### Control Unit
![control unit](resources/ControlUnit.svg)

Control unit здесь реализован как hardwire, в нем находится тактовый генератор и счетчик команд, всегда сначала происходит цикл выборки команды,
которая потом приходит через шину на декодер команды - логическую схему, которая активирует необходимые сигналы и передает управление логическим схемам Циклов:

После окончания цикла исполнения, логическая схема декодера команды дает сигнал счетчику, который обнуляется и происходит цикл выборки следующей команды, и так до команды `halt`,
которая прервет сигналы от декодера команд - на ней все просто закончится


## Тестирование

В CI находятся две работы:
* Тестирование 
* Проверка форматирования и линтер

Для алгоритмов реализованы golden-тесты:
* [Hello world](golden/hello_world.yml)
* [Cat](golden/cat.yml)
* [Hello User](golden/hello_user.yml)
* [Prob2](golden/fib.yml)
* [Cycle](golden/cycles.yml)
* [Arith](golden/arithmetic.yml)

### Prob2

#### [Код программы](programs/fib/program.q):
```
number a = 1;
number b = 1;
number sum = 0;
while (b < 4000000){
     if (b % 2 == 0){
        sum = sum + b;
     }
     b = a + b;
     a = b - a;
}
print(sum);
```
#### Транслированный [машинный код](programs/fib/compile):

``` 
[{"memory": 4096, "opcode": "ld", "first": "1", "second": "r1", "third": null},
 {"memory": 4097, "opcode": "st", "first": "r1", "second": "#100", "third": null},
 {"memory": 4098, "opcode": "ld", "first": "1", "second": "r1", "third": null},
 {"memory": 4099, "opcode": "st", "first": "r1", "second": "#101", "third": null},
 {"memory": 4100, "opcode": "ld", "first": "0", "second": "r1", "third": null},
 {"memory": 4101, "opcode": "st", "first": "r1", "second": "#102", "third": null},
 {"memory": 4102, "opcode": "ld", "first": "#101", "second": "r1", "third": null},
 {"memory": 4103, "opcode": "ld", "first": "4000000", "second": "r2", "third": null},
 {"memory": 4104, "opcode": "cmp", "first": "r1", "second": "r2", "third": null},
 {"memory": 4105, "opcode": "jl", "first": 4107, "second": null, "third": null},
 {"memory": 4106, "opcode": "jmp", "first": 4126, "second": null, "third": null},
 {"memory": 4107, "opcode": "ld", "first": "#101", "second": "bx", "third": null},
 {"memory": 4108, "opcode": "mod", "first": "bx", "second": "2", "third": "r1"},
 {"memory": 4109, "opcode": "ld", "first": "0", "second": "r2", "third": null},
 {"memory": 4110, "opcode": "cmp", "first": "r1", "second": "r2", "third": null},
 {"memory": 4111, "opcode": "je", "first": 4113, "second": null, "third": null},
 {"memory": 4112, "opcode": "jmp", "first": 4117, "second": null, "third": null},
 {"memory": 4113, "opcode": "ld", "first": "#102", "second": "bx", "third": null},
 {"memory": 4114, "opcode": "ld", "first": "#101", "second": "cx", "third": null},
 {"memory": 4115, "opcode": "add", "first": "bx", "second": "cx", "third": "r1"},
 {"memory": 4116, "opcode": "st", "first": "r1", "second": "#102", "third": null},
 {"memory": 4117, "opcode": "ld", "first": "#100", "second": "bx", "third": null},
 {"memory": 4118, "opcode": "ld", "first": "#101", "second": "cx", "third": null},
 {"memory": 4119, "opcode": "add", "first": "bx", "second": "cx", "third": "r1"},
 {"memory": 4120, "opcode": "st", "first": "r1", "second": "#101", "third": null},
 {"memory": 4121, "opcode": "ld", "first": "#101", "second": "bx", "third": null},
 {"memory": 4122, "opcode": "ld", "first": "#100", "second": "cx", "third": null},
 {"memory": 4123, "opcode": "sub", "first": "bx", "second": "cx", "third": "r1"},
 {"memory": 4124, "opcode": "st", "first": "r1", "second": "#100", "third": null},
 {"memory": 4125, "opcode": "jmp", "first": 4102, "second": null, "third": null},
 {"memory": 4126, "opcode": "ld", "first": "#102", "second": "r1", "third": null},
 {"memory": 4127, "opcode": "cmp", "first": "r1", "second": 0, "third": null},
 {"memory": 4128, "opcode": "jl", "first": 4139, "second": null, "third": null},
 {"memory": 4129, "opcode": "je", "first": 4134, "second": null, "third": null},
 {"memory": 4130, "opcode": "mod", "first": "r1", "second": 10, "third": "bx"},
 {"memory": 4131, "opcode": "div", "first": "r1", "second": 10, "third": "r1"},
 {"memory": 4132, "opcode": "push", "first": "bx", "second": null, "third": null},
 {"memory": 4133, "opcode": "jmp", "first": 4129, "second": null, "third": null},
 {"memory": 4134, "opcode": "cmp", "first": "sp", "second": 8191, "third": null},
 {"memory": 4135, "opcode": "je", "first": 4153, "second": null, "third": null},
 {"memory": 4136, "opcode": "pop", "first": "r1", "second": null, "third": null},
 {"memory": 4137, "opcode": "add", "first": "r1", "second": 48, "third": "r1"},
 {"memory": 4138, "opcode": "print", "first": "r1", "second": null, "third": null},
 {"memory": 4139, "opcode": "jmp", "first": 4134, "second": null, "third": null},
 {"memory": 4140, "opcode": "mul", "first": "r1", "second": -1, "third": "r1"},
 {"memory": 4141, "opcode": "je", "first": 4146, "second": null, "third": null},
 {"memory": 4142, "opcode": "mod", "first": "r1", "second": 10, "third": "bx"},
 {"memory": 4143, "opcode": "div", "first": "r1", "second": 10, "third": "r1"},
 {"memory": 4144, "opcode": "push", "first": "bx", "second": null, "third": null},
 {"memory": 4145, "opcode": "jmp", "first": 4141, "second": null, "third": null},
 {"memory": 4146, "opcode": "print", "first": "-", "second": null, "third": null},
 {"memory": 4147, "opcode": "cmp", "first": "sp", "second": 8191, "third": null},
 {"memory": 4148, "opcode": "je", "first": 4153, "second": null, "third": null},
 {"memory": 4149, "opcode": "pop", "first": "r1", "second": null, "third": null},
 {"memory": 4150, "opcode": "add", "first": "r1", "second": 48, "third": "r1"},
 {"memory": 4151, "opcode": "print", "first": "r1", "second": null, "third": null},
 {"memory": 4152, "opcode": "jmp", "first": 4147, "second": null, "third": null},
 {"memory": 4153, "opcode": "hlt", "first": null, "second": null, "third": null}]
```

#### [Такты процессора](programs/fib/tick.txt):
```
<tick_number: 1;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4096;cr: 0;dr: 0;sp: 8191;NF: False;ZF: False>
<tick_number: 2;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4096;cr: ld 1 Register.R1 None 4096;dr: 0;sp: 8191;NF: False;ZF: False>
<tick_number: 3;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4096;cr: ld 1 Register.R1 None 4096;dr: 0;sp: 8191;NF: False;ZF: False>
<tick_number: 4;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4097;cr: ld 1 Register.R1 None 4096;dr: 0;sp: 8191;NF: False;ZF: False>
<tick_number: 5;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4097;cr: st Register.R1 #100 None 4097;dr: 0;sp: 8191;NF: False;ZF: False>
<tick_number: 6;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4097;cr: st Register.R1 #100 None 4097;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 7;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4097;cr: st Register.R1 #100 None 4097;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 8;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4098;cr: st Register.R1 #100 None 4097;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 9;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4098;cr: ld 1 Register.R1 None 4098;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 10;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4098;cr: ld 1 Register.R1 None 4098;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 11;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4099;cr: ld 1 Register.R1 None 4098;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 12;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4099;cr: st Register.R1 #101 None 4099;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 13;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4099;cr: st Register.R1 #101 None 4099;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 14;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4099;cr: st Register.R1 #101 None 4099;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 15;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4100;cr: st Register.R1 #101 None 4099;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 16;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4100;cr: ld 0 Register.R1 None 4100;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 17;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4100;cr: ld 0 Register.R1 None 4100;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 18;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4101;cr: ld 0 Register.R1 None 4100;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 19;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4101;cr: st Register.R1 #102 None 4101;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 20;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4101;cr: st Register.R1 #102 None 4101;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 21;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4101;cr: st Register.R1 #102 None 4101;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 22;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4102;cr: st Register.R1 #102 None 4101;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 23;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 24;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 25;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 26;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 27;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 28;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 29;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 30;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 31;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 32;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 33;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 34;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 35;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 36;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 0;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 37;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 38;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 39;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 40;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 41;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 42;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 43;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 44;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 45;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 46;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 47;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 48;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 49;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 50;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 51;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 52;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 53;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 54;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 55;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 56;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 57;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 58;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 0;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 59;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 1;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 60;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 1;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 61;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 1;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 62;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 1;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 63;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 1;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 64;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 1;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 65;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 1;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 66;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 1;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 67;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 1;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 68;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 1;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 69;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 1;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 70;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 1;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 71;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 72;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 73;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 74;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 75;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 76;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 77;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 78;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 79;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 80;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 81;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 82;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 83;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 84;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 85;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 86;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 87;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 88;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 89;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 90;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 91;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 92;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 93;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 94;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 95;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 96;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 97;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 98;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 99;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 100;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 101;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 102;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 103;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 104;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 105;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 106;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 107;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 108;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 109;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 110;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 111;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 112;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 113;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 114;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4113;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 115;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 116;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 117;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 1;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 118;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 1;dx: 0;ip: 4114;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 119;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 1;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 120;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 1;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 121;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 2;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 122;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 2;dx: 0;ip: 4115;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 123;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 2;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 124;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 2;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 125;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 2;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 126;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 2;dx: 0;ip: 4116;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 127;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 2;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 128;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 2;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 129;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 2;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 130;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 2;dx: 0;ip: 4117;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 131;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 2;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 132;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 0;cx: 2;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 133;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 134;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 135;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 136;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 137;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 138;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 139;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 140;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 141;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 142;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 143;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 144;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 145;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 146;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 147;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 148;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 149;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 150;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 151;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 152;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 153;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 154;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 155;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 156;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 157;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 158;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 159;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 160;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 161;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 162;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 163;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 164;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 165;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 166;r1: 2;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 167;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 168;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 169;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 170;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 171;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 172;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 173;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 174;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 175;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 176;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 177;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 178;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 179;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 180;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 181;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 182;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 183;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 184;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 185;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 186;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 187;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 188;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 189;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 190;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 191;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 192;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 193;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 194;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 195;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 196;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 1;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 197;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 198;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 199;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 200;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 1;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 201;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 202;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 203;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 204;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 205;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 206;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 207;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 208;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 209;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 210;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 211;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 212;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 213;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 3;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 214;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 3;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 215;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 3;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 216;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 3;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 217;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 218;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 219;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 220;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 221;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 222;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 223;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 224;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 225;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 226;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 227;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 228;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 229;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 230;r1: 3;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 231;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 232;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 233;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 234;r1: 5;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 235;r1: 5;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 236;r1: 5;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 237;r1: 5;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 238;r1: 5;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 239;r1: 5;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 240;r1: 5;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 241;r1: 5;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 242;r1: 5;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 243;r1: 5;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 244;r1: 5;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 245;r1: 5;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 246;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 247;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 248;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 249;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 250;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 251;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 252;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 253;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 254;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 255;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 256;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 257;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 258;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 259;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 260;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 2;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 261;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 262;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 263;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 264;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 265;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 5;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 266;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 5;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 267;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 5;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 268;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 5;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 269;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 5;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 270;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 5;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 271;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 5;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 272;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 5;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 273;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 5;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 274;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 5;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 275;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 5;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 276;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 5;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 277;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 5;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 278;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 5;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 279;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 5;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 280;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 5;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 281;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 282;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 283;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 284;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 285;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 286;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 287;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 288;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 289;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 290;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 291;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 292;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 293;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 294;r1: 5;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 295;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 296;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 297;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 298;r1: 8;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 299;r1: 8;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 300;r1: 8;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 301;r1: 8;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 302;r1: 8;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 303;r1: 8;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 304;r1: 8;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 305;r1: 8;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 306;r1: 8;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 307;r1: 8;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 308;r1: 8;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 309;r1: 8;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 310;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 311;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 312;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 313;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 314;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 315;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 316;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 317;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 318;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 319;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 320;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4113;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 321;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 322;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 3;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 323;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 324;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4114;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 325;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 326;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 3;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 327;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 8;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 328;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 8;dx: 0;ip: 4115;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 329;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 8;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 330;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 8;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 331;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 8;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 332;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 8;dx: 0;ip: 4116;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 333;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 8;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 334;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 8;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 335;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 8;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 336;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 8;dx: 0;ip: 4117;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 337;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 8;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 338;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 8;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 339;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 340;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 341;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 342;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 343;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 344;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 345;r1: 10;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 346;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 347;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 348;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 349;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 350;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 351;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 352;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 353;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 354;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5;cx: 8;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 355;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 8;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 356;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 8;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 357;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 8;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 358;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 8;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 359;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 360;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 361;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 362;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 363;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 364;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 365;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 366;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 367;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 368;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 369;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 370;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 371;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 372;r1: 8;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 373;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 374;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 375;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 376;r1: 13;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 377;r1: 13;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 378;r1: 13;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 379;r1: 13;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 380;r1: 13;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 381;r1: 13;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 382;r1: 13;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 383;r1: 13;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 384;r1: 13;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 385;r1: 13;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 386;r1: 13;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 387;r1: 13;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 388;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 389;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 390;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 391;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 392;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 393;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 394;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 395;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 396;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 397;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 398;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 399;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 400;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 401;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 402;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 5;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 403;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 5;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 404;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 5;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 405;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 5;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 406;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 5;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 407;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 13;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 408;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 13;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 409;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 13;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 410;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 13;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 411;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 13;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 412;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 13;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 413;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 13;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 414;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 13;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 415;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 13;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 416;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 13;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 417;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 13;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 418;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 8;cx: 13;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 419;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 13;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 420;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 13;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 421;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 13;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 422;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 13;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 423;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 424;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 425;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 426;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 427;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 428;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 429;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 430;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 431;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 432;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 433;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 434;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 435;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 436;r1: 13;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 437;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 438;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 439;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 440;r1: 21;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 441;r1: 21;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 442;r1: 21;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 443;r1: 21;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 444;r1: 21;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 445;r1: 21;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 446;r1: 21;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 447;r1: 21;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 448;r1: 21;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 449;r1: 21;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 450;r1: 21;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 451;r1: 21;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 452;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 453;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 454;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 455;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 456;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 457;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 458;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 459;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 460;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 461;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 462;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 463;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 464;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 465;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 466;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 8;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 467;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 8;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 468;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 8;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 469;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 8;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 470;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 8;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 471;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 21;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 472;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 21;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 473;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 21;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 474;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 21;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 475;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 21;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 476;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 21;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 477;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 21;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 478;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 21;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 479;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 21;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 480;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 21;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 481;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 21;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 482;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 13;cx: 21;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 483;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 21;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 484;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 21;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 485;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 21;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 486;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 21;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 487;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 488;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 489;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 490;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 491;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 492;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 493;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 494;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 495;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 496;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 497;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 498;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 499;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 500;r1: 21;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 501;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 502;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 503;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 504;r1: 34;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 505;r1: 34;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 506;r1: 34;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 507;r1: 34;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 508;r1: 34;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 509;r1: 34;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 510;r1: 34;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 511;r1: 34;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 512;r1: 34;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 513;r1: 34;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 514;r1: 34;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 515;r1: 34;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 516;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 517;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 518;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 519;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 520;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 521;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 522;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 523;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 524;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 525;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 526;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4113;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 527;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 528;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 13;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 529;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 13;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 530;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 13;dx: 0;ip: 4114;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 531;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 13;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 532;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 13;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 533;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 34;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 534;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 34;dx: 0;ip: 4115;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 535;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 34;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 536;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 34;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 537;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 34;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 538;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 34;dx: 0;ip: 4116;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 539;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 34;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 540;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 34;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 541;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 34;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 542;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 34;dx: 0;ip: 4117;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 543;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 34;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 544;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10;cx: 34;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 545;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 546;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 547;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 548;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 549;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 550;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 551;r1: 44;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 552;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 553;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 554;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 555;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 556;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 557;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 558;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 559;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 560;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 21;cx: 34;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 561;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 34;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 562;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 34;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 563;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 34;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 564;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 34;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 565;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 566;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 567;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 568;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 569;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 570;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 571;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 572;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 573;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 574;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 575;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 576;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 577;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 578;r1: 34;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 579;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 580;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 581;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 582;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 583;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 584;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 585;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 586;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 587;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 588;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 589;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 590;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 591;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 592;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 593;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 594;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 595;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 596;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 597;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 598;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 599;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 600;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 601;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 602;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 603;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 604;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 605;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 606;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 607;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 608;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 21;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 609;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 21;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 610;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 21;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 611;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 21;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 612;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 21;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 613;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 55;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 614;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 55;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 615;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 55;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 616;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 55;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 617;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 55;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 618;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 55;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 619;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 55;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 620;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 55;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 621;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 55;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 622;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 55;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 623;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 55;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 624;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 34;cx: 55;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 625;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 55;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 626;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 55;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 627;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 55;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 628;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 55;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 629;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 630;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 631;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 632;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 633;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 634;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 635;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 636;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 637;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 638;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 639;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 640;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 641;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 642;r1: 55;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 643;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 644;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 645;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 646;r1: 89;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 647;r1: 89;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 648;r1: 89;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 649;r1: 89;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 650;r1: 89;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 651;r1: 89;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 652;r1: 89;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 653;r1: 89;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 654;r1: 89;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 655;r1: 89;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 656;r1: 89;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 657;r1: 89;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 658;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 659;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 660;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 661;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 662;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 663;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 664;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 665;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 666;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 667;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 668;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 669;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 670;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 671;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 672;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 34;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 673;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 34;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 674;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 34;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 675;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 34;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 676;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 34;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 677;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 89;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 678;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 89;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 679;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 89;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 680;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 89;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 681;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 89;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 682;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 89;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 683;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 89;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 684;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 89;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 685;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 89;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 686;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 89;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 687;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 89;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 688;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 55;cx: 89;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 689;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 89;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 690;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 89;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 691;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 89;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 692;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 89;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 693;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 694;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 695;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 696;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 697;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 698;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 699;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 700;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 701;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 702;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 703;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 704;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 705;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 706;r1: 89;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 707;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 708;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 709;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 710;r1: 144;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 711;r1: 144;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 712;r1: 144;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 713;r1: 144;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 714;r1: 144;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 715;r1: 144;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 716;r1: 144;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 717;r1: 144;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 718;r1: 144;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 719;r1: 144;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 720;r1: 144;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 721;r1: 144;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 722;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 723;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 724;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 725;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 726;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 727;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 728;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 729;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 730;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 731;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 732;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4113;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 733;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 734;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 55;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 735;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 55;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 736;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 55;dx: 0;ip: 4114;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 737;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 55;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 738;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 55;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 739;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 144;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 740;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 144;dx: 0;ip: 4115;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 741;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 144;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 742;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 144;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 743;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 144;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 744;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 144;dx: 0;ip: 4116;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 745;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 144;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 746;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 144;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 747;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 144;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 748;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 144;dx: 0;ip: 4117;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 749;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 144;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 750;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 44;cx: 144;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 751;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 752;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 753;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 754;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 755;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 756;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 757;r1: 188;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 758;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 759;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 760;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 761;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 762;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 763;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 764;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 765;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 766;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 89;cx: 144;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 767;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 144;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 768;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 144;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 769;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 144;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 770;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 144;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 771;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 772;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 773;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 774;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 775;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 776;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 777;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 778;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 779;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 780;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 781;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 782;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 783;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 784;r1: 144;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 785;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 786;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 787;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 788;r1: 233;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 789;r1: 233;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 790;r1: 233;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 791;r1: 233;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 792;r1: 233;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 793;r1: 233;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 794;r1: 233;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 795;r1: 233;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 796;r1: 233;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 797;r1: 233;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 798;r1: 233;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 799;r1: 233;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 800;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 801;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 802;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 803;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 804;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 805;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 806;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 807;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 808;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 809;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 810;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 811;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 812;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 813;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 814;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 89;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 815;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 89;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 816;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 89;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 817;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 89;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 818;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 89;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 819;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 233;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 820;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 233;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 821;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 233;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 822;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 233;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 823;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 233;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 824;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 233;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 825;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 233;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 826;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 233;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 827;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 233;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 828;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 233;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 829;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 233;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 830;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 144;cx: 233;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 831;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 233;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 832;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 233;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 833;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 233;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 834;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 233;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 835;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 836;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 837;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 838;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 839;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 840;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 841;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 842;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 843;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 844;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 845;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 846;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 847;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 848;r1: 233;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 849;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 850;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 851;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 852;r1: 377;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 853;r1: 377;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 854;r1: 377;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 855;r1: 377;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 856;r1: 377;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 857;r1: 377;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 858;r1: 377;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 859;r1: 377;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 860;r1: 377;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 861;r1: 377;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 862;r1: 377;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 863;r1: 377;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 864;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 865;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 866;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 867;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 868;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 869;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 870;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 871;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 872;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 873;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 874;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 875;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 876;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 877;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 878;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 144;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 879;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 144;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 880;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 144;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 881;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 144;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 882;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 144;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 883;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 377;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 884;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 377;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 885;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 377;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 886;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 377;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 887;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 377;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 888;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 377;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 889;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 377;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 890;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 377;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 891;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 377;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 892;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 377;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 893;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 377;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 894;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 233;cx: 377;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 895;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 377;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 896;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 377;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 897;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 377;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 898;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 377;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 899;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 900;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 901;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 902;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 903;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 904;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 905;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 906;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 907;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 908;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 909;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 910;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 911;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 912;r1: 377;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 913;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 914;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 915;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 916;r1: 610;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 917;r1: 610;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 918;r1: 610;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 919;r1: 610;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 920;r1: 610;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 921;r1: 610;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 922;r1: 610;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 923;r1: 610;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 924;r1: 610;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 925;r1: 610;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 926;r1: 610;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 927;r1: 610;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 928;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 929;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 930;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 931;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 932;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 933;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 934;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 935;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 936;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 937;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 938;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4113;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 939;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 940;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 233;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 941;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 233;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 942;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 233;dx: 0;ip: 4114;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 943;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 233;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 944;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 233;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 945;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 610;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 946;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 610;dx: 0;ip: 4115;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 947;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 610;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 948;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 610;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 949;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 610;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 950;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 610;dx: 0;ip: 4116;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 951;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 610;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 952;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 610;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 953;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 610;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 954;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 610;dx: 0;ip: 4117;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 955;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 610;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 956;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 188;cx: 610;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 957;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 958;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 959;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 960;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 961;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 962;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 963;r1: 798;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 964;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 965;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 966;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 967;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 968;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 969;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 970;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 971;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 972;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 377;cx: 610;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 973;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 610;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 974;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 610;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 975;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 610;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 976;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 610;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 977;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 978;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 979;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 980;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 981;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 982;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 983;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 984;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 985;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 986;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 987;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 988;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 989;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 990;r1: 610;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 991;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 992;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 993;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 994;r1: 987;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 995;r1: 987;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 996;r1: 987;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 997;r1: 987;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 998;r1: 987;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 999;r1: 987;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1000;r1: 987;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1001;r1: 987;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1002;r1: 987;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1003;r1: 987;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1004;r1: 987;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1005;r1: 987;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1006;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1007;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1008;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1009;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1010;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1011;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1012;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1013;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1014;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1015;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1016;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1017;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1018;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1019;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1020;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 377;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1021;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 377;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1022;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 377;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1023;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 377;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1024;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 377;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1025;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 987;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1026;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 987;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1027;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 987;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1028;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 987;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1029;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 987;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1030;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 987;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1031;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 987;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1032;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 987;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1033;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 987;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1034;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 987;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1035;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 987;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1036;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 610;cx: 987;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1037;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 987;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1038;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 987;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1039;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 987;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1040;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 987;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1041;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1042;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1043;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1044;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1045;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1046;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1047;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1048;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1049;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1050;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1051;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1052;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1053;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1054;r1: 987;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1055;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1056;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1057;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1058;r1: 1597;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1059;r1: 1597;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1060;r1: 1597;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1061;r1: 1597;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1062;r1: 1597;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1063;r1: 1597;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1064;r1: 1597;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1065;r1: 1597;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1066;r1: 1597;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1067;r1: 1597;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1068;r1: 1597;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1069;r1: 1597;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1070;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1071;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1072;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1073;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1074;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1075;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1076;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1077;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1078;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1079;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1080;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1081;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1082;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1083;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1084;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 610;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1085;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 610;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1086;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 610;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1087;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 610;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1088;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 610;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1089;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 1597;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1090;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 1597;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1091;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 1597;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1092;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 1597;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1093;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 1597;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1094;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 1597;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1095;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 1597;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1096;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 1597;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1097;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 1597;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1098;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 1597;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1099;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 1597;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1100;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 987;cx: 1597;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1101;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 1597;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1102;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 1597;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1103;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 1597;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1104;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 1597;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1105;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1106;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1107;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1108;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1109;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1110;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1111;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1112;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1113;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1114;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1115;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1116;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1117;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1118;r1: 1597;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1119;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1120;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1121;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1122;r1: 2584;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1123;r1: 2584;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1124;r1: 2584;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1125;r1: 2584;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1126;r1: 2584;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1127;r1: 2584;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1128;r1: 2584;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1129;r1: 2584;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1130;r1: 2584;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1131;r1: 2584;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1132;r1: 2584;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1133;r1: 2584;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1134;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1135;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1136;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1137;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1138;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1139;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1140;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1141;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1142;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1143;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1144;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4113;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1145;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1146;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 987;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1147;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 987;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1148;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 987;dx: 0;ip: 4114;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1149;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 987;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1150;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 987;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1151;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 2584;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1152;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 2584;dx: 0;ip: 4115;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1153;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 2584;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1154;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 2584;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1155;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 2584;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1156;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 2584;dx: 0;ip: 4116;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1157;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 2584;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1158;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 2584;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1159;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 2584;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1160;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 2584;dx: 0;ip: 4117;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1161;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 2584;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1162;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 798;cx: 2584;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1163;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1164;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1165;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1166;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1167;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1168;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1169;r1: 3382;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1170;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1171;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1172;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1173;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1174;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1175;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1176;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1177;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1178;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1597;cx: 2584;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1179;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 2584;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1180;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 2584;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1181;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 2584;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1182;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 2584;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1183;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1184;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1185;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1186;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1187;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1188;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1189;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1190;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1191;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1192;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1193;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1194;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1195;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1196;r1: 2584;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1197;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1198;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1199;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1200;r1: 4181;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1201;r1: 4181;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1202;r1: 4181;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1203;r1: 4181;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1204;r1: 4181;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1205;r1: 4181;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1206;r1: 4181;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1207;r1: 4181;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1208;r1: 4181;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1209;r1: 4181;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1210;r1: 4181;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1211;r1: 4181;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1212;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1213;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1214;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1215;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1216;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1217;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1218;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1219;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1220;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1221;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1222;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1223;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1224;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1225;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1226;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 1597;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1227;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 1597;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1228;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 1597;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1229;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 1597;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1230;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 1597;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1231;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 4181;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1232;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 4181;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1233;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 4181;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1234;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 4181;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1235;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 4181;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1236;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 4181;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1237;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 4181;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1238;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 4181;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1239;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 4181;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1240;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 4181;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1241;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 4181;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1242;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2584;cx: 4181;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1243;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 4181;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1244;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 4181;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1245;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 4181;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1246;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 4181;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1247;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1248;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1249;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1250;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1251;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1252;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1253;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1254;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1255;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1256;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1257;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1258;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1259;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1260;r1: 4181;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1261;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1262;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1263;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1264;r1: 6765;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1265;r1: 6765;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1266;r1: 6765;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1267;r1: 6765;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1268;r1: 6765;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1269;r1: 6765;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1270;r1: 6765;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1271;r1: 6765;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1272;r1: 6765;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1273;r1: 6765;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1274;r1: 6765;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1275;r1: 6765;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1276;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1277;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1278;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1279;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1280;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1281;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1282;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1283;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1284;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1285;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1286;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1287;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1288;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1289;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1290;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 2584;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1291;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 2584;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1292;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 2584;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1293;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 2584;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1294;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 2584;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1295;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 6765;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1296;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 6765;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1297;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 6765;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1298;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 6765;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1299;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 6765;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1300;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 6765;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1301;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 6765;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1302;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 6765;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1303;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 6765;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1304;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 6765;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1305;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 6765;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1306;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4181;cx: 6765;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1307;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 6765;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1308;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 6765;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1309;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 6765;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1310;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 6765;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1311;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1312;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1313;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1314;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1315;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1316;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1317;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1318;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1319;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1320;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1321;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1322;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1323;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1324;r1: 6765;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1325;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1326;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1327;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1328;r1: 10946;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1329;r1: 10946;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1330;r1: 10946;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1331;r1: 10946;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1332;r1: 10946;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1333;r1: 10946;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1334;r1: 10946;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1335;r1: 10946;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1336;r1: 10946;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1337;r1: 10946;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1338;r1: 10946;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1339;r1: 10946;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1340;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1341;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1342;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1343;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1344;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1345;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1346;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1347;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1348;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1349;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1350;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4113;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1351;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1352;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 4181;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1353;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 4181;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1354;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 4181;dx: 0;ip: 4114;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1355;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 4181;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1356;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 4181;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1357;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 10946;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1358;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 10946;dx: 0;ip: 4115;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1359;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 10946;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1360;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 10946;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1361;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 10946;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1362;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 10946;dx: 0;ip: 4116;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1363;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 10946;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1364;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 10946;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1365;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 10946;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1366;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 10946;dx: 0;ip: 4117;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1367;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 10946;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1368;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3382;cx: 10946;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1369;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1370;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1371;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1372;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1373;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1374;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1375;r1: 14328;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1376;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1377;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1378;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1379;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1380;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1381;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1382;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1383;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1384;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6765;cx: 10946;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1385;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 10946;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1386;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 10946;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1387;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 10946;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1388;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 10946;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1389;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1390;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1391;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1392;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1393;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1394;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1395;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1396;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1397;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1398;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1399;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1400;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1401;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1402;r1: 10946;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1403;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1404;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1405;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1406;r1: 17711;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1407;r1: 17711;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1408;r1: 17711;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1409;r1: 17711;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1410;r1: 17711;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1411;r1: 17711;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1412;r1: 17711;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1413;r1: 17711;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1414;r1: 17711;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1415;r1: 17711;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1416;r1: 17711;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1417;r1: 17711;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1418;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1419;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1420;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1421;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1422;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1423;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1424;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1425;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1426;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1427;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1428;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1429;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1430;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1431;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1432;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 6765;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1433;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 6765;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1434;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 6765;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1435;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 6765;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1436;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 6765;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1437;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 17711;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1438;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 17711;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1439;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 17711;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1440;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 17711;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1441;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 17711;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1442;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 17711;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1443;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 17711;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1444;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 17711;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1445;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 17711;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1446;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 17711;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1447;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 17711;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1448;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 10946;cx: 17711;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1449;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 17711;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1450;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 17711;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1451;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 17711;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1452;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 17711;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1453;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1454;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1455;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1456;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1457;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1458;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1459;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1460;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1461;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1462;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1463;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1464;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1465;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1466;r1: 17711;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1467;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1468;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1469;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1470;r1: 28657;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1471;r1: 28657;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1472;r1: 28657;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1473;r1: 28657;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1474;r1: 28657;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1475;r1: 28657;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1476;r1: 28657;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1477;r1: 28657;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1478;r1: 28657;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1479;r1: 28657;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1480;r1: 28657;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1481;r1: 28657;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1482;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1483;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1484;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1485;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1486;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1487;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1488;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1489;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1490;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1491;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1492;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1493;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1494;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1495;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1496;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 10946;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1497;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 10946;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1498;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 10946;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1499;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 10946;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1500;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 10946;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1501;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 28657;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1502;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 28657;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1503;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 28657;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1504;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 28657;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1505;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 28657;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1506;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 28657;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1507;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 28657;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1508;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 28657;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1509;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 28657;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1510;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 28657;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1511;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 28657;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1512;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 17711;cx: 28657;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1513;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 28657;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1514;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 28657;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1515;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 28657;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1516;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 28657;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1517;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1518;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1519;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1520;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1521;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1522;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1523;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1524;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1525;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1526;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1527;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1528;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1529;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1530;r1: 28657;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1531;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1532;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1533;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1534;r1: 46368;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1535;r1: 46368;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1536;r1: 46368;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1537;r1: 46368;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1538;r1: 46368;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1539;r1: 46368;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1540;r1: 46368;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1541;r1: 46368;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1542;r1: 46368;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1543;r1: 46368;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1544;r1: 46368;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1545;r1: 46368;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1546;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1547;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1548;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1549;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1550;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1551;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1552;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1553;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1554;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1555;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1556;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4113;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1557;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1558;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 17711;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1559;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 17711;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1560;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 17711;dx: 0;ip: 4114;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1561;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 17711;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1562;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 17711;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1563;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 46368;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1564;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 46368;dx: 0;ip: 4115;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1565;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 46368;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1566;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 46368;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1567;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 46368;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1568;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 46368;dx: 0;ip: 4116;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1569;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 46368;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1570;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 46368;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1571;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 46368;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1572;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 46368;dx: 0;ip: 4117;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1573;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 46368;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1574;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 14328;cx: 46368;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1575;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1576;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1577;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1578;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1579;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1580;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1581;r1: 60696;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1582;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1583;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1584;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1585;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1586;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1587;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1588;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1589;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1590;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 28657;cx: 46368;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1591;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 46368;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1592;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 46368;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1593;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 46368;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1594;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 46368;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1595;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1596;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1597;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1598;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1599;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1600;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1601;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1602;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1603;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1604;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1605;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1606;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1607;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1608;r1: 46368;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1609;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1610;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1611;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1612;r1: 75025;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1613;r1: 75025;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1614;r1: 75025;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1615;r1: 75025;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1616;r1: 75025;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1617;r1: 75025;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1618;r1: 75025;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1619;r1: 75025;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1620;r1: 75025;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1621;r1: 75025;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1622;r1: 75025;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1623;r1: 75025;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1624;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1625;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1626;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1627;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1628;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1629;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1630;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1631;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1632;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1633;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1634;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1635;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1636;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1637;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1638;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 28657;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1639;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 28657;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1640;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 28657;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1641;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 28657;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1642;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 28657;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1643;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 75025;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1644;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 75025;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1645;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 75025;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1646;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 75025;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1647;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 75025;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1648;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 75025;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1649;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 75025;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1650;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 75025;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1651;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 75025;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1652;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 75025;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1653;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 75025;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1654;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 46368;cx: 75025;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1655;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 75025;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1656;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 75025;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1657;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 75025;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1658;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 75025;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1659;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1660;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1661;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1662;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1663;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1664;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1665;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1666;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1667;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1668;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1669;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1670;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1671;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1672;r1: 75025;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1673;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1674;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1675;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1676;r1: 121393;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1677;r1: 121393;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1678;r1: 121393;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1679;r1: 121393;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1680;r1: 121393;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1681;r1: 121393;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1682;r1: 121393;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1683;r1: 121393;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1684;r1: 121393;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1685;r1: 121393;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1686;r1: 121393;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1687;r1: 121393;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1688;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1689;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1690;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1691;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1692;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1693;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1694;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1695;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1696;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1697;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1698;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1699;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1700;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1701;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1702;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 46368;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1703;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 46368;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1704;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 46368;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1705;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 46368;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1706;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 46368;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1707;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 121393;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1708;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 121393;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1709;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 121393;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1710;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 121393;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1711;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 121393;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1712;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 121393;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1713;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 121393;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1714;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 121393;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1715;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 121393;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1716;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 121393;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1717;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 121393;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1718;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 75025;cx: 121393;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1719;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 121393;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1720;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 121393;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1721;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 121393;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1722;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 121393;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1723;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1724;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1725;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1726;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1727;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1728;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1729;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1730;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1731;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1732;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1733;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1734;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1735;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1736;r1: 121393;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1737;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1738;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1739;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1740;r1: 196418;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1741;r1: 196418;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1742;r1: 196418;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1743;r1: 196418;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1744;r1: 196418;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1745;r1: 196418;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1746;r1: 196418;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1747;r1: 196418;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1748;r1: 196418;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1749;r1: 196418;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1750;r1: 196418;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1751;r1: 196418;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1752;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1753;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1754;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1755;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1756;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1757;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1758;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1759;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1760;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1761;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1762;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4113;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1763;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1764;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 75025;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1765;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 75025;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1766;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 75025;dx: 0;ip: 4114;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1767;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 75025;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1768;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 75025;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1769;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 196418;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1770;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 196418;dx: 0;ip: 4115;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1771;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 196418;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1772;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 196418;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1773;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 196418;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1774;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 196418;dx: 0;ip: 4116;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1775;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 196418;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1776;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 196418;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1777;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 196418;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1778;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 196418;dx: 0;ip: 4117;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1779;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 196418;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1780;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 60696;cx: 196418;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1781;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1782;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1783;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1784;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1785;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1786;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1787;r1: 257114;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1788;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1789;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1790;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1791;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1792;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1793;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1794;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1795;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1796;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 121393;cx: 196418;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1797;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 196418;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1798;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 196418;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1799;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 196418;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1800;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 196418;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1801;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1802;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1803;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1804;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1805;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1806;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1807;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1808;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1809;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1810;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1811;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1812;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1813;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1814;r1: 196418;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1815;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1816;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1817;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1818;r1: 317811;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1819;r1: 317811;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1820;r1: 317811;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1821;r1: 317811;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1822;r1: 317811;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1823;r1: 317811;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1824;r1: 317811;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1825;r1: 317811;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1826;r1: 317811;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1827;r1: 317811;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1828;r1: 317811;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1829;r1: 317811;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1830;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1831;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1832;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1833;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1834;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1835;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1836;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1837;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1838;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1839;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1840;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1841;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1842;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1843;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1844;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 121393;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1845;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 121393;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1846;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 121393;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1847;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 121393;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1848;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 121393;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1849;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 317811;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1850;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 317811;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1851;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 317811;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1852;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 317811;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1853;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 317811;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1854;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 317811;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1855;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 317811;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1856;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 317811;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1857;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 317811;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1858;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 317811;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1859;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 317811;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1860;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 196418;cx: 317811;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1861;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 317811;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1862;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 317811;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1863;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 317811;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1864;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 317811;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1865;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1866;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1867;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1868;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1869;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1870;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1871;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1872;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1873;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1874;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1875;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1876;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1877;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1878;r1: 317811;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1879;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1880;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1881;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1882;r1: 514229;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1883;r1: 514229;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1884;r1: 514229;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1885;r1: 514229;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1886;r1: 514229;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1887;r1: 514229;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1888;r1: 514229;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1889;r1: 514229;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1890;r1: 514229;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1891;r1: 514229;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1892;r1: 514229;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1893;r1: 514229;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1894;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1895;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1896;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1897;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1898;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1899;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1900;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1901;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1902;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1903;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1904;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1905;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1906;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1907;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1908;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 196418;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1909;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 196418;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1910;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 196418;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1911;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 196418;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1912;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 196418;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1913;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 514229;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1914;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 514229;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1915;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 514229;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1916;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 514229;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1917;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 514229;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1918;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 514229;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1919;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 514229;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1920;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 514229;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1921;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 514229;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1922;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 514229;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1923;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 514229;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1924;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 317811;cx: 514229;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1925;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 514229;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1926;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 514229;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1927;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 514229;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1928;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 514229;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1929;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1930;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1931;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1932;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1933;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1934;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1935;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1936;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1937;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1938;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1939;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1940;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1941;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1942;r1: 514229;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1943;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1944;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1945;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1946;r1: 832040;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1947;r1: 832040;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1948;r1: 832040;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1949;r1: 832040;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1950;r1: 832040;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1951;r1: 832040;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1952;r1: 832040;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1953;r1: 832040;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1954;r1: 832040;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1955;r1: 832040;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1956;r1: 832040;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1957;r1: 832040;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1958;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 1959;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1960;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1961;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1962;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1963;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1964;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1965;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1966;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1967;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1968;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4113;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1969;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1970;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 317811;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1971;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 317811;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1972;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 317811;dx: 0;ip: 4114;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1973;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 317811;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 1974;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 317811;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1975;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 832040;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1976;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 832040;dx: 0;ip: 4115;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1977;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 832040;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1978;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 832040;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 1979;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 832040;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1980;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 832040;dx: 0;ip: 4116;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1981;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 832040;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1982;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 832040;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1983;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 832040;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1984;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 832040;dx: 0;ip: 4117;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1985;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 832040;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 1986;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 257114;cx: 832040;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1987;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1988;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1989;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 1990;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1991;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1992;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1993;r1: 1089154;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1994;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1995;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1996;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1997;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1998;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 1999;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2000;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2001;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2002;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 514229;cx: 832040;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2003;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 832040;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2004;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 832040;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2005;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 832040;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2006;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 832040;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2007;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2008;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2009;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2010;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2011;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2012;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2013;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2014;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2015;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2016;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2017;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2018;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2019;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2020;r1: 832040;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2021;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2022;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2023;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2024;r1: 1346269;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2025;r1: 1346269;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2026;r1: 1346269;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2027;r1: 1346269;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2028;r1: 1346269;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2029;r1: 1346269;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2030;r1: 1346269;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2031;r1: 1346269;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2032;r1: 1346269;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2033;r1: 1346269;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2034;r1: 1346269;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2035;r1: 1346269;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2036;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2037;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2038;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2039;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2040;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2041;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2042;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2043;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2044;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2045;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2046;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2047;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2048;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2049;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2050;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 514229;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2051;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 514229;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2052;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 514229;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2053;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 514229;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2054;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 514229;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2055;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 1346269;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2056;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 1346269;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2057;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 1346269;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2058;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 1346269;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2059;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 1346269;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2060;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 1346269;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2061;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 1346269;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2062;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 1346269;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2063;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 1346269;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2064;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 1346269;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2065;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 1346269;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2066;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 832040;cx: 1346269;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2067;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 1346269;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2068;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 1346269;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2069;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 1346269;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2070;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 1346269;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2071;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2072;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2073;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2074;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2075;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2076;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2077;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2078;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2079;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2080;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2081;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2082;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2083;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2084;r1: 1346269;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2085;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2086;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2087;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2088;r1: 2178309;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2089;r1: 2178309;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2090;r1: 2178309;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2091;r1: 2178309;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2092;r1: 2178309;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2093;r1: 2178309;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2094;r1: 2178309;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2095;r1: 2178309;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2096;r1: 2178309;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2097;r1: 2178309;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2098;r1: 2178309;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2099;r1: 2178309;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2100;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2101;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2102;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2103;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2104;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2105;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2106;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2107;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2108;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2109;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2110;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4112;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2111;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4112;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2112;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4117;cr: jmp 4117 None None 4112;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2113;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2114;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 832040;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2115;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 832040;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2116;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 832040;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2117;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 832040;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2118;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 832040;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2119;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 2178309;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2120;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 2178309;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2121;r1: 1;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 2178309;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2122;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 2178309;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2123;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 2178309;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2124;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 2178309;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2125;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 2178309;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2126;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 2178309;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2127;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 2178309;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2128;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 2178309;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2129;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 2178309;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2130;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1346269;cx: 2178309;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2131;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 2178309;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2132;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 2178309;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2133;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 2178309;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2134;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 2178309;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2135;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2136;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2137;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2138;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2139;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2140;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2141;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2142;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2143;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2144;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2145;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2146;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2147;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2148;r1: 2178309;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2149;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2150;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2151;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2152;r1: 3524578;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2153;r1: 3524578;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2154;r1: 3524578;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2155;r1: 3524578;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2156;r1: 3524578;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2157;r1: 3524578;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2158;r1: 3524578;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4107;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2159;r1: 3524578;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2160;r1: 3524578;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2161;r1: 3524578;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4107;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2162;r1: 3524578;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4108;cr: ld #101 bx None 4107;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2163;r1: 3524578;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2164;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: True;ZF: False>
<tick_number: 2165;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4108;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2166;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4109;cr: mod bx 2 Register.R1 4108;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2167;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2168;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4109;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2169;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4110;cr: ld 0 Register.R2 None 4109;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2170;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2171;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4110;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2172;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4111;cr: cmp Register.R1 Register.R2 None 4110;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2173;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4111;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2174;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4113;cr: je 4113 None None 4111;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2175;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2176;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3524578;cx: 1346269;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 2177;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 1346269;dx: 0;ip: 4113;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 2178;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 1346269;dx: 0;ip: 4114;cr: ld #102 bx None 4113;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 2179;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 1346269;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 102;sp: 8191;NF: False;ZF: True>
<tick_number: 2180;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 1346269;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2181;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 3524578;dx: 0;ip: 4114;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2182;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 3524578;dx: 0;ip: 4115;cr: ld #101 cx None 4114;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2183;r1: 0;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 3524578;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2184;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 3524578;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: True>
<tick_number: 2185;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 3524578;dx: 0;ip: 4115;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2186;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 3524578;dx: 0;ip: 4116;cr: add bx cx Register.R1 4115;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2187;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 3524578;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2188;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 3524578;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2189;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 3524578;dx: 0;ip: 4116;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2190;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 3524578;dx: 0;ip: 4117;cr: st Register.R1 #102 None 4116;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2191;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 3524578;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2192;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1089154;cx: 3524578;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2193;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4117;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2194;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4118;cr: ld #100 bx None 4117;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2195;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2196;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2197;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4118;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2198;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4119;cr: ld #101 cx None 4118;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2199;r1: 4613732;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2200;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2201;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4119;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2202;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4120;cr: add bx cx Register.R1 4119;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2203;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2204;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2205;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4120;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2206;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4121;cr: st Register.R1 #101 None 4120;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2207;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2208;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2178309;cx: 3524578;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2209;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 3524578;dx: 0;ip: 4121;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2210;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 3524578;dx: 0;ip: 4122;cr: ld #101 bx None 4121;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2211;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 3524578;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2212;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 3524578;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2213;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4122;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2214;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4123;cr: ld #100 cx None 4122;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2215;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2216;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2217;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4123;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2218;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4124;cr: sub bx cx Register.R1 4123;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2219;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2220;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2221;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4124;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2222;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4125;cr: st Register.R1 #100 None 4124;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2223;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4125;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2224;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4102;cr: jmp 4102 None None 4125;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2225;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 100;sp: 8191;NF: False;ZF: False>
<tick_number: 2226;r1: 3524578;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2227;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4102;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2228;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4103;cr: ld #101 Register.R1 None 4102;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2229;r1: 5702887;r2: 0;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2230;r1: 5702887;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4103;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2231;r1: 5702887;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4104;cr: ld 4000000 Register.R2 None 4103;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2232;r1: 5702887;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2233;r1: 5702887;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4104;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2234;r1: 5702887;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4105;cr: cmp Register.R1 Register.R2 None 4104;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2235;r1: 5702887;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4105;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2236;r1: 5702887;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4106;cr: jl 4107 None None 4105;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2237;r1: 5702887;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4106;cr: jmp 4126 None None 4106;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2238;r1: 5702887;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4126;cr: jmp 4126 None None 4106;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2239;r1: 5702887;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4126;cr: ld #102 Register.R1 None 4126;dr: 101;sp: 8191;NF: False;ZF: False>
<tick_number: 2240;r1: 5702887;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4126;cr: ld #102 Register.R1 None 4126;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2241;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4126;cr: ld #102 Register.R1 None 4126;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2242;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4127;cr: ld #102 Register.R1 None 4126;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2243;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4127;cr: cmp Register.R1 0 None 4127;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2244;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4127;cr: cmp Register.R1 0 None 4127;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2245;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4128;cr: cmp Register.R1 0 None 4127;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2246;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4128;cr: jl 4139 None None 4128;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2247;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4129;cr: jl 4139 None None 4128;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2248;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4129;cr: je 4134 None None 4129;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2249;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4130;cr: je 4134 None None 4129;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2250;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 5702887;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2251;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2252;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2253;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4131;cr: mod Register.R1 10 bx 4130;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2254;r1: 4613732;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2255;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2256;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2257;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4132;cr: div Register.R1 10 Register.R1 4131;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2258;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 102;sp: 8191;NF: False;ZF: False>
<tick_number: 2259;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8191;sp: 8191;NF: False;ZF: False>
<tick_number: 2260;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8191;sp: 8191;NF: False;ZF: False>
<tick_number: 2261;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2262;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4133;cr: push bx None None 4132;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2263;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4133;cr: jmp 4129 None None 4133;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2264;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4129;cr: jmp 4129 None None 4133;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2265;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4129;cr: je 4134 None None 4129;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2266;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4130;cr: je 4134 None None 4129;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2267;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 2;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2268;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2269;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2270;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4131;cr: mod Register.R1 10 bx 4130;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2271;r1: 461373;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2272;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2273;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2274;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4132;cr: div Register.R1 10 Register.R1 4131;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2275;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8191;sp: 8190;NF: False;ZF: False>
<tick_number: 2276;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8190;sp: 8190;NF: False;ZF: False>
<tick_number: 2277;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8190;sp: 8190;NF: False;ZF: False>
<tick_number: 2278;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2279;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4133;cr: push bx None None 4132;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2280;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4133;cr: jmp 4129 None None 4133;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2281;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4129;cr: jmp 4129 None None 4133;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2282;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4129;cr: je 4134 None None 4129;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2283;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4130;cr: je 4134 None None 4129;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2284;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2285;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2286;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2287;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4131;cr: mod Register.R1 10 bx 4130;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2288;r1: 46137;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2289;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2290;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2291;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4132;cr: div Register.R1 10 Register.R1 4131;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2292;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8190;sp: 8189;NF: False;ZF: False>
<tick_number: 2293;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8189;sp: 8189;NF: False;ZF: False>
<tick_number: 2294;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8189;sp: 8189;NF: False;ZF: False>
<tick_number: 2295;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2296;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4133;cr: push bx None None 4132;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2297;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4133;cr: jmp 4129 None None 4133;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2298;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4129;cr: jmp 4129 None None 4133;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2299;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4129;cr: je 4134 None None 4129;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2300;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4130;cr: je 4134 None None 4129;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2301;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 7;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2302;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2303;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2304;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4131;cr: mod Register.R1 10 bx 4130;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2305;r1: 4613;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2306;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2307;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2308;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4132;cr: div Register.R1 10 Register.R1 4131;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2309;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8189;sp: 8188;NF: False;ZF: False>
<tick_number: 2310;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8188;sp: 8188;NF: False;ZF: False>
<tick_number: 2311;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8188;sp: 8188;NF: False;ZF: False>
<tick_number: 2312;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2313;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4133;cr: push bx None None 4132;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2314;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4133;cr: jmp 4129 None None 4133;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2315;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4129;cr: jmp 4129 None None 4133;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2316;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4129;cr: je 4134 None None 4129;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2317;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4130;cr: je 4134 None None 4129;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2318;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 3;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2319;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2320;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2321;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4131;cr: mod Register.R1 10 bx 4130;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2322;r1: 461;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2323;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2324;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2325;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4132;cr: div Register.R1 10 Register.R1 4131;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2326;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8188;sp: 8187;NF: False;ZF: False>
<tick_number: 2327;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8187;sp: 8187;NF: False;ZF: False>
<tick_number: 2328;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8187;sp: 8187;NF: False;ZF: False>
<tick_number: 2329;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2330;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4133;cr: push bx None None 4132;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2331;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4133;cr: jmp 4129 None None 4133;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2332;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4129;cr: jmp 4129 None None 4133;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2333;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4129;cr: je 4134 None None 4129;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2334;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4130;cr: je 4134 None None 4129;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2335;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 1;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2336;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2337;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2338;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4131;cr: mod Register.R1 10 bx 4130;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2339;r1: 46;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2340;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2341;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2342;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4132;cr: div Register.R1 10 Register.R1 4131;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2343;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8187;sp: 8186;NF: False;ZF: False>
<tick_number: 2344;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8186;sp: 8186;NF: False;ZF: False>
<tick_number: 2345;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8186;sp: 8186;NF: False;ZF: False>
<tick_number: 2346;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8186;sp: 8185;NF: False;ZF: False>
<tick_number: 2347;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4133;cr: push bx None None 4132;dr: 8186;sp: 8185;NF: False;ZF: False>
<tick_number: 2348;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4133;cr: jmp 4129 None None 4133;dr: 8186;sp: 8185;NF: False;ZF: False>
<tick_number: 2349;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4129;cr: jmp 4129 None None 4133;dr: 8186;sp: 8185;NF: False;ZF: False>
<tick_number: 2350;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4129;cr: je 4134 None None 4129;dr: 8186;sp: 8185;NF: False;ZF: False>
<tick_number: 2351;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4130;cr: je 4134 None None 4129;dr: 8186;sp: 8185;NF: False;ZF: False>
<tick_number: 2352;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 6;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8186;sp: 8185;NF: False;ZF: False>
<tick_number: 2353;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8186;sp: 8185;NF: False;ZF: False>
<tick_number: 2354;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4130;cr: mod Register.R1 10 bx 4130;dr: 8186;sp: 8185;NF: False;ZF: False>
<tick_number: 2355;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4131;cr: mod Register.R1 10 bx 4130;dr: 8186;sp: 8185;NF: False;ZF: False>
<tick_number: 2356;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8186;sp: 8185;NF: False;ZF: False>
<tick_number: 2357;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8186;sp: 8185;NF: False;ZF: False>
<tick_number: 2358;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4131;cr: div Register.R1 10 Register.R1 4131;dr: 8186;sp: 8185;NF: False;ZF: True>
<tick_number: 2359;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4132;cr: div Register.R1 10 Register.R1 4131;dr: 8186;sp: 8185;NF: False;ZF: True>
<tick_number: 2360;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8186;sp: 8185;NF: False;ZF: True>
<tick_number: 2361;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8185;sp: 8185;NF: False;ZF: True>
<tick_number: 2362;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8185;sp: 8185;NF: False;ZF: True>
<tick_number: 2363;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4132;cr: push bx None None 4132;dr: 8185;sp: 8184;NF: False;ZF: True>
<tick_number: 2364;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4133;cr: push bx None None 4132;dr: 8185;sp: 8184;NF: False;ZF: True>
<tick_number: 2365;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4133;cr: jmp 4129 None None 4133;dr: 8185;sp: 8184;NF: False;ZF: True>
<tick_number: 2366;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4129;cr: jmp 4129 None None 4133;dr: 8185;sp: 8184;NF: False;ZF: True>
<tick_number: 2367;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4129;cr: je 4134 None None 4129;dr: 8185;sp: 8184;NF: False;ZF: True>
<tick_number: 2368;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: je 4134 None None 4129;dr: 8185;sp: 8184;NF: False;ZF: True>
<tick_number: 2369;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8185;sp: 8184;NF: False;ZF: True>
<tick_number: 2370;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8185;sp: 8184;NF: True;ZF: False>
<tick_number: 2371;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: cmp sp 8191 None 4134;dr: 8185;sp: 8184;NF: True;ZF: False>
<tick_number: 2372;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: je 4153 None None 4135;dr: 8185;sp: 8184;NF: True;ZF: False>
<tick_number: 2373;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: je 4153 None None 4135;dr: 8185;sp: 8184;NF: True;ZF: False>
<tick_number: 2374;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8185;sp: 8184;NF: True;ZF: False>
<tick_number: 2375;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8185;sp: 8185;NF: True;ZF: False>
<tick_number: 2376;r1: 0;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8185;sp: 8185;NF: True;ZF: False>
<tick_number: 2377;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8185;sp: 8185;NF: True;ZF: False>
<tick_number: 2378;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: pop Register.R1 None None 4136;dr: 8185;sp: 8185;NF: True;ZF: False>
<tick_number: 2379;r1: 4;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8185;sp: 8185;NF: True;ZF: False>
<tick_number: 2380;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8185;sp: 8185;NF: True;ZF: False>
<tick_number: 2381;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8185;sp: 8185;NF: False;ZF: False>
<tick_number: 2382;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: add Register.R1 48 Register.R1 4137;dr: 8185;sp: 8185;NF: False;ZF: False>
<tick_number: 2383;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8185;sp: 8185;NF: False;ZF: False>
<tick_number: 2384;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8185;sp: 8185;NF: False;ZF: False>
<tick_number: 2385;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: print Register.R1 None None 4138;dr: 8185;sp: 8185;NF: False;ZF: False>
<tick_number: 2386;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: jmp 4134 None None 4139;dr: 8185;sp: 8185;NF: False;ZF: False>
<tick_number: 2387;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: jmp 4134 None None 4139;dr: 8185;sp: 8185;NF: False;ZF: False>
<tick_number: 2388;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8185;sp: 8185;NF: False;ZF: False>
<tick_number: 2389;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8185;sp: 8185;NF: True;ZF: False>
<tick_number: 2390;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: cmp sp 8191 None 4134;dr: 8185;sp: 8185;NF: True;ZF: False>
<tick_number: 2391;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: je 4153 None None 4135;dr: 8185;sp: 8185;NF: True;ZF: False>
<tick_number: 2392;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: je 4153 None None 4135;dr: 8185;sp: 8185;NF: True;ZF: False>
<tick_number: 2393;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8185;sp: 8185;NF: True;ZF: False>
<tick_number: 2394;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8185;sp: 8186;NF: True;ZF: False>
<tick_number: 2395;r1: 52;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8186;sp: 8186;NF: True;ZF: False>
<tick_number: 2396;r1: 6;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8186;sp: 8186;NF: True;ZF: False>
<tick_number: 2397;r1: 6;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: pop Register.R1 None None 4136;dr: 8186;sp: 8186;NF: True;ZF: False>
<tick_number: 2398;r1: 6;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8186;sp: 8186;NF: True;ZF: False>
<tick_number: 2399;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8186;sp: 8186;NF: True;ZF: False>
<tick_number: 2400;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8186;sp: 8186;NF: False;ZF: False>
<tick_number: 2401;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: add Register.R1 48 Register.R1 4137;dr: 8186;sp: 8186;NF: False;ZF: False>
<tick_number: 2402;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8186;sp: 8186;NF: False;ZF: False>
<tick_number: 2403;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8186;sp: 8186;NF: False;ZF: False>
<tick_number: 2404;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: print Register.R1 None None 4138;dr: 8186;sp: 8186;NF: False;ZF: False>
<tick_number: 2405;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: jmp 4134 None None 4139;dr: 8186;sp: 8186;NF: False;ZF: False>
<tick_number: 2406;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: jmp 4134 None None 4139;dr: 8186;sp: 8186;NF: False;ZF: False>
<tick_number: 2407;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8186;sp: 8186;NF: False;ZF: False>
<tick_number: 2408;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8186;sp: 8186;NF: True;ZF: False>
<tick_number: 2409;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: cmp sp 8191 None 4134;dr: 8186;sp: 8186;NF: True;ZF: False>
<tick_number: 2410;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: je 4153 None None 4135;dr: 8186;sp: 8186;NF: True;ZF: False>
<tick_number: 2411;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: je 4153 None None 4135;dr: 8186;sp: 8186;NF: True;ZF: False>
<tick_number: 2412;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8186;sp: 8186;NF: True;ZF: False>
<tick_number: 2413;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8186;sp: 8187;NF: True;ZF: False>
<tick_number: 2414;r1: 54;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8187;sp: 8187;NF: True;ZF: False>
<tick_number: 2415;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8187;sp: 8187;NF: True;ZF: False>
<tick_number: 2416;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: pop Register.R1 None None 4136;dr: 8187;sp: 8187;NF: True;ZF: False>
<tick_number: 2417;r1: 1;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8187;sp: 8187;NF: True;ZF: False>
<tick_number: 2418;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8187;sp: 8187;NF: True;ZF: False>
<tick_number: 2419;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8187;sp: 8187;NF: False;ZF: False>
<tick_number: 2420;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: add Register.R1 48 Register.R1 4137;dr: 8187;sp: 8187;NF: False;ZF: False>
<tick_number: 2421;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8187;sp: 8187;NF: False;ZF: False>
<tick_number: 2422;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8187;sp: 8187;NF: False;ZF: False>
<tick_number: 2423;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: print Register.R1 None None 4138;dr: 8187;sp: 8187;NF: False;ZF: False>
<tick_number: 2424;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: jmp 4134 None None 4139;dr: 8187;sp: 8187;NF: False;ZF: False>
<tick_number: 2425;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: jmp 4134 None None 4139;dr: 8187;sp: 8187;NF: False;ZF: False>
<tick_number: 2426;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8187;sp: 8187;NF: False;ZF: False>
<tick_number: 2427;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8187;sp: 8187;NF: True;ZF: False>
<tick_number: 2428;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: cmp sp 8191 None 4134;dr: 8187;sp: 8187;NF: True;ZF: False>
<tick_number: 2429;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: je 4153 None None 4135;dr: 8187;sp: 8187;NF: True;ZF: False>
<tick_number: 2430;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: je 4153 None None 4135;dr: 8187;sp: 8187;NF: True;ZF: False>
<tick_number: 2431;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8187;sp: 8187;NF: True;ZF: False>
<tick_number: 2432;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8187;sp: 8188;NF: True;ZF: False>
<tick_number: 2433;r1: 49;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8188;sp: 8188;NF: True;ZF: False>
<tick_number: 2434;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8188;sp: 8188;NF: True;ZF: False>
<tick_number: 2435;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: pop Register.R1 None None 4136;dr: 8188;sp: 8188;NF: True;ZF: False>
<tick_number: 2436;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8188;sp: 8188;NF: True;ZF: False>
<tick_number: 2437;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8188;sp: 8188;NF: True;ZF: False>
<tick_number: 2438;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8188;sp: 8188;NF: False;ZF: False>
<tick_number: 2439;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: add Register.R1 48 Register.R1 4137;dr: 8188;sp: 8188;NF: False;ZF: False>
<tick_number: 2440;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8188;sp: 8188;NF: False;ZF: False>
<tick_number: 2441;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8188;sp: 8188;NF: False;ZF: False>
<tick_number: 2442;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: print Register.R1 None None 4138;dr: 8188;sp: 8188;NF: False;ZF: False>
<tick_number: 2443;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: jmp 4134 None None 4139;dr: 8188;sp: 8188;NF: False;ZF: False>
<tick_number: 2444;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: jmp 4134 None None 4139;dr: 8188;sp: 8188;NF: False;ZF: False>
<tick_number: 2445;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8188;sp: 8188;NF: False;ZF: False>
<tick_number: 2446;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8188;sp: 8188;NF: True;ZF: False>
<tick_number: 2447;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: cmp sp 8191 None 4134;dr: 8188;sp: 8188;NF: True;ZF: False>
<tick_number: 2448;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: je 4153 None None 4135;dr: 8188;sp: 8188;NF: True;ZF: False>
<tick_number: 2449;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: je 4153 None None 4135;dr: 8188;sp: 8188;NF: True;ZF: False>
<tick_number: 2450;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8188;sp: 8188;NF: True;ZF: False>
<tick_number: 2451;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8188;sp: 8189;NF: True;ZF: False>
<tick_number: 2452;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8189;sp: 8189;NF: True;ZF: False>
<tick_number: 2453;r1: 7;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8189;sp: 8189;NF: True;ZF: False>
<tick_number: 2454;r1: 7;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: pop Register.R1 None None 4136;dr: 8189;sp: 8189;NF: True;ZF: False>
<tick_number: 2455;r1: 7;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8189;sp: 8189;NF: True;ZF: False>
<tick_number: 2456;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8189;sp: 8189;NF: True;ZF: False>
<tick_number: 2457;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8189;sp: 8189;NF: False;ZF: False>
<tick_number: 2458;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: add Register.R1 48 Register.R1 4137;dr: 8189;sp: 8189;NF: False;ZF: False>
<tick_number: 2459;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8189;sp: 8189;NF: False;ZF: False>
<tick_number: 2460;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8189;sp: 8189;NF: False;ZF: False>
<tick_number: 2461;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: print Register.R1 None None 4138;dr: 8189;sp: 8189;NF: False;ZF: False>
<tick_number: 2462;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: jmp 4134 None None 4139;dr: 8189;sp: 8189;NF: False;ZF: False>
<tick_number: 2463;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: jmp 4134 None None 4139;dr: 8189;sp: 8189;NF: False;ZF: False>
<tick_number: 2464;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8189;sp: 8189;NF: False;ZF: False>
<tick_number: 2465;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8189;sp: 8189;NF: True;ZF: False>
<tick_number: 2466;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: cmp sp 8191 None 4134;dr: 8189;sp: 8189;NF: True;ZF: False>
<tick_number: 2467;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: je 4153 None None 4135;dr: 8189;sp: 8189;NF: True;ZF: False>
<tick_number: 2468;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: je 4153 None None 4135;dr: 8189;sp: 8189;NF: True;ZF: False>
<tick_number: 2469;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8189;sp: 8189;NF: True;ZF: False>
<tick_number: 2470;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8189;sp: 8190;NF: True;ZF: False>
<tick_number: 2471;r1: 55;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8190;sp: 8190;NF: True;ZF: False>
<tick_number: 2472;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8190;sp: 8190;NF: True;ZF: False>
<tick_number: 2473;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: pop Register.R1 None None 4136;dr: 8190;sp: 8190;NF: True;ZF: False>
<tick_number: 2474;r1: 3;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8190;sp: 8190;NF: True;ZF: False>
<tick_number: 2475;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8190;sp: 8190;NF: True;ZF: False>
<tick_number: 2476;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8190;sp: 8190;NF: False;ZF: False>
<tick_number: 2477;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: add Register.R1 48 Register.R1 4137;dr: 8190;sp: 8190;NF: False;ZF: False>
<tick_number: 2478;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8190;sp: 8190;NF: False;ZF: False>
<tick_number: 2479;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8190;sp: 8190;NF: False;ZF: False>
<tick_number: 2480;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: print Register.R1 None None 4138;dr: 8190;sp: 8190;NF: False;ZF: False>
<tick_number: 2481;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: jmp 4134 None None 4139;dr: 8190;sp: 8190;NF: False;ZF: False>
<tick_number: 2482;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: jmp 4134 None None 4139;dr: 8190;sp: 8190;NF: False;ZF: False>
<tick_number: 2483;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8190;sp: 8190;NF: False;ZF: False>
<tick_number: 2484;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8190;sp: 8190;NF: True;ZF: False>
<tick_number: 2485;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: cmp sp 8191 None 4134;dr: 8190;sp: 8190;NF: True;ZF: False>
<tick_number: 2486;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: je 4153 None None 4135;dr: 8190;sp: 8190;NF: True;ZF: False>
<tick_number: 2487;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: je 4153 None None 4135;dr: 8190;sp: 8190;NF: True;ZF: False>
<tick_number: 2488;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8190;sp: 8190;NF: True;ZF: False>
<tick_number: 2489;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8190;sp: 8191;NF: True;ZF: False>
<tick_number: 2490;r1: 51;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8191;sp: 8191;NF: True;ZF: False>
<tick_number: 2491;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4136;cr: pop Register.R1 None None 4136;dr: 8191;sp: 8191;NF: True;ZF: False>
<tick_number: 2492;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: pop Register.R1 None None 4136;dr: 8191;sp: 8191;NF: True;ZF: False>
<tick_number: 2493;r1: 2;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8191;sp: 8191;NF: True;ZF: False>
<tick_number: 2494;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8191;sp: 8191;NF: True;ZF: False>
<tick_number: 2495;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4137;cr: add Register.R1 48 Register.R1 4137;dr: 8191;sp: 8191;NF: False;ZF: False>
<tick_number: 2496;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: add Register.R1 48 Register.R1 4137;dr: 8191;sp: 8191;NF: False;ZF: False>
<tick_number: 2497;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8191;sp: 8191;NF: False;ZF: False>
<tick_number: 2498;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4138;cr: print Register.R1 None None 4138;dr: 8191;sp: 8191;NF: False;ZF: False>
<tick_number: 2499;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: print Register.R1 None None 4138;dr: 8191;sp: 8191;NF: False;ZF: False>
<tick_number: 2500;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4139;cr: jmp 4134 None None 4139;dr: 8191;sp: 8191;NF: False;ZF: False>
<tick_number: 2501;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: jmp 4134 None None 4139;dr: 8191;sp: 8191;NF: False;ZF: False>
<tick_number: 2502;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8191;sp: 8191;NF: False;ZF: False>
<tick_number: 2503;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4134;cr: cmp sp 8191 None 4134;dr: 8191;sp: 8191;NF: False;ZF: True>
<tick_number: 2504;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: cmp sp 8191 None 4134;dr: 8191;sp: 8191;NF: False;ZF: True>
<tick_number: 2505;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4135;cr: je 4153 None None 4135;dr: 8191;sp: 8191;NF: False;ZF: True>
<tick_number: 2506;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4153;cr: je 4153 None None 4135;dr: 8191;sp: 8191;NF: False;ZF: True>
<tick_number: 2507;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4153;cr: hlt None None None 4153;dr: 8191;sp: 8191;NF: False;ZF: True>
<tick_number: 2508;r1: 50;r2: 4000000;r3: 0;r4: 0;r5: 0;r6: 0;bx: 4;cx: 2178309;dx: 0;ip: 4153;cr: hlt None None None 4153;dr: 8191;sp: 8191;NF: False;ZF: True>

```

### Аналитика

```
|           Full name        | alg            | loc | bytes | instr | exec_instr | tick |                                            variant                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Потапенко Артем Денисович  | prob2          | 7   | -     | 57    |  736       | 2508 |     alg -> asm | risc | neum | hw | tick -> instr | struct | stream | mem | cstr | prob2 | cache|
| Потапенко Артем Денисович  | cat            | 3   | -     | 12    | 6362       | 19792|     alg -> asm | risc | neum | hw | tick -> instr | struct | stream | mem | cstr | prob2 | cache|
| Потапенко Артем Денисович  | hello_world    | 1   | -     | 14    | 19         | 58   |     alg -> asm | risc | neum | hw | tick -> instr | struct | stream | mem | cstr | prob2 | cache|
| Потапенко Артем Денисович  | hello_user     | 17  | -     | 15    | 45         | 5074 |     alg -> asm | risc | neum | hw | tick -> instr | struct | stream | mem | cstr | prob2 | cache|
| Потапенко Артем Денисович  | cycles         | 3   | -     | 47    | 1029       | 3774 |     alg -> asm | risc | neum | hw | tick -> instr | struct | stream | mem | cstr | prob2 | cache|
| Потапенко Артем Денисович  | arith          | 2   | -     |44     | 68         | 281 |     alg -> asm | risc | neum | hw | tick -> instr | struct | stream | mem | cstr | prob2 | cache|

```
