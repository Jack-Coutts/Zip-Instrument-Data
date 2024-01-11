
import os
import zipfile
import shutil
import time


def get_directory():
    while True:
        directory = input('Please enter directory path:')
        if os.path.isdir(directory):
            print("File path accepted.")
            return directory
        else:
            print("The path entered is not a valid directory. Please try again.")

def should_zip_files():
    while True:
        choice = input('Do you want to zip the files in the target directory as well as the folders? (yes/no): ').lower()
        if choice in ['yes', 'no']:
            if choice == 'yes':
                return True
            else:
                return False
        else:
            print("Please enter 'yes' or 'no'.")


def get_zip_targets(directory_name):
    target_directories = [os.path.join(directory_name, dir) for dir in os.listdir(directory_name) if os.path.isdir(os.path.join(directory_name, dir))]
    return target_directories


def zip_the_targets(target_directories, zip_files, directory, delete_original=False):
    print('Directory compression has started.')
    count = 0
    start_time = time.time()

    if zip_files:
        # Zip individual files in the parent directory into their own zip file
        for file in os.listdir(directory):
            count += 1
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                zip_path = f'{file_path}.zip'
                with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    zipf.write(file_path, os.path.basename(file_path))
            elapsed_time = time.time() - start_time
            print(f'File {count} of {len(os.listdir(directory))} zipped. Elapsed time: {elapsed_time:.2f} seconds.')

    for directory in target_directories:
        count += 1
        zip_path = f'{directory}.zip'
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), directory))

        if delete_original:
            shutil.rmtree(directory)
        elapsed_time = time.time() - start_time
        print(f'Directory {count} of {len(target_directories)} zipped. Elapsed time: {elapsed_time:.2f} seconds.')



def main():
    try:
        print('Program Started (Press Ctrl + C to exit)')
        directory = get_directory()
        zip_files = should_zip_files()
        target_directories = get_zip_targets(directory)
        zip_the_targets(target_directories, zip_files, directory)
        print('Zipping complete.')

    except Exception as e:
        print('Zipping Failed:', e)


if __name__ == "__main__":
    main()
