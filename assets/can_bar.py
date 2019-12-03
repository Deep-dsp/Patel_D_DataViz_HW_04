import matplotlib.pyplot as plt;
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

country = ('USA', 'CANADA')
y_pos = np.arange(len(country))
Number_Of_Medals = [653, 625]

plt.bar(y_pos, Number_Of_Medals, align='center', alpha=0.5)
plt.xticks(y_pos, country)
plt.ylabel('Number_Of_Medals')
plt.xlabel('country')
plt.title('Number Of Medals Won By USA and CANADA')

plt.legend(country,
          title="country",
          loc="upper right",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()