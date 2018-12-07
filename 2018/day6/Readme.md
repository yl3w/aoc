Note to future self - I'm not very happy with this algorithm. I couldn't come up with a better one. I describe it below,
if you are looking at the code and come up with a better way, I want to know.

#### algorithm

(a) Given a list of point creating a bounding box.

```
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
```

```
A.......
........
.......C
..D.....
....E...
B.......
........
........
.......F
```

(b) eliminate any points on the edge as having infinite areas. A,B,C & F are eliminated.

(c) For each non eliminated point, determine `owner` of the edge point on it's axis.
- For vertex D - check (0,3) (3, 7), (2, 0), (2, 8)

(d) eliminate the vertex if it owns the edge point.

(c) for each remaining point, compute the grid owner ship.
