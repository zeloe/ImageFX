# Rolling Feedback
<p align="center">
<img src="Renders/image.png" width=250 height=250>
</p >
## Feedback

When you feed any output back to the input you get feedback. 

### Feedback on audio data

In world of audio this can create a lot of different effects. \
To keep this processing stable feedback factor, the factor that you scale your data with \
should be < 1 and bigger > -1. If your feedback amount is too big then your processing might becomes instable and you  end up blowing up your speakers or even your ears. 
<p align="center">
<img src="Desc_images/desc_feedback.png" width=250 height=250>
</p >

### Feedback on image data
When using feedback processing on images you actually don't hear results you only \
see them. So you basically can use bigger factors but in most cases it will end up in \
a black or a white image. 
<p align="center">
<img src="Desc_images/desc_feedback_2.png" width=250 height=250>
</p >


This is an example on how it can look:

<p align="center">
<img src="Renders/feedback.png" width=250 height=250>
</p >

## Rolling

Numpy has a interesting function called [np.roll](https://numpy.org/doc/stable/reference/generated/numpy.roll.html). By "rolling" a section of an image you get: 

<p align="center">
<img src="Renders/rolling.png" width=250 height=250>
</p >

## Rolling Feedback
Putting these two processing methods togheter you can create a "rolling feedback":

<p> <center><b> with negative feedback coefficient</b></center> </p>
<p align="center">
<img src="Renders/rolling_feedback.gif" width=250 height=250>
</p >
