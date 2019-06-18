from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" %(from_file, to_file))

#We could do these two on one line too, how?
in_file = open(from_file)
in_date = in_file.read()

print("The input file is %d byte long" % len(in_date))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CRTL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_date)

print("Alright, all done.")

out_file.close()
in_file.close()