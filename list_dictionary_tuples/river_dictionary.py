major_rivers = { "Ganga" : "India" ,
                "Nile" : "Egypt",
                "Amazon" : "Brazil",
                }

print("="*38, end="")
for river, country in major_rivers.items():
    print(f'\nThe {river} river runs through {country}.\n')
print("="*38+"\n\nRiver List\n"+"-"*12)
for river in major_rivers.keys():
    print(river)
print("\nCountry List\n"+"-"*12)
for country in major_rivers.values():
    print(country)