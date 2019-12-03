from matplotlib import pyplot as plt

Medals = 'Gold', 'Silver', 'Bronze'
average_medal_ratio = [25.57, 48.85, 25.57]  
explode = (0,0.1,0)  # it "explode" the 1st slice   
  
fig1, ax1 = plt.subplots()  
ax1.pie(average_medal_ratio, explode=explode, labels=Medals, autopct='%1.1f%%',  
        shadow=True, startangle=90)  
ax1.axis('equal')
ax1.set_title("Medals Won By USA\n(Using %,  Medal Category)")  # Equal aspect ratio ensures that pie is drawn as a circle.  

ax1.legend(Medals,
          title="Medals",
          loc="upper right",
          bbox_to_anchor=(1, 0, 0.1, 1))
  
plt.show() 