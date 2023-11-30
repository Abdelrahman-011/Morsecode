# This is a sample Python script.
morseEncryptDict = {'A': '10111', 'B': '111010101',
                    'C': '11101011101', 'D': '1110101', 'E': '1',
                    'F': '101011101', 'G': '111011101', 'H': '1010101',
                    'I': '101', 'J': '1011101110111', 'K': '111010111',
                    'L': '101110101', 'M': '1110111', 'N': '11101',
                    'O': '11101110111', 'P': '10111011101', 'Q': '1110111010111',
                    'R': '1011101', 'S': '10101', 'T': '111',
                    'U': '1010111', 'V': '101010111', 'W': '101110111',
                    'X': '11101010111', 'Y': '1110101110111', 'Z': '11101110101',
                    '1': '10111011101110111', '2': '101011101110111', '3': '1010101110111',
                    '4': '10101010111', '5': '101010101', '6': '11101010101',
                    '7': '1110111010101', '8': '111011101110101', '9': '11101110111011101',
                    '0': '1110111011101110111', ', ': '1110111010101110111', '.': '10111010111010111',
                    '?': '101011101110101', '/': '1110101011101', '-': '111010101010111',
                    ',': '1110111010101110111', '\'': '1011101110111011101'
                    }

morseDecryptDict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
                    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
                    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
                    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
                    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
                    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
                    '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-',
                    '-.--.': '(', '-.--.-': ')', '.----.': '\''}


def encrypt(inputString):
    outputString = ''
    inputString = inputString.upper()

    for i in range(len(inputString)):
        if (inputString[i] != ' '):
            outputString += morseEncryptDict[inputString[i]]
            if (i != len(inputString) - 1):
                if (inputString[i + 1] != ' '):
                    outputString += '000'
        else:
            outputString += '0000000'
    return outputString


def decrypt(inputString):
    outputString = ''

    inputString = inputString.replace('0000000', '_')
    inputString = inputString.replace('111', '-')
    inputString = inputString.replace('1', '.')
    inputString = inputString.replace('000', ' ')
    inputString = inputString.replace('0', '')

    characterBuffer = ''

    for i in range(len(inputString)):
        if (inputString[i] == "_"):
            if characterBuffer != '':
                outputString += morseDecryptDict[characterBuffer]
            outputString += ' '
            characterBuffer = ''
        elif (inputString[i] == ' '):
            outputString += morseDecryptDict[characterBuffer]
            characterBuffer = ''
        else:
            characterBuffer += inputString[i]
        if i == len(inputString) - 1 and characterBuffer != '':
            outputString += morseDecryptDict[characterBuffer]

    return outputString


def main():
    userInput = input('Please select one of the following options Encrypt/Decrypt/Exit:\n').upper()
    if userInput == 'ENCRYPT' or userInput == '1':
        userInput = input('Please enter the string that you would like to encrypt:\n')
        print(encrypt(userInput))
    elif userInput == 'DECRYPT' or userInput == '2':
        userInput = input('Please enter the string that you would like to decrypt:\n')
        print(decrypt(userInput))
    elif userInput == 'EXIT' or userInput == '3':
        print('Exiting program')
    else:
        print("invalid user input!")
    return


main()