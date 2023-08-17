import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import face_recognition
import numpy as np


os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
# assign the folder name to a variable

# TODO: change the path
KNOWN_FACES_DIR = '../eg3d/eg3d/test_known'


print('Loading known faces...')

def pose_change(names):
    final_list = []
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            final_list.append(round((j-i)*0.4, 2))
    return final_list


# create empty dictionary and list pairs for storing encoded faces and their names
known_faces = {}
known_encoded_faces = []
known_numbered_names = {}
known_names = []
face_tilt = {}

count = 0
# iterate over the images in the directory
for index in range(len(os.listdir(KNOWN_FACES_DIR))):
    name = os.listdir(KNOWN_FACES_DIR)[index]
    # load each image strip
    image_strip = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}')
    # split the loaded image into 5 distinct arrays
    image = np.split(image_strip, 5, axis=1)

    # iterate over the arrays in image and encode each face
    for i in range(len(image)):
        count += 1
        encoding = face_recognition.face_encodings(image[i])
        if len(encoding) > 0:
            image_encoding = encoding[0]
            known_names.append(f"image{index}.{i}")
            known_encoded_faces.append(image_encoding)

        else:
            continue

    # create a temporary variable to store the face encodings and respective names
    temp_encoded_faces = known_encoded_faces.copy()
    temp_known_names = known_names.copy()
    angle = pose_change(temp_known_names)

    # add the encodings and names to the dictionaries once every iteration
    known_faces[index] = temp_encoded_faces
    known_numbered_names[index] = temp_known_names
    face_tilt[index] = angle

    # clear the variables at the end of the loop
    known_encoded_faces.clear()
    known_names.clear()

print('Generating results...')



results = []
final_results = []
# loop through the keys in known_faces dictionary
for j in range(len(known_faces.keys())):
    # assign the values of each key to a variable
    known_values = known_faces[j]
    known_poses = face_tilt[j]



    # make 5 choose 3 comparisons on each strip and append the face distance to result
    for k in range(len(known_values)):
        for l in range(k + 1, len(known_values)):
            face_distance = face_recognition.face_distance([known_values[k]], known_values[l])
            results.append(face_distance)
            new_results = results.copy()


    for index in range(len(new_results)):
        if len(known_poses) > 0:
            final_results.append((known_poses[index], new_results[index]))

    results.clear()


#print(final_results)
#print(f"Total images analyzed: {count}")
#print(f"Total comparisons computed: {len(final_results)}")

x = []
y = []
for item in final_results:
    x.append(item[0])
    y.append(item[1])

plt.scatter(x, y, c = "green", linewidths=1)
plt.xlabel("Pose Difference")
plt.ylabel("Face Distance")

plt.savefig('Graph.png')
print("Graph image saved.")

