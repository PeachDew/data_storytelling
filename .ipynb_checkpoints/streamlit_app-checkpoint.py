import streamlit as st
import random
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from matplotlib.ticker import FormatStrFormatter

random.seed(42)

st.set_page_config(
        page_title="Data Storytelling",
        page_icon="📊"
)

data = {
    'Year': [],
    'Sales': [],
    'Expenses': [],
    'Profit': [],
    'Region': []
}

for _ in range(99):
    year = random.randint(2010, 2022)
    sales = random.randint(10000, 200000)
    expenses = random.randint(5000, 100000)
    profit = sales - expenses
    region = random.choice(['North', 'South', 'East', 'West'])
    
    data['Year'].append(year)
    data['Sales'].append(sales)
    data['Expenses'].append(expenses)
    data['Profit'].append(profit)
    data['Region'].append(region)

# Add one outlier 
data['Year'].append(2022)
sales = 98020042
expenses = random.randint(5000, 100000)
profit = sales - expenses
data['Sales'].append(sales)  
data['Expenses'].append(expenses)
data['Profit'].append(profit)
data['Region'].append(random.choice(['North', 'South', 'East', 'West']))

df = pd.DataFrame(data)

st.title("Storytelling with Data 🎭📈")

st.markdown(''' Welcome! Here I attempt to visualise and implement valuable lessons and insights from Cole Nussbaumer Knaflic's book, "Storytelling with Data,". Hope you enjoy your stay! ''')

st.markdown('''# Choosing a Visual 🔍👁️
In the vast landscape of data visualization, numerous graphs and visual displays exist, each serving a specific purpose. However, you'll be delighted to know that a select few can meet the majority of your data visualization needs.''')

st.divider()

st.markdown('''
## Using numbers themselves
When presenting/comparing few numbers, often a good idea to present the numbers themselves.
''')

max_sale = df.Sales.max()
mean_sale = df.Sales.mean()
percentage_difference = ((max_sale - mean_sale) / mean_sale) * 100
max_sales_year = df.loc[df['Sales'].idxmax(), 'Year']
st.divider()
st.markdown(f'''
<span style="font-size:25px;">In **{max_sales_year}** we had </span>

<span style="font-size:90px;font-weight:bold;color: #0099ff;">{max_sale} </span><span style="font-size:90px;">sales</span> 

<span style="font-size:25px;"> This was </span><span style="font-size:35px;font-weight:bold;color: #ff6600;">{percentage_difference:.2f}% </span> <span style="font-size:25px;"> larger than average!</span>
''', unsafe_allow_html=True)
st.divider()

st.markdown("## Heatmaps")
st.markdown("A heatmap is an effective visualization technique used to represent tabular data, replacing or supplementing numerical values with colored cells to visually depict the relative magnitudes of the data.")

years = np.arange(2015, 2023)
regions = ['North', 'South', 'East', 'West']
sales_data = np.random.randint(50000, 200000, size=(len(years), len(regions)))

df = pd.DataFrame(sales_data, columns=regions)
df['Year'] = years
df = df.set_index('Year')

plt.style.use('dark_background')

fig, ax = plt.subplots()
ax = sns.heatmap(df, cmap='YlGnBu', annot=True, fmt='.0f', cbar=True)
fig.patch.set_facecolor("#0B0B43")
fig.patch.set_alpha(1)
plt.title('Sales Performance by Year and Region')
ax.set_yticklabels(ax.get_yticklabels(), rotation=45, ha='right')

st.pyplot(fig)

st.write("To enhance visualization and reduce mental processing, color saturation can be employed as a powerful tool to provide visual cues. By incorporating a heatmap, our eyes and brains can swiftly identify potential points of interest. The varying saturation levels in the heatmap enable quick identification of areas that stand out, allowing for a more efficient analysis and interpretation of the data.")

st.markdown("## Scatterplots")
st.markdown("Scatterplots are a powerful tool for visualizing the relationship between two variables. By encoding data on both the horizontal x-axis and the vertical y-axis, scatterplots provide a clear representation of the relationship and allow for insightful analysis. They enable us to examine the presence and nature of the relationship between variables, facilitating the identification of patterns, trends, and correlations in the data.")

iris = sns.load_dataset('iris')

fig2 = sns.pairplot(iris, hue='species', markers=['o', 's', 'D'])
st.columns([1.2,5,1])[1].write("Iris Dataset: Pairwise Relationships among Flower Measurements")
st.pyplot(fig2)

