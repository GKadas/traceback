#traceback.py
import re

workfile = "Threads.txt"

begin = re.compile(r'\d+:\s0x[0-9a-z]+\s\<')


def find_function(data, startlist, endlist):

    matches = []
    loop_data = []
    i = 0
    j = 0

    stripped_data = [line.strip() for line in data]

    for new in stripped_data:
        if new != '':
            loop_data.append(new)


    for datum in loop_data:
        if i < len(startlist):
            if startlist[i] in datum:
                if endlist[j] in datum:
                    # Find and validate before-part.
                    pos_a = datum.find(startlist[i])
                    # Find and validate after part.
                    pos_b = datum.find(endlist[j])
                    # Return middle part.
                    adjusted_pos_a = pos_a + len(startlist[i])
                    matches.append(datum[adjusted_pos_a:pos_b])
                    i += 1
                    j += 1

    matches = '\n'.join(matches)
    return matches


def trim (data, end):
    startlist = []
    endlist = []

    for line in data:
        if begin.search(line):
            startlist.append(begin.search(line).group())
            if end.search(line):
                endlist.append(end.search(line).group())


    return startlist, endlist









# def main():
#     if __name__ == '__main__':
#         start, end = trim()
#         find_function(workfile, start, end)
#
# main()
