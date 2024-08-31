.data
prompt_x: .asciiz "Entre com o valor de X: "
prompt_y: .asciiz "Entre com o valor de Y: "
result_msg: .asciiz "A soma de X e Y é igual a: "

.text
main:
    # Solicita o valor de X
    li $v0, 4
    la $a0, prompt_x
    syscall

    # Lê o valor de X
    li $v0, 5
    syscall
    move $t0, $v0

    # Solicita o valor de Y
    li $v0, 4
    la $a0, prompt_y
    syscall

    # Lê o valor de Y
    li $v0, 5
    syscall
    move $t1, $v0

    # Calcula a soma de X e Y
    add $t2, $t0, $t1

    # Imprime o resultado
    li $v0, 4
    la $a0, result_msg
    syscall

    li $v0, 1
    move $a0, $t2
    syscall

    # Encerra o programa
    li $v0, 10
    syscall