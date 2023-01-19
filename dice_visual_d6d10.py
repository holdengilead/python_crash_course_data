import plotly.express as px

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die(10)
poss_results = list(range(2, die_1.num_sides + die_2.num_sides + 1))

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for _ in range(50_000)]

# Analyze the results.
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