st.markdown("## Lineplots")

flights = sns.load_dataset("flights")
agg_df = flights[['year','passengers']].groupby('year').mean()

years = agg_df.index
passengers = agg_df['passengers']

fig3, ax = plt.subplots()
ax.plot(years, passengers, marker='o')

ax.set_title('Flights Dataset: Passenger Traffic Over the Years')
ax.set_xlabel('Year')
ax.set_ylabel('Passenger Count')

l1, l2 = st.columns(2)
with l2:
    st.markdown("Line graphs are a widely used visualization technique for representing continuous data. They are particularly effective for illustrating trends, patterns, and relationships over a continuous range of values. By connecting the data points with lines, line graphs emphasize the continuity and progression of the data.")
with l1:    
    st.pyplot(fig3)
    
    
data = {
    'Year': [2019, 2020],
    'Apple': [45.3, 48.2],
    'Samsung': [21.2, 20.4],
    'Huawei': [16.3, 14.6],
    'Xiaomi': [9.2, 11.4],
    'OPPO': [4, 5.4]
}


st.markdown("## Slope Graphs")


df = pd.DataFrame(data)

df_melted = df.melt('Year', var_name='Brand', value_name='MarketShare')


fig, ax = plt.subplots()
sns.lineplot(data=df_melted, x='Year', y='MarketShare', hue='Brand', marker='o')

ax.set_title('Smartphone Market Share: 2019 vs 2020')
ax.set_xlabel('Year')
ax.set_ylabel('Market Share (%)')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xticks([2019,2020])

s1, s2 = st.columns([2,5])
with s2:
    st.pyplot(fig)
with s1:
    st.markdown("Slopegraphs are a valuable visualization technique for comparing two time periods or points of reference and effectively showcasing relative increases, decreases, or differences across various categories.")
    
st.markdown("## Bar Graphs")
st.markdown("Bar charts are often avoided due to their commonness, but this is actually a misconception. Instead, bar charts should be embraced precisely because they are familiar to a wide audience. The ubiquity of bar charts reduces the learning curve for viewers and allows them to quickly interpret the data.")
tips = sns.load_dataset('tips')

avg_total_bill = tips.groupby('day')['total_bill'].mean()
avg_tip_amount = tips.groupby('day')['tip'].mean()


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

# non-zero baseline
axes[0].bar(avg_total_bill.index, avg_total_bill, color='blue')
axes[0].bar(avg_tip_amount.index, avg_tip_amount, color='orange')
axes[0].set_title('Average Total Bill and Tip Amount by Day')
axes[0].set_xlabel('Day')
axes[0].set_ylabel('Amount')
axes[0].set_ylim([16, 30])
axes[0].legend(['Total Bill', 'Tip Amount'])

# zero
axes[1].bar(avg_total_bill.index, avg_total_bill, color='blue')
axes[1].bar(avg_tip_amount.index, avg_tip_amount, color='orange')
axes[1].set_title('(Baseline at Zero)')
axes[1].set_xlabel('Day')
axes[1].set_ylabel('Amount')
axes[1].legend(['Total Bill', 'Tip Amount'])

# Display the plot using Streamlit
st.pyplot(fig)
st.markdown("One critical aspect to remember is that bar charts should always include a zero baseline.")
st.markdown("For example, one might mistakenly perceive a significant disparity in business between Sunday and Friday when it may not actually be the case.")
st.divider()
st.markdown('''# Principles of 
# Visual Perception🧩👀''')
st.markdown('''To better identify the important elements in our visuals, distinguishing the signal (the information we want to convey) from the noise (clutter), we can turn to the **Gestalt Principles of Visual Perception**. 

Developed by the Gestalt School of Psychology in the early 1900s, these principles shed light on how individuals perceive order in their surroundings. They continue to be widely accepted and provide valuable insights into how people interact with and organize visual stimuli.''')

st.divider()
st.markdown("### Proximity 🚶‍♂️")
colp1, colp2 = st.columns([3,2])
colpp1, colpp2 = st.columns(2)
with colpp1:
    df1 = pd.DataFrame(np.random.randint(1, 10, size=(5, 3)), columns=['Column 1', 'Column 2', 'Column 3'])
    styled_df1 = df1.style.set_table_styles([
        {'selector': 'td', 'props': [('min-width', '100px'), ('text-align', 'center')]},  
    ])
    st.dataframe(styled_df1, hide_index=True)
