import os
import glob
import string

# Global variables
VOBS = {}


def grep(filename, needle):
    # Simple grep function
    with open(filename, 'r') as f_in:
        matches = ((i, line.find(needle), line) for i, line in enumerate(f_in))
        return [match for match in matches if match[1] != -1]

def main(root_dir, needle):
    # Looking for config_specs, grep lines with load, splitting by \ and put the result to dictionary VOBS
    for filename in glob.iglob(root_dir + '**/**/config_spec', recursive=True):
        matches = grep(filename, needle)
        print(filename)

        if matches:
            for line in matches:
                load_line = list(line[2].split("\\"))
                VOBS[load_line[1]] = 1
            print(VOBS.keys())
            #return 1
        else:
            #return -1
            pass

if __name__=='__main__':
    import sys
    import string

    root_dir = "v:/views"
    needle = "load "
    main(root_dir, needle)
    print(VOBS.keys())