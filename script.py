import git

repo = git.Repo('/Users/integro/Documents/Capitales del mundo')
f1 = open('capitales', 'r')

i = 0
for line in f1:
	f2 = open('capitalesdelmundo.txt', 'a')
	f2.write(line)
	print repo.git.add( 'capitalesdelmundo.txt')
	msg = "Escribe la capital numero " + str(i)
	i = i + 1
	print i
	print repo.index.commit(message=msg)
	f2.close()

f1.close()


