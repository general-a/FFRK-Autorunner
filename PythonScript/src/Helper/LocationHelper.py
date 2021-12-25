import cv2

class LocationHelper:
    
    @staticmethod
    def makeLocation(imagePath, locations) -> None:
        image = cv2.imread(imagePath)
        for pt in locations:  # Switch collumns and rows
            print(pt)
            cv2.rectangle(image, pt, (pt[0] + 3, pt[1] + 3), (0, 0, 255), 2)

        cv2.imwrite('result.png', image)