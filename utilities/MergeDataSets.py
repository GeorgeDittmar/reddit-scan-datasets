import argparse
import glob


def read_file(file_path):
    with open(file_path, "r") as f:
        return f.readlines()


def merge(paths):
    return sum(map(read_file, paths), [])


def read_directory(dir_path):
    return glob.glob(dir_path)

def main():
    parser = argparse.ArgumentParser(description='Utility to merge multiple line by line text files together to make'
                                                 ' a new single dataset.')
    parser.add_argument('--directory', help="directory where files to merge exist.", required=True)
    parser.add_argument('--output', help="output file path", required=True)
    args = parser.parse_args()

    if args.directory and args.output:
        file_paths = read_directory(args.directory)
        merged_files = merge(file_paths)

        with open(args.output, "w") as file_handler:
            file_handler.writelines("%s\n" % line.strip() for line in merged_files)

if __name__ == '__main__':
    main()
