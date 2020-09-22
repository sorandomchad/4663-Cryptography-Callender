import cipher
import os
import sys



def mykwargs(argv):
    '''
    Processes argv list into plain args (list) and kwargs (dict).
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
            kargs{arg3 : val1, arg4 : val2}

        Params with dashes (flags) can now be processed seperately
    Shortfalls:
        spaces between k=v would result in bad params
        Flags aren't handled at all. Maybe in the future but this function
            is meant to be simple.
    Returns:
        tuple  (args,kargs)
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs


def usage(message=None):
    if message:
        print(message)
    name = os.path.basename(__file__)
    print(f"Usage: python {name} [input=string filename] [output=string filename] [key=string] [op=encrypt/decrypt]")
    print(f"Example:\n\t python {name} input=input_file.txt output=output_file.txt key=machine op=encrypt\n")
    sys.exit()

if __name__=='__main__':
    """
    Change the required params value below accordingly.
    """

    required_params = 5 # adjust accordingly

    # get processed command line arguments 
    _,params = mykwargs(sys.argv[1:])

    # print usage if not called correctly
    if len(params) < required_params:
        usage()

    operation = params.get('op',None)
    infile = params.get('input',None)
    outfile = params.get('output',None)
    key1 = params.get('key1',None)
    key2 = params.get('key2',None)

    C = cipher.Adfgx(key1, key2)

    if not operation and not infile and not outfile and not key1 and not key2:
        usage()

    if operation.lower() == 'encrypt':
        C.encrypt(**params)
    elif operation.lower() == 'decrypt':
        C.decrypt(**params)
    else:
        usage()

#example: plaintext=alimony, key1=matrix key2=radon
# ciphertext should be DA AF AX AD XG GA XG