with colpp2:
    df2 = pd.DataFrame({'Column 1': [123456789, 987654321, 456789123],
                'Column 2': [9876543210, 1234567890, 5678901234],
                'Column 3': [567890123, 890123456, 234567890]})
    st.dataframe(df2, hide_index=True)            
st.markdown('''Objects that are physically close together are often perceived as belonging to the same group. Our minds naturally associate proximity with connectedness and group membership. 

We can use this tendency in table design. By adjusting the spacing between rows/columns, we can guide the viewer's eyes either down the columns or across the rows. ''')
st.divider()
st.markdown("### Similarity 👥")
cols1, cols2 = st.columns(2)
with cols1:
    st.markdown('''Objects that share similarities in color, shape, size, or orientation are naturally perceived as being related or belonging to the same group. 

This principle can be effectively employed in tables to guide the attention of our audience towards specific areas we want them to focus on.''')
with cols2:
    datas = {
    'Name': ['John', 'Emily', 'Michael', 'Sophia', 'William'],
    'Age': [25, 30, 29, 28, 32],
    'City': ['London', 'Japan', 'New York', 'New York', 'Sydney'],
    'Salary': [50000, 60000, 70000, 75000, 42000]
    }

    dfs = pd.DataFrame(datas)
    highlight_rows = [2, 3]
    styled_dfs = dfs.style.apply(lambda x: ['background-color: rgba(255, 255, 0, 0.3)' if i in highlight_rows else '' for i in range(len(x))], axis=0)
    st.dataframe(styled_dfs, hide_index=True)
st.divider()
st.markdown("### Enclosure 📦")
cole1, cole2 = st.columns(2)
with cole1:
    years = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
    values = [10, 15, 8, 9, 11, 10, 9]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(years, values)
    ax.set_xlabel('Year')
    ax.set_ylabel('Sales')

    highlight_start = 2016.5
    highlight_end = 2020
    highlight_rect = plt.Rectangle((highlight_start, min(values)-1), highlight_end - highlight_start, max(values)-min(values)+1, facecolor='yellow', alpha=0.3)
    ax.add_patch(highlight_rect)

    st.pyplot(fig)
with cole2:
    st.write("When objects are physically enclosed together, we naturally perceive them as belonging to a cohesive group. We can make use of the enclosure principle to visually differentiate and highlight specific elements within our data. ")
st.divider()
st.markdown("### Closure ⭕️")
colcl1, colcl2 = st.columns(2)
with colcl1:
    st.markdown('''Our minds prefer simplicity and tend to fill in missing parts to make sense of incomplete shapes. We automatically complete the picture, allowing us to perceive a whole even when some elements are missing.
             
Removing unnecessary elements like chart borders and background shading, as guided by the closure principle, allows our graph to appear cohesive. Furthermore, this helps emphasize our data.''')
with colcl2:
    categories = ['Category 1', 'Category 2', 'Category 3']
    values = [10, 15, 8]

    fig, axes = plt.subplots(2, 1, figsize=(8, 5))

    axes[0].barh(np.arange(len(categories)), values, color='red', edgecolor='black')
    axes[0].set_yticks(np.arange(len(categories)))
    axes[0].set_yticklabels(categories)
    axes[0].set_title('Bar Chart with Borders and Shading')

    axes[1].barh(np.arange(len(categories)), values, edgecolor='none')
    axes[1].set_yticks(np.arange(len(categories)))
    axes[1].set_yticklabels(categories)
    axes[1].set_title('Bar Chart Simplified')

    axes[1].spines['left'].set_visible(False)
    axes[1].spines['bottom'].set_visible(False)
    axes[1].spines['right'].set_visible(False)
    axes[1].spines['top'].set_visible(False)
    
    plt.subplots_adjust(hspace=0.5)

    st.pyplot(fig)
st.divider()
st.markdown("### Continuity 📈")
colc3, colc4 = st.columns(2)
with colc3:
    categories = ['Category 1', 'Category 2', 'Category 3']
    values = [10, 15, 8]
    
    fig, ax = plt.subplots()
    ax.bar(categories, values, edgecolor='none')

    # Remove axis lines
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    for i, v in enumerate(values):
        ax.text(i, v, str(v), ha='center', va='bottom')

    st.pyplot(fig)
