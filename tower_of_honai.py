def tower_of_honai(n,sou,axu,dis):
    if(n==1):
        print(f"moving disk 1 from {sou} to {dis}")
        return
    tower_of_honai(n-1,sou,dis,axu)
    print(f"moving disk {n} from {sou} to {dis}")
    tower_of_honai(n-1,axu,sou,dis)

tower_of_honai(4,"A","B","C")