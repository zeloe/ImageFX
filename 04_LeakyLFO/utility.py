
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from datetime import datetime





def magphase_plot(t_sig : np.ndarray,plot_label : str, fftSize = 512,onlyPositive = False):
    """
    Computes the Discrete Fourier Transform (DFT) of the input signal 
    and generates magnitude and phase plots.

    Args:
        t_sig (np.ndarray): 
            The input time-domain signal as a NumPy array.
        
        plot_label (string) :   
            Label of plot
        
        fftSize (int, optional): 
            The number of points used for the DFT computation. 
            Defaults to 512.
        
       

        onlyPositive (bool, optional): 
            If True, the plot will display only the positive frequency components.
            If False, both positive and negative frequency components are shown.
            Defaults to False.
    
    Returns:
        None: This function generates and displays the plots but does not return a value.

    Example:
        >>> import numpy as np
        >>> t_sig = np.sin(2 * np.pi * 5 * np.linspace(0, 1, 128))
        >>> magphase_plot(t_sig,mySine, fftSize=256, onlyPositive=True)
    """


    # Zero-pad the signal to match fftSize
    padded_sig = np.pad(t_sig, (0, max(0, fftSize - len(t_sig))), mode='constant', constant_values=0)

    # Compute the FFT
    fft_result = np.fft.fft(padded_sig, n=fftSize)
    
    # Get the magnitude and phase
    magnitude = np.abs(fft_result)
    phase = np.angle(fft_result)
   
    # Frequency axis setup
    if onlyPositive:
        magnitude = magnitude[:fftSize // 2]
        phase = phase[:fftSize // 2]
        freq_axis = np.linspace(0,.5, fftSize // 2)
    else:
        freq_axis = np.linspace(-.5, .5, fftSize)
        temp = np.zeros_like(magnitude)
        temp[fftSize // 2:fftSize] = magnitude[:fftSize // 2]
        temp[:fftSize // 2] = magnitude[fftSize // 2:fftSize]
        magnitude = temp
        temp2 = np.zeros_like(phase)
        temp2[fftSize // 2:fftSize] = phase[:fftSize // 2]
        temp2[:fftSize // 2] = phase[fftSize // 2:fftSize]
        phase = temp2

       

    # Example usage
    fig, ax = plt.subplots(2, figsize=(8, 6))  # Adjust figsize for overall plot size
    fig.suptitle(str(plot_label))
    ax[0].set_title('Magnitude')
    ax[0].plot(freq_axis, magnitude)
    
    ax[1].set_title('Phase')
    ax[1].plot(freq_axis, phase, color='r')
    


    
    # Adjust spacing between subplots
    plt.subplots_adjust(hspace=0.5)  # Increase vertical spacing
   
    plt.show()
    
    
