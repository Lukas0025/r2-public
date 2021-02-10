# from: https://github.com/ActiveState/code/blob/master/recipes/Python/142812_Hex_dumper/recipe-142812.py
# Under MIT

FILTER=''.join([(len(repr(chr(x)))==3) and chr(x) or '.' for x in range(256)])

def hexdump(src, length=16, bytes_lim=None):
    N=0; result=''
    while src:
       s,src = src[:length],src[length:]
       hexa = ' '.join(["<td>%02X</td>"% x for x in s])
       s = s.translate(FILTER)
       result += "<tr><td>%04X</td>%-*s<td>%s</td></tr>\n" % (N, length*3, hexa, s)
       N+=length
       
       if not(bytes_lim is None) and byte_lim < N:
           result += "<tr>Bytes removed - over limit %s</tr>\n" % (N)
           break

    return result
