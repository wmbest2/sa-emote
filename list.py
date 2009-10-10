import smilies
print ""
print "<table>"
for name, src in smilies.smilies:
  print "\t<tr>"
  print "\t\t<td>%s</td>" % name
  print "\t\t<td><img src=\"assets/emotes/%s\"></td>" % src
  print "\t</tr>"
print "</table>"