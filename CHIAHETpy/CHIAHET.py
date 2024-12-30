file_input=open("CHIAHET.INP","r")
file_output=open("CHIAHET.OUT","w")
output = ""

a,b  = map(int, file_input.readline().split())
for i in range(a,b+1):
    if i % 3 == 0 and i % 5 == 0:
        output = str(i) +"\n"




file_output.write(output)
