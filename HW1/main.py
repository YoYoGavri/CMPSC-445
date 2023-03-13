import seaborn as sns

tips = sns.load_dataset('tips')

# Box plot
sns.boxplot(x='day', y='total_bill', data=tips)

# Bar plot
sns.barplot(x='sex', y='tip', data=tips)

# Count plot
sns.countplot(x='day', data=tips)

# Dist plot
sns.displot(tips['tip'])

# Clustermap
sns.clustermap(tips.corr(), cmap='coolwarm')

# Pairplot
sns.pairplot(tips, hue='sex')
