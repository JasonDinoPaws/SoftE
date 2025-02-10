# Introduction
This program will take any card that we an image size of `480X680` and will crop it to only show the top part. Then it will try to read it using tesseract and saves it toa failed called `outfile.txt`. This can be done in 2 ways, but both of theme use the library's `cv2` and `os`.

# How it works
First we use python's built-in function called `open()` to open a file called `outfile.txt` and sets it to a variable called file. Now we loop through the folder that contains all of the images we want to read by using `os.listdir()` to create a list of all the files in that directory.

## Opening and modifying the image
To start it uses cv2 to first open the image as an array and crops it to only show the top. But sometimes color can mess up tesseract and so it will also create another array that is the gray scale of the same image.


## Getting the text from the image
Then this is where the 2 methods differ from each other, that is because you can either use `pytesseract` or `os.system()`.

### Pytesseract
Pytesseract will only reads an image if it's open using the libary `Pillows`. But at the current moment our image is a array and not a image file. But Pillows has a function called `Image.fromarray()` that will create a Pillow image if we give it both our color and gray arrays. Another thing that differs with pytesseract is we can use a fucntion called `image_to_string` that will return a string when it is called so we can set it to a variable called text.

### os.system()
`os.system()` allows us to run commands as if they were being ran by the command line. The way the tesseract works from the cli is `tesseract [img path] [outfile name]`. But we run into 2 issue, the first one being that the image is currently an array in memory, but cv2 has a function called `imwrite()` which will create a image file when you give it the array, name of the file, and the file type. The second issue that it will create a file instead of returnning a string. But if we use the `open()` function we used to create the `outfile.txt` we can just use it on the files that tesseract will create. And so we just keep on reading and saving it to a variable called text.

## Saving
Now that both the gray and the color images have been read. How do we save it? First off the reason why we have 2 images in the first place is that color images can fail to be read by ai because of stuff like color blending. 

So first we check if the color image was able to be read and if it can we save it to the outfile. But if it wasn't able to get anything from the color then we check if the gray got anything. If both fail we just say that it wasn't able to get anyhting from the file and save that.

and finally we close the the outfile and remove anything file that was created from using `os.system()` method.

# In what ways could this technology be misused, and how can safeguards be implemented?
One way this technology can be misused is by capturing peoples license plates inorder to figure out all infromation about someone for extorsion. Another way would be to capture specific things like someones SSN, credit, or debit card information. Some safeguards that could be implemented could be like it doesn't reconize numbers or using a multitude of diffrent fonts that can cause the ai to get confused, but methods can be overcome with time. So adding safegaurds for this to not be misused is possible but they would need to be maintined preferably the font one.

# Sources
Cv2: litterly the code it self
https://docs.python.org/3/library/os.html
https://github.com/h/pytesseract
https://manpages.ubuntu.com/manpages/xenial/man1/tesseract.1.html