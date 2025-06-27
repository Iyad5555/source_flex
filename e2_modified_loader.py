import marshal
import zlib

with open('e2_modified.encrypted', 'rb') as f:
    compressed_code = f.read()

marshalled_code = zlib.decompress(compressed_code)
compiled_code = marshal.loads(marshalled_code)
exec(compiled_code)
