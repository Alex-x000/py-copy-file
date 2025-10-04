def copy_file(command: str) -> None:  # copy_file("cp file.txt file.txt")
    spl = command.split(" ")
    if (len(spl) != 3 or spl[0] != "cp"
            or spl[1] == spl[2]):
        return
    else:
        try:
            _, file, new_file = spl
            with open(file, "r") as f1, open(new_file, "w") as f2:
                for line in f1.read():
                    f2.write(line)
        except FileNotFoundError:
            pass
