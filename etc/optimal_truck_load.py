def optimal_truck_load(arr, truck):
    # arr = [1,2,3,4,5]
    # Truck  = 3
    sub = sum(arr) % truck
    print(f'sub : {sub}') 
    if sub == 0:
        return 0

    if len(arr) < truck:
        return arr[-1]

    # 수정해오겠습니다. 
    else:
        return arr[-1] - sum(arr[:sub])




arr = [1,2,3,4,5]
truck = 10

print(optimal_truck_load(arr, truck))
    