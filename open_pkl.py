import pickle

# Load the content of the .pkl file
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)

# Print the content
print(data)