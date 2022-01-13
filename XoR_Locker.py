"""
#=========================================================#
# [+] Title: Image XoR Encryption and Decryption          #
# [+] Script: XoR_Locker.py                               #
# [+] Creator : Danyah Alharthi                           #
#=========================================================#
"""

import argparse
import sys
import hashlib
from random import randint


class bcolors:
    FAIL = '\033[91m'
    BANNER = '\033[93m'
    HELP = '\033[42m'
    ENDC = '\033[0m'
    INPUT = '\033[94m'
    DONE = '\033[92m'


class xorLocker:
    def __init__(self):
        self.path = ''

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description=print(bcolors.BANNER + '''
                            
         ██╗░░██╗░█████╗░██████╗░  ██╗░░░░░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
         ╚██╗██╔╝██╔══██╗██╔══██╗  ██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
         ░╚███╔╝░██║░░██║██████╔╝  ██║░░░░░██║░░██║██║░░╚═╝█████═╝░█████╗░░██████╔╝
         ░██╔██╗░██║░░██║██╔══██╗  ██║░░░░░██║░░██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
         ██╔╝╚██╗╚█████╔╝██║░░██║  ███████╗╚█████╔╝╚█████╔╝██║░╚██╗███████╗██║░░██║
         ╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                            
                                     Tool :- XOR Locker
                Tool type :- Image Encryption and Decryption using XOR Operartion
                                    Created by :- Danyah Alharthi
                            Syntax :  python <filename> <option> <path>
        
    __________________________________________________________________________________________
    |                                                                                         |
    | -e or --encryption {                                                                    |
    |     Use : To Encrypt an Image File                                                      |
    |     Explaination : The Path of the Image you want to Encrypt                            |
    | }                                                                                       |
    |                                                                                         |
    | -d or --decryption {                                                                    |
    |      Use : To Decrypt an Image File                                                     |
    |      Explaination : The Path of the Image you want to Decrypt                           |
    |                                                                                         |
    | }                                                                                       |
    |                                                                                         |
    |  -c or --compare {                                                                      |
    |      Use : To Compare Between Two Hashes                                                |
    |      Explaination : The Path of the Image you want to Compare its Hash                  |
    |                                                                                         |
    | }                                                                                       |
    |                                                                                         |
    |  -cm or --computeHash {                                                                 |
    |       Use : To Compute the Hash of an Image                                             |
    |       Explaination : The Path of the Image you want to Compare its Hash                 |
    | }                                                                                       |
    | Example {                                                                               |
    |    Command : python XoR_Locker.py -e /Desktop/example_dir/example_img                  |
    | }                                                                                       |
    \_________________________________________________________________________________________/       
  
     
           ''' + bcolors.ENDC))
        parser.add_argument("-op", "--options", help=bcolors.BANNER+"Listing all Options"+bcolors.ENDC)
        parser.add_argument("-e", "--encryption", help=bcolors.BANNER + "Encrypting the Image" + bcolors.ENDC)
        parser.add_argument("-d", "--decryption", help=bcolors.BANNER + "Decrypting the Image" + bcolors.ENDC)
        parser.add_argument("-c","--compare", help=bcolors.BANNER +"Compare the Hashes"+ bcolors.ENDC)
        parser.add_argument('-cm', '--computeHash', help=bcolors.BANNER +"Calculate the Hash"+ bcolors.ENDC)
        return parser.parse_args()

    def imgEncrypter(self, path):
        try:
            # Open & read file from given path
            with open(path, "rb") as input_file:
                image = input_file.read()

            image = bytearray(image)
            key = randint(0, 100)

            # Perform Encryption operation
            for index, value in enumerate(image):
                image[index] = value ^ key

            # Write updated values in file from given path
            with open(path, "wb") as output_file:
                output_file.write(image)
            # Storing Encryption key
            with open('/Users/xxx/Desktop/example_dir/Encryption_Info.txt', 'w') as server:
                server.write(f"Image Path: {path} --> Key {key}")

            print(bcolors.DONE + "[✔] Encryption Done Successfully " + bcolors.ENDC)



        except Exception:

            print(bcolors.FAIL + "[✖] Fail to Encrypt" + bcolors.ENDC)

    def imgDecrypter(self, path):
        while True:  # Keep running untill the user enters the correct key
            try:
                print(bcolors.INPUT + "Note : Encryption and Decryption Key Must Be The Same" + bcolors.INPUT)
                key = int(input(bcolors.INPUT + "[+] Please Enter Image Key To Decrypt : " + bcolors.INPUT))
                # Validating the entered key
                with open('/Users/xxx/Desktop/example_dir/Encryption_Info.txt', 'r') as server:
                    line = server.readline()
                    line = line[-2:]
                    if key == int(line):
                        # Open & read file from given path
                        with open(path, "rb") as input_file:
                            image = input_file.read()

                        image = bytearray(image)

                        # Perform Decryption operation
                        for index, value in enumerate(image):
                            image[index] = value ^ key

                        # Write updated values in file from given path
                        with open(path, "wb") as output_file:
                            output_file.write(image)

                        print(bcolors.DONE + "[✔] Decryption Done Successfully  " + bcolors.ENDC)

                        # Cleaning the file that contains Encryption keys
                        with open('/Users/xxx/Desktop/example_dir/Encryption_Info.txt', 'w') as file_earasing:
                            file_earasing.truncate()
                            file_earasing.close()
                        break
                    else:
                        print(bcolors.FAIL + "[✖] Key Is Not Correct"+ bcolors.ENDC)


            except Exception:
                print(bcolors.FAIL + "[✖] Fail to Decrypt" + bcolors.ENDC)

    def computeHash(self, path):
        with open(path, "rb") as input_file:
            image = input_file.read()
            Hash = hashlib.md5(image).hexdigest()
            print(bcolors.DONE +"[✔] MD5: " + Hash + bcolors.ENDC)

    def compareHash(self, path):
        with open(path, "rb") as input_file:
            image = input_file.read()
            new = hashlib.md5(image).hexdigest()

        old = input(bcolors.INPUT+"[+] Old Hash : "+bcolors.ENDC)

        if old == new:
            print(bcolors.HELP +"[+] New Hash : "+new+ bcolors.ENDC)
            print(bcolors.DONE +"[✔] Hashes Matched"+ bcolors.ENDC)

        else:
            print(bcolors.FAIL +"[✖] Hash MisMatch"+bcolors.ENDC)

    def main(self):
        args = self.get_args()

        if args.encryption:
            self.imgEncrypter(args.encryption)

        elif args.decryption:
            self.imgDecrypter(args.decryption)

        elif args.computeHash:
            self.computeHash(args.computeHash)

        elif args.compare:
            self.compareHash(args.compare)

        else:
            print(bcolors.FAIL + '[✖] Invalid Syntax' + bcolors.ENDC)
            print(bcolors.HELP + 'Use --help or -h for options.' + bcolors.ENDC)
            sys.exit(1)


if __name__ == '__main__':
    obj = xorLocker()
    obj.main()
