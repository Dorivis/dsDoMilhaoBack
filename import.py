import os
import django
import pandas as pd

# Configuração do ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from questions.models import Question

def import_from_excel(file_path):
    # Carrega a planilha Excel
    df = pd.read_excel(file_path)
    
    # Verifica colunas obrigatórias
    required_columns = ['Pergunta', 'A', 'B', 'C', 'D', 'Resposta Correta', 'Nivel']
    if not all(col in df.columns for col in required_columns):
        print(df.columns)
        raise ValueError("A planilha deve conter as colunas: Pergunta, A, B, C, D, Resposta Correta, Nivel")
    
    # Contadores para relatório
    total = 0
    created = 0
    errors = 0
    
    for index, row in df.iterrows():
        total += 1
        try:
            Question.objects.create(
                text=row['Pergunta'],
                option_a=row['A'],
                option_b=row['B'],
                option_c=row['C'],
                option_d=row['D'],
                correct_option=row['Resposta Correta'].upper(),  # Garante maiúscula
                level=row['Nivel'],
                wrong_options=get_wrong_options(row)  # Função auxiliar
            )
            created += 1
        except Exception as e:
            errors += 1
            print(f"Erro na linha {index + 2}: {str(e)}")
    
    print(f"\nResumo:")
    print(f"Total de registros: {total}")
    print(f"Criados com sucesso: {created}")
    print(f"Erros: {errors}")

def get_wrong_options(row):
    options = ['A', 'B', 'C', 'D']
    correct = row['Resposta Correta'].upper()
    return ','.join([opt for opt in options if opt != correct])

if __name__ == "__main__":
    # Caminho para sua planilha Excel
    excel_file = "perguntas.xlsx"  # Altere para o caminho do seu arquivo
    
    print(f"Importando perguntas de {excel_file}...")
    import_from_excel(excel_file)