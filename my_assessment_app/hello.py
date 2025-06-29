from preswald import connect, get_df
    
connect()  # Initialize connection to preswald.toml data sources
df = get_df("NHIS_Adult_Summary_Health_Statistics.csv")  # Load data


from preswald import query
    
sql = "SELECT * FROM NHIS_Adult_Summary_Health_Statistics.csv WHERE value > 50"
filtered_df = query(sql, "NHIS_Adult_Summary_Health_Statistics.csv")


from preswald import table, text

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

from preswald import slider, view
threshold = slider("Threshold", min_val=0, max_val=100, default=50)
table(df[df["value"] > threshold], title="Dynamic Data View")


from preswald import plotly
import plotly.express as px

fig = px.scatter(df, x="column1", y="column2", color="category")
plotly(fig)

#Create an interactive dashboard
from preswald import text, slider, table

text("# Interactive Dashboard")

rows = slider("Rows to Display", min_val=5, max_val=50, default=10)
table(data, limit=rows)


from preswald import topbar

#Add the topbar
topbar()



