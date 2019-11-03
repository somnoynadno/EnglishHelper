#!/usr/bin/env python3

from argparse import ArgumentParser
from googletrans import Translator
from pathlib import Path
import datetime as dt
import os

HISTORY_PATH = str(Path.home()) + "/" + ".english_helper_history.txt"
EXIT_WORDS = ["q!", "exit", "quit"]


def add_arguments(parser):
	parser.add_argument("--history", action="store_true",
						dest="history", default=False,
						help="show history")


def show_history():
	print("Translator history:")
	print()
	text = open(HISTORY_PATH, 'r').read()
	print(text, end='')


def main():
	parser = ArgumentParser(description='Simple en-ru translate helper')
	add_arguments(parser)
	args = parser.parse_args()

	if args.history:
		show_history()
		return

	handler = open(HISTORY_PATH, 'a')

	translator = Translator()

	os.system('clear')
	time = dt.datetime.now()

	handler.write("# SESSION FROM " + time.strftime('%d.%m.%Y %H:%M') + '\n')

	print("Session started " + time.strftime('%d.%m.%Y at %H:%M'))
	print()
	print("Just write the words you want to translate")
	print("Or type 'q!' to exit")
	print()

	exit = False

	while not exit:
		word = input().strip()
		if word in EXIT_WORDS:
			exit = True 
			continue

		translation = translator.translate(word, src='en', dest='ru')
		print(translation.text)
		print()

		handler.write("     " + word.ljust(28, ' ') + "|     " + translation.text + '\n')

	handler.write('\n')
	handler.close()
	print("See you next time!")


if __name__ == "__main__":
	main()

