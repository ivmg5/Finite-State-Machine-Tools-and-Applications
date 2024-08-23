from types import NoneType
from typing import Callable, Union

# Defines a state (Node) and it's transitions
class State():
	# Constructor for the State class.
		# name: the name of the state - what is shown in generated graphs
		# value: the value of the state - for storing aditional information related to the state
		# isFinal: wether or not the state is a final state
  def __init__(self, name: str, value: str, isFinal: bool):
    self.name = name
    self.isFinal = isFinal
    self.value = value
		# use two hashmaps for storing
		# transition -> state maps
		# transition -> onNavigate maps
    self.transitions: dict[str, 'State'] = {} 
    self.onNavigates: dict[str, Union[Callable[['State', str], NoneType], NoneType]] = {}

	# Adds a transition to the given state
		# symbol: the char that triggers the transition
		# state: the state that is triggered by the transition
		# onNavigate: a function that is called when the transition is triggered
  def addTransition(self,
                    symbol: str,
                    state: 'State',
                    onNavigate: Union[Callable[['State', str], NoneType], NoneType] = None):
    self.transitions[symbol] = state
    self.onNavigates[symbol] = onNavigate

	# returns the next state given a symbol (or None if it does not exist)
  def getNextState(self, symbol: str):
    return self.transitions.get(symbol)
