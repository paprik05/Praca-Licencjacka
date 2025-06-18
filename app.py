from flask import Flask, request, jsonify, render_template
import os

from problems.prob1 import prob1
from problems.prob2 import prob2
from problems.prob3 import prob3
from problems.prob4 import prob4
from problems.prob5 import prob5
from problems.prob6 import prob6
from problems.prob7 import prob7
from problems.prob8 import prob8
from problems.prob9 import prob9
from problems.prob10 import prob10
from problems.prob11 import prob11
from problems.prob12 import prob12
from problems.prob13 import prob13
from problems.prob14 import prob14
from problems.prob15 import prob15
from problems.prob16 import prob16
from problems.prob17 import prob17
from problems.prob18 import prob18
from problems.prob19 import prob19
from problems.prob20 import prob20
from problems.prob21 import prob21
from problems.prob22 import prob22
from problems.prob23 import prob23
from problems.prob24 import prob24
from problems.prob25 import prob25
from problems.prob26 import prob26
from problems.prob27 import prob27
from problems.prob28 import prob28
from problems.prob29 import prob29
from problems.prob30 import prob30
from problems.prob31 import prob31
from problems.prob32 import prob32
from problems.prob33 import prob33
from problems.prob34 import prob34
from problems.prob35 import prob35
from problems.prob36 import prob36
from problems.prob37 import prob37
from problems.prob38a import prob38a
from problems.prob38b import prob38b
from problems.prob38c import prob38c
from problems.prob39 import prob39
from problems.prob40 import prob40
from problems.prob41 import prob41
from problems.prob42 import prob42
from problems.prob43 import prob43
from problems.prob44 import prob44
from problems.prob45 import prob45
from problems.prob46 import prob46
from problems.prob47 import prob47
from problems.prob48 import prob48
from problems.prob49 import prob49
from problems.prob50 import prob50
from problems.prob51 import prob51
from problems.prob51a import prob51a
from problems.prob52 import prob52
from problems.prob53 import prob53
from problems.prob54 import prob54
from problems.prob55 import prob55
from problems.prob56 import prob56
from problems.prob57 import prob57
from problems.prob58 import prob58
from problems.prob59 import prob59
from problems.prob60 import prob60
from problems.prob61 import prob61
from problems.prob62 import prob62
from problems.prob63 import prob63
from problems.prob64 import prob64
from problems.prob66 import prob66
from problems.prob67 import prob67
from problems.prob68 import prob68
from problems.prob69 import prob69
from problems.prob70 import prob70
from problems.prob71 import prob71
from problems.prob72 import prob72
from problems.prob74 import prob74
from problems.prob75 import prob75
from problems.prob76 import prob76
from problems.prob77 import prob77
from problems.prob78 import prob78
from problems.prob79 import prob79
from problems.prob80 import prob80
from problems.prob81 import prob81
from problems.prob82 import prob82
from problems.prob83 import prob83
from problems.prob84 import prob84
from problems.prob85 import prob85
from problems.prob86 import prob86
from problems.prob87 import prob87
from problems.prob88 import prob88
from problems.prob90 import prob90
from problems.prob91 import prob91
from problems.prob92 import prob92
from problems.prob93 import prob93
from problems.prob94 import prob94
from problems.prob95 import prob95
from problems.prob96 import prob96
from problems.prob97 import prob97
from problems.prob98 import prob98
from problems.prob99 import prob99
from problems.prob100 import prob100
from problems.prob105 import prob105
from problems.prob111 import prob111
from problems.prob116 import prob116
from problems.prob120 import prob120
from problems.prob121 import prob121
from problems.prob122 import prob122
from problems.prob123 import prob123
from problems.prob124 import prob124
from problems.prob125 import prob125
from problems.prob131 import prob131
from problems.prob135 import prob135
from problems.prob137 import prob137
from problems.prob139 import prob139

problem_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 381, 382, 383, 39, 40,
               41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 511, 52, 53, 54, 55, 56, 57, 58, 59,
               60, 61, 62, 63, 64, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91,
               92, 93, 94, 95, 96, 97, 98, 99, 100, 105, 111, 116, 120, 121, 122, 123, 124, 125, 131, 135, 137, 139,
                ]

