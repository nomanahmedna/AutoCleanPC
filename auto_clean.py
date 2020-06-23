import os


def createfolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")


if __name__ == '__main__':

    files = os.listdir()
    files.remove('auto_clean.py')

    print(files)
    createfolder('software')
    createfolder('pdf')
    createfolder('images')
    createfolder('videos')
    createfolder('songs')
    createfolder('word')
    createfolder('excel')
    createfolder('presentations')
    createfolder('zip_rar')
    createfolder('text')
    createfolder('torrents')
    createfolder('others')

    # for software files to be transferred in software folder
    software_ext = ['.exe', '.msi']

    software = [file for file in files if os.path.splitext(file)[1].lower() in software_ext]

    # for software files to be transferred in software folder
    pdf_ext = ['.pdf']

    pdf = [file for file in files if os.path.splitext(file)[1].lower() in pdf_ext]

    # for image files to be transferred in image folder
    img_ext = ['.jpg', '.jpeg', '.gif', '.bmp', '.png', '.tif']

    images = [file for file in files if os.path.splitext(file)[1].lower() in img_ext]

    # for videos files to be transferred in videos folder
    videos_ext = ['.mp4', '.avi', '.mkv', '.flv', '.wmv', '.webm', '.mpg', '.mov']

    videos = [file for file in files if os.path.splitext(file)[1].lower() in videos_ext]

    # for songs files to be transferred in songs folder
    songs_ext = ['.mp3', '.wma']

    songs = [file for file in files if os.path.splitext(file)[1].lower() in songs_ext]

    # for word files to be transferred in word folder
    word_ext = ['.doc', '.docx']

    word = [file for file in files if os.path.splitext(file)[1].lower() in word_ext]

    # for excel files to be transferred in excel folder
    excel_ext = ['.xls', '.xlsx']

    excel = [file for file in files if os.path.splitext(file)[1].lower() in excel_ext]

    # for power point files to be transferred in power point folder
    ppt_ext = ['.ppt', '.pptx']

    presentations = [file for file in files if os.path.splitext(file)[1].lower() in ppt_ext]

    # for zip and rar files to be transferred in zip rar folder
    zip_ext = ['.zip', '.rar']

    zip_rar = [file for file in files if os.path.splitext(file)[1].lower() in zip_ext]

    # for zip and rar files to be transferred in zip rar folder
    txt_ext = ['.txt']

    text = [file for file in files if os.path.splitext(file)[1].lower() in txt_ext]

    # for torrents and rar files to be transferred in zip rar folder
    torrent_ext = ['.torrent']

    torrents = [file for file in files if os.path.splitext(file)[1].lower() in torrent_ext]

    others = []

    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in software_ext) and (ext not in pdf_ext) and (ext not in pdf_ext) and (ext not in img_ext) and (
                ext not in videos_ext) and (ext not in songs_ext) and (ext not in word_ext) and (
                ext not in excel_ext) and (
                ext not in ppt_ext) and (ext not in zip_ext) and (ext not in txt_ext) and (
                ext not in torrent_ext) and os.path.isfile(file):
            others.append(file)

    move("software", software)
    move("pdf", pdf)
    move("images", images)
    move("videos", videos)
    move("songs", songs)
    move("word", word)
    move("excel", excel)
    move("presentations", presentations)
    move("zip_rar", zip_rar)
    move("text", text)
    move("torrents", torrents)
    move("others", others)
