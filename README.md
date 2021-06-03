<h1>Pasting threat objects onto X-Ray backgrounds</h1>
<h2>File1 : Rotating and resizing</h2>
<ol>
    <li>Read all the images using opencv.imread()</li>
    <li><b>resize function</b>:Takes an image and a constant(width of final image) and calculates dimension of final image without losing aspect ratio and returns resized image.</li>
    <li><b>rotate function</b>:Takes an image and rotates it by 45 degrees and fills the residual area with White color.</li>
    <li>Finally all images are passed into functions to get final image.</li>
    <li>These images are stored as jpgs using cv2.imwrite()</li>
</ol>
<h2>File2 : Masking and pasting</h2>
<ol>
    <li>Read backgrounds(XRays) and outputs from first file</li>
    <li>Reshape outputs to match backgrounds.(used array cropping)</li>
    <li><b>Isolate function</b>: Takes in an image as uses cv2.inRange() function to remove white background (lower range(240,240,240) to upper range(255,255,255) on the threat images and get pixel values where object is present(mask).Then it uses mask to make all the pixel values without object 0. Finally returning mask and isolated image </li>
    <li>Now, using the mask returned we change pixels of background image to 0 (pixels where there is object)</li>
    <li>Now, we multiple an alpha value to the isolated image to reduce intensity</li>
    <li>adding isolated image and background image to obtain final image</li>
    <li>Save the image using cv2.imwrite()</li>
</ol>