# System Logging Profile 
logging_profile = ("192.168.1.100", 8080)
 ip_address, server_port = logging_profile
  print("IP Address:", ip_address)
   print("Server Port:", server_port)
    try: logging_profile[0] = "192.168.1.200"
     except TypeError:
         print("Modification failed: Tuple is immutable.") 