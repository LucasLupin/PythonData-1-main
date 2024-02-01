#!/usr/bin/env python3

def file_extensions(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        no_extension = []
        extensions = {}

        for line in file:
            line = line.strip()
            if '.' in line:
                ext = line.split('.')[-1]
                extensions.setdefault(ext, []).append(line)
            else:
                no_extension.append(line)

        return no_extension, extensions


def main():
    no_extension, extensions = file_extensions(r"C:\Users\lukr\Desktop\H3\Python\PythonData-1-main\øvelser\e27_file_extensions\src\filenames.txt")

    print(f"{len(no_extension)} files with no extension")
    for ext in sorted(extensions):
        print(f"{ext} {len(extensions[ext])}")

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
