import argparse
import re
import subprocess

REGEX = r"\[\s*(\d+)\s*\]"

def solved_question():
    print('Getting list of solved questions.')
    out = subprocess.Popen(
        ['leetcode', 'list', '-q', 'd'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    stdout,stderr = out.communicate()
    if stderr:
        print(stderr, file=sys.stderr)
        return[]

    problems = []
    for line in stdout.decode().split('\n'):
        matches = re.search(REGEX, line)
        if not matches:
            continue
        problems.append(matches.group(1))
    return problems

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get list of solved questions.')

    question_numbers = solved_question()

    print(', '.join(question_numbers))