with colc4:
    st.markdown('''The principle of continuity is closely related to closure. When we observe objects, our eyes instinctively follow the smoothest path and mentally bridge gaps to create a sense of continuity. 
    
Even without the vertical y-axis line from the graph, our eyes naturally perceive that the bars align at the same point due to the consistent white space between them. As mentioned in the closure principle, removing unnecessary elements enables our data to take center stage.''')
st.divider()
st.markdown("### Connection 👫")
colc1, colc2 = st.columns([3,4])
with colc1:
    st.markdown("Our perception naturally associates physically connected objects as belonging to a group. This principle of connection is commonly utilized, for instance, in line graphs, where it helps our eyes discern patterns and find order within the presented data.")
with colc2:
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Scatter plot
    sns.scatterplot(data=df_melted, x='Year', y='MarketShare', hue='Brand', marker='o', ax=axes[0])
    axes[0].set_title('Smartphone Market Share: 2019 vs 2020')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Market Share (%)')
    axes[0].set_xticks([2019, 2020])
    axes[0].legend('',frameon=False)

    # Line plot
    sns.lineplot(data=df_melted, x='Year', y='MarketShare', hue='Brand', marker='o', ax=axes[1])
    axes[1].set_title('Smartphone Market Share: 2019 vs 2020')
    axes[1].set_xlabel('Year')
    axes[1].set_ylabel('Market Share (%)')
    axes[1].legend(loc='center left', bbox_to_anchor=(1, 0.5))
    axes[1].set_xticks([2019, 2020])

    st.pyplot(fig)
    
st.markdown("## Strategic Constrast 🎯🎭")

metrics = ['Price', 'Convenience', 'Service']
your_scores = [8, 9, 7]
competitor1_scores = [7, 8, 8]
competitor2_scores = [6, 7, 9]

bar_width = 0.2

r1 = np.arange(len(metrics))
r2 = [x + bar_width for x in r1]
r3 = [x + 2 * bar_width for x in r1]

colsc1, colsc2 = st.columns(2)
with colsc1:
    fig, ax = plt.subplots()
    b1 = ax.barh(r1, your_scores, height=bar_width, label='Our Company')
    b2 = ax.barh(r2, competitor1_scores, color='grey', height=bar_width, label='Competitor 1')
    b3 = ax.barh(r3, competitor2_scores, color='grey', height=bar_width, label='Competitor 2')
    tboxes = ax.bar_label(b1, label_type='center', labels = ["Our Company" for x in range(3)])
    for label in tboxes:
        label.set_color('black')
    ax.bar_label(b2, label_type='center', labels = ["Competitor 1" for x in range(3)])
    ax.bar_label(b3, label_type='center', labels = ["Competitor 2" for x in range(3)])

    ax.set_xlabel('Scores')
    ax.set_title('Comparison: Our Company vs Competitors')
    ax.set_yticks([r + bar_width for r in range(len(metrics))])
    ax.set_yticklabels(metrics)

    st.pyplot(fig)
with colsc2:
    fig, ax = plt.subplots()
    ax.scatter(metrics, your_scores, marker='o', s=100, label='Your Company')
    ax.scatter(metrics, competitor1_scores, marker='s', s=100, label='Competitor 1')
    ax.scatter(metrics, competitor2_scores, marker='^', s=100, label='Competitor 2')

    ax.set_xlabel('Metrics')
    ax.set_ylabel('Scores')
    ax.set_title('Comparison: Our Company vs Competitors')
    ax.set_xticks(r1)
    ax.set_xticklabels(metrics)
    ax.legend()

    st.pyplot(fig)
    
st.markdown('''
By employing effective contrast and incorporating thoughtful design choices, we can significantly enhance the process of obtaining the information we seek. Contrast, along with other deliberate design decisions, allows us to access information more swiftly, effortlessly, and with a sense of comfort. 😌
''')

x = np.arange(2010, 2023, 1)
y1 = np.random.randn(len(x)) *10020+15000
y2 = np.random.randn(len(x)) *10000+15000
y1.append(30512)
y2.append(25858)

fig, ax = plt.subplots()
ax.plot(x, y1, 'b-', label='Apple')
ax.plot(x, y2, 'r-', label='Samsung')
ax.scatter(x, y1, c='b', marker='o')
ax.scatter(x, y2, c='r', marker='o')

#Add chart borders and prominent gridlines
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.grid(color='white', linestyle='--', linewidth=1.5)

ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

#Add legend
ax.legend()

st.pyplot(fig)








