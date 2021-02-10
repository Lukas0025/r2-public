# from: https://github.com/ActiveState/code/blob/master/recipes/Python/142812_Hex_dumper/recipe-142812.py
# Under MIT

def hexdump(src, length=16, bytes_lim=None):
  sep = '.'
  FILTER = ''.join([(len(repr(chr(x))) == 3) and chr(x) or sep for x in range(256)])
  lines = []
  for c in range(0, len(src), length):
    chars = src[c:c+length]
    hexstr = ''.join(["<td>%02x</td>" % ord(x) for x in chars]) if type(chars) is str else ''.join(['<td>{:02x}</td>'.format(x) for x in chars])
    printable = ''.join(["%s" % ((ord(x) <= 127 and FILTER[ord(x)]) or sep) for x in chars]) if type(chars) is str else ''.join(['{}'.format((x <= 127 and FILTER[x]) or sep) for x in chars])
    lines.append("<tr><td>%08x</td>%-*s<td>%s</td></tr>" % (c, length*3, hexstr, printable))
    
    if not(bytes_lim is None) and (bytes_lim < c):
      lines.append("<tr><td colspan='18'>Bytes removed - over limit %s</td></tr>\n" % (bytes_lim))
      break
  return '\n'.join(lines)
