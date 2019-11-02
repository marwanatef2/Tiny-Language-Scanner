def isReservedWord (word):
    # check if word is reserved word
    # return its token type
    # otherwise return false
    if word == 'if':
        return 'IF token'
    elif word == 'then':
        return 'THEN token'
    elif word == 'else':
        return 'ELSE token'
    elif word == 'end':
        return 'END token'
    elif word == 'repeat':
        return 'REPEAT token'
    elif word == 'until':
        return 'UNTIL token'
    elif word == 'read':
        return 'READ token'
    elif word == 'write':
        return 'WRITE token'
    else:
        # not a reserved token
        return False

def isSpecialSymbol (char):
    if char == '+':
        return 'PLUS sign'
    elif char == '-':
        return 'MINUS sign'
    elif char == '*':
        return 'MULTIPLY sign'
    elif char == '/':
        return 'DIVIDE sign'
    elif char == '=':
        return 'EQUAL sign'
    elif char == '<':
        return 'SMALLER THAN sign'
    elif char == '>':
        return 'GREATER THAN sign'
    elif char == '(':
        return 'OPEN BRACKET'
    elif char == ')':
        return 'CLOSED BRACKET'
    elif char == '[':
        return 'OPEN SQUARE BRACKET'
    elif char == ']':
        return 'CLOSED SQUARE BRACKET'
    elif char == '{':
        return 'OPEN CURLY BRACES'
    elif char == '}':
        return 'CLOSED CURLY BRACES'
    elif char == ';':
        return 'SEMICOLON'
    elif char == ':':
        return 'COLON'
    elif char == '!':
        return 'EXCLAMATION'
    # not special symbol
    else :
        return False 

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


print("Please write the test cases in the input text file then Save.")
run = input('If ready, Enter "r" to run...\n')

while run=='r':

    with open('input.txt', 'r') as reader:

        first_line = True
        in_a_comment = False

        # iterate over input lines
        for line in reader:
            
            error_flag = False

            # add space to end of line
            if not line[-1].isspace():
                line += ' '

            # dictionary of {tokenvalue : tokentype}
            tokens = dict()
            # string to add characters in to get a complete word
            identifier = ''
            
            previous_char = ''

            # iterate over characters per line input
            for char in line:
                    
                # special symbol case or end of identifier
                if isSpecialSymbol(char) or char.isspace():
                    # end of word

                    # in case of reserved word, append to dict & reset identifier
                    if isReservedWord(identifier):
                        tokens[identifier] = isReservedWord(identifier)
                        identifier = ''

                    # in case of number
                    elif identifier.isnumeric() or isFloat(identifier) :
                        tokens[identifier] = 'Number'
                        identifier = ''

                    # case random word or empty string
                    else:
                        
                        # possible identifier if starting with letter
                        # more than 1 character
                        if ( len(identifier)>1 and identifier[0].isalpha() ):
                            for character in identifier:
                                # if containing weird characters
                                if not ( character.isalpha() or character.isdigit() ):
                                    tokens[identifier] = 'Error!'
                                    error_flag = True
                                    break
                            # correct identifier
                            if identifier not in tokens.keys():
                                tokens[identifier] = 'Identifier'

                            identifier = ''
                        
                        # just 1 letter
                        elif (identifier.isalpha()):
                            tokens[identifier] = 'Identifier'
                            identifier = ''

                        # empty str
                        elif (len(identifier)==0):
                            pass
                        
                        else:
                            tokens[identifier] = 'Error!'
                            identifier = ''
                            error_flag = True

                    if error_flag:
                        print('\nError! Found token not in regular expressions.')
                        break

                    # check for comments
                    if isSpecialSymbol(char)=='OPEN CURLY BRACES':
                        # {
                        in_a_comment = True
                        # indicate start of comment
                        tokens[char]=isSpecialSymbol(char)+' - Start Comment'
                    elif isSpecialSymbol(char)=='CLOSED CURLY BRACES':
                        in_a_comment = False
                        # indicate end of comment just in case it started already
                        if '{' in tokens.keys():
                            tokens[char]=isSpecialSymbol(char)+' - End Comment'
                
                    elif isSpecialSymbol(char)=='COLON':
                        previous_char = ':'
                    elif isSpecialSymbol(char)=='EXCLAMATION':
                        previous_char = '!'
                    elif isSpecialSymbol(char)=='SMALLER THAN sign':
                        if previous_char == '=':
                            tokens['=<']='SMALLER THAN or EQUAL sign'
                            previous_char='' 
                        else:
                            previous_char='<'        
                    elif isSpecialSymbol(char)=='GREATER THAN sign':
                        if previous_char == '=':
                            tokens['=>']='GREATER THAN or EQUAL sign'
                            previous_char='' 
                        else:
                            previous_char='>'
                    elif isSpecialSymbol(char)=='EQUAL sign':
                        if previous_char == ':':
                            tokens[':=']='ASSIGN'
                            previous_char=''
                        elif previous_char == '!':
                            tokens['!=']='NOT EQUAL'
                            previous_char=''
                        elif previous_char == '<':
                            tokens['<=']='SMALLER THAN or EQUAL sign'
                            previous_char=''
                        elif previous_char == '>':
                            tokens['>=']='GREATER THAN or EQUAL sign'
                            previous_char=''
                        else:
                            previous_char = '='
                        
                    # else append to tokens dictionary
                    else:
                        # check first for previous char
                        if previous_char == '<' or previous_char == '>' or previous_char=='=':
                            tokens[previous_char]=isSpecialSymbol(previous_char)
                            previous_char=''
                        # then append if not space
                        if not char.isspace():
                            tokens[char]=isSpecialSymbol(char)
                # any other character 
                else:
                    # skip if in a comment
                    if not in_a_comment:
                        identifier += char


            # to overwrite the output file just in case it's the 1st line
            if first_line:
                first_line = False
                with open ('output.txt', 'w') as writer:
                    for key, item in tokens.items():
                        writer.write(key + ' : ' + item + '\n')
                    writer.write('--------------------\n')
            # append otherwise
            else:
                with open ('output.txt', 'a') as writer:
                    for key, item in tokens.items():
                        writer.write(key + ' : ' + item + '\n')
                    writer.write('--------------------\n')

    print("\nPlease check the output text file.")
    run = input('Press "r" to run another test case, any other key to exit.\n')