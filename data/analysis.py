import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Pour l'affichage de la heatmap

class DataAnalysis:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.corr = None  # Ajout pour éviter les erreurs d'attribut manquant
    
    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            print(f"Data loaded successfully from {self.file_path}")
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def preprocess_data(self):
        if self.data is not None:
            self.data_numeric = self.data[['Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit', 'Cost', 'Revenue']]
            print("Preprocessing complete: numeric columns selected.")
        else:
            print("Data not loaded. Please load data first.")

    def calculate_correlation(self):
        if hasattr(self, 'data_numeric') and self.data_numeric is not None:
            self.corr = self.data_numeric.corr()
            print("Correlation matrix calculated.")
        else:
            print("Data not preprocessed. Please preprocess data first.")

    def plot_correlation(self):  # Assurez-vous que cette méthode existe bien
        """
        Affiche la matrice de corrélation sous forme de heatmap avec Seaborn et Matplotlib.
        """
        if self.corr is not None:
            plt.figure(figsize=(8, 8))
            sns.heatmap(self.corr, annot=True, cmap='RdBu', center=0, linewidths=0.5, fmt=".2f")
            plt.title("Matrice de corrélation")
            plt.xticks(rotation=45)
            plt.yticks(rotation=0)
            plt.show()
        else:
            print("Correlation not calculated. Please calculate correlation first.")

# Utilisation de la classe
if __name__ == "__main__":
    file_path = r'C:\Users\PC1\Desktop\MYPROJECT\data\sales_data.csv'

    analysis = DataAnalysis(file_path)

    analysis.load_data()
    analysis.preprocess_data()
    analysis.calculate_correlation()
    analysis.plot_correlation()  # Vérifiez que cette ligne correspond bien à la méthode définie
