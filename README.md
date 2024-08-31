- This main_mips.py algorithm basically generates a .pdf document that contains the analysis of all assembly files that are in the MIPS_ASSEMBLY folder and classifies the direct instructions, the pseudo-instructions, the number of cycles for each instruction and counts the average number of cycles per instruction (CPI)

- The book “Computer Organization and Design” by Patterson was used as a reference in order to define the number of cycles of the MIPS-I instructions

- Basically the instructions are organized in this way
  
  -> R instructions = 4 cycles
  
  -> J and control instructions = 3 cycles
  
  -> I instructions = 5 cycles
  
  -> SYSCALL and BREAK instructions = 5 cycles
