l = ['$3', '$5', '$5']


my_html_list = ''
for word in l:
    #my_list += '<li>' + word + '</li>'
    #my_list += '<li>{}</li>'.format(word)
    my_html_list += f'<li>{word}</li>'

my_html = f'''
<h1>Testing101</h1>
<p>A quick test to see if this HTML would work</p>
<p> any changes? <p>
<ol>
    <li>Water</li>
    <li>Chicken</li>
    <li>Apples</li>
</ol>

<ul>
    {my_html_list}
</ul>
'''
f = open('render.html', 'w')
f.write(my_html)
f.close()
