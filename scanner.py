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
        return 'CLOSE BRACKET'
    elif char == '{':
        return 'OPEN CURLY BRACES'
    elif char == '}':
        return 'CLOSE CURLY BRACES'
    elif char == ';':
        return 'SEMICOLON'
    elif char == ':=':
        return 'ASSIGN'
    # not special symbol
    else :
        return False 

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

with open('input.txt', 'r') as reader:

    first_line = True

    # iterate over input lines
    for line in reader:
        
        # add space to end of line
        if not line[-1].isspace():
            line += ' '

        # dictionary of {tokenvalue : tokentype}
        tokens = {}
        # string to add characters in to get a complete word
        identifier = ''
        
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
                                identifier = ''
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

                # append to tokens dictionary
                if not char.isspace():
                    tokens[char]=isSpecialSymbol(char)
            
            # any other character 
            else:
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

