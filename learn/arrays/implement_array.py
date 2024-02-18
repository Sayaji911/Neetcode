from array import ArrayType
from ctypes import LittleEndianStructure
from re import A
from typing import Union


class Array:
    """ This class implements and handles operations on an arrat
    """
    def __init__(self) -> None:
        """
        This is a constructor function to initialize an arrray.
        """
        self.length : int = 0
        self.data : dict = {}
        
    def push(self, element: Union[int, str]) -> None:
        """
        This function is used to push an element into the array
        
        Args:
            element : Union[int, str]

        Returns:
            None
        """
        if not element:
            raise Exception
        self.data[self.length] = element
        self.length += 1
        return None


    def show(self,) -> dict:
        """
        This method displays all the elements inside the array
        
        Args:
            None

        Returns
            self.data : dict

        Returns:
            dict: _description_
        """
        return self.data
    
    def pop(self,) -> None:
        """
        This method pops the last element from the array
        
        Args:
            None

        Returns:
            None
        """
        del self.data[self.length - 1]
        return None

    def delete(self,index: int) -> None:
        """
        This method deletes the element at the specified index

        Args:
            index : int
        
        Return:
            None
        """
        del self.data[index]
        for i in range(index , self.length - 1):
            self.data[i] = self.data[i+1]
         
        del self.data[self.length - 1] 

alphabets = Array()
alphabets.push("apple")
alphabets.push("banana")
alphabets.push("mango")
print(alphabets.show())
print("Now popping")
alphabets.pop()
print(alphabets.show())
alphabets.delete(index=1)
print(alphabets.show())



"""
[a,b,d]
 1 2 3 4
 
 
 ///
 from the index provided to till the length all the index must be decremented by 1
 
""" 