N = int(input())
pay=0
zarr=[N]
while max(zarr)>=2:
    z = zarr[0]
    zarr.remove(z)
    while z >= 2:
        pay+=z
        if z%2 == 0:
            z = z//2
            if z == 2:
                pay+=2
            elif z > 2:
                zarr.append(z)
        else:
            if z==5:
                pay += 2
            elif z > 5:
                zarr.append((z-1)//2)
            z = (z+1)//2
    if len(zarr) == 0:
        break
print(pay)