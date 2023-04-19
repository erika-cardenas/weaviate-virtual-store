import weaviate

client = weaviate.Client("http://localhost:8080")


schema = {
    "classes": [
        {
            "class": "Product",
            "description": "Images of different products",
            "moduleConfig": {
                "img2vec-neural": {
                    "imageFields": [
                        "image"
                    ]
                }
            },
            "vectorIndexType": "hnsw", 
            "vectorizer": "img2vec-neural", 
            "properties": [
                {
                    "name": "image",
                    "dataType": ["blob"],
                    "description": "image",
                },
                {
                "dataType": ["text"],
                "moduleConfig": {
                    "multi2vec-clip": {
                        "skip": True,
                        "vectorizePropertyName": False
                    }
                },
                "name": "imagePath",
                "description": "A product.",
            },
            ]
        }
    ]
}

client.schema.create(schema)