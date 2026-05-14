import PyPDF2
import os

mesclar_PDF = PyPDF2.PdfMerger()
lista_aquivos = os.listdir('arquivos')
lista_aquivos.sort()

for arquivo in lista_aquivos:
    if '.pdf' in arquivo:
        caminho_completo = os.path.join('arquivos', arquivo)
        mesclar_PDF.append(caminho_completo)
        
caminho_saida = os.path.join('arquivos', 'Pdf_Pronto.pdf')
mesclar_PDF.write(caminho_saida)
mesclar_PDF.close()
