lmxb
keys:


def buf2PIL(txn, key, type='RGB'):
    imgbuf = txn.get(key)
    buf = six.BytesIO()
    buf.write(imgbuf)
    buf.seek(0)
    im = Image.open(buf).convert(type)
    return im


nSamples = int(txn.get(b'num-samples'))

label_key = b'label-%09d' % index
word = str(txn.get(label_key).decode())

img_HR_key = b'image_hr-%09d' % index
img_lr_key = b'image_lr-%09d' % index
img_HR = buf2PIL(txn, img_HR_key, 'RGB')
img_lr = buf2PIL(txn, img_lr_key, 'RGB')