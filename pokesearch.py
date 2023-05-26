import requests

print("\nEnter the name of a Pokemon: ", end ='')
name = input().lower()

url = "https://pokeapi.co/api/v2/pokemon/{}/".format(name)
response = requests.get(url)

if response.status_code != 200:
	print(response.text + "\n")
else:
	data = response.json()
	print("Name: " + data["name"].capitalize())

	abilities = data["abilities"]
	i = 0
	total = len(abilities)
	print(str(total) + " Abilities:")
	while (i < total):
		print("\t" + str(i + 1) + "- " + abilities[i]["ability"]["name"].capitalize())
		i += 1
	print()
