# DICOM and NIFTI

In this section, we're going to look at two really great Python libraries for 
interacting with neuroimaging file formats
[`pydicom`](https://pydicom.github.io/) 
and
[`nibabel`](https://nipy.org/nibabel/).

!!! tip "Use a virtual environment"
    To have full control over installing the packages described within this 
    section, consider using virtual environment demonstrated
    [here](/virtualenv/#virtual-environments).

## dicom

DICOM is a very popular file format (and transmission protocol) used within 
the medical imaging community. Certainly one of the more popular packages for 
reading and writing DICOM files in Python is
[`pydicom`](https://pydicom.github.io/pydicom/stable/index.html).

### installation

To install `pydicom` use `pip`

```bash
pip install pydicom
```

You'll also want to install `numpy` to access more advanced functionality

```bash
pip install numpy
```

After you've installed `pydicom`, you can import it

```python
import pydicom
```

### read

To read a DICOM file into variable named `ds`, use `pydicom.dcmread()`

```python
ds = pydicom.dcmread('file.dcm')
```

!!! note "Lazy loading"
    The `pydicom.dcmread()` function will only read the DICOM file headers 
    until you attempt to access the pixel data. This design pattern can 
    save time and resources.

#### headers

DICOM headers are traditionally identified by `group` and `element` pairs. Some 
common DICOM headers are

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

You can access these DICOM headers by indexing into the `ds` object using a 
tuple of `( group, element )`. To access the Patient Name for example, you 
would use

```python
element = ds[( '0010', '0010' )]
```

In the above example, the returned value (`element`) will be an instance of 
`pydicom.dataelem.DataElement`. To access the actual _value_ of the header, 
you want to access the `value` property of the data element

```python
patientname = element.value
```

#### pixel data

To read the DICOM image pixel data as a series of bytes, you can access the 
`PixelData` property on the `ds` object

```python
pixels = ds.PixelData
```

To receive the pixel data as a more useful NumPy array, you would use the 
`pixel_array` property

```python
pixels = ds.pixel_array
```

## nifti

For reading NIFTI files, I would highly recommend using the 
[`nibabel`](https://nipy.org/nibabel/)
package.

### installing 

To install `nibabel`, use `pip`

```bash
pip install nibabel
```

After you've installed `nibabel`, you can import it

```python
import nibabel
```

### read

To read a NIFTI file, use `nibabel.load()`

```python
ds = nibabel.load('file.nii.gz')
```

#### headers 

The NIFTI file headers are stored in a `header` property on the `ds` object 
shown above. Since the `header` property is `dict`-like, you can use a `for` 
loop to iterate over all the header names and values

```python
formatter = 'header = {}, value = {}'

for header,value in ds.header.items():
    a = formatter.format(header, value)
    print(a)
```

#### pixel data

The NIFTI pixel data can be accessed using the `.get_fdata()` method which 
will return the data as a NumPy array

```python
pixels = ds.get_fdata()
```

!!! tip "Memory efficiency"
    The `ds.get_fdata()` method has many features for handling large images 
    efficiently. For more details, read the official documentation
    [here](https://nipy.org/nibabel/images_and_memory.html#use-the-array-proxy-instead-of-get-fdata).

