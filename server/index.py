from deepface import DeepFace
import os
import json


def detect_face(imgpath: str, dbpath: str) -> dict:
    """
    Detects the face in the given image and returns the result.
    """

    images = []
    if imgpath == "" or dbpath == "":
        return {"error": "No Path Provided!"}

    stored_images = os.listdir(dbpath)


    for i in range(2, len(stored_images)):

        img2 = dbpath + "/" + stored_images[i]
        result = DeepFace.verify(
            img1_path=imgpath,
            img2_path=img2,
            enforce_detection=False,
            model_name="Facenet",
            distance_metric="euclidean",
        )
        if result["verified"]:
          
            images.append(img2)

    
    x = {
        "status": "success",
        "message": "Face Detected!",
        "images": images,
    }
    print(json.dumps(x))


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python index.py <image_path> <database_path>")
        sys.exit(1)

    path1 = str(sys.argv[1])
    path2 = str(sys.argv[2])
    result = detect_face(path1, path2)

    
