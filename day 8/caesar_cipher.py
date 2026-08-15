logo = """
   ____                             ____ _       _              
  / ___|__ _  ___  ___  __ _ _ __  / ___(_)_ __  | |__   ___ _ __ 
 | |   / _` |/ _ \\/ __|/ _` | '__| | |   | | '_ \\ | '_ \\ / _ \\ '__|
 | |__| (_| |  __/\\__ \\ (_| | |    | |___| | |_) || | | |  __/ |   
  \\____\\__,_|\\___||___/\\__,_|_|     \\____|_| .__(_)_| |_|\\___|_|   
                                            |_|                    
"""

print(logo)

alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"

def cipher(message, shift):
    alphabet_list = alphabet.split(",")
    new_message = ""
    for letter in message:
        if letter in alphabet_list:
            index = alphabet_list.index(letter)
            new_index = (index + shift) % len(alphabet_list)
            new_message += alphabet_list[new_index]
        else:
            new_message += letter
    return new_message


def decode(message, shift):
    return cipher(message, -shift)

if __name__ == "__main__":
    while True:
        choice = input("Type 'encode' to encrypt, type 'decode' to decrypt, or type 'exit' to quit:\n")
        if choice == "encode":
            message = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            encoded_message = cipher(message, shift)
            print(f"Encoded message: {encoded_message}")
        elif choice == "decode":
            message = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            decoded_message = decode(message, shift)
            print(f"Decoded message: {decoded_message}")
        elif choice == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")