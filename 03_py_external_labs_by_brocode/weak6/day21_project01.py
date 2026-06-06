

# hello how are today  i am gonna cover bar chart.
# bar chart is used to compare two or more categories by thier actual value
import matplotlib.pyplot as plt
players = ["Salah", "Haaland", "Mbappe", "Kane", "Lewandowski"]
goals = [29, 34, 28, 26, 24]

plt.bar(players,goals)
plt.title("top goal scorer")
plt.xlabel("players")
plt.ylabel("goal")

plt.show()


