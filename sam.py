import sys
from subprocess import Popen
import wave
import re

def sam(line):
    sum_cla = 0             

    lines_parsed = []
    
    #Get rid of bad characters
    line = re.sub('[\n,?\'!*\"]', '', line).replace('[', '').replace(']', '')

    #Shorten lines to 90 length
    while len(line) > 90:
        end_pos = -1
        for i in range(min(len(line), 90), 0, -1):
            if len(line) >= i + 2 and line[i] == ' ' and end_pos == -1:
                end_pos = i
                lines_parsed.append(line[0:i])
                line = line[i+1:]
        if end_pos == -1:
            lines_parsed.append(line[0:90])
            line = line[90:]
            
    lines_parsed.append(line)
        
    #Open the output file
    output_file = open('SAM.bat', 'w')

    #Keep track of line number for wav file naming
    line_number = 0
    
    #Disable messages
    output_file.write('@echo off\n')

    #Enter the correct directory to make files in
    output_file.write('cd .\\SAM\n')

    #Set beginning of output line, contains directory to save wav file in
    command = 'sam -wav ..\\output\\'

    in_wav_files = []
    wav_file_names = []
    for line in lines_parsed:
        if len(line) >= 1:
            #Write a line
            wav_file_name = str(line_number) + line.replace(' ', '')[0:min(len(line), 30)] + '.wav'
            wav_file_names.append(wav_file_name)
            in_wav_files.append(wav_file_name)
            output_file.write(command + wav_file_name +' \"' + line + '\"\n')
            line_number += 1

    #Re-enable messages
    output_file.write('@echo on\n')

    #Close output file
    output_file.close()

    #Try to run the batch file, output message regarding success or failure
    try:
        p = Popen("SAM.bat", cwd=r".\\")
        stdout, stderr = p.communicate()
    except:
        print("Opening batch file failed. Try to open it yourself?")

    return wav_file_names
