import argparse
import subprocess

DEFAULT_LANGUAGE = 'python3'

def get_question(question_number, language, folder):
    folder = folder or language
    out = subprocess.check_output(
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
    )
    return out.decode()

if __name__ == '__main__':
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

    print(
        get_question(args.question_number, args.language, args.folder)
    )
