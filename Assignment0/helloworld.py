import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="Insert your name for a personalized message!")
parser.add_argument("Interest", help="list one of your interests!")
args = parser.parse_args()

message = 'hello ' + args.name
# This is a comment 
print(message)