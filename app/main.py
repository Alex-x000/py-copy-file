def copy_file(command: str) -> None:  # copy_file("cp file.txt file.txt")
    parts = command.split(" ")
    if (len(parts) != 3 or parts[0] != "cp"
            or parts[1] == parts[2]):
        return
    else:
        try:
            with open(parts[1], "r") as f1, open(parts[2], "w") as f2:
                for line in f1.readline():
                    f2.write(line)
        except FileNotFoundError:
            pass
