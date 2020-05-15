import argparse
import collections
import subprocess
import sys
import time

from get_question import get_question, DEFAULT_LANGUAGE
from solved_questions import solved_questions

PAUSE_SECONDS_DEFAULT = 1.5

def get_all_questions(language, folder, pause):
    all_questions = solved_questions()
    question_count = 1
    all_questions_count = len(all_questions)
    for question_number in all_questions:
        try:
            print(f'Question {question_number} ({question_count}/{all_questions_count})')
            out = get_question(question_number, language, folder)
            print(out)
            time.sleep(pause)
            question_count += 1
        except Exception as e:
            print(f'Error: {e}', file=sys.stderr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download all approved questions and answers.')
    parser.add_argument(
        '--language',
        '-l',
        default=DEFAULT_LANGUAGE,
        help='Language for template.',
    )
    parser.add_argument(
        '--folder',
        '-f',
        help='Target folder.',
    )
    parser.add_argument(
        '--pause',
        '-p',
        type=int,
        default=PAUSE_SECONDS_DEFAULT,
        help='Seconds to wait between requests to avoid throttling.',
    )
    args = parser.parse_args()

    get_all_questions(args.language, args.folder, args.pause)
