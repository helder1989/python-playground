
# Construção da classe logicGate

class logicGate:
    def __init__(self, gate_name):
        self.name = gate_name
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGatelogic()
        return self.output


# A BinaryGate vai herdar da logicGate, o logicGate e super class do BinaryGate e
# o BinaryGate é subclasse da logicGate

class BinaryGate(logicGate):
    def __init__(self, gate_name):
        super().__init__(gate_name) # está se refererindo logicGate
        self.pinA = None
        self.pinB = None

# criando funções para que o usuário saiba o que está no pinA e pinB e as funções para o usuário definir
# o que vai ter no pinA e no pinB
    def getPinA(self):
        return self.pinA

    def getPinB(self):
        return self.pinB

    def putPinA(self):
        return int(input("Digite a entrada do Pino A para a porta " + self.getName() + " : ")) # só pode ser número inteiro

    def putPinB(self):
        return int(input("Digite a entrada do Pino B para a porta " + self.getName() + " : ")) # só pode ser número inteiro

class UnaryGate(logicGate):
    def __init__(self, gate_name):
        super().__init__(gate_name) # está se refererindo logicGate
        self.pinA = None

    def getPinA(self):
        if self.pinA == None:
            return self.putPinA()
        else:
            return self.pinA

    def putPinA(self):
        return int(input("Digite a entrada do Pino A para a porta " + self.getName() + " : "))

class ANDGate(BinaryGate): # está herdando do UnaryGate
    def __init__(self, gate_name):
        super().__init__(gate_name)  # está se refererindo BinaryGate

# definindo a lógica do ANDGate
    def performGatelogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

class ORGate(BinaryGate): # está herdando do ANDGate
    def __init__(self, gate_name):
        super().__init__(gate_name)

    def performGatelogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate): # está herdando do UnaryGate
    def __init__(self, gate_name):
        super().__init__(gate_name)

    def performGatelogic(self):
        a = self.getPinA()

        if a == 1:
            return 0
        else:
            return 1


