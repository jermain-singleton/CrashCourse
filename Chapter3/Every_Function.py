languages = ['Python', 'Javascript', 'SQL', 'HTML', 'CSS']
print(languages)

print(sorted(languages))
languages.reverse()
print(languages)
print(len(languages))
print(languages.pop())
print(languages)
languages.append('python')
print(languages)
del languages[4]
print(languages)
languages.remove('SQL')
print(languages[2])
print(languages)
languages.insert(2, 'Python')
languages.insert(3, 'SQL')
print(languages)
print("I am removing " + languages.pop() + " from the list.")