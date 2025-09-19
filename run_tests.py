import os
from collections import defaultdict
from pathlib import Path


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_directory_name_from_path(path):
    return path[2:]


def get_list_of_python_files(directory):
    directory = Path(directory)
    return ["\".\\" + str(file) + "\"" for file in directory.rglob('*.py') if file.is_file()]


def get_file_name_from_file(file):
    return file.split("\\")[2][:-1]


def print_test_succeeded(file_name):
    print(bcolors.OKGREEN, '-', file_name, "succeeded", bcolors.ENDC)


def print_test_failed(file_name):
    print(bcolors.FAIL, bcolors.BOLD, "-", bcolors.UNDERLINE, file_name, "has failed", bcolors.ENDC)


error_files_by_directory = defaultdict(list)

def run_tests(directory):
    python_files = get_list_of_python_files(directory)
    print(bcolors.HEADER)
    print("========================================")
    print("Running tests for", get_directory_name_from_path(directory), "files")
    print("========================================" + bcolors.ENDC)

    for file in python_files:
        file_name = get_file_name_from_file(file)
        
        if os.system('py ' + file):
            error_files_by_directory[directory].append(file)
            print_test_failed(file_name)
            print()
        else:
            print_test_succeeded(file_name)


def display_errors():
    if error_files_by_directory:
        for directory in error_files_by_directory:
            print(bcolors.FAIL)
            print("=================================")
            print("Failed", get_directory_name_from_path(directory), "tests")
            print("=================================" + bcolors.ENDC)

            for file in error_files_by_directory[directory]:
                file_name = get_file_name_from_file(file)

                print('--------------------------------------------------------------------------------------------------------')
                os.system('py ' + file)
                print_test_failed(file_name)
                print()


folders = list(filter(lambda folder: len(folder.split("\\")) == 2 and folder[2].isalpha() and folder[2].isupper(), ([x[0] for x in os.walk('.')])))
folders = list(map(lambda folder: "./" + folder[2:], folders))
for folder in folders:
    run_tests(folder)

if error_files_by_directory:
    display_errors()
else:
    print(bcolors.OKGREEN, bcolors.BOLD)
    print()
    print("*" * 38)
    print("*", " " * 34, "*")
    print("*", " " * 7, "All tests succeded." + bcolors.ENDC, bcolors.OKGREEN, " " * 5, "*")
    print("*", " " * 34, "*")
    print("*" * 38, bcolors.ENDC, "\n")