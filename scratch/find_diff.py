import urllib.request

with urllib.request.urlopen('http://127.0.0.1:5500/include/header.html') as resp:
    data = resp.read()

with open('scratch/liveserver_header.html', 'wb') as f:
    f.write(data)

with open('include/header.html', 'rb') as f:
    local_data = f.read()

print('Live server len:', len(data))
print('Local len:', len(local_data))

# Find where they diverge
diff_at = -1
min_len = min(len(data), len(local_data))
for i in range(min_len):
    if data[i] != local_data[i]:
        diff_at = i
        break

print('Diverge at byte index:', diff_at)
if diff_at != -1:
    print('Local around diff:')
    print(local_data[max(0, diff_at-50):diff_at+100])
    print('Live server around diff:')
    print(data[max(0, diff_at-50):diff_at+100])