problem_data = {
    1: {
        "description": r"1.Find all positive integers \(n\) such that \( n^2 + 1 \) is divisible by \( n + 1 \)",
        "inputs": [
            {
                "id": "inputNumber1",
                "label": "Podaj maksymalną wartość n do sprawdzenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER01:1", "url": "http://mizar.uwb.edu.pl/version/current/html/number01.html#T1"}
        ]
    },
    2: {
        "description": r"2.Find all integers \( x \neq 3 \) such that \( x - 3 | x^3 - 3\)",
        "inputs": [
            {
                "id": "inputMin",
                "label": "Minimalna sprawdzana wartość x:",
                "type": "number",
            },
            {
                "id": "inputMax",
                "label": "Maksymalna sprawdzana wartość x:",
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER01:5", "url": "http://mizar.uwb.edu.pl/version/current/html/number01.html#T5"}
        ]
    },
    3: {
        "description": r"3.Prove that there exists infinitely many positive integers \(n\) such that \(4n^2+1\) is divisible both by \(5\) and \(13\)",
        "inputs": [
            {
                "id": "inputNumber3",
                "label": "Podaj liczbę rozwiązań do wyświetlenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER01:6", "url": "http://mizar.uwb.edu.pl/version/current/html/number01.html#T6"}
        ]
    },
    4: {
        "description": r"4.Prove that for positive integer \(n\) we have \(169|3^{3n+3}-26n-27\)",
        "inputs": [
            {
                "id": "inputNumber4",
                "label": "Podaj maksymalną wartość n do sprawdzenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER01:7", "url": "http://mizar.uwb.edu.pl/version/current/html/number01.html#T7"}
        ]
    },
    5: {
        "description": r"5.Prove that \(19|2^{2^{6k+2}}+3\) for \(k = 0, 1, 2, ...\)",
        "inputs": [
            {
                "id": "inputNumber5",
                "label": "Podaj maksymalną liczbę k do sprawdzenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER01:8", "url": "http://mizar.uwb.edu.pl/version/current/html/number01.html#T8"}
        ]
    },
    6: {
        "description": r"6.Prove the theorem, due to Kraitchik, asserting that \(13|2^70+3^70\)",
        "inputs": [],
        "links": [
            {"title": "NUMBER01:9", "url": "http://mizar.uwb.edu.pl/version/current/html/number01.html#T9"}
        ]
    },
    7: {
        "description": r"7.Prove that \(11*31*61|20^15-1\)",
        "inputs": [],
        "links": [
            {"title": "NUMBER01:10", "url": "http://mizar.uwb.edu.pl/version/current/html/number01.html#T10"}
        ]
    },
    8: {
        "description": "8. Prove that for a positive integer \\(m\\) and \\(a > 1\\), we have \n\\[\n\\gcd\\left(\\frac{a^m - 1}{a - 1},\\, a - 1\\right) = \\gcd(a - 1, m).\n\\]\n",
        "inputs": [
            {
                "id": "inputNumberM8",
                "label": "Podaj liczbę m:",
                "min": 1,
                "type": "number",
            },
            {
                "id": "inputNumberA8",
                "label": "Podaj liczbę a:",
                "min": 2,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER01:13", "url": "http://mizar.uwb.edu.pl/version/current/html/number01.html#T13"}
        ]
    },
    9: {
        "description": r"9.Prove that for every positive integer \(n\) the number \(3(1^5+2^5+...+n^5)\) is divisible by \(1^3+2^3+...+n^3\).",
        "inputs": [
            {
                "id": "inputNumber9",
                "label": "Podaj liczbę n",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER01:14", "url": "http://mizar.uwb.edu.pl/version/current/html/number01.html#T14"}
        ]
    },
    10: {
        "description": r"10.Find all integers \(n>1\) such that \(1^n+2^n+...+(n-1)^n\) is divisible by \(n\).",
        "inputs": [
            {
                "id": "inputNumber10",
                "label": "Podaj maksymalną liczbę n do sprawdzenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER01:18", "url": "http://mizar.uwb.edu.pl/version/current/html/number01.html#T18"}
        ]
    },
    11: {
        "description": r"11.For positive integer \(n\), find which of the two numbers \(a_n=2^{2n+1}-2^{n+1}+1\) and \(b_n=2^{2n+1}+2^{n+1}+1\) is divisible by \(5\) and which is not.",
        "inputs": [
            {
                "id": "inputNumber11",
                "label": "Podaj liczbę n:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER03:39", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T39"},
            {"title": "NUMBER03:40", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T40"},
            {"title": "NUMBER03:41", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T41"}
        ]
    },
    12: {
        "description": r"12.Prove that for every positive integer \(n\) there exists a positive integer \(x\) such that each of the terms of the infinite sequence \(x+1,x^x+1,x^{x^x}+1,...\) is divisible by \(n\)",
        "inputs": [
            {
                "id": "inputNumber12",
                "label": "Podaj wartość x:",
                "min": 1,
                "type": "number",
            },
            {
                "id": "inputNumberMax12",
                "label": "Podaj maksymalną wartość n do sprawdzenia::",
                "min": 1,
                "type": "number",
            },
            {
                "id": "inputNumberIt12",
                "label": "Podaj maksymalną liczbę iteracji:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER05:2", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T2"}
        ]
    },
    13: {
        "description": r"13.Prove that there exists infinitely many positive integers \(n\) such that for every even \(x\) none of the terms of the sequence \(x^x+1,x^{x^x}+1,x^{x^{x^x}}+1,...\) is divisible by \(n\).",
        "inputs": [
            {
                "id": "inputNumber13",
                "label": "Podaj wartość x:",
                "min": 2,
                "type": "number",
            },
            {
                "id": "inputNumberMax13",
                "label": "Podaj maksymalną wartość n do sprawdzenia:",
                "min": 1,
                "type": "number",
            },
            {
                "id": "inputNumberIt13",
                "label": "Podaj maksymalną liczbę iteracji:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER05:5", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T5"}
        ]
    },
    14: {
        "description": r"14.Prove that for positive integer \(n\) we have \(n^2|(n+1)^n-1.\)",
        "inputs": [
            {
                "id": "inputNumber14",
                "label": "Podaj liczbę n:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER02:42", "url": "http://mizar.uwb.edu.pl/version/current/html/number02.html#T42"}
        ]
    },
    15: {
        "description": r"15.Prove that for positive integer \(n\) we have \((2^n-1)^2|2^{(2^{n}-1)n}-1.\)",
        "inputs": [
            {
                "id": "inputNumber15",
                "label": "Podaj liczbę n:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER02:43", "url": "http://mizar.uwb.edu.pl/version/current/html/number02.html#T43"}
        ]
    },
    16: {
        "description": r"16.Prove that there exist infinitely many positive integers \(n\) such that \(n|2^n+1\); find all such prime numbers",
        "inputs": [
            {
                "id": "inputNumber16",
                "label": "Podaj liczbę n spełniających warunek do wyświetlenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER03:42", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T42"},
            {"title": "NUMBER03:43", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T43"}
        ]
    },
    17: {
        "description": r"17.Prove that for every positive integer \(a>1\) there exist infinitely many positive integers \(n\) such that \(n|a^n+1\).",
        "inputs": [
            {
                "id": "inputNumberA17",
                "label": "Podaj liczbę a:",
                "min": 1,
                "type": "number",
            },
            {
                "id": "inputNumberRange17",
                "label": "Podaj liczbę n spełniających warunek do wyświetlenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER04:25", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T25"}
        ]
    },
    18: {
        "description": r"18.Prove that there exist infinitely many positive integers \(n\) such that \(n|2^n+2\).",
        "inputs": [
            {
                "id": "inputNumber18",
                "label": "Podaj liczbę n spełniających warunek do wyświetlenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER04:26", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T26"}
        ]
    },
    19: {
        "description": r"19.Find all positive integers \(a\) for which \(a^{10}+1\) is divisible by \(10\).",
        "inputs": [
            {
                "id": "inputNumber19",
                "label": "Podaj maksymalną wartość a do sprawdzenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER03:44", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T44"}
        ]
    },
    20: {
        "description": r"20.Prove that there are no integers \(n>1\) for which \(n|2^n-1\).",
        "inputs": [
            {
                "id": "inputNumber20",
                "label": "Podaj maksymalną wartość n do sprawdzenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER03:46", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T46"}
        ]
    },
    21: {
        "description": r"21.Find all odd \(n\) such that \(n|3^n+1\).",
        "inputs": [
            {
                "id": "inputNumber21",
                "label": "Podaj maksymalną wartość n do sprawdzenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER03:47", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T47"}
        ]
    },

    22: {
        "description": r"22.Find all positive integers \(n\) for which \(3|n2^n+1\).",
        "inputs": [
            {
                "id": "inputNumber22",
                "label": "Podaj maksymalną wartość n do sprawdzenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER03:48", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T48"}
        ]
    },

    23: {
        "description": r"23.Prove that for every odd prime \(p\) there exist infinitely many positive integers \(n\) such that \(p|n2^n+1\).",
        "inputs": [
            {
                "id": "inputNumberPRange23",
                "label": "Podaj wartość p:",
                "min": 1,
                "type": "number",
            },
            {
                "id": "inputNumberNRange23",
                "label": "Podaj liczbę n spełniających warunek do wyświetlenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER03:51", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T51"}
        ]
    },

    24: {
        "description": r"24.Prove that for every positive integer \(n\) there exist positive integers \(x>n\) and \(y\) such that \(x^x|y^y\) but \(x \neq y\).",
        "inputs": [
            {
                "id": "inputNumber24",
                "label": "Podaj wartość n:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER03:52", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T52"}
        ]
    },

    25: {
        "description": r"25.Prove that for odd \(n\) we have \(n|2^{2!}-1\).",
        "inputs": [
            {
                "id": "inputNumber25",
                "label": "Podaj maksymalną wartość n do sprawdzenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER08:48", "url": "http://mizar.uwb.edu.pl/version/current/html/number08.html#T48"}
        ]
    },

    26: {
        "description": r"26.Prove that the infinite sequence \(2^n-3 (n=2,3,4,...)\) contains infinitely many terms divisible by \(5\) and infinitely many terms divisible by 13, but contains no term divisible by \(5*13\).",
        "inputs": [
            {
                "id": "inputNumber26",
                "label": "Podaj maksymalną wartość n do sprawdzenia:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER04:27", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T27"},
            {"title": "NUMBER04:28", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T28"},
            {"title": "NUMBER04:31", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T31"}
        ]
    },

    27: {
        "description": r"27.Find two least composite numbers \(n\) such that \(n|2^n-2\) and \(n|3^n-3\).",
        "inputs": [],
        "links": [
            {"title": "NUMBER04:33", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T33"},
            {"title": "NUMBER04:35", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T35"},
            {"title": "NUMBER04:40", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T40"},
            {"title": "NUMBER04:48", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T48"},
            {"title": "NUMBER04:54", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T54"},
            {"title": "NUMBER04:60", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T60"},
            {"title": "NUMBER04:61", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T61"}
        ]
    },

    28: {
        "description": r"28.Find the least positive integer \(n\) such that \(n|2^n-2\) but \(n\not|\;3^n-3\).",
        "inputs": [],
        "links": [
            {"title": "NUMBER04:36", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T36"},
            {"title": "NUMBER04:50", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T50"},
            {"title": "NUMBER04:63", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T63"}
        ]
    },

    29: {
        "description": r"29.Find the least integer \(n\) such that \(n\not|\;2^n-2\) but \(n|3^n-3\).",
        "inputs": [],
        "links": [
            {"title": "NUMBER02:44", "url": "http://mizar.uwb.edu.pl/version/current/html/number02.html#T44"}
        ]
    },

    30: {
        "description": r"30.For every positive integer \(a\), find a composite number \(n\) such that \(n|a^n-a\).",
        "inputs": [
            {
                "id": "inputNumber30",
                "label": "Podaj liczbę a:",
                "min": 1,
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER02:45", "url": "http://mizar.uwb.edu.pl/version/current/html/number02.html#T45"}
        ]
    },

    31: {
        "description": r"31.Prove that if for some integers \(a,b,c\) we have \(9|a^3+b^3+c^3\), then at least one of the numbers \(a,b,c\) is divisible by \(3\).",
        "inputs": [
            {
                "id": "inputNumberA31",
                "label": "Podaj liczbę a:",
                "type": "number",
                "min": 1
            },
            {
                "id": "inputNumberB31",
                "label": "Podaj liczbę b:",
                "type": "number",
                "min": 1
            },
            {
                "id": "inputNumberC31",
                "label": "Podaj liczbę c:",
                "type": "number",
                "min": 1
            }
        ],
        "links": [
            {"title": "NUMBER05:7", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T7"}
        ]
    },
    32: {
        "description": r"32.Prove that if for positive integers \(a_k(k=1,2,3,4,5)\) we have \(9|a_1^3+a_2^3+a_3^3+a_4^3+a_5^3\), then \(3|a_1a_2a_3a_4a_5\).",
        "inputs": [
            {
                "id": "inputNumber32",
                "label": "Podaj maksymalną wartość liczby a do sprawdzenia:",
                "min": 1,
                "type": "number"
            }
        ],
        "links": [
            {"title": "NUMBER05:11", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T11"}
        ]
    },
    33: {
        "description": r"33.Prove that if \(x,y,z\) are positive integers such that \((x,y) = 1\) and \(x^2+y^2=z^4\), then \(7|xy\);show that the condition \((x,y)=1\) is necessary.",
        "inputs": [
            {
                "id": "inputNumberX33",
                "label": "Podaj liczbę x:",
                "type": "number",
                "min": 1
            },
            {
                "id": "inputNumberY33",
                "label": "Podaj liczbę y:",
                "type": "number",
                "min": 1
            },
            {
                "id": "inputNumberZ33",
                "label": "Podaj liczbę z:",
                "type": "number",
                "min": 1
            }
        ],
        "links": [
            {"title": "NUMBER05:13", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T13"},
            {"title": "NUMBER05:14", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T14"}
        ]
    },
    34: {
        "description": r"34.Prove that if for integers \(a\) and \(b\) we have \(7|a^2+b^2\), then \(7|a\) and \(7|b\).",
        "inputs": [
            {
                "id": "inputNumberA34",
                "label": "Podaj liczbę a:",
                "type": "number",
            },
            {
                "id": "inputNumberB34",
                "label": "Podaj liczbę b:",
                "type": "number",
            }
        ],
        "links": [
            {"title": "NUMBER02:52", "url": "http://mizar.uwb.edu.pl/version/current/html/number02.html#T52"}
        ]
    },
    35: {
        "description": r"35.Prove that there exist infinitely many pairs of positive integers \(x,y\) such that \(x(x+1)|y(y+1)\), \(x\not|y\), \(x+1\not|y\), \(x\not|y+1\), \(x+1\not|y+1\), and find the least such pair.",
        "inputs": [
            {
                "id": "inputNumber35",
                "label": "Podaj liczbę par spełniających warunek do wyświetlenia:",
                "min": 1,
                "type": "number"
            }
        ],
        "links": [
            {"title": "NUMBER05:16", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T16"},
            {"title": "NUMBER05:17", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T17"},
            {"title": "NUMBER05:18", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T18"}
        ]
    },
    36: {
        "description": r"36.For every positive integer \(s\leq25\) and for \(s = 100\), find the least positive integer \(n\) with the sum of digits (in decimal system) equal to \(s\), which is divisible by \(s\).",
        "inputs": [
            {
                "id": "inputNumber36",
                "label": "Podaj wartość s do sprawdzenia:",
                "min": 1,
                "type": "number"
            }
        ]
    },
    37: {
        "description": r"37. Prove that for every positive integer \(s\) there exists a positive integer \(n\) with the sum of digists (in decimal system) equal to \(s\) which is divisible by \(s\).",
        "inputs": [
            {
                "id": "inputNumber37",
                "label": "Podaj wartość s do sprawdzenia:",
                "min": 1,
                "type": "number"
            }
        ]
    },
    381: {
        "description": r"38a.Prove that every positive integer has at least as many divisors of the form \(4k+1\) as divisors of the form \(4k+3\).",
        "inputs": [
            {
                "id": "inputNumber381",
                "label": "Podaj liczbę do sprawdzenia:",
                "min": 1,
                "type": "number"
            }
        ],
        "links": [
            {"title": "NUMBER15:22", "url": "http://mizar.uwb.edu.pl/version/current/html/number15.html#T22"}
        ]
    },
    382: {
        "description": r"38b.Prove that there exist infinitely many positive integers which have as many divisors of the form \(4k+1\) as divisors of the form \(4k+3\).",
        "inputs": [
            {
                "id": "inputNumber382",
                "label": "Podaj ilośc liczb spełniąjących dany warunek do wyświetlenia:",
                "min": 1,
                "type": "number"
            }
        ],
        "links": [
            {"title": "NUMBER15:33", "url": "http://mizar.uwb.edu.pl/version/current/html/number15.html#T33"}
        ]
    },
    383: {
        "description": r"38c.Prove that there exist infinitely many positive integers which have more divisors of the form \(4k+1\) than divisors of the form \(4k+3\).",
        "inputs": [
            {
                "id": "inputNumber383",
                "label": "Podaj ilośc liczb spełniąjących dany warunek do wyświetlenia:",
                "min": 1,
                "type": "number"
            }
        ],
        "links": [
            {"title": "NUMBER15:40", "url": "http://mizar.uwb.edu.pl/version/current/html/number15.html#T40"}
        ]
    },
    39: {
        "description": r"39.Prove that if \(a,b,c\) are any integers, and \(n\) is an integer \(>3\), then there exists an integer \(k\) such that none of the numbers \(k+a,k+b,k+c\) is divisible by \(n\).",
        "inputs": [
            {
                "id": "inputNumberA39",
                "label": "Podaj liczbę a:",
                "type": "number",
                "min": 1
            },
            {
                "id": "inputNumberB39",
                "label": "Podaj liczbę b:",
                "type": "number",
                "min": 1
            },
            {
                "id": "inputNumberC39",
                "label": "Podaj liczbę c:",
                "type": "number",
                "min": 1
            },
            {
                "id": "inputNumberN39",
                "label": "Podaj liczbę n:",
                "min": 3,
                "type": "number"
            }
        ],
        "links": [
            {"title": "NUMBER03:53", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T53"}
        ]
    },
    40: {
        "description": r"40.Prove that for \(F_n = 2^{2^n}+1\) we have \(F_n|2^{F_n}-2 (n=1,2,...)\).",
        "inputs": [
            {
                "id": "inputNumber40",
                "label": "Podaj liczbę n do sprawdzenia:",
                "min": 1,
                "type": "number"
            }
        ],
        "links": [
            {"title": "NUMBER05:20", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T20"}
        ]
    },
    41: {
        "description": r"41.Prove that for every integer \(k\) the numbers \(2k+1\) and \(9k+4\) are relatively prime, and for numbers \(2k-1\) and \(9k+4\) find their greatest common divisor as a function of \(a\).",
        "inputs": [
            {
                "id": "inputNumber41",
                "label": "Podaj liczbę k:",
                "min": 1,
                "type": "number"
            }
        ],
        "links": [
            {"title": "NUMBER13:6", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T6"},
            {"title": "NUMBER13:7", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T7"}
        ]
    },
    42: {
        "description": r"42.Prove that there exists an increasing infinite sequence of triangular numbers (i.e. numbers of the form \(t_n=\frac{1}{2}n(n + 1),\;n=1,2,...)\) such that every two of them are relatively prime.",
        "inputs": [
            {
                "id": "inputNumber42",
                "label": "Podaj limit długośći sekwencji do wyświetlenia:",
                "min": 1,
                "type": "number"
            }
        ],
        "links": [
            {"title": "NUMBER12:10", "url": "http://mizar.uwb.edu.pl/version/current/html/number12.html#T10"}
        ]
    },
    43: {
        "description": r"43.Prove that there exists an increasing infinite sequence of tetrahedral numbers (i.e. numbers of the form \(T_n=\frac{1}{6}n(n + 1)(n + 2),\;n=1,2,...)\) such that every two of them are relatively prime.",
        "inputs": [
            {
                "id": "inputNumber43",
                "label": "Podaj limit długośći sekwencji do wyświetlenia:",
                "min": 1,
                "type": "number"
            }
        ],
        "links": [
            {"title": "NUMBER12:11", "url": "http://mizar.uwb.edu.pl/version/current/html/number12.html#T11"}
        ]
    },
    44: {
        "description": r"44.Prove that if \(a\) and \(b\) are different integers, then there exist infinitely many positive integers \(n\) such that \(a+n\) and \(b+n\) are relatively prime.",
        "inputs": [
            {
                "id": "inputNumberA44",
                "label": "Podaj liczbę a:",
                "min": 1,
                "type": "number"
            },
            {
                "id": "inputNumberB44",
                "label": "Podaj liczbę b:",
                "min": 1,
                "type": "number"
            },
            {
                "id": "inputNumberLimit44",
                "label": "Podaj ilość liczb n spełniających dany warunek do wyświetlenia:",
                "min": 1,
                "type": "number"
            }
        ],
        "links": [
            {"title": "NUMBER03:54", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T54"}
        ]
    },
    45: {
        "description": r"45.Prove that if \(a,b,c\) are three different integers, then there exist infinitely many positive integers \(n\) such that \(a+n,b+n,c+n\) are pairwise relatively prime.",
        "inputs": [
            {"id": "inputNumberA45", "label": "Podaj liczbę a:", "type": "number", "min": 1},
            {"id": "inputNumberB45", "label": "Podaj liczbę b:", "type": "number", "min": 1},
            {"id": "inputNumberC45", "label": "Podaj liczbę c:", "type": "number", "min": 1},
            {"id": "inputNumberN45", "label": "Podaj ilość liczb n spełniających dany warunek do wyświetlenia:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER14:46", "url": "http://mizar.uwb.edu.pl/version/current/html/number14.html#T46"}
        ]
    },
    46: {
        "description": r"46.Give an example of four different positive integers \(a,b,c,d\) such that there exists no positive integer \(n\) for which \(a+n,b+n,c+n,\) and \(d+n\) are pairwise relatively prime.",
        "inputs": [
            {"id": "inputNumberA46", "label": "Podaj liczbę a:", "type": "number", "min": 1},
            {"id": "inputNumberB46", "label": "Podaj liczbę b:", "type": "number", "min": 1},
            {"id": "inputNumberC46", "label": "Podaj liczbę c:", "type": "number", "min": 1},
            {"id": "inputNumberD46", "label": "Podaj liczbę d:", "type": "number", "min": 1},
            {"id": "inputNumberN46", "label": "Podaj maksymalną liczbę n do sprawdzenia:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER03:57", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T57"}
        ]
    },
    47: {
        "description": r"47.Prove that every integer \(>6\) can be represented as a sum of two integers \(>1\) which are relatively prime.",
        "inputs": [
            {"id": "inputNumber47", "label": "Podaj liczbę:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER05:22", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T22"}
        ]
    },
    48: {
        "description": r"48.Prove that every integer \(>17\) can be represented as a sum of three integers \(>1\) which are pairwise relatively prime, and show that \(17\) does not have this property.",
        "inputs": [
            {"id": "inputNumber48", "label": "Podaj liczbę:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER07:42", "url": "http://mizar.uwb.edu.pl/version/current/html/number07.html#T42"},
            {"title": "NUMBER07:43", "url": "http://mizar.uwb.edu.pl/version/current/html/number07.html#T43"}
]

    },
    49: {
        "description": r"49.Prove that for every positive integer \(m\) every even number \(2k\) can be represented as a difference of two positive integers relatively prime to \(m\).",
        "inputs": [
            {"id": "inputNumberM49", "label": "Podaj liczbę m:", "type": "number", "min": 1},
            {"id": "inputNumberE49", "label": "Podaj liczbę parzystą:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER14:54", "url": "http://mizar.uwb.edu.pl/version/current/html/number14.html#T54"},
            {"title": "NUMBER14:55", "url": "http://mizar.uwb.edu.pl/version/current/html/number14.html#T55"}
        ]
    },
    50: {
        "description": r"50.Prove that Fibonacci's sequence (defined by conditions \(u_1 = u_2 = 1, u_{n+2} = u_n+u_{n+1}, n=1,2,...\)) contains an infinite increasing sequence such that every two terms of this sequence are relatively prime.",
        "inputs": [
            {"id": "inputNumber50", "label": "Podaj maksymalną liczbę do sprawdzenia:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER06:17", "url": "http://mizar.uwb.edu.pl/version/current/html/number06.html#T17"}
        ]
    },
    51: {
        "description": r"51.Prove that \((n,2^{2^n}+1) = 1\) for \(n = 1,2,...\).",
        "inputs": [
            {"id": "inputNumber51", "label": "Podaj liczbę n:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER12:12", "url": "http://mizar.uwb.edu.pl/version/current/html/number12.html#T12"}
        ]

    },
    511: {
        "description": r"51a.Prove that there exist infinitely many positive integers \(n\) such that \((n,2^n-1)>1\), and find the least of them.",
        "inputs": [
            {"id": "inputNumber511", "label": "Podaj ilość liczb n spełniających dany warunek do wyświetlenia:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER12:15", "url": "http://mizar.uwb.edu.pl/version/current/html/number12.html#T15"}
        ]
    },
    52: {
        "description": r"52.Prove that there exist arbitrarily long arithmetic progressions formed of different positive integers such that every two terms of these progressions are relatively prime.",
        "inputs": [
            {"id": "inputNumber52", "label": "Podaj długość ciągu", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER06:22", "url": "http://mizar.uwb.edu.pl/version/current/html/number06.html#T22"}
        ]
    },
    53: {
        "description": r"53.Prove that for every positive integer \(k\) the set of all positive integers \(n\) whose number of positive integer divisiors is divisible by \(k\) contains an infinite arithmetic progression.",
        "inputs": [
            {"id": "inputNumberK53", "label": "Podaj liczbę k:", "type": "number", "min": 1},
            {"id": "inputNumberLen53", "label": "Podaj długośc progresji:", "type": "number", "min": 2},
            {"id": "inputNumberMax53", "label": "Podaj limit poszukiwań:", "type": "number", "min": 1}
        ]
    },
    54: {
        "description": r"54.Prove that there exist infinitely many triplets of positive integers \(x,y,z\) for which the numbers \(x(x+1),y(y+1),z(z+1)\) form an increasing arithmetic progression.",
        "inputs": [
            {"id": "inputNumber54", "label": "Podaj maksymalną liczbę x do sprawdzenia:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER06:24", "url": "http://mizar.uwb.edu.pl/version/current/html/number06.html#T24"}
        ]
    },
    55: {
        "description": r"55.Find all rectangular triangles with integer sides forming an arithmetic progression.",
        "inputs": [
            {"id": "inputNumber55", "label": "Maksymalna długośc najdłuższego boku trójkąta::", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER06:25", "url": "http://mizar.uwb.edu.pl/version/current/html/number06.html#T25"}
        ]

    },
    56: {
        "description": r"56.Find an increasing arithmetic progression with the least possible difference, formed of positive integers and containing no triangular number.",
        "inputs": [
            {"id": "inputNumber56", "label": "Podaj długość ciągu:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER06:34", "url": "http://mizar.uwb.edu.pl/version/current/html/number06.html#T34"}
        ]
    },
    57: {
        "description": r"57.Give a necessary and sufficient condition for an arithmetic progression \(ak+b(k=0,1,2,...)\) with positive integer \(a\) and \(b\) to contain infinitely many squares of integers.",
        "inputs": [
            {"id": "inputNumberA57", "label": "Podaj liczbę a:", "type": "number", "min": 1},
            {"id": "inputNumberB57", "label": "Podaj liczbę b:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER12:19", "url": "http://mizar.uwb.edu.pl/version/current/html/number12.html#T19"}
        ]
    },
    58: {
        "description": r"58.Prove that there exist arbitrarily long arithmetic progressions formed of different positive integers, whose terms are powers of positive integers with integer exponents \(>1\).",
        "inputs": [
            {"id": "inputNumber58", "label": "Podaj długość ciągu:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER15:51", "url": "http://mizar.uwb.edu.pl/version/current/html/number15.html#T51"}
        ]
    },
    59: {
        "description": r"59.Prove that there is no infinite arithmetic progression formed of different positive integers such that each term is a power of a positive integer with an integer exponent \(>1\).",
        "inputs": [
            {"id": "inputNumberStart59", "label": "Podaj limit przeszukiwania:", "type": "number", "min": 1},
            {"id": "inputNumberDiff59", "label": "Podaj róznicę między liczbami:", "type": "number", "min": 1},
            {"id": "inputNumberLen59", "label": "Podaj długość ciągu:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER12:22", "url": "http://mizar.uwb.edu.pl/version/current/html/number12.html#T22"}
        ]
    },
    60: {
        "description": r"60.Prove that there are no four consecutive positive integers such that each of them is a power of a positive integer with an integer exponent \(>1\).",
        "inputs": [
            {"id": "inputNumberStart60", "label": "Podaj początek zakresu:", "type": "number", "min": 1},
            {"id": "inputNumberEnd60", "label": "Podaj koniec zakresu:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER06:40", "url": "http://mizar.uwb.edu.pl/version/current/html/number06.html#T40"}
        ]
    },
    61: {
        "description": r"61.Prove by elementary means that each increasing arithmetic progression of positive integers contains an arbitrarily long sequence of consecutive terms which are composite numbers.",
        "inputs": [
            {"id": "inputNumberA61", "label": "Podaj liczbę a:", "type": "number", "min": 1},
            {"id": "inputNumberB61", "label": "Podaj liczbę b:", "type": "number", "min": 1},
            {"id": "inputNumberM61", "label": "Podaj liczbę m:", "type": "number", "min": 1}
        ]
    },
    62: {
        "description": r"62.Prove by elementary means that if \(a\) and \(b\) are relatively prime positive integers, then for every positive integer \(m\) the arithmetic progressions \(ak+b(k=0,1,2,...)\) contains infinitely many terms relatively prime to \(m\).",
        "inputs": [
            {"id": "inputNumberA62", "label": "Podaj liczbę a:", "type": "number", "min": 1},
            {"id": "inputNumberB62", "label": "Podaj liczbę b:", "type": "number", "min": 1},
            {"id": "inputNumberM62", "label": "Podaj liczbę m:", "type": "number", "min": 1},
            {"id": "inputNumberN62", "label": "Podaj liczbę wyrazów do wyświetlenia:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER09:17", "url": "http://mizar.uwb.edu.pl/version/current/html/number09.html#T17"}
        ]
    },
    63: {
        "description": r"63.Prove that for evey positive integer \(s\) every increasing arithmetic progression of positive integers contains terms with arbitrary first \(s\) digits (in decimal system).",
        "inputs": [
            {"id": "inputNumberA63", "label": "Podaj liczbę a:", "type": "number", "min": 1},
            {"id": "inputNumberB63", "label": "Podaj liczbę b:", "type": "number", "min": 1},
            {"id": "inputNumberPrefix63", "label": "Podaj prefix:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER16:4", "url": "http://mizar.uwb.edu.pl/version/current/html/number16.html#T4"}
        ]
    },
    64: {
        "description": r"64. Find all increasing arithmetic progressions formed of three terms of the Fibonacci sequence (see Problem 50), and prove that there are no increasing arithmetic progressions formed of four terms of this sequence.",
        "inputs": [
            {
                "id": "inputNumber64",
                "label": "Podaj koniec przeszukiwanego zakresu:",
                "min": 1,
                "type": "number"
            }
        ],
        "links": [
            {"title": "NUMBER06:41", "url": "http://mizar.uwb.edu.pl/version/current/html/number06.html#T41"}
        ]
    },
    66: {
        "description": r"66.Find a progression \(ak+b(k=0,1,2,...)\), with positive integers \(a\) and \(b\) such that \((a,b)=1\), which does not contain any term of Fibonacci sequence.",
        "inputs": [
            {"id": "inputNumber66", "label": "Podaj długość ciągu:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER16:15", "url": "http://mizar.uwb.edu.pl/version/current/html/number16.html#T15"}
        ]
    },
    67: {
        "description": r"67.Prove that the arithmetic progression \(ak+b(k=0,1,2,...)\) with positive integers \(a\) and \(b\) such that \((a,b)=1\) contains infinitely many terms pairwise relatively prime.",
        "inputs": [
            {"id": "inputNumberA67", "label": "Podaj liczbę a:", "type": "number", "min": 1},
            {"id": "inputNumberB67", "label": "Podaj liczbę b:", "type": "number", "min": 1},
            {"id": "inputNumberN67", "label": "Podaj liczbę wyrazów do wyświetlenia:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER16:5", "url": "http://mizar.uwb.edu.pl/version/current/html/number16.html#T5"}
        ]
    },
    68: {
        "description": r"68.Prove that in each arithmetic progression \(ak+b(k=0,1,2,...)\) with positive integers \(a\) and \(b\) there exist infinitely many terms with the same prime divisors.",
        "inputs": [
            {"id": "inputNumberA68", "label": "Podaj liczbę a:", "type": "number", "min": 1},
            {"id": "inputNumberB68", "label": "Podaj liczbę b:", "type": "number", "min": 1},
            {"id": "inputNumberN68", "label": "Podaj liczbę wyrazów:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER16:6", "url": "http://mizar.uwb.edu.pl/version/current/html/number16.html#T6"}
        ]
    },
    69: {
        "description": r"69.From the theorem of Lejeune-Dirichlet, asserting that each arithmetic progression \(ak+b\) \((k=0,1,2,...)\) with relatively prime positive integers \(a\) and \(b\) contains infinitely many primes, deduce that for every such progression and every positive integer \(s\) there exist infinitely any terms which are products of \(s\) distinct primes.",
        "inputs": [
            {"id": "inputNumberA69", "label": "Podaj liczbę a:", "type": "number", "min": 1},
            {"id": "inputNumberB69", "label": "Podaj liczbę b:", "type": "number", "min": 1},
            {"id": "inputNumberS69", "label": "Podaj liczbę s:", "type": "number", "min": 1},
            {"id": "inputNumberCount69", "label": "Podaj liczbę wyrazów:", "type": "number", "min": 1},
            {"id": "inputNumberLimit69", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 1}
        ]
    },
    70: {
        "description": r"70.Find all arithmetic progressions with difference 10 formed of more than two primes.",
        "inputs": [
            {"id": "inputNumberDiff70", "label": "Podaj rożninice między wyrazami:", "type": "number", "min": 1},
            {"id": "inputNumberLength70", "label": "Podaj długość ciągu:", "type": "number", "min": 1},
            {"id": "inputNumberLimit70", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 1},
        ],
        "links": [
            {"title": "NUMBER06:49", "url": "http://mizar.uwb.edu.pl/version/current/html/number06.html#T49"},
            {"title": "NUMBER06:50", "url": "http://mizar.uwb.edu.pl/version/current/html/number06.html#T50"}
        ]
    },
    71: {
        "description": r"71.Find all arithmetic progressions with difference 100 formed of more than two primes.",
        "inputs": [
            {"id": "inputNumberDiff71", "label": "Podaj rożninice między wyrazami:", "type": "number", "min": 1},
            {"id": "inputNumberLength71", "label": "Podaj długość ciągu:", "type": "number", "min": 1},
            {"id": "inputNumberLimit71", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 1},
        ],
        "links": [
            {"title": "NUMBER06:51", "url": "http://mizar.uwb.edu.pl/version/current/html/number06.html#T51"}
        ]
    },
    72: {
        "description": r"72. Find an increasing arithmetic progression with ten terms, formed of primes, with the least possible last term.",
        "inputs": [
            {"id": "inputNumberLength72", "label": "Podaj długość ciągu:", "type": "number", "min": 1},
            {"id": "inputNumberStart72", "label": "Podaj maksymalną liczbę startową przeszukiwań:", "type": "number", "min": 1},
            {"id": "inputNumberDiff72", "label": "Podaj maksymalną różnicę między wyrazami:", "type": "number", "min": 1},
        ],
        "links": [
            {"title": "NUMBER12:41", "url": "http://mizar.uwb.edu.pl/version/current/html/number12.html#T41"}
        ]
    },
    74: {
        "description": r"74.Prove that for every even \(n > 6\) there exist primes \(p\) and \(q\) such that \((n-p,n-q) = 1\).",
        "inputs": [
            {"id": "inputNumber74", "label": "Podaj liczbę n:", "type": "number", "min": 8}
        ],
        "links": [
            {"title": "NUMBER03:58", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T58"}
        ]
    },
    75: {
        "description": r"75.Find all primes which can be represented both as sums and as differences of two primes.",
        "inputs": [
            {"id": "inputNumber75", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 2}
        ],
        "links": [
            {"title": "NUMBER03:59", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T59"}
        ]
    },
    76: {
        "description": r"76.Find three least positive integers \(n\) such that there are no primes between \(n\) and \(n+10\), and three least positive integers \(m\) such that there are no primes between \(10m\) and \(10(m+1)\).",
        "inputs": [
            {"id": "inputNumber76", "label": "Podaj liczbę startową do sprawdzenia:", "type": "number", "min": 10}
        ],
        "links": [
            {"title": "NUMBER05:30", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T30"},
            {"title": "NUMBER05:36", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T36"}
        ]
    },
    77: {
        "description": r"77.Prove that every prime of the form \(4k+1\) is a hypotenuse of a rectangular triangle with integer sides.",
        "inputs": [
            {"id": "inputNumber77", "label": "Podaj liczbę wyników spełniających dany warunek do wyświetlenia:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER03:61", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T61"}
        ]
    },
    78: {
        "description": r"78.Find four solutions of the equation \(p^2+1=q^2+r^2\) with primes \(p,q,\) and \(r\).",
        "inputs": [
            {"id": "inputNumber78", "label": "Podaj dolną granicę dla p:", "type": "number", "min": 10},
            {"id": "inputNumberSol78", "label": "Podaj liczbę wyników spełniających dany warunek do wyświetlenia:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER02:53", "url": "http://mizar.uwb.edu.pl/version/current/html/number02.html#T53"}
        ]
    },
    79: {
        "description": r"79.Prove that the equation \(p^2+q^2=r^2+s^2+t^2\) has no solution with primes \(p,q,r,s,t\).",
        "inputs": [
            {"id": "inputNumber79", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER05:45", "url": "http://mizar.uwb.edu.pl/version/current/html/number05.html#T45"}
        ]
    },
    80: {
        "description": r"80.Find all prime solutions \(p,q,r\) of the equation \(p(p+1)+q(q+1)=r(r+1)\).",
        "inputs": [
            {"id": "inputNumber80", "label": "Podaj dolną granicę dla p i q", "type": "number", "min": 10}
        ],
        "links": [
            {"title": "NUMBER07:45", "url": "http://mizar.uwb.edu.pl/version/current/html/number07.html#T45"}
        ]
    },
    81: {
        "description": r"81. Find all primes \(p,q,\) and \(r\) such that the nubers \(p(p+1\), \(q(q+1)\), \(r(r+1)\) form an increasing arithmetic progression.",
        "inputs": [
            {"id": "inputNumber81", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 1}
        ]
    },
    82: {
        "description": r"82.Find all positive integers \(n\) such that each of the numbers \(n+1,n+3,n+7,n+9,n+13\) and \(n+15\) is a prime.",
        "inputs": [
            {"id": "inputNumber82", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 10}
        ],
        "links": [
            {"title": "NUMBER03:63", "url": "http://mizar.uwb.edu.pl/version/current/html/number03.html#T63"}
        ]
    },
    83: {
        "description": r"83.Find five primes which are sums of two fourth powers of integers.",
        "inputs": [
            {"id": "inputNumber83", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 10},
            {"id": "inputNumberSol83", "label": "Podaj liczbę rozwiązań:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER02:54", "url": "http://mizar.uwb.edu.pl/version/current/html/number02.html#T54"}
        ]
    },
    84: {
        "description": r"84.Prove that there exist infinitely many pairs of consecutive primes which are not twin primes.",
        "inputs": [
            {"id": "inputNumber84", "label": "Podaj liczbę wyników spełniających dany warunek do wyświetlenia:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER10:36", "url": "http://mizar.uwb.edu.pl/version/current/html/number10.html#T36"}
        ]
    },
    85: {
        "description": r"85.Using the theorem of \(Lejeune-Dirichlet\) on arithmetic progressions, prove that there exist infinitely many primes which do not belong to any pair of twin primes.",
        "inputs": [
            {"id": "inputNumber85", "label": "Podaj liczbę wyników spełniających dany warunek do wyświetlenia:", "type": "number", "min": 1},
            {"id": "inputNumberLimit85", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 1}
        ]
    },
    86: {
        "description": r"86.Find five least positive integers for which \(n^2-1\) is a product of three different primes",
        "inputs": [
            {"id": "inputNumber86", "label": "Podaj liczbę wyników spełniających dany warunek do wyświetlenia:", "type": "number", "min": 10},
            {"id": "inputNumberSol86", "label": "Podaj liczbę rozwiązań", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER08:59", "url": "http://mizar.uwb.edu.pl/version/current/html/number08.html#T59"},
            {"title": "NUMBER08:64", "url": "http://mizar.uwb.edu.pl/version/current/html/number08.html#T64"}
        ]
    },
    87: {
        "description": r"87.Find five least positive integers \(n\) for which \(n^2+1\) is a product of three different primes, and find a positive integer \(n\) for which \(n^2+1\) is a product of three different odd primes.",
        "inputs": [
            {"id": "inputNumber87", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 10},
            {"id": "inputNumberSol87", "label": "Podaj liczbę wyników spełniających dany warunek do wyświetlenia", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER07:56", "url": "http://mizar.uwb.edu.pl/version/current/html/number07.html#T56"},
            {"title": "NUMBER07:58", "url": "http://mizar.uwb.edu.pl/version/current/html/number07.html#T58"}
        ]
    },
    88: {
        "description": r"88.Prove that among each three consecutive integers \(>7\) at least one has at least two different prime divisors.",
        "inputs": [
            {"id": "inputNumber88", "label": "Podaj liczbę:", "type": "number", "min": 8}
        ],
        "links": [
            {"title": "NUMBER08:79", "url": "http://mizar.uwb.edu.pl/version/current/html/number08.html#T79"}
        ]
    },
    90: {
        "description": r"90.Prove that the theorem asserting that there exist only finitely many positive integers \(n\) such that both \(n\) and \(n+1\) have only one prime divisor is equivalent to the theorem asserting that there exist only finitely many prime Mersenne numbers and finitely many prime Fermat numbers.",
        "inputs": [
            {"id": "inputNumber90", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 1}
        ],
    },
    91: {
        "description": r"91.Find all numbers of the form \(2^n-1\) with positive integer \(n\), not exceeding million, which are products of two primes, and prove that if \(n\) is even and \(>4\), then \(2^n-1\) is a product of at least three integers \(>1\).",
        "inputs": [],
        "links": [
            {"title": "NUMBER09:26", "url": "http://mizar.uwb.edu.pl/version/current/html/number09.html#T26"},
            {"title": "NUMBER09:28", "url": "http://mizar.uwb.edu.pl/version/current/html/number09.html#T28"}
        ]
    },
    92: {
        "description": r"92.Using Problem 47, prove that if \(p_k\) denotes the \(kth\) prime, then for \(k \geq 3\) we have the inequality \(p_{k+1}+p_{k+2} \leq p_1p_2...p_k\).",
        "inputs": [
            {"id": "inputNumber92", "label": "Podaj k:", "type": "number", "min": 4}
        ],
        "links": [
            {"title": "NUMBER13:23", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T23"}
        ]
    },
    93: {
        "description": r"93.For positive integer \(n\), let \(q_n\) dente the least prime which is not a divisor of \(n\). Using Problem 92, prove that the ratio \( q_n/n \) tends to zero as \(n\) increases to infinity.",
        "inputs": [
            {"id": "inputNumber93", "label": "Podaj limit k:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER16:34", "url": "http://mizar.uwb.edu.pl/version/current/html/number16.html#T34"}
        ]
    },
    94: {
        "description": r"94.Prove by elementary means that Chebyshev's theorem (asserting that for integer \(n>1\) there exists at least one prime between \(n\) and \(2n\) there exists at least one number which is a product of two different primes, and that for integer \(>15\) between \(n\) and \(2n\) there exists at least one number which is a product of three different primes.",
        "inputs": [
            {"id": "inputNumber94", "label": "Podaj dolną granicę:", "type": "number", "min": 1},
            {"id": "inputNumberMax94", "label": "Podaj górną granicę:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER10:38", "url": "http://mizar.uwb.edu.pl/version/current/html/number10.html#T38"},
            {"title": "NUMBER10:39", "url": "http://mizar.uwb.edu.pl/version/current/html/number10.html#T39"}
        ]
    },
    95: {
        "description": r"95. Prove by elementary means that the Chebyshev theorem implies that for every positive integer \(s\), for all sufficiently large \(n\), between \(n\) and \(2n\) there exists at least one number which is a product of \(s\) different primes.",
        "inputs": [
            {"id": "inputNumberS95", "label": "Podaj liczbę s:", "type": "number", "min": 1},
            {"id": "inputNumberMin95", "label": "Podaj dolną granicę przeszukiwanego zakresu:", "type": "number", "min": 1},
            {"id": "inputNumberMax95", "label": "Podaj górną granicę przeszukiwanego zakresu", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER16:35", "url": "http://mizar.uwb.edu.pl/version/current/html/number16.html#T35"}
        ]
    },
    96: {
        "description": r"96.Prove that the infinite sequence \(1,31,331,3331,...\) contains infinitely many composite numbers and find the least of them (to solve the second part of the problem, one can use the microfilm containing all primes up to one hundred millions).",
        "inputs": [
            {"id": "inputNumber96", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 1},
            {"id": "inputNumberSol96", "label": "Podaj liczbe wyników:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER16:20", "url": "http://mizar.uwb.edu.pl/version/current/html/number16.html#T20"}
        ]
    },
    97: {
        "description": r"97.Find the least positive integer \(n\) for which \(n^4+(n+1)^4\) is composite.",
        "inputs": [
            {"id": "inputNumber97", "label": "Podaj dolną granicę:", "type": "number", "min": 10},
            {"id": "inputNumberSol97", "label": "Podaj liczbę rozwiązań n do wyświetlenia:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER02:60", "url": "http://mizar.uwb.edu.pl/version/current/html/number02.html#T60"}
        ]
    },
    98: {
        "description": r"98.Show that there are infinitely many composite numbers of the form \(10^n+3\) \((n=1,2,3,...)\).",
        "inputs": [
            {"id": "inputNumber98", "label": "Podaj liczbę rozwiązań n do wyświetlenia:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER04:67", "url": "http://mizar.uwb.edu.pl/version/current/html/number04.html#T67"}
        ]
    },
    99: {
        "description": r"99.Show that for integers \(n>1\) the number \(\frac{1}{5}(2^{4n+2}+1)\) is composite.",
        "inputs": [
            {"id": "inputNumber99", "label": "Podaj limit n do sprawdzenia:", "type": "number", "min": 2}
        ],
        "links": [
            {"title": "NUMBER10:41", "url": "http://mizar.uwb.edu.pl/version/current/html/number10.html#T41"}
        ]
    },
    100: {
        "description": r"100.Prove that the infinite sequence \(2^n-1\) \((n=1,2,...)\) contains arbitrarily long subsequences of consecutive terms consisting of composite numbers.",
        "inputs": [
            {"id": "inputNumber100", "label": "Podaj wartość m:", "type": "number", "min": 1}
        ]
    },
    105: {
        "description": r"105.Find the least prime \(p\) for which each of the numbers \(p-1\) and \(p+1\) has at least three different prime divisors.",
        "inputs": [
            {"id": "inputNumber105", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 10},
            {"id": "inputNumberSol105", "label": "Podaj liczbę rozwiązań do wyświetlenia:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER08:82", "url": "http://mizar.uwb.edu.pl/version/current/html/number08.html#T82"},
            {"title": "NUMBER08:83", "url": "http://mizar.uwb.edu.pl/version/current/html/number08.html#T83"}
        ]
    },
    111: {
        "description": r"111.Find all primes \(p\) such that the sum of all positive integer divisors of \(p^4\) is equal to a square of an integer.",
        "inputs": [
            {"id": "inputNumber111", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER08:87", "url": "http://mizar.uwb.edu.pl/version/current/html/number08.html#T87"},
            {"title": "NUMBER08:88", "url": "http://mizar.uwb.edu.pl/version/current/html/number08.html#T88"}
        ]
    },
    116: {
        "description": r"116.Prove that there exist infinitely many odd numbers \(k>0\) such that all numbers \(2^{2^n}+k\) \((n=1,2,...)\) are composite.",
        "inputs": [
            {"id": "inputNumber116", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 10}
        ],
        "links": [
            {"title": "NUMBER02:65", "url": "http://mizar.uwb.edu.pl/version/current/html/number02.html#T65"}
        ]
    },
    120: {
        "description": r"120.Prove that if \(k\) is a power of \(2\) with positive integer exponent, then for sufficiently large \(n\) all numbers \(k \cdot 2^{2^n}+1\) are composite.",
        "inputs": [
            {"id": "inputNumberM120", "label": "Podaj wykładnik potęgi liczby k: ", "type": "number", "min": 1},
            {"id": "inputNumberLimit120", "label": "Podaj limit n:", "type": "number", "min": 1},
            {"id": "inputNumberTime120", "label": "Podaj maksymalny czas obliczeń (w sekundach):", "type": "number", "min": 5}
        ],
        "links": [
            {"title": "NUMBER14:56", "url": "http://mizar.uwb.edu.pl/version/current/html/number14.html#T56"}
        ]
    },
    121: {
        "description": r"121.For every positive integer \(k \leq 10\), find the least positive integer \(n\) for which \(k \cdot 2^{2^n} + 1\) is composite.",
        "inputs": [
            {"id": "inputNumber121", "label": "Podaj wartość liczby k:", "type": "number", "min": 1},
            {"id": "inputNumberLimit121", "label": "Podaj limit przeszukiwań:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER13:24", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T24"},
            {"title": "NUMBER13:25", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T25"},
            {"title": "NUMBER13:26", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T26"},
            {"title": "NUMBER13:27", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T27"},
            {"title": "NUMBER13:28", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T28"},
            {"title": "NUMBER13:29", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T29"},
            {"title": "NUMBER13:30", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T30"},
            {"title": "NUMBER13:31", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T31"},
            {"title": "NUMBER13:32", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T32"},
            {"title": "NUMBER13:33", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T33"}
        ]
    },
    122: {
        "description": r"122.Find all positive integers \(k \leq 10\) such that every number \(k \cdot 2^{2^n} + 1\) \((n=1,2,...)\) is composite.",
        "inputs": [
            {"id": "inputNumber122", "label": "Podaj limit wartośći n:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER13:38", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T38"}
        ]
    },
    123: {
        "description": r"123.Prove that for integer \(n>1\) the numbers \(\frac{1}{3}(2^{2^{n+1}}+2^{2^n}+1)\) are all composite.",
        "inputs": [
            {"id": "inputNumber123", "label": "Podaj limit przeszukiwań wartośći n:", "type": "number", "min": 1},
            {"id": "inputNumberTime123", "label": "Podaj maksymalny czas obliczeń (w sekundach):", "type": "number", "min": 5}
        ],
        "links": [
            {"title": "NUMBER13:46", "url": "http://mizar.uwb.edu.pl/version/current/html/number13.html#T46"}
        ]
    },
    124: {
        "description": r"124.Prove that there exist infinitely many composite numbers of the form \((2^{2n}+1)^2+2^2\).",
        "inputs": [
            {"id": "inputNumber124", "label": "Podaj limit wartości n:", "type": "number", "min": 1},
            {"id": "inputNumberTime124", "label": "Podaj maksymalny czas obliczeń (w sekundach):", "type": "number", "min": 5}
        ],
        "links": [
            {"title": "NUMBER07:79", "url": "http://mizar.uwb.edu.pl/version/current/html/number07.html#T79"}
        ]
    },
    125: {
        "description": r"125.Prove that for every \(a\) with \(1 < a \leq 100\) there exists at least positive integer \(n \leq 6\) such that \(a^{2^n}+1\) is composite.",
        "inputs": [
            {"id": "inputNumber125", "label": "Podaj a", "type": "number", "min": 1, "max": 100}
        ],
        "links": [
            {"title": "NUMBER09:49", "url": "http://mizar.uwb.edu.pl/version/current/html/number09.html#T49"}
        ]
    },
    131: {
        "description": r"131.Find all integers \(k \geq 0\) for which the sequence \(k+1,k+2,...,k+10\) contains maximal numbers of primes.",
        "inputs": [
            {"id": "inputNumber131", "label": "Podaj limit wartości k:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER14:86", "url": "http://mizar.uwb.edu.pl/version/current/html/number14.html#T86"},
            {"title": "NUMBER14:87", "url": "http://mizar.uwb.edu.pl/version/current/html/number14.html#T87"},
            {"title": "NUMBER14:88", "url": "http://mizar.uwb.edu.pl/version/current/html/number14.html#T88"}
        ]
    },
    135: {
        "description": r"135.Find all numbers \(p\) such that all six numbers \(p,p+2,p+6,p+8,p+12\) and \(p+14\) are primes.",
        "inputs": [
            {"id": "inputNumber135", "label": "Podaj limit wartości p:", "type": "number", "min": 2}
        ],
        "links": [
            {"title": "NUMBER12:44", "url": "http://mizar.uwb.edu.pl/version/current/html/number12.html#T44"}
        ]
    },
    137: {
        "description": r"137.Prove by elementary means that the equation \(3x^2-7y^2+1=0\) has infinitely many solutions in positive integers x,y.",
        "inputs": [
            {"id": "inputNumber137", "label": "Podaj ilość oczekiwanych rozwiązań:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER08:93", "url": "http://mizar.uwb.edu.pl/version/current/html/number08.html#T93"}
        ]
    },
    139: {
        "description": r"139.Prove by elementary means that the equation \((x-1)^2+(x+1)^2=y^2+1\) has infinitely many solutions in positive integers x,y.",
        "inputs": [
            {"id": "inputNumber139", "label": "Podaj ilość oczekiwanych rozwiązań:", "type": "number", "min": 1}
        ],
        "links": [
            {"title": "NUMBER08:99", "url": "http://mizar.uwb.edu.pl/version/current/html/number08.html#T99"}
        ]
    }

};

app = Flask(__name__)

code_filename_map = {
    381: "38a",
    382: "38b",
    383: "38c",
    511: "51a"
}

def split_proof_content(text):
    proof_start = text.find("proof")
    end_pos = text.find("end;", proof_start)
    if proof_start == -1 or end_pos == -1:
        return text, ""
    proof_before = text[:proof_start + len("proof")]
    proof_inside = text[proof_start + len("proof"):]
    proof_before = proof_before.strip()
    proof_inside = proof_inside.replace("\n", "", 1)
    return proof_before, proof_inside

@app.route('/problem/<int:prob_id>')
def problem_page(prob_id):
    filename_suffix = code_filename_map.get(prob_id, str(prob_id))

    problem_file_path = os.path.join('problems', f'prob{filename_suffix}.py')
    text_file_path = os.path.join('test', f'problem{filename_suffix}.txt')

    if os.path.exists(problem_file_path):
        with open(problem_file_path, 'r') as file:
            code_content = file.read()
    else:
        code_content = "Brak dostępnego kodu dla tego problemu."

    if os.path.exists(text_file_path):
        with open(text_file_path, 'r') as file:
            proof_content = file.read()
        proof_before, proof_inside = split_proof_content(proof_content)
    else:
        proof_before, proof_inside = "", ""

    problem = problem_data.get(prob_id)
    if not problem:
        return "Nieznany problem", 404

    return render_template("problem.html", prob_id=prob_id, problem=problem,
                           code_content=code_content,
                           proof_before=proof_before,
                           proof_inside=proof_inside,
                           links=problem.get('links', []))


@app.route('/')
def home():
    problems_with_descriptions = []

    for prob_id in problem_ids:
        if prob_id in problem_data:
            if prob_id == 381:
                display_id = "38a"
            elif prob_id == 382:
                display_id = "38b"
            elif prob_id == 383:
                display_id = "38c"
            elif prob_id == 511:
                display_id = "51a"
            else:
                display_id = str(prob_id)

            problems_with_descriptions.append({
                "id": prob_id,
                "display_id": display_id,
                "description": problem_data[prob_id]["description"]
            })

    return render_template('index.html', problems=problems_with_descriptions)


@app.route('/calculate1', methods=['POST'])
def calculate1():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob1(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate2', methods=['POST'])
def calculate2():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        min_val = next((int(value) for key, value in data.items() if key.startswith("inputMin")), None)
        max_val = next((int(value) for key, value in data.items() if key.startswith("inputMax")), None)

        if min_val >= max_val:
            return jsonify({"error": "Min musi być mniejsze od Max"}), 400

        return jsonify(prob2(min_val, max_val))

    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate3', methods=['POST'])
def calculate3():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob3(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate4', methods=['POST'])
def calculate4():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob4(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate5', methods=['POST'])
def calculate5():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob5(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate6', methods=['POST'])
def calculate6():
    return jsonify(prob6())


@app.route('/calculate7', methods=['POST'])
def calculate7():
    return jsonify(prob7())

@app.route('/calculate8', methods=['POST'])
def calculate8():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        m = next((int(value) for key, value in data.items() if key.startswith("inputNumberM")), None)
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        return jsonify(prob8(m,a))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate9', methods=['POST'])
def calculate9():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob9(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate10', methods=['POST'])
def calculate10():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob10(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate11', methods=['POST'])
def calculate11():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob11(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate12', methods=['POST'])
def calculate12():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        max_x = next((int(value) for key, value in data.items() if key.startswith("inputNumberMax")), None)
        iterations = next((int(value) for key, value in data.items() if key.startswith("inputNumberIt")), None)

        return jsonify(prob12(n, max_x, iterations))

    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate13', methods=['POST'])
def calculate13():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        x = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        max_n = next((int(value) for key, value in data.items() if key.startswith("inputNumberMax")), None)
        iterations = next((int(value) for key, value in data.items() if key.startswith("inputNumberIt")), None)

        return jsonify(prob13(x, max_n, iterations))

    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate14', methods=['POST'])
def calculate14():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob14(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate15', methods=['POST'])
def calculate15():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob15(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate16', methods=['POST'])
def calculate16():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob16(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate17', methods=['POST'])
def calculate17():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumberRange")), None)
        return jsonify(prob17(a, r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate18', methods=['POST'])
def calculate18():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob18(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate19', methods=['POST'])
def calculate19():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob19(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate20', methods=['POST'])
def calculate20():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob20(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate21', methods=['POST'])
def calculate21():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob21(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate22', methods=['POST'])
def calculate22():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob22(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate23', methods=['POST'])
def calculate23():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        p = next((int(value) for key, value in data.items() if key.startswith("inputNumberPRange")), None)
        n_range = next((int(value) for key, value in data.items() if key.startswith("inputNumberNRange")), None)
        return jsonify(prob23(p, n_range))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate24', methods=['POST'])
def calculate24():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob24(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate25', methods=['POST'])
def calculate25():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob25(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate26', methods=['POST'])
def calculate26():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob26(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate27', methods=['POST'])
def calculate27():
    return jsonify(prob27())


@app.route('/calculate28', methods=['POST'])
def calculate28():
    return jsonify(prob28())


@app.route('/calculate29', methods=['POST'])
def calculate29():
    return jsonify(prob29())


@app.route('/calculate30', methods=['POST'])
def calculate30():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob30(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate31', methods=['POST'])
def calculate31():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        c = next((int(value) for key, value in data.items() if key.startswith("inputNumberC")), None)

        return jsonify(prob31(a, b, c))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate32', methods=['POST'])
def calculate32():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob32(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate33', methods=['POST'])
def calculate33():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        x = next((int(value) for key, value in data.items() if key.startswith("inputNumberX")), None)
        y = next((int(value) for key, value in data.items() if key.startswith("inputNumberY")), None)
        z = next((int(value) for key, value in data.items() if key.startswith("inputNumberZ")), None)

        return jsonify(prob33(x,y,z))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate34', methods=['POST'])
def calculate34():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)

        return jsonify(prob34(a, b))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400



@app.route('/calculate35', methods=['POST'])
def calculate35():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob35(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate36', methods=['POST'])
def calculate36():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob36(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate37', methods=['POST'])
def calculate37():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        s = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob37(s))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate381', methods=['POST'])
def calculate381():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob38a(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate382', methods=['POST'])
def calculate382():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob38b(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate383', methods=['POST'])
def calculate383():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob38c(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate39', methods=['POST'])
def calculate39():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        c = next((int(value) for key, value in data.items() if key.startswith("inputNumberC")), None)
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumberN")), None)

        return jsonify(prob39(a, b, c, n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate40', methods=['POST'])
def calculate40():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob40(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate41', methods=['POST'])
def calculate41():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob41(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate42', methods=['POST'])
def calculate42():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob42(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate43', methods=['POST'])
def calculate43():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob43(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate44', methods=['POST'])
def calculate44():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumberLimit")), None)

        return jsonify(prob44(a, b, limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate45', methods=['POST'])
def calculate45():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        c = next((int(value) for key, value in data.items() if key.startswith("inputNumberC")), None)
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumberN")), None)

        return jsonify(prob45(a, b, c, n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate46', methods=['POST'])
def calculate46():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        c = next((int(value) for key, value in data.items() if key.startswith("inputNumberC")), None)
        d = next((int(value) for key, value in data.items() if key.startswith("inputNumberD")), None)
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumberN")), None)

        return jsonify(prob46(a, b, c, d, n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate47', methods=['POST'])
def calculate47():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob47(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate48', methods=['POST'])
def calculate48():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob48(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate49', methods=['POST'])
def calculate49():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        m = next((int(value) for key, value in data.items() if key.startswith("inputNumberM")), None)
        e = next((int(value) for key, value in data.items() if key.startswith("inputNumberE")), None)
        return jsonify(prob49(m, e))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate50', methods=['POST'])
def calculate50():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob50(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate51', methods=['POST'])
def calculate51():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob51(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate511', methods=['POST'])
def calculate511():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        r = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob51a(r))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate52', methods=['POST'])
def calculate52():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        m = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob52(m))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate53', methods=['POST'])
def calculate53():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        k = next((int(value) for key, value in data.items() if key.startswith("inputNumberK")), None)
        len = next((int(value) for key, value in data.items() if key.startswith("inputNumberLen")), None)
        max = next((int(value) for key, value in data.items() if key.startswith("inputNumberMax")), None)

        return jsonify(prob53(k,len,max))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate54', methods=['POST'])
def calculate54():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob54(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate55', methods=['POST'])
def calculate55():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob55(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate56', methods=['POST'])
def calculate56():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob56(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate57', methods=['POST'])
def calculate57():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        return jsonify(prob57(a, b))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate58', methods=['POST'])
def calculate58():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        s = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob58(s))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate59', methods=['POST'])
def calculate59():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        start = next((int(value) for key, value in data.items() if key.startswith("inputNumberStart")), None)
        diff = next((int(value) for key, value in data.items() if key.startswith("inputNumberDiff")), None)
        len = next((int(value) for key, value in data.items() if key.startswith("inputNumberLen")), None)

        return jsonify(prob59(start,diff,len))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate60', methods=['POST'])
def calculate60():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        start = next((int(value) for key, value in data.items() if key.startswith("inputNumberStart")), None)
        end = next((int(value) for key, value in data.items() if key.startswith("inputNumberEnd")), None)
        return jsonify(prob60(start, end))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate61', methods=['POST'])
def calculate61():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        m = next((int(value) for key, value in data.items() if key.startswith("inputNumberM")), None)

        return jsonify(prob61(a,b,m))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate62', methods=['POST'])
def calculate62():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        m = next((int(value) for key, value in data.items() if key.startswith("inputNumberM")), None)
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumberN")), None)
        return jsonify(prob62(a, b, m, n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate63', methods=['POST'])
def calculate63():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        prefix = next((int(value) for key, value in data.items() if key.startswith("inputNumberPrefix")), None)

        return jsonify(prob63(a,b,prefix))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate64', methods=['POST'])
def calculate64():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob64(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate66', methods=['POST'])
def calculate66():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob66(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate67', methods=['POST'])
def calculate67():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumberN")), None)
        return jsonify(prob67(a, b, n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate68', methods=['POST'])
def calculate68():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumberN")), None)
        return jsonify(prob68(a, b, n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate69', methods=['POST'])
def calculate69():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumberA")), None)
        b = next((int(value) for key, value in data.items() if key.startswith("inputNumberB")), None)
        s = next((int(value) for key, value in data.items() if key.startswith("inputNumberS")), None)
        count = next((int(value) for key, value in data.items() if key.startswith("inputNumberCount")), None)
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumberLimit")), None)

        return jsonify(prob69(a, b, s, count, limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate70', methods=['POST'])
def calculate70():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        diff = next((int(value) for key, value in data.items() if key.startswith("inputNumberDiff")), None)
        length = next((int(value) for key, value in data.items() if key.startswith("inputNumberLength")), None)
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumberLimit")), None)
        return jsonify(prob70(diff,length,limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate71', methods=['POST'])
def calculate71():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        diff = next((int(value) for key, value in data.items() if key.startswith("inputNumberDiff")), None)
        length = next((int(value) for key, value in data.items() if key.startswith("inputNumberLength")), None)
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumberLimit")), None)
        return jsonify(prob71(diff,length,limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate72', methods=['POST'])
def calculate72():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        length = next((int(value) for key, value in data.items() if key.startswith("inputNumberLength")), None)
        start = next((int(value) for key, value in data.items() if key.startswith("inputNumberStart")), None)
        diff = next((int(value) for key, value in data.items() if key.startswith("inputNumberDiff")), None)
        return jsonify(prob72(length,start,diff))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate74', methods=['POST'])
def calculate74():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob74(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate75', methods=['POST'])
def calculate75():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob75(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate76', methods=['POST'])
def calculate76():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob76(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate77', methods=['POST'])
def calculate77():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob77(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate78', methods=['POST'])
def calculate78():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        num_of_sol = next((int(value) for key, value in data.items() if key.startswith("inputNumberSol")), None)
        return jsonify(prob78(limit, num_of_sol))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calcuate79', methods=['POST'])
def calculate79():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob79(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate80', methods=['POST'])
def calculate80():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob80(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate81', methods=['POST'])
def calculate81():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob81(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate82', methods=['POST'])
def calculate82():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob82(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate83', methods=['POST'])
def calculate83():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        num_of_sol = next((int(value) for key, value in data.items() if key.startswith("inputNumberSol")), None)
        return jsonify(prob83(limit, num_of_sol))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calcuate84', methods=['POST'])
def calculate84():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob84(n))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calcuate85', methods=['POST'])
def calculate85():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumberLimit")), None)

        return jsonify(prob85(n,limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate86', methods=['POST'])
def calculate86():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        num_of_sol = next((int(value) for key, value in data.items() if key.startswith("inputNumberSol")), None)
        return jsonify(prob86(limit, num_of_sol))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate87', methods=['POST'])
def calculate87():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        num_of_sol = next((int(value) for key, value in data.items() if key.startswith("inputNumberSol")), None)
        return jsonify(prob87(limit, num_of_sol))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate88', methods=['POST'])
def calculate88():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        i = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob88(i))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate90', methods=['POST'])
def calculate90():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob90(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate91', methods=['POST'])
def calculate91():
    return jsonify(prob91())


@app.route('/calculate92', methods=['POST'])
def calculate92():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        k = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob92(k))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate93', methods=['POST'])
def calculate93():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        k = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob93(k))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate94', methods=['POST'])
def calculate94():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        max = next((int(value) for key, value in data.items() if key.startswith("inputNumberMax")), None)

        return jsonify(prob94(n,max))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate95', methods=['POST'])
def calculate95():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        s = next((int(value) for key, value in data.items() if key.startswith("inputNumberS")), None)
        min = next((int(value) for key, value in data.items() if key.startswith("inputNumberMin")), None)
        max = next((int(value) for key, value in data.items() if key.startswith("inputNumberMax")), None)

        return jsonify(prob95(s,min,max))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate96', methods=['POST'])
def calculate96():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        sol = next((int(value) for key, value in data.items() if key.startswith("inputNumberSol")), None)

        return jsonify(prob96(n,sol))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate97', methods=['POST'])
def calculate97():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        num_of_sol = next((int(value) for key, value in data.items() if key.startswith("inputNumberSol")), None)
        return jsonify(prob97(limit, num_of_sol))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate98', methods=['POST'])
def calculate98():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob98(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate99', methods=['POST'])
def calculate99():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob99(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate100', methods=['POST'])
def calculate100():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        m = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)

        return jsonify(prob100(m))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate105', methods=['POST'])
def calculate105():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        num_of_sol = next((int(value) for key, value in data.items() if key.startswith("inputNumberSol")), None)
        return jsonify(prob105(limit, num_of_sol))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate111', methods=['POST'])
def calculate111():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob111(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate116', methods=['POST'])
def calculate116():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob116(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate120', methods=['POST'])
def calculate120():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        m = next((int(value) for key, value in data.items() if key.startswith("inputNumberM")), None)
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumberLimit")), None)
        time = next((int(value) for key, value in data.items() if key.startswith("inputNumberTime")), None)

        return jsonify(prob120(m, n, time))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate121', methods=['POST'])
def calculate121():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        k = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumberLimit")), None)
        return jsonify(prob121(k, limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate122', methods=['POST'])
def calculate122():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob122(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate123', methods=['POST'])
def calculate123():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        time = next((int(value) for key, value in data.items() if key.startswith("inputNumberTime")), None)
        return jsonify(prob123(n, time))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate124', methods=['POST'])
def calculate124():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        n = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        time = next((int(value) for key, value in data.items() if key.startswith("inputNumberTime")), None)
        return jsonify(prob124(n, time))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate125', methods=['POST'])
def calculate125():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        a = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob125(a))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate131', methods=['POST'])
def calculate131():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob131(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


@app.route('/calculate135', methods=['POST'])
def calculate135():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob135(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate137', methods=['POST'])
def calculate137():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob137(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400

@app.route('/calculate139', methods=['POST'])
def calculate139():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400

    try:
        limit = next((int(value) for key, value in data.items() if key.startswith("inputNumber")), None)
        return jsonify(prob139(limit))
    except ValueError:
        return jsonify({"error": "Invalid number"}), 400


if __name__ == '__main__':
    app.run(debug=True)
