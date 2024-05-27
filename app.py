import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

# Load the data

fifa19 = pd.read_csv('FIFA.csv', index_col=0)


# Set Seaborn style
sns.set(style="whitegrid")

# Explore Age variable
st.subheader("Explore Age variable")
x = fifa19['Age']
st.pyplot(sns.distplot(x, bins=10).figure)

# Comment
st.write("It can be seen that the Age variable is slightly positively skewed.")

# Explore Preferred Foot variable
st.subheader("Explore Preferred Foot variable")
st.write("Number of unique values:", fifa19['Preferred Foot'].nunique())
st.write("Value counts:")
st.write(fifa19['Preferred Foot'].value_counts())

# Count plot
st.pyplot(sns.countplot(x="Preferred Foot", data=fifa19, color="c").figure)

# Count plot with Real Face
st.pyplot(sns.countplot(x="Preferred Foot", hue="Real Face", data=fifa19).figure)

# Catplot
st.pyplot(sns.catplot(x="Preferred Foot", kind="count", palette="ch:.25", data=fifa19).figure)

# Explore International Reputation variable
st.subheader("Explore International Reputation variable")
st.write("Number of unique values:", fifa19['International Reputation'].nunique())
st.write("Value counts:")
st.write(fifa19['International Reputation'].value_counts())

# Set Seaborn style
sns.set(style="whitegrid")

st.subheader("Barplot of International Reputation and Potential")
fig, ax = plt.subplots(figsize=(8, 6))  # Specify the figure size
sns.barplot(x="International Reputation", y="Potential", data=fifa19, ci="sd", ax=ax)  # Pass the axes object to sns.barplot
st.pyplot(fig)


# Scatterplot
st.subheader("Scatterplot of Height and Weight")
fig, ax = plt.subplots(figsize=(8, 15))  # Specify the figure size
sns.scatterplot(x="Height", y="Weight", data=fifa19, ax=ax)  # Pass the axes object to sns.scatterplot
st.pyplot(fig)


# Lineplot
st.subheader("Lineplot of Stamina and Strength")
fig, ax = plt.subplots(figsize=(8, 6))  # Specify the figure size
sns.lineplot(x="Stamina", y="Strength", data=fifa19, ax=ax)  # Pass the axes object to sns.lineplot
st.pyplot(fig)


# lmplot
st.subheader("lmplot of Overall and Potential")
g = sns.lmplot(x="Overall", y="Potential", hue="Preferred Foot", data=fifa19, palette="Set1")
st.pyplot(g.fig)

# FacetGrid
st.subheader("Histogram of Potential based on Preferred Foot")
g = sns.FacetGrid(fifa19, col="Preferred Foot")
g = g.map(plt.hist, "Potential")
st.pyplot(g.fig)
