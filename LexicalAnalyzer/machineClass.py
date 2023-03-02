from enum import Enum
from tkinter import *


class State():
    Start = 0
    Letter = 1
    Num = 2
    Dot = 3
    Del = 4
    SingleOp = 5
    Divider = 6
    Sravn = 7
    EOF = 8
    Error = 9
    StrConst = 10
    LetterAndNum = 1.2
    NumAndDot = 2.3
    LetterAndDot = 1.3
    End = 999


class Machine:
    def __init__(self, state, alphabet):
        self._state = state
        self.alph = alphabet

    buffer: str = ""

    dividers = {}
    operators = {}
    identifics = {}
    service = {}
    constants ={}

    result = ""

    with open('dividers.txt.') as f:
        dividers = f.read().split('\n')
        dividers.append(' ')
        dividers.append('\n')
    f.close()

    with open('operators.txt') as f:
        operators = f.read().split('\n')
    f.close()

    with open('service.txt') as f:
        service = f.read().split('\n')
    f.close()

    with open('identif.txt.') as f:
        identifics = f.read().split('\n')
    f.close()

    with open('constants.txt') as f:
        constants = f.read().split('\n')
    f.close()

    # 0 - start
    # 1 - bukva
    # 2 - cifra
    # 3 - .
    # 4 - /
    # 5 - OdnoliterOper
    # 6 - Razdelitel
    # 7 - <
    # 8 - EOF
    # 9 - ERROR

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @state.deleter
    def state(self):
        del self._state

    def eat(self, c):
        match self.state:
            case State.Start:
                self.stateStart(c)
            case State.Letter:
                self.stateLetter(c)
            case State.Num:
                self.stateNum(c)
            case State.Dot:
                self.stateDot(c)
            case State.Del:
                123
            case State.SingleOp:
                self.stateOper(c)
            case State.Divider:
                self.stateDiv(c)
            case State.StrConst:
                self.stateStrConst(c)
            case State.Sravn:
                123
            case State.EOF:
                self.stateEOF(c)
            case State.Error:
                self.stateError(c)
            case State.LetterAndNum:
                self.stateLetNum(c)
            case State.NumAndDot:
                self.stateNumDot(c)
            case State.LetterAndDot:
                self.stateLetterDot(c)
            case State.End:
                self.stateEnd(c)

    def stateStart(self, c):
        Machine.buffer = ""
        if c.isalpha():
            Machine.buffer += c
            self.state = State.Letter
            return
        if c.isnumeric():
            Machine.buffer += c
            self.state = State.Num
            return
        if c == '.':
            Machine.buffer += c
            self.state = State.Dot
            return
        if Machine.operators.__contains__(c):
            Machine.buffer += c
            self.stateOper(c)
            return
        if Machine.dividers.__contains__(c)|(c=='\n'):
            Machine.buffer += c
            self.stateDiv(c)
            return
        if Machine.dividers.__contains__(c):
            self.state = State.EOF
            return
        else:
            self.state = State.Error
            return

    def stateLetter(self, c):
        if c.isalpha():
            Machine.buffer += c
            self.state = State.Letter
            return
        if c.isnumeric():
            Machine.buffer += c
            self.state = State.LetterAndNum
            return
        if Machine.dividers.__contains__(c) | Machine.operators.__contains__(c):
            self.state = State.Start
            Machine.Semant2()
            self.eat(c)
            return
        else:
            self.state = State.Error
            return

    def stateNum(self, c):
        if c.isnumeric():
            Machine.buffer += c
            self.state = State.Num
            return
        if Machine.dividers.__contains__(c) | Machine.operators.__contains__(c):
            if c == '.':
                Machine.buffer += c
                self.state = State.NumAndDot
                return
            else:
                self.state = State.Start
                Machine.Semant3()
                self.eat(c)
                return
        else:
            self.state = State.Error
            return

    def stateDot(self, c):
        if c.isnumeric():
            Machine.buffer += c
            self.state = State.NumAndDot
            return
        if c.isalpha():
            Machine.buffer += c
            self.state = State.LetterAndDot
            return
        if Machine.dividers.__contains__(c) | Machine.operators.__contains__(c):
            self.state = State.Start
            Machine.Semant9()
            self.eat(c)
            return
        else:
            self.state = State.Error
            return

    def stateStrConst(self, c):
        if c == '"':
            Machine.buffer += c
            Machine.Semant3()
            self.state = State.Start
        else:
            Machine.buffer += c
            self.state = State.StrConst

    def stateOper(self, c):
        Machine.Semant6()
        self.state = State.Start

    def stateDiv(self, c):
        Machine.Semant4()
        if c=='"':
            self.state=State.StrConst
            Machine.buffer=""
        else:
            self.state = State.Start

    def stateEOF(self, c):
        self.state = State.End

    def stateEnd(self, c):
        123

    def stateLetNum(self, c):
        if c.isalpha() | c.isnumeric():
            Machine.buffer += c
            self.state = State.LetterAndNum
            return

        if Machine.dividers.__contains__(c) | Machine.operators.__contains__(c):
            self.state = State.Start
            Machine.Semant1()
            self.eat(c)
            return

        else:
            self.state = State.Error
            return

    def stateNumDot(self, c):
        if c.isnumeric():
            Machine.buffer += c
            self.state = State.NumAndDot
            return
        if Machine.dividers.__contains__(c) | Machine.operators.__contains__(c):
            self.state = State.Start
            Machine.Semant3()
            self.eat(c)
            return

    def stateLetterDot(self, c):
        if c.isalpha():
            Machine.buffer += c
            self.state = State.LetterAndDot
            return
        if Machine.dividers.__contains__(c) | Machine.operators.__contains__(c):
            self.state = State.Start
            Machine.Semant10()
            self.eat(c)
            return

    def stateError(self, c):
        Machine.Semant11()
        self.state = State.End

    @staticmethod
    def Semant1():
        if not (Machine.identifics.__contains__(Machine.buffer)):
            Machine.identifics.append(Machine.buffer)
        Machine.result = Machine.result + "I" + str(Machine.identifics.index(Machine.buffer)) + " "

    @staticmethod
    def Semant2():
        if not (Machine.service.__contains__(Machine.buffer)):
            Machine.Semant1()
        else:
            Machine.result = Machine.result + "W" + str(Machine.service.index(Machine.buffer)) + " "

    @staticmethod
    def Semant3():
        if(Machine.buffer[-1]=='"'):
            Machine.Semant3_str()
        else:
            Machine.Semant3_dig()


    @staticmethod
    def Semant3_str():
        if not (Machine.constants.__contains__(Machine.buffer[:-1])):
            Machine.constants.append(Machine.buffer[:-1])
            print(Machine.constants)
        Machine.result = Machine.result + "C" + str(Machine.constants.index(Machine.buffer[:-1])) + " "
        Machine.result = Machine.result + "R" + str(Machine.dividers.index(Machine.buffer[-1])) + " "

    @staticmethod
    def Semant3_dig():
        if not (Machine.constants.__contains__(Machine.buffer)):
            Machine.constants.append(Machine.buffer)
        Machine.result = Machine.result + "C" + str(Machine.constants.index(Machine.buffer)) + " "

    @staticmethod
    def Semant4():
        Machine.result = Machine.result + "R" + str(Machine.dividers.index(Machine.buffer)) + " "
        if (Machine.buffer == '\n'):
            Machine.result += '\n'

    @staticmethod
    def Semant6():
        Machine.result = Machine.result + "O" + str(Machine.operators.index(Machine.buffer)) + " "

    @staticmethod
    def Semant9():
        Machine.result = Machine.result + "R" + str(Machine.dividers.index(Machine.buffer)) + " "
        if(Machine.buffer=='\n'):
            Machine.result+='\n'

    @staticmethod
    def Semant10():#нужен для распознавания методов
        if Machine.identifics.__contains__(Machine.buffer):
            Machine.result = Machine.result + "I" + str(Machine.dividers.index(Machine.buffer)) + " "

        if Machine.service.__contains__(Machine.buffer):
            Machine.result = Machine.result + "W" + str(Machine.dividers.index(Machine.buffer)) + " "

    @staticmethod
    def Semant11():
        Machine.result+=" ERROR"

    @classmethod
    def start(cls, prgTxt):
        Machine.identifics.clear()
        Machine.constants.clear()
        Machine.result = ""
        return cls(0, 0).run(prgTxt)

    def run(self, prgTxt):
        for c in prgTxt:
            self.eat(c)
        if self.state!=State.Start:
            Machine.Semant11()
        Machine.updateIdentific()
        Machine.updateConstants()
        return Machine.result

    @staticmethod
    def updateIdentific():
        with open('identif.txt', 'w') as f:
            for iden in Machine.identifics:
                f.write(iden+'\n')
        f.close()

    @staticmethod
    def updateConstants():
        with open('constants.txt', 'w') as f:
            for cons in Machine.constants:
                f.write(cons + '\n')
        f.close()


