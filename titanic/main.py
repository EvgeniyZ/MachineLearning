from scipy.stats.stats import pearsonr
import pandas


def get_first_name(trimmed_name):
    result = ""
    for x in trimmed_name:
        if x == ' ':
            return result
        else:
            result += x
    return result


def get_female_first_name(name):
    if "Ms." in name:
        if "(" in name:
            return get_first_name(name[name.index("(") + 1:])
        return get_first_name(name[name.index("Ms") + 4:])
    if "Mrs." in name:
        if "(" in name:
            return get_first_name(name[name.index("(") + 1:])
        return get_first_name(name[name.index("Mrs") + 5:])
    if "Miss." in name:
        if "(" in name:
            return get_first_name(name[name.index("(") + 1:])
        return get_first_name(name[name.index("Miss") + 6:])
    return 0

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
sex = data['Sex'].value_counts()
survived = 0
firstClass = 0
femaleFirstNames = {}
for x in data.get_values():
    if x[1] == 1:
        firstClass += 1
    if x[0] == 1:
        survived += 1
    femaleFirstName = get_female_first_name(x[2])
    if femaleFirstName == 0:
        continue
    if femaleFirstName in femaleFirstNames.keys():
        femaleFirstNames[femaleFirstName] += 1
    else:
        femaleFirstNames[femaleFirstName] = 1
maxValue = max(femaleFirstNames.values())
print maxValue
position = 0
for value in femaleFirstNames.itervalues():
    if value == maxValue:
        print femaleFirstNames.keys()[position]
    position += 1
ageMean = data['Age'].mean(axis=0)
ageMedian = data['Age'].median(axis=0)
correlationParchSibSp = pearsonr(data['Parch'], data['SibSp'])
print correlationParchSibSp
print ageMean
print ageMedian
print survived
print float(survived) / float(891)
print float(firstClass) / float(891)
