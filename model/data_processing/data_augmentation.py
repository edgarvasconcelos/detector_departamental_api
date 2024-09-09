import pandas as pd
from sklearn.utils import resample
from translate import Translator
from .summarization import resumir
from utils.translation import translate_round_trip

def aumentar_departamentos(df, target_count):
    """
    Augments the dataset to ensure each department has at least `target_count` samples.

    Args:
        df (pd.DataFrame): DataFrame with the dataset.
        target_count (int): Target number of samples per department.

    Returns:
        pd.DataFrame: Augmented DataFrame.
    """
    array_de_copias = []
    department_counts = df['departamento'].value_counts()

    for departamento, count in department_counts.items():
        df_depto = df[df['departamento'] == departamento]

        if count < target_count:
            while len(df_depto) < target_count:
                for _, row in df_depto.iterrows():
                    if len(df_depto) >= target_count:
                        break

                    copia = row.copy()
                    traducao = translate_round_trip(copia['resumo'])
                    copia['resumo'] = resumir(traducao)
                    array_de_copias.append(copia)
                    df_depto = pd.concat([df_depto, pd.DataFrame([copia])], ignore_index=True)

    return pd.concat([df, pd.DataFrame(array_de_copias)], ignore_index=True)
