def jsontext(data):
    '''

    This function gets a json file and converts it to html test.
    '''

    data_dict = dict(data)
    text = []

    for key in data_dict.keys():
        if data_dict[key] != None:
            if 'http' in data_dict[key]:
                text.append('<br>'+key+': '+'<a href='+data_dict[key]+'>'+data_dict[key]+'</a>')
            else:
                text.append('<br>'+key+': '+data_dict[key])
        else:
            text.append('<br>'+key+': Not given')

    fulltext = ''.join(text)

    return fulltext
