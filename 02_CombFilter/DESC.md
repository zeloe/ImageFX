# Comb Filter

## Delay

As soon as data gets on a virtual device it is somehow finite. \
Like having a list containing your data. As soon as it has some index or a duration \
you can read that data after a duration. 

## Delay on audio data

Audio data is sampled. That means you take data and you "map" it to a finite set of points. These points \
are called samples. As soon as you have a finite set of points basically you can say I want to read them after some "time" or samples.
A delay can work like this. I insert "0" at beginning of my samples. Amount of these "0" are amount of delay. 
Then I just start reading the list from beginning.

## Combfilters on audio data

Combfilters in signal processing are used for many audio effects. You delay your audio by a time in samples and based on your processing you delay input (feedforward) or output (feedback) or both and add them back to your input. This creates a intresting [spectrum](https://en.wikipedia.org/wiki/Comb_filter).


## Delay on image data

Image data is also sampled. A video contains frames. These frames are images. There is a framerate in each video that are frames a second. 
<p align="center">
<img src="Renders/circles.gif" width=250 height=250>
</p >

You can delay a image by one frame. 
<p align="center">
<img src="Renders/delay_image.gif" width=250 height=250>
</p >

## Combfilter on image data

So basically you can apply a combfilter to an image. It is more you treat image data as audio data. Image data is a 2d matrix with different planes. Reshape it to a 1d matrix. Like that image data has same structure as audio data.  Define a delay in samples (audio samples) and apply following processing: 
<p align="center">
<img src="Desc_images/signal_flow.png" width=250 height=250>
</p >

Color white is displayed on screen when all pixel values are [255](https://medium.com/@patelharsh7458/normalization-in-image-preprocessing-scaling-pixel-values-by-1-255-111b2fa496d4#:~:text=Pixel%20Value%20Range%3A,black%2C%20and%20255%20represents%20white.). By delaying your "image audio data" you change these values and they aren't all 255 anymore. At the end you reshape your image data in shape of audio data back to a 2d matrix and you can following get results:

<p align="center">
<img src="Renders/image_comb_filter.gif" width=250 height=250>
</p >



<p align="center">
<img src="Renders/image_rolling_comb_filter_v2.gif" width=250 height=250>
</p >


## References
[Feedback Comb Filters](https://ccrma.stanford.edu/~jos/waveguide/Feedback_Comb_Filters.html)
[Feedforward Comb Filters](https://ccrma.stanford.edu/~jos/waveguide/Feedforward_Comb_Filters.html)
