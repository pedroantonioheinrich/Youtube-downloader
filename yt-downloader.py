from pytubefix import YouTube
from pytubefix.cli import on_progress


def downloader():
    url = input(f'Adicione a URL aqui: ')
    # Cria a barra de progresso do download
    yt = YouTube(url, on_progress_callback=on_progress)

    print(f'Fazendo download: {yt.title}')

    # Seleciona a melhor resolução de vídeo
    stream = yt.streams.get_highest_resolution()
    stream.download()

downloader()
