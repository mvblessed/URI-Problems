def sqrt(n):
    return n**0.5

def dot(v,w):
    x,y = v
    X,Y = w
    return x*X + y*Y

def length(v):
    x,y = v
    return sqrt(x*x + y*y)

def vector(b,e):
    x,y = b
    X,Y = e
    return (X-x, Y-y)

def unit(v):
    x,y = v
    mag = length(v)
    return (x/mag, y/mag)

def distance(p0,p1):
    return length(vector(p0,p1))

def scale(v,sc):
    x,y = v
    return (x * sc, y * sc)

def add(v,w):
    x,y = v
    X,Y = w
    return (x+X, y+Y)

def pnt2seg(pnt, start, end):
    seg_vec = vector(start, end)
    pnt_vec = vector(start, pnt)
    seg_len = length(seg_vec)
    seg_unitvec = unit(seg_vec)
    pnt_vec_scaled = scale(pnt_vec, 1.0/seg_len)
    t = dot(seg_unitvec, pnt_vec_scaled)    
    if t < 0.0:
        t = 0.0
    elif t > 1.0:
        t = 1.0
    nearest = scale(seg_vec, t)
    dist = distance(nearest, pnt_vec)
    nearest = add(nearest, start)
    return (dist, nearest)

T = int(input())
for _ in range(T):

    magic_dic = {'fire': [200, 20, 30, 50], 'water': [300, 10, 25, 40], 'earth': [400, 25, 55, 70], 'air': [100, 18, 38, 60]}
    
    dimen = []
    magic = []
    dimen = list(map(int, input().split(' ')))
    magic = list(input().split(' '))

    x1, y1, x2, y2 = [dimen[2], dimen[3], dimen[2]+dimen[0], dimen[3]]
    x3, y3, x4, y4 = [dimen[2]+dimen[0], dimen[3]+dimen[1], dimen[2], dimen[3]+dimen[1]]
    
    level, cx, cy = map(int, [magic[1], magic[2], magic[3]])
    r = magic_dic[magic[0]][level]
    
    if (x1 <= cx <= x2) and (y1 <= cy <= y3):
        print(magic_dic[magic[0]][0])
    else:
        if (dimen[0] == 0) and (dimen[1] == 0):
            menor_dist_P = distance((cx, cy), (x1, y1))
        elif dimen[0] == 0:
            SegAD_P = pnt2seg((cx, cy), (x1, y1), (x4, y4))
            menor_dist_P = SegAD_P[0]
        elif dimen[1] == 0:
            SegAB_P = pnt2seg((cx, cy), (x1, y1), (x2, y2))
            menor_dist_P = SegAD_P[1]
        else:
            SegAB_P = pnt2seg((cx, cy), (x1, y1), (x2, y2))
            SegBC_P = pnt2seg((cx, cy), (x2, y2), (x3, y3))
            SegCD_P = pnt2seg((cx, cy), (x3, y3), (x4, y4))
            SegAD_P = pnt2seg((cx, cy), (x1, y1), (x4, y4))
            menor_dist_P = min(SegAB_P[0], SegBC_P[0], SegCD_P[0], SegAD_P[0])
    
        if menor_dist_P <= r:
            print(magic_dic[magic[0]][0])
        else:
            print('0')
