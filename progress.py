def get_values():
    progress = open('progress.txt', 'r+')
    lines = progress.readlines()
    levels_passed = int
    names_passed_levels = list
    for line in lines:
        index = line.find(':')
        value = line[index + 1:].strip()
        if line.startswith('LEVELS_PASSED'):
            levels_passed = value
        elif line.startswith('NAMES_PASSED_LEVELS'):
            if value == '[]':
                names_passed_levels = []
            else:
                names_passed_levels = value
    return int(levels_passed), names_passed_levels


def change_values(levels_passed, append_passed_levels):
    progress = open('progress.txt', 'r+')
    lines = progress.readlines()
    from os import remove, rename
    new_progress = open('new_progress.txt', 'w')
    old_levels_passed, old_names_passed_levels = get_values()

    for line in lines:
        if line.startswith('LEVELS_PASSED') and levels_passed != 'none':
            line = line.replace(str(old_levels_passed), str(levels_passed))
            print(line)
        elif line.startswith('NAMES_PASSED_LEVELS') and append_passed_levels != ['none']:
            index = line.find(':')
            value = line[index + 2]
            if value != ']':
                line = line.replace(']', f', {append_passed_levels}]')
            else:
                line = line.replace(']', f'{append_passed_levels}]')
            print(line)
        new_progress.write(line)

    remove('progress.txt')
    rename('new_progress.txt', 'progress.txt')
