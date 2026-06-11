import faiss
import numpy as np

# Create an index — IVF (Inverted File) for fast ANN search
dimension = 1536
quantizer = faiss.IndexFlatL2(dimension)
#index = faiss.IndexIVFFlat(quantizer, dimension, 100)  # 100 clusters - required for 1000000 vectors, but causes memory issues on smaller machines
index = faiss.IndexIVFFlat(quantizer, dimension, 4)  # 4 clusters - suitable for 400 vectors

# Add 1 million patent vectors
# vectors = np.random.rand(1000000, 1536).astype('float32') #numpy._core._exceptions._ArrayMemoryError: Unable to allocate 11.4 GiB for an array with shape (1000000, 1536) and data type float64
vectors = np.random.rand(400, 1536).astype('float32')
print("############vectors shape :", vectors.shape)
print("############vectors size :", vectors.size)

print("############vectors data :", vectors)

############################

vectors2 = np.random.rand(3, 7).astype('float32')
print("############vectors shape :", vectors2.shape)
print("############vectors size :", vectors2.size)

print("############vectors data :", vectors2)
#############################

index.train(vectors)
index.add(vectors)

# Search — finds top 5 nearest neighbours in milliseconds
query = np.random.rand(1, 1536).astype('float32')

print("query query query :", query)
print("query query query shape :", query.shape)
print("query query query size :", query.size)

distances, indices = index.search(query, k=5)
# Returns the 5 most similar patent vectors, nearly instantly


# Add these lines to see the output:
print("Distances (similarity scores):", distances)
print("Indices (IDs of the 5 nearest neighbors):", indices)