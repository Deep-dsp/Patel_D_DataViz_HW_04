import matplotlib.pyplot as plt;
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

sports = ('Bobsleigh', 'Ice Hockey', 'Skating', 'Skiing')
y_pos = np.arange(len(sports))
Number_Of_Medals = [93, 269, 179, 98]

plt.bar(y_pos, Number_Of_Medals, align='center', alpha=0.5)
plt.xticks(y_pos, sports)
plt.ylabel('Number_Of_Medals')
plt.xlabel('Sports')
plt.title('Medals Won By USA In Several Sports')

plt.legend(sports,
          title="Medals Won",
          loc="upper right",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()