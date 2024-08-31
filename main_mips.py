#Acessar os dicionarios e fazer as devidas importações
import os
from fpdf import FPDF

#Se não fizer isso no terminal não vai funcionar -> pip install fpdf2

from instructions_dictionaries import mips_cycles as mips
from instructions_dictionaries import pseudo_mips_cycles as pseudo_mips

# Obter o diretório do script atual
diretorio_script = os.path.dirname(__file__)

# Caminho para a pasta onde estão os arquivos
caminho_pasta = os.path.join(diretorio_script, 'MIPS_ASSEMBLY')

# Listar todos os arquivos na pasta
arquivos = [f for f in os.listdir(caminho_pasta) if os.path.isfile(os.path.join(caminho_pasta, f))]

texto = '1. Arquitetura MIPS-I\n'
# Verificar se há arquivos na pasta
if arquivos:
    contador = 0
    for nome_arquivo in arquivos:
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
        
        # Abrir e ler o conteúdo do arquivo
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            
            # Processar as linhas
            contador += 1
            texto += "1." + str(contador) + ". Arquivo " + nome_arquivo + "\n"

            total_cycles_direct = 0
            total_instructions_direct = 0

            texto += "1." + str(contador) + ".1. Instruções diretas do MIPS-I\n"
            texto += "1." + str(contador) + ".1.1. Valores\n"
            for i, linha in enumerate(linhas):
                    linha = linha.upper()
                    for key in mips:
                        if key in linha: 
                            #print("Instrução " + str(total_instructions) + ": " + key)
                            total_cycles_direct += mips.get(key)
                            total_instructions_direct += 1
                            texto += "      Item " + str(total_instructions_direct) + ": " + key + " -> " + str(mips.get(key)) + " ciclos\n"

            total_cycles_pseudo = 0
            total_instructions_pseudo = 0

            texto += "1." + str(contador) + ".1.2. Total de intruções diretas: " + str(total_instructions_direct) + "\n"
            texto += "1." + str(contador) + ".1.3. Total de ciclos de instruções diretas: " + str(total_cycles_direct) + "\n"

            texto += "1." + str(contador) + ".2. Pseudo-instruções do MIPS-I\n"
            texto += "1." + str(contador) + ".2.1. Valores\n"
            for i, linha in enumerate(linhas):
                    linha = linha.upper()
                    for key in pseudo_mips:
                        if key in linha: 
                            #print("Instrução " + str(total_instructions) + ": " + key)
                            total_cycles_pseudo += pseudo_mips.get(key)
                            total_instructions_pseudo += 1
                            texto += "      Item " + str(total_instructions_pseudo) + ": " + key + " -> " + str(pseudo_mips.get(key)) + " ciclos\n"

            cpi = (total_cycles_direct + total_cycles_pseudo) / (total_instructions_direct + total_instructions_pseudo)
            texto += "1." + str(contador) + ".2.2. Total de pseudo-instruções: " + str(total_instructions_pseudo) + "\n"
            texto += "1." + str(contador) + ".2.3. Total de ciclos das pseudo-instruções: " + str(total_cycles_pseudo) + "\n"
            texto += "1." + str(contador) + ".3. Ciclos por instrução(CPI) médio geral: " + str(cpi) + "\n"

else:
    print(f"Nenhum arquivo encontrado na pasta {caminho_pasta}.")

texto += '\n\nObservações:\n'

texto += '- O relatório considera todas as instruções, mesmo estando como observações\n'
texto += '- Códigos que tenham loop não serão contabilizados novamente'


# Cria uma classe que herda de FPDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Relatório de análise e classificação de arquivos assembly', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

# Instancia a classe PDF
pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)

# Adiciona texto ao PDF
pdf.multi_cell(0, 10, texto)


# Salva o PDF em um arquivo
caminho_arquivo = 'relatorio_M1.pdf'
pdf.output(caminho_arquivo)

print(f"PDF salvo como {caminho_arquivo}")