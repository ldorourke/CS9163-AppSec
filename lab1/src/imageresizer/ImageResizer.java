import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
/* Nikhil Padhye nsp307
   Lucas O'Rourke lor215
   This program takes an image and creates a 1024 x 1024 resized square image
   For this example i will be resizing a picture of the NYC skyline to a 
   square called squareNYC. 
*/

public class ImageResizer
{
	/*
		base: Path of original image
		square: PAth of square image
		side: length of side of square image

		This method uses File, BufferedImage, Graphics2D and ImageIO
		to create a new image and copy and save the existing image into the 
		new created square image.
	*/
	public void saveSquare(String base, String square, int side) throws IOException
	{
		File imgFile = new File(base);//Open file
		BufferedImage img = ImageIO.read(imgFile); //Create BufferredImage object of image going to be resized

		BufferedImage sqrImg = new BufferedImage(side,side,img.getType());//Create the square image object of square length sidexside
		Graphics2D fillSqrImg = sqrImg.createGraphics(); //To be able to copy img into sqrImg we use Graphics2D API
		fillSqrImg.drawImage(img, 0, 0, side,side, null);//Draws img into sqrImg
		ImageIO.write(sqrImg,square.substring(square.lastIndexOf(".")+1),new File(square));//Creates the new imageFile
	}
	public static void main(String [] args)
	{
		String pic = "../data/new-york-city-night-and-day-photo-l.jpg";//Path of currentFile
		String squarePic = "../data/squareNYC.jpg";//Path of newFile
		int sideLength = 1024; //Size of square 
		ImageResizer ir = new ImageResizer();
		try
		{
			ir.saveSquare(pic, squarePic, sideLength);
		}catch (IOException e)
		{
			System.out.println("Error File Not Found");
		}
		return ;	
	}
}