# działania z plikami
# context manager
# with - context manager w pythonie
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:
    fh.write("Powitanie\n")  # \n - nowa linia
    fh.write("Kolejne\n")  # \n - nowa linia
    fh.write("Kolejne\n")  # \n - nowa linia

with open('test.log', "a", encoding='utf-8') as f:
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dośdane\n")
    f.write("Dośąźćdane\n")

with open('test.log', 'r', encoding='utf-8') as file:
    lines = file.read()

print(lines)
