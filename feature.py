# Create a new feature: Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

# Drop the 'SibSp' and 'Parch' columns as we have captured the information in FamilySize
df.drop(['SibSp', 'Parch'], axis=1, inplace=True)
