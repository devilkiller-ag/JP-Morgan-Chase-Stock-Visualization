from preswald import connect, get_df, text

text("# All time JPMorgan Chase Stock Data Visualization 1980 - 2025")

connect()  # Initialize connection to preswald.toml data sources
df = get_df("JPM_1940-01-01_2025-03-04.csv")  # Load data

