
import string

normal_chars = set(string.ascii_letters + '_ ')

def is_normal_string(string: str) -> bool:
    for c in string:
        if c not in normal_chars:
            return False
    return True

def s():
    # Go through the stuff.
    fh = open("final.txt", "r")
    lines = fh.readlines()
    fh.close()
    for line in lines:
        if line[-1] == '\n':
            line = line[:-1]
        line = line[1:-1] # Cut the first and last part of the shit.
        # Now we have the thing
        
        assert "\n" not in line

        if is_normal_string(line):
            continue

        if len(line) == 0 or len(line) == 1:
            continue
        # print("Converting this here: "+str(line))
        as_hex = '\\x'.join([hex(ord(x))[2:] for x in line])
        res = "\"" + as_hex + "\""
        print(res)


if __name__=="__main__":
    s()
    exit()
