class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:                                    #y       #x
        if image[sr][sc] == color: 
            return image 

        originalColor = image[sr][sc]
        image[sr][sc] = color

        # Check if coordinates are valid 
        left = (sc - 1) if (sc - 1) >= 0 else -1
        right = (sc + 1) if (sc + 1) < len(image[0]) else -1
        up = (sr - 1) if (sr - 1) >= 0 else -1 
        down = (sr + 1) if (sr + 1) < len(image) else -1


        # For all valid coordinates of correct color, recursively run floodFill 
        if (left >= 0) and (image[sr][left] == originalColor): 
            image = self.floodFill(image, sr, left, color)    
        
        if (right >= 0) and (image[sr][right] == originalColor): 
            image = self.floodFill(image, sr, right, color)  
        
        if (down >= 0) and (image[down][sc] == originalColor):  
            image = self.floodFill(image, down, sc, color)  
        
        if (up >= 0) and (image[up][sc] == originalColor):  
            image = self.floodFill(image, up, sc, color)  

        return image