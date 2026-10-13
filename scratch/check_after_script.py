with open('scratch/liveserver_header.html', 'rb') as f:
    data = f.read()

# find where script ends
script_end = data.find(b'</script>')
print('script_end:', script_end)
print('Content after script:')
print(data[script_end+9:script_end+500])
print('Total length:', len(data))
