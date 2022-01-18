import pathlib


def rename_photos():
    path = pathlib.Path('.') / 'NoiseFree_not_resized'
    for folder in path.iterdir():
        if folder.is_dir():
            count = 1
            for file in folder.iterdir():
                if file.is_file():
                    new_file = folder.name + '_' + str(count) + file.suffix
                    file.rename(path / folder.name / new_file)
                    count += 1


# if __name__ == '__main__':
#     rename_photos()
