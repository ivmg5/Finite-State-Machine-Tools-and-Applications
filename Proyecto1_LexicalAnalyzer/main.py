from sm import stateMachine

# void lexer(string filepath)
def lexer(filepath: str) -> None:
	# open the file and split the lines
  with open(filepath, "r") as f:
    contents = f.read()
    lines = contents.split("\n")

	# create the automaton (from definition in sm.py)
  automaton = stateMachine()
  
	# This line creates an automaton.png graph
	# dynamically from the automaton definition.
	# this can get a bit slow on replit, so if
	# you don't want the graph, comment the line
  # automaton.graph()

  print("Token\tType")
  for line in lines:
		# very simple pre-processing, add a space at the end
		# to make sure the last character is a space
    line += " "
    automaton.match(line)


lexer("input.txt")
