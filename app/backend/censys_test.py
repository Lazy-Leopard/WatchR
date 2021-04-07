from censys import censys_ip
#import unittest


def censys_test(IP):
  if IP.count(".") == 3:
    output_value = censys_ip(IP)
    
    if(output_value == None):
      print("IP Adress not in use or Invalid\n")

    else:
      print("Valid IP Address\n")

  else:
    print("Invalid IP\n")
    
  #print(IP)


censys_test("127")

censys_test("127.23")

censys_test("127.12.12")

censys_ip("127.0.")

censys_test("117.203.224.85")

censys_test("12.88.36.233.12")

censys_test("172.256.233.108")

censys_test("A.A.A.A")


