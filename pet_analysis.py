import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    # Handling missing values and ensuring appropriate data types
    df.dropna(inplace=True)
    df['Birthdate'] = pd.to_datetime(df['Birthdate'])
    return df

def calculate_average_price(df, species):
    return df[df['Species'] == species]['Price'].mean()

def find_pets_with_feature(df, feature):
    return list(df[df['SpecialFeature'] == feature]['Name'])

def get_species_statistics(df):
    species_stats = {}
    for species in df['Species'].unique():
        avg_price = df[df['Species'] == species]['Price'].mean()
        avg_age = df[df['Species'] == species]['Age'].mean()
        species_stats[species] = {'Average Price': avg_price, 'Average Age': avg_age}
    return species_stats

def plot_price_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['Price'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.title('Price Distribution')
    plt.savefig('price_distribution.png')
    plt.show()

def plot_average_price_by_species(df):
    avg_prices = df.groupby('Species')['Price'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(data=avg_prices, x='Species', y='Price', palette='viridis')
    plt.xlabel('Species')
    plt.ylabel('Average Price')
    plt.title('Average Price by Species')
    plt.xticks(rotation=45)
    plt.savefig('average_price_by_species.png')
    plt.show()

def plot_price_vs_age(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Age', y='Price', hue='Species', palette='viridis')
    plt.xlabel('Age')
    plt.ylabel('Price')
    plt.title('Price vs Age')
    plt.grid(True)
    plt.savefig('price_vs_age.png')
    plt.show()

def plot_age_distribution_by_species(df):
    fig = px.box(df, x='Species', y='Age', title='Age Distribution by Species')
    fig.update_layout(xaxis_title='Species', yaxis_title='Age', title='Age Distribution by Species')
    fig.write_image('age_distribution_by_species.png')
    fig.show()
