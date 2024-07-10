import cv2
import numpy as np

class CosmicTracerService:
    def __init__(self, template_path):
        self.template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        self.sift = cv2.SIFT_create()

        # Compute keypoints and descriptors for the template image
        self.keypoints_template, self.descriptors_template = self.sift.detectAndCompute(self.template, None)

    def identify_constellation(self, image_bytes):
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)

        if img is None or self.template is None:
            return {"error": "Failed to load images"}

        # Compute keypoints and descriptors for the input image
        keypoints_image, descriptors_image = self.sift.detectAndCompute(img, None)

        # Match descriptors between template and input image
        matcher = cv2.BFMatcher()
        matches = matcher.knnMatch(self.descriptors_template, descriptors_image, k=2)

        # Apply ratio test to select good matches
        good_matches = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                good_matches.append(m)

        # Calculate confidence score based on the ratio of good matches to total keypoints in the template image
        confidence = len(good_matches) / len(self.keypoints_template)

        # Determine result based on confidence score
        if confidence >= 1.0:  # Adjust this threshold as needed
            return {"result": "Yes, this is a known constellation", "confidence": confidence}
        else:
            return {"result": "No, this is not a known constellation", "confidence": confidence}
