import sys
import os
import fileinput

textToSearch = '<script src="jquery-1.10.2.min.js"></script>'

textToReplace = '<!--<script src="jquery-1.10.2.min.js"></script>-->'


def findReplace(directory, find, replace):
    tempFile = open(directory, 'r+')
    for line in open(directory, errors='ignore'): ##in fileinput.input(directory):
        if textToReplace in line:
            print('NOPE. PUBLISH AGAIN')
            input('\n\n Failure! Press Enter to exit...')
            sys.exit()
        if textToSearch in line:
            print('replaced!')
        tempFile.write(line.replace(textToSearch, textToReplace))
    tempFile.close()


findReplace(os.path.abspath(os.getcwd() + "/html/a001_module_00_0_1_getting_around.html"), textToSearch, textToReplace)
findReplace(os.path.abspath(os.getcwd() + "/html/a001_module_00_0_2_seat_time_and_course_completion_.html"), textToSearch, textToReplace)
findReplace(os.path.abspath(os.getcwd() + "/html/a001_module_01_1_1_welcome.html"), textToSearch, textToReplace)
findReplace(os.path.abspath(os.getcwd() + "/html/a001_module_02_2_1_introduction.html"), textToSearch, textToReplace)
findReplace(os.path.abspath(os.getcwd() + "/html/a001_module_03_3_1_additional_requirements.html"), textToSearch, textToReplace)

input('\n\n Success! Press Enter to exit...')

