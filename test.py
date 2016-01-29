import time, sys

tests = [
    "insert into a (a, b, c) values ('a', 'b', 'c');",
    "delete from b where a = 1 and b = 2 and c = 3;",
    "update c set a = 1, b = 2, c = 3 where a = 2;",
    "alter table something add someid int(10) after someotherid;",
    "INSERT INTO tbl_name (a,b,c) VALUES(1,2,3,4,5,6,7,8,9);",
    "select * from sometable;"
]

x = 0
while True:
    x+=1
    print tests[x % len(tests)]
    sys.stdout.flush()
    print