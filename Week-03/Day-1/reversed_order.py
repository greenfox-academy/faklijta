# Create a method that decrypts reversed-order.txt
def decrypt(file_name):
    with open(file_name, "r") as f:
        text = f.readlines()
        reversed = text[::-1]
    print(reversed)

    f.close()
decrypt("reversed_order.txt")
