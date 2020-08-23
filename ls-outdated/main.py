#! /usr/bin/env python

import subprocess

commands = [
  ['npm', '-g', 'outdate'],
  ['brew', 'outdated'],
  ['pip3', 'list', '-o'],
]


def print_result(result):
  up_to_date = 'up to date' if result.returncode == 0 and not len(result.stdout) else 'outdated'
  print(f'> {result.args[0]}: {up_to_date}')
  
  if result.returncode == 0:
    print(result.stdout)
  else:
    print(result.stderr)


def run_commands():
  for command in commands:
    result = subprocess.run(command, text=True, capture_output=True)
    print_result(result)


if __name__ == '__main__':
  run_commands()