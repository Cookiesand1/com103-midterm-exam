mlbb_roster = [
    ["Layla", "Marksman"],
    ["Tigreal", "Tank"],
    ["Gusion", "Assassin"],
    ["Kagura", "Mage"],
    ["Chou", "Fighter"]
]

ign = input("In-game name (IGN): ")
rank = input("Current rank: ").capitalize()

print("=========================================")
print(f"{'MOBILE LEGENDS -- HERO ROSTER':^40}")
print("=========================================")

for i in range(len(mlbb_roster)):
    print(f"{i +1}. {mlbb_roster[i][0]:<10} [{mlbb_roster[i][1]}]")
print("=========================================")
