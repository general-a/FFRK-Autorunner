import cv2
import numpy as np
from numpy.linalg import norm

class ElementFinder:

    @staticmethod
    def findOneElement(screenFile: str, elementFile:str):
        result = []
        screen = cv2.imread(screenFile)
        element = cv2.imread(elementFile)
        centery, centerx = tuple(int(i/2) for i in element.shape[:-1])

        res = cv2.matchTemplate(screen, element, cv2.TM_CCOEFF_NORMED)
        match = np.max(res)
        loc = np.where(res == match)
        for pt in zip(*loc[::-1]):
            result.append((pt[0] + centerx, pt[1] + centery))
        
        return result[0]

        
    @staticmethod
    def findMultipleElements(screenFile: str, elementFile:str, threshold = .98):
        uniques = []        
        def removeDuplicates():

            def deleteClosePoints():
                removeItems = []
                for i, d in enumerate(distances):
                    if d < 100:
                        removeItems.append(i)
                while len(removeItems) > 0:
                    p = points.pop(removeItems.pop())
                        
                        

            while len(points) > 0:
                point = np.array(points.pop(0))
                distances = list(map(lambda x: norm(np.array(x)-point), points))
                deleteClosePoints()
                uniques.append(tuple(point))
            
        
        screen = cv2.imread(screenFile)
        element = cv2.imread(elementFile)
        centery, centerx = tuple(int(i/2) for i in element.shape[:-1])
        
        res = cv2.matchTemplate(screen, element, cv2.TM_CCORR_NORMED)
        loc = np.where(res >= threshold)
        points = []
        for pt in zip(*loc[::-1]):  # Switch collumns and rows
            points.append((pt[0] + centerx, pt[1] + centery))
        
        removeDuplicates()
        return tuple(uniques)
    
    def matchPercentage(screenFile: str, elementFile:str):
        screen = cv2.imread(screenFile)
        element = cv2.imread(elementFile)
        res = cv2.matchTemplate(screen, element, cv2.TM_CCOEFF_NORMED)
        result = np.max(res)
        return result
        

if __name__ == '__main__':
    res = ElementFinder.matchPercentage('etc/images/leave.png', 'etc/images/elements/fatigue.png')
    print(res)