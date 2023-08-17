
import os
import zipfile
import shutil
import time


def get_directory():
    while True:
        directory = input('Please enter directory path:')
        if os.path.isdir(directory):
            print("File path accepted. Directory compression has started.")
            return directory
        else:
            print("The path entered is not a valid directory. Please try again.")


def get_zip_targets(directory_name):
    target_directories = [os.path.join(directory_name, dir) for dir in os.listdir(directory_name) if os.path.isdir(os.path.join(directory_name, dir))]
    return target_directories


def zip_the_targets(target_directories, delete_original=False):
    count = 0
    start_time = time.time()  # Store the start time
    for directory in target_directories:
        count += 1
        zip_path = f'{directory}.zip'
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), directory))

        if delete_original:
            shutil.rmtree(directory)  # Delete original directory only if delete_original is True
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        print(f'Directory {count} of {len(target_directories)} zipped. Elapsed time: {elapsed_time:.2f} seconds.')


def main():
    try:
        print('Program Started (Press Ctrl + C to exit)')
        directory = get_directory()
        target_directories = get_zip_targets(directory)
        zip_the_targets(target_directories, False)
        print('Zipping complete.')

    except Exception as e:
        print('Zipping Failed:', e)


if __name__ == "__main__":
    main()
