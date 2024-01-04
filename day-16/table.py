from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ['Pikachu', 'Charmander', 'Skuertel'])
table.add_column("Type", ['Electric', 'Fire', 'Water'])
table.align = 'l'
print(table)
