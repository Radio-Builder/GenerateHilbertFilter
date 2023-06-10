import numpy as np
from scipy.signal import firwin, hilbert, freqz
import matplotlib.pyplot as plt

# Specify the filter specifications
order = 161                     # Filter order (adjust as needed)
bandwidth = 2500                 # Bandwidth in Hz
sample_rate = 44100              # Sample rate in Hz

# Calculate the desired cutoff frequency
cutoff_freq = bandwidth / (sample_rate / 2)

# Design the lowpass FIR filter
taps_lowpass = firwin(order + 1, cutoff_freq, window='hamming')

# Apply the Hilbert transform to the lowpass filter coefficients
taps_hilbert = hilbert(taps_lowpass)

# Adjust the filter coefficients for a +45 degree phase shift
taps_adjusted = taps_hilbert * np.exp((+1j) * np.pi / 4)

# Create the final Hilbert bandpass filter taps
taps_hilbert_bandpass = taps_adjusted.real

# Save the filter coefficients to a text file
with open('filter_coefficients_plus45.txt', 'w') as file:
    file.write("float filter_plus45[]{")
    file.write(", ".join([str(coeff) for coeff in taps_hilbert_bandpass]))
    file.write("};")

# Adjust the filter coefficients for a +45 degree phase shift
taps_adjusted = taps_hilbert * np.exp((-1j) * np.pi / 4)

# Create the final Hilbert bandpass filter taps
taps_hilbert_bandpass = taps_adjusted.real

# Save the filter coefficients to a text file
with open('filter_coefficients_minus_45.txt', 'w') as file:
    file.write("float filter_minus45[]{")
    file.write(", ".join([str(coeff) for coeff in taps_hilbert_bandpass]))
    file.write("};")

# Compute the frequency response of the Hilbert bandpass filter
w, h = freqz(taps_hilbert_bandpass)

# Convert the angular frequency to Hz
f = (w / np.pi) * (sample_rate / 2)

# Plot the frequency response of the Hilbert bandpass filter in dB
plt.figure()
plt.plot(f, 20 * np.log10(np.abs(h)))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Hilbert Bandpass Filter Frequency Response')
plt.xlim(0, 5000)  # Limit the x-axis up to 5000 Hz
plt.grid(True)
plt.show()
