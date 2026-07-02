#INPUT
verb = input("Ingrese el verbo que desea conjugar: ")



#PROCESS
pronouns = [ 'yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']
terminations = {
    'ar': [ 'o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': [ 'o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': [ 'o', 'es', 'e', 'imos', 'is', 'en']
}

stem = verb[:-2]
ending = verb [-2:]
endings_list = terminations[ending]

#OUTPUT
for index, pronoun in enumerate(pronouns):
    termination = endings_list[index]
    print(f"{pronoun} {stem}{termination}")