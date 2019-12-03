import matplotlib.pyplot as plt

years = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
Number_Of_Records = [60, 70, 84, 75, 68, 60, 54, 65, 75, 88, 98]
CAN_Records = [60, 65, 75, 72, 71, 69, 68, 73, 80, 85, 91]

plt.plot(years, Number_Of_Records)
plt.plot(years, CAN_Records)
plt.xlabel('years')
plt.ylabel('Number_Of_Records')
plt.title('USA VS CANADA')

Country = 'USA', 'CANADA'

plt.legend(Country,
          title="Country",
          loc="upper left")

plt.show()
