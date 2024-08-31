.data
	vetor: .space 32 # Vetor de 8 elementos de 4 bytes cada (8 x 4 = 32)
	m1: .asciiz "Entrada de dados:\n"
	put: .asciiz "A["
	put2: .asciiz "]: "
	m2: .asciiz "\nElementos do vetor:\n"
	n: .asciiz "\n"

.text

main:
    # Inicializa o vetor
    li $t0, 0           # |Indice do vetor
    la $t1, vetor       # Endereço base do vetor
    
    # Exibe mensagem de leitura
    li $v0, 4
    la $a0, m1
    syscall

loop:
    
    # Carrega a string "A["
    li $v0, 4
    la $a0, put
    syscall

    # Carrega o valor do índice para exibir na string
    move $a0, $t0
    li $v0, 1
    syscall

    # "]: "
    li $v0, 4
    la $a0, put2
    syscall

    # Solicita input do usuário
    li $v0, 5
    syscall
    move $t2, $v0

    # Calcula o deslocamento correto multiplicando o índice pelo tamanho do elemento (4 bytes)
    sll $t3, $t0, 2      # $t3 = $t0 * 4
    add $t4, $t1, $t3    # $t4 = $t1 + $t3 (endereço do elemento no vetor)
    sw $t2, 0($t4)       # Armazena o valor no vetor

    
    addi $t0, $t0, 1
    
    #  $t0 > 8? Se sim entra no laço
    bne $t0, 8, loop
    
    li $v0, 4
    la $a0, m2
    syscall
    
    li $t0, 0 #Reseta o índice do vetor para exibir os elementos corretamente


loop2:
    # $t0 = 8? se sim entra no laço
    beq $t0, 8, exit
    
    #Carrega a string "A["
    li $v0, 4
    la $a0, put
    syscall

    #Carrega o valor do índice para exibir na string
    move $a0, $t0
    li $v0, 1
    syscall

    # "]: "
    li $v0, 4
    la $a0, put2
    syscall

    #Carrega valor do vetor para exibir o int
    sll $t3, $t0, 2      #$t3 = $t0 * 4
    add $t4, $t1, $t3    #$t4 = $t1 + $t3 (endereço do elemento no vetor)
    lw $a0, 0($t4)       #Carrega o valor do vetor para imprimir
    li $v0, 1
    syscall

    #Quebra a linha
    li $v0, 4
    la $a0, n
    syscall

    #Avança para o próximo elemento do vetor
    addi $t0, $t0, 1

    #Loop para imprimir o próximo elemento
    j loop2
    
exit:
    #Encerra o programa
    li $v0, 10
    syscall
