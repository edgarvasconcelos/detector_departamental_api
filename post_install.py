import subprocess

def download_spacy_model():
    try:
        subprocess.run(["python", "-m", "spacy", "download", "pt_core_news_lg"], check=True)
        print("Modelo pt_core_news_lg instalado com sucesso!")
    except subprocess.CalledProcessError as e:
        print("Erro ao instalar o modelo pt_core_news_lg:", e)

if __name__ == "__main__":
    download_spacy_model()
