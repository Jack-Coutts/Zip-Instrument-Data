
import os
import zipfile
import shutil
import time


def get_directory():
    directory = input('Please enter directory path E.g. data/home/instruments/raw_data:')
    return directory


def get_zip_targets(directory_name):
    target_directories = []
    for root, dirs, files in os.walk(directory_name, topdown=False):
        for dir in dirs:
            target_directories.append(os.path.join(root, dir))
    return target_directories


def zip_the_targets(target_directories):
    count = 0
    start_time = time.time()  # Store the start time
    for directory in target_directories:
        count += 1
        zipf = zipfile.ZipFile(f'{directory}.zip', 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(directory):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file),
                                           os.path.join(directory, '..')))
        zipf.close()
        shutil.rmtree(directory)  # Delete original directory
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        print(f'Directory {count} of {len(target_directories)} zipped. Elapsed time: {elapsed_time:.2f} seconds.')


def main():
    try:
        directory = get_directory()
        target_directories = get_zip_targets(directory)
        zip_the_targets(target_directories)
        print('Zipping complete.')

    except Exception as e:
        print('Zipping Failed:', e)


if __name__ == "__main__":
    main()
