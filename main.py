from pytube import YouTube
from pytube.cli import on_progress  # importa barra de progresso


def salvar_video(link_do_video):
    print('Iniciando download...')

    try:
        # captura o caminho do vídeo do youtube e exibe a barra de progresso
        yt = YouTube(link_do_video, on_progress_callback=on_progress)
        # pega a maior resolução possível
        video_stream = yt.streams.get_highest_resolution()

        video_stream.download()  # baixa o vídeo no diretório do projeto

        return '\nDownload completo!'
    except:
        return 'Não foi possível baixar o vídeo.'


if __name__ == "__main__":
    while True:
        link_do_video = input(
            'Informe o link do YouTube para baixar ou aperte Enter para encerrar o progarma: ')

        if link_do_video != '':
            print(salvar_video(link_do_video))
            continue
        else:
            print('Programa encerrado!')
            break
