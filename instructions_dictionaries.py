#Está certo essa disposição de ciclos por instrução? Qual é a fonte?
#São quantas instruções ao total do MIPS-I ? Qual a fonte?

mips_cycles = {
    # Instruções de Tipo R (R-Type)
    'ADD': 4,
    'ADDU': 4,
    'SUB': 4,
    'SUBU': 4,
    'MULT': 4,
    'MULTU': 4,
    'DIV': 4,
    'DIVU': 4,
    'AND': 4,
    'OR': 4,
    'XOR': 4,
    'NOR': 4,
    'SLL': 4,
    'SRL': 4,
    'SRA': 4,
    'SLT': 4,
    'SLTU': 4,
    'MFHI': 4,
    'MFLO': 4,
    'MTHI': 4,
    'MTLO': 4,
    # Instruções de Tipo I (I-Type)
    'LW': 5,
    'SW': 5,
    'LB': 5,
    'SB': 5,
    'LH': 5,
    'SH': 5,
    'LUI': 5,
    'ADDI': 5,
    'ADDIU': 5,
    'ANDI': 5,
    'ORI': 5,
    'XORI': 5,
    'SLTI': 5,
    'SLTIU': 5,
    'BEQ': 3,
    'BNE': 3,
    'BLEZ': 3,
    'BGTZ': 3,
    'JALR': 3,
    # Instruções de Tipo J (J-Type)
    'J': 3,
    'JAL': 3,
    # Instruções de Controle
    'NOP': 3,
    # Instruções de Entrada/Saída de Exceção
    'SYSCALL': 5,
    'BREAK': 5,
}

pseudo_mips_cycles = {
    'LI': 4,
    'LA': 4, 
    'MOVE': 4, 
    'BGE': 4, 
    'BLT': 4, 
}


'''
n = 'asc SYSCALL'
n = n.upper()
for key in mips_cycles:
    if key in n:
        print(mips_cycles.get(key))
'''