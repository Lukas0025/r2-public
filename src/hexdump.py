def hexdump(src, length=16, sep='.', lines_num=None):
  FILTER = ''.join([(len(repr(chr(x))) == 3) and chr(x) or sep for x in range(256)])
  lines = []
  count = 0
  for c in range(0, len(src), length):
    chars = src[c:c+length]
    hexstr = ' '.join(["%02x" % ord(x) for x in chars]) if type(chars) is str else ' '.join(['{:02x}'.format(x) for x in chars])
    if len(hexstr) > 24:
      hexstr = "%s %s" % (hexstr[:24], hexstr[24:])
    printable = ''.join(["%s" % ((ord(x) <= 127 and FILTER[ord(x)]) or sep) for x in chars]) if type(chars) is str else ''.join(['{}'.format((x <= 127 and FILTER[x]) or sep) for x in chars])
    lines.append("<tr><td>%08x</td><td>%-*s</td><td>%s</td></tr>" % (c, length*3, hexstr, printable))
    
    count += 1
    if (lines_num is not None) and (count >= lines_num):
        lines.append("<tr><td>Rows deleted. Rows limit is %s</td></tr>" % (lines_num))
        break

  return '\n'.join(lines)