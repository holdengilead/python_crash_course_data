import plotly.express as px

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()
poss_results = list(range(2, die_1.num_sides * 2 + 1))

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for _ in range(1000)]

# Analyze the results.
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
