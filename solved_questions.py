import argparse
import re
import subprocess

REGEX = r'\[\s*(\d+)\s*\]'

def solved_questions():
    print('Getting list of solved questions.')
    out = subprocess.check_output(
        ['leetcode', 'list', '-q', 'd'],
    )
    problems = []
    for line in out.decode().split('\n'):
        matches = re.search(REGEX, line)
        if not matches:
            continue
        problems.append(matches.group(1))
    return problems

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get list of solved questions.')

    question_numbers = solved_questions()

    print(', '.join(question_numbers))
