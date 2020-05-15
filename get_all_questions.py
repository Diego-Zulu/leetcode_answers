import argparse
import collections
import subprocess
import time

from .get_question import get_question, DEFAULT_LANGUAGE
from .solved_questions import solved_questions

PAUSE_SECONDS_DEFAULT = 2

def get_all_questions(language, folder, pause):
    all_questions = solved_questions()
    out_dir = collections.OrderedDict()
    for question_number in all_questions:
        try:
            sub[i] = get_question(question_number, language, folder)
            time.sleep(pause)
        except Exception as e:
            print("Error: {e}", file=sys.stderr)
    return out_dir

if __name__ == "__main__":
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

    out_dir = get_all_questions(args.language, args.folder, args.pause)

    for out in out_dir.values():
        stdout,stderr = out.communicate()
        if stderr:
            print(stderr, file=sys.stderr)
        else:
            print(stdout)
