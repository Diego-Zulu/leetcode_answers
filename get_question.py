import argparse
import subprocess

DEFAULT_LANGUAGE = 'python3'

def get_question(question_number, language, folder):
    folder = folder or language
    print(f'Starting subprocess for question {question_number}')
    return subprocess.Popen(
        [
			'leetcode',
			'submission',
			question_number,
			'-x',
			'-l',
			language,
			'-o',
			folder,
		],
		stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT,
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download target question and approved answer.')
    parser.add_argument(
        'question_number',
        help='Question to download.'
    )
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
    args = parser.parse_args()

    out = get_question(args.question_number, args.language, args.folder)

    stdout,stderr = out.communicate()
    if stderr:
        print(stderr, file=sys.stderr)
    else:
        print(stdout)
