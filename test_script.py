import sys

def main(loan_id):
    if loan_id.strip().isnumeric():
        print(int(loan_id))
        return(int(loan_id))
    else:
        print("please provide a number")

if __name__ == "__main__":
    main(sys.argv[1])
