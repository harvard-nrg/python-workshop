# DICOM and NIFTI
In this section, we're going to look at two Python libraries for 
interacting with common neuroimaging file formats
[`pydicom`](https://pydicom.github.io/) 
and
[`nibabel`](https://nipy.org/nibabel/).

!!! tip "Use a virtual environment"
    To have full control over installing the packages described in this 
    section, it may be beneficial to create a
    [virtual environment](/python-workshop/virtualenv).

## DICOM
DICOM is perhaps the most popular imaging file format used within the medical 
imaging community. One of the more popular Python packages for reading and 
writing DICOM files is
[`pydicom`](https://pydicom.github.io/pydicom/stable/index.html).

!!! note ""
    You'll need to install `numpy` for more advanced functionality.

```bash
pip install pydicom numpy
```

### reading a file
To read a DICOM file into variable named `ds`, use 
[`dcmread()`](https://pydicom.github.io/pydicom/dev/reference/generated/pydicom.filereader.dcmread.html)

```python
import pydicom

ds = pydicom.dcmread('file.dcm')
```

!!! note "Lazy loading"
    By default, `pydicom.dcmread()` will only read the DICOM file headers 
    until you attempt to access the pixel data. This design choice saves 
    time and resources.

#### reading headers
DICOM headers are identified by their `group` and `element`. Some example 
headers include

| Name                | group | element | 
|---------------------|-------|---------|
| Study Date          | 0008  | 0020    |
| Study Time          | 0008  | 0030    |
| Patient Name        | 0010  | 0010    |
| Series Number       | 0020  | 0011    |
| Accession Number    | 0008  | 0050    |
| Instance ID         | 0020  | 0013    |
| Study UID           | 0020  | 000D    |
| Series UID          | 0020  | 000E    |

You can access these headers by indexing into the `ds` object using a tuple of 
`(group, element)`. To access the Patient Name for example, you would use

```python
element = ds[('0010', '0010')]
```

In the example above, the returned `element` will be an instance of 
`pydicom.dataelem.DataElement`. Use the `value` property to access the value 
of this element

```python
patientname = element.value
```

#### reading pixel data
To read the raw DICOM pixel data as a series of bytes, you can access the 
`PixelData` property

```python
pixels = ds.PixelData
```

To receive the pixel data in a more useful `numpy` array format, use the 
`pixel_array` property

```python
pixels = ds.pixel_array
```

#### visualizing pixel data
Let's take a look at
[matplotlib](https://matplotlib.org/)
to visualize DICOM pixel data. First, you need to install `matplotlib`

```bash
pip install matplotlib
```

Now, import `matplotlib.pyplot` and use
[`imshow()`](https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.imshow.html)
to render the pixel data (a NumPy `ndarray`) as an image

```python
import matplotlib.pyplot as plt

plt.imshow(ds.pixel_array)

plt.show()
```

## NIfTI
For reading and writing NIFTI files, use the 
[`nibabel`](https://nipy.org/nibabel/)
package

```bash
pip install nibabel
```

### reading a file
To read a NIFTI file, use `nibabel.load()`

```python
import nibabel

ds = nibabel.load('file.nii.gz')
```

#### reading headers 
The NIFTI file headers are stored in a `header` property on the `ds` object. 
Since the `header` property behaves like a dictionary, you can use a `for` 
loop to iterate over all the headers

```python
formatter = f'header = {header} value = {value}'

for header,value in ds.header.items():
    print(formatter)
```

#### reading pixel data
The `.get_fdata()` method will return the NIfTI pixel data as a NumPy array

```python
pixels = ds.get_fdata()
```

!!! tip "Memory efficiency"
    The `ds.get_fdata()` method has many excellent features for handling large 
    images efficiently. For more details, read the official documentation
    [here](https://nipy.org/nibabel/images_and_memory.html#use-the-array-proxy-instead-of-get-fdata).

#### visualizing pixel data
Let's take a look at
[matplotlib](https://matplotlib.org/)
to visualize NIfTI pixel data. First, you need to install `matplotlib`

```bash
pip install matplotlib
```

Now, import `matplotlib.pyplot` and use
[`imshow()`](https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.imshow.html)
to render image `50` along the z-axis

```python
import matplotlib.pyplot as plt

fdata = ds.get_fdata()

plt.imshow(fdata[:,:,50])

plt.show()
```

