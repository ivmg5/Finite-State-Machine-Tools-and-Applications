import re
import html

operators = re.compile(r'\=\=|\!\=|\<\=|\>\=|\=|\+\=|\-\=|\<|\>|\+|\-|\*\*|\/\/|\*|\/|\%')
literals = re.compile(r'(\d+\.\d+|\d+|True|False|None|".*?"|\'.*?\')')
comments = re.compile(r'(#.*)')
keywords = re.compile(r'(def|if|else|elif|return|class|for|while|break|continue|and|or|not)')
identifiers = re.compile(r'([a-zA-Z_]\w*)')
data_structs = re.compile(r'(\[.*?\]|\(.*?,.*?\)|\{.*?\})')

def get_first_match(start: int, code: str):
    preceding_char = code[max(0, start - len("</span> ")):][0]
    code = code[start:]
    oper_match = operators.match(code)
    lit_match = literals.match(code)
    coment_match = comments.match(code)
    key_match = keywords.match(code)
    iden_match = identifiers.match(code)
    data_match = data_structs.match(code)
    matches = [oper_match, lit_match, coment_match, key_match, iden_match, data_match]
    matches = [m for m in matches if m is not None]
    
    if len (matches)==0:
      return None, None
    
    sorted_matches = sorted(matches, key=lambda x: x.start())
    first_match = sorted_matches[0]
  
    if first_match == oper_match:
      return first_match, "operator"
    if first_match == lit_match:
      return first_match, "literal"
    if first_match == coment_match:
      return first_match, "comment"
    if first_match == key_match:
      next_char = code[first_match.end()]
      if next_char.isalnum() or next_char == '_':
        return None, None
      return first_match, "keyword"
    if first_match == iden_match:
      return first_match, "identifier"
    if first_match == data_match:
      if preceding_char.isalnum():
        return None, None
      return first_match, "data_struct"
    
    return None, None

  
def main():
    with open('template.html', 'r') as html:
      template = html.read()
    
    with open('input.txt', 'r') as file:
      code = file.read()
    i = 0
    while i < len(code):
      first_match, type_match = get_first_match(i, code)
      if first_match is None:
        i += 1
        continue
      code_before_match = code[:first_match.start() + i]
      code_after_match = code[first_match.end() + i:]
      new_middle = f'<span class="{type_match}">{first_match.group()}</span>'
      code = code_before_match + new_middle + code_after_match
      i += len(new_middle) + first_match.start()

      
    with open('out.html', 'w') as file:
      file.write(template.replace("{{CODE}}", code))

if __name__ == "__main__":
    main()