#!/usr/bin/python3
import sys

ERROR_MESSAGE = "This is a custom error message: 'and that piece of art is useful - Dora Korpar, 2015-10-19'"

def main():
  """Main function for error handling and message output."""
  sys.stderr.write(f"{ERROR_MESSAGE}\n")
  sys.exit(1)

if __name__ == "__main__":
  main()

