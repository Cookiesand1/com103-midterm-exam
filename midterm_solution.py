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

matches = []

# LOOP FOR 4 MATCHES
for i in range(4):
    print(f"\n--- MATCH {i +1} ---")
    
    hero_choice = int(input("Hero number (0 to skip): "))

    if hero_choice == 0:
        continue

    if hero_choice < 1 or hero_choice > 5:
        print("Invalid hero number")
        continue

    hero = mlbb_roster[hero_choice - 1][0]

    k = int(input("Kill/s: "))
    d = int(input("Death/s: "))
    a = int(input("Assist/s: "))
    r = input("Result (W/L): ").upper()

    if d == 0:
        d = 1

    kda = (k + a) / d

    if kda >= 5 and r == "W":
        tag = "DOMINATION!"
    elif kda >= 5 and r == "L":
        tag = "Carried Hard"
    elif kda < 5 and r == "W":
        tag = "Team Effort"
    else:
        tag = "Better Luck Next Game"

    matches.append({
        "hero": hero,
        "kda": kda,
        "result": r,
        "tag": tag,
        "match_no": i + 1
    })

# STATS
wins = 0
for m in matches:
    if m["result"] == "W":
        wins += 1

losses = len(matches) - wins

if len(matches) > 0:
    winrate = int((wins / len(matches)) * 100)
else:
    winrate = 0

best = matches[0]
for m in matches:
    if m["kda"] > best["kda"]:
        best = m

