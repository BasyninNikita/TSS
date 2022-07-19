import sys
import os

if __name__ == "__main__":
    langs = sys.argv[1].split(',')
    #langs = 'python,golang,java'.split(',')
    for lang in langs:
        if lang.casefold() == 'python':
            Out = os.popen('pipreqs --print').read()
            print('%s deps: \n' %lang, Out)
        elif lang.casefold() == 'java':
            #os.popen('gradle init')
            #Out = os.popen('gradle dependencies').read()
            print("Java deps in process of development")
        elif lang.casefold() == 'nodejs' or lang.casefold() == 'javascript':
            Out = os.popen('npm list').read()
            print('%s deps: \n' %lang, Out)
        elif lang.casefold() == 'go':
            Out = os.popen('go list -json | jq ".Deps"').read() 
            print('%s deps: \n' %lang, Out)
        else:
            print('%s lang is unknown for me' %lang)
