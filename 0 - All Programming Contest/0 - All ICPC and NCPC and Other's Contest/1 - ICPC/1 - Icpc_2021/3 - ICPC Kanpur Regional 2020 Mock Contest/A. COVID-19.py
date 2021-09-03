# Accept
from math import ceil
def solve():
    n = int(input())
    if n <= 5:
        print(1)
    else:
        arr = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210, 216, 222, 228, 234, 240, 246, 252, 258, 264, 270, 276, 282, 288, 294, 300, 306, 312, 318, 324, 330, 336, 342, 348, 354, 360, 366, 372, 378, 384, 390, 396, 402, 408, 414, 420, 426, 432, 438, 444, 450, 456, 462, 468, 474, 480, 486, 492, 498, 504, 510, 516, 522, 528, 534, 540, 546, 552, 558, 564, 570, 576, 582, 588, 594, 600, 606, 612, 618, 624, 630, 636, 642, 648, 654, 660, 666, 672, 678, 684, 690, 696, 702, 708, 714, 720, 726, 732, 738, 744, 750, 756, 762, 768, 774, 780, 786, 792, 798, 804, 810, 816, 822, 828, 834, 840, 846, 852, 858, 864, 870, 876, 882, 888, 894, 900, 906, 912, 918, 924, 930, 936, 942, 948, 954, 960, 966, 972, 978, 984, 990, 996, 1002, 1008, 1014, 1020, 1026, 1032, 1038, 1044, 1050, 1056, 1062, 1068, 1074, 1080, 1086, 1092, 1098, 1104, 1110, 1116, 1122, 1128, 1134, 1140, 1146, 1152, 1158, 1164, 1170, 1176, 1182, 1188, 1194, 1200, 1206, 1212, 1218, 1224, 1230, 1236, 1242, 1248, 1254, 1260, 1266, 1272, 1278, 1284, 1290, 1296, 1302, 1308, 1314, 1320, 1326, 1332, 1338, 1344, 1350, 1356, 1362, 1368, 1374, 1380, 1386, 1392, 1398, 1404, 1410, 1416, 1422, 1428, 1434, 1440, 1446, 1452, 1458, 1464, 1470, 1476, 1482, 1488, 1494, 1500, 1506, 1512, 1518, 1524, 1530, 1536, 1542, 1548, 1554, 1560, 1566, 1572, 1578, 1584, 1590, 1596, 1602, 1608, 1614, 1620, 1626, 1632, 1638, 1644, 1650, 1656, 1662, 1668, 1674, 1680, 1686, 1692, 1698, 1704, 1710, 1716, 1722, 1728, 1734, 1740, 1746, 1752, 1758, 1764, 1770, 1776, 1782, 1788, 1794, 1800, 1806, 1812, 1818, 1824, 1830, 1836, 1842, 1848, 1854, 1860, 1866, 1872, 1878, 1884, 1890, 1896, 1902, 1908, 1914, 1920, 1926, 1932, 1938, 1944, 1950, 1956, 1962, 1968, 1974, 1980, 1986, 1992, 1998, 2004, 2010, 2016, 2022, 2028, 2034, 2040, 2046, 2052, 2058, 2064, 2070, 2076, 2082, 2088, 2094, 2100, 2106, 2112, 2118, 2124, 2130, 2136, 2142, 2148, 2154, 2160, 2166, 2172, 2178, 2184, 2190, 2196, 2202, 2208, 2214, 2220, 2226, 2232, 2238, 2244, 2250, 2256, 2262, 2268, 2274, 2280, 2286, 2292, 2298, 2304, 2310, 2316, 2322, 2328, 2334, 2340, 2346, 2352, 2358, 2364, 2370, 2376, 2382, 2388, 2394, 2400, 2406, 2412, 2418, 2424, 2430, 2436, 2442, 2448, 2454, 2460, 2466, 2472, 2478, 2484, 2490, 2496, 2502, 2508, 2514, 2520, 2526, 2532, 2538, 2544, 2550, 2556, 2562, 2568, 2574, 2580, 2586, 2592, 2598, 2604, 2610, 2616, 2622, 2628, 2634, 2640, 2646, 2652, 2658, 2664, 2670, 2676, 2682, 2688, 2694, 2700, 2706, 2712, 2718, 2724, 2730, 2736, 2742, 2748, 2754, 2760, 2766, 2772, 2778, 2784, 2790, 2796, 2802, 2808, 2814, 2820, 2826, 2832, 2838, 2844, 2850, 2856, 2862, 2868, 2874, 2880, 2886, 2892, 2898, 2904, 2910, 2916, 2922, 2928, 2934, 2940, 2946, 2952, 2958, 2964, 2970, 2976, 2982, 2988, 2994, 3000, 3006, 3012, 3018, 3024, 3030, 3036, 3042, 3048, 3054, 3060, 3066, 3072, 3078, 3084, 3090, 3096, 3102, 3108, 3114, 3120, 3126, 3132, 3138, 3144, 3150, 3156, 3162, 3168, 3174, 3180, 3186, 3192, 3198, 3204, 3210, 3216, 3222, 3228, 3234, 3240, 3246, 3252, 3258, 3264, 3270, 3276, 3282, 3288, 3294, 3300, 3306, 3312, 3318, 3324, 3330, 3336, 3342, 3348, 3354, 3360, 3366, 3372, 3378, 3384, 3390, 3396, 3402, 3408, 3414, 3420, 3426, 3432, 3438, 3444, 3450, 3456, 3462, 3468, 3474, 3480, 3486, 3492, 3498, 3504, 3510, 3516, 3522, 3528, 3534, 3540, 3546, 3552, 3558, 3564, 3570, 3576, 3582, 3588, 3594, 3600, 3606, 3612, 3618, 3624, 3630, 3636, 3642, 3648, 3654, 3660, 3666, 3672, 3678, 3684, 3690, 3696, 3702, 3708, 3714, 3720, 3726, 3732, 3738, 3744, 3750, 3756, 3762, 3768, 3774, 3780, 3786, 3792, 3798, 3804, 3810, 3816, 3822, 3828, 3834, 3840, 3846, 3852, 3858, 3864, 3870, 3876, 3882, 3888, 3894, 3900, 3906, 3912, 3918, 3924, 3930, 3936, 3942, 3948, 3954, 3960, 3966, 3972, 3978, 3984, 3990, 3996, 4002, 4008, 4014, 4020, 4026, 4032, 4038, 4044, 4050, 4056, 4062, 4068, 4074, 4080, 4086, 4092, 4098, 4104, 4110, 4116, 4122, 4128, 4134, 4140, 4146, 4152, 4158, 4164, 4170, 4176, 4182, 4188, 4194, 4200, 4206, 4212, 4218, 4224, 4230, 4236, 4242, 4248, 4254, 4260, 4266, 4272, 4278, 4284, 4290, 4296, 4302, 4308, 4314, 4320, 4326, 4332, 4338, 4344, 4350, 4356, 4362, 4368, 4374, 4380, 4386, 4392, 4398, 4404, 4410, 4416, 4422, 4428, 4434, 4440, 4446, 4452, 4458, 4464, 4470, 4476, 4482, 4488, 4494, 4500, 4506, 4512, 4518, 4524, 4530, 4536, 4542, 4548, 4554, 4560, 4566, 4572, 4578, 4584, 4590, 4596, 4602, 4608, 4614, 4620, 4626, 4632, 4638, 4644, 4650, 4656, 4662, 4668, 4674, 4680, 4686, 4692, 4698, 4704, 4710, 4716, 4722, 4728, 4734, 4740, 4746, 4752, 4758, 4764, 4770, 4776, 4782, 4788, 4794, 4800, 4806, 4812, 4818, 4824, 4830, 4836, 4842, 4848, 4854, 4860, 4866, 4872, 4878, 4884, 4890, 4896, 4902, 4908, 4914, 4920, 4926, 4932, 4938, 4944, 4950, 4956, 4962, 4968, 4974, 4980, 4986, 4992, 4998, 5004, 5010, 5016, 5022, 5028, 5034, 5040, 5046, 5052, 5058, 5064, 5070, 5076, 5082, 5088, 5094, 5100, 5106, 5112, 5118, 5124, 5130, 5136, 5142, 5148, 5154, 5160, 5166, 5172, 5178, 5184, 5190, 5196, 5202, 5208, 5214, 5220, 5226, 5232, 5238, 5244, 5250, 5256, 5262, 5268, 5274, 5280, 5286, 5292, 5298, 5304, 5310, 5316, 5322, 5328, 5334, 5340, 5346, 5352, 5358, 5364, 5370, 5376, 5382, 5388, 5394, 5400, 5406, 5412, 5418, 5424, 5430, 5436, 5442, 5448, 5454, 5460, 5466, 5472, 5478, 5484, 5490, 5496, 5502, 5508, 5514, 5520, 5526, 5532, 5538, 5544, 5550, 5556, 5562, 5568, 5574, 5580, 5586, 5592, 5598, 5604, 5610, 5616, 5622, 5628, 5634, 5640, 5646, 5652, 5658, 5664, 5670, 5676, 5682, 5688, 5694, 5700, 5706, 5712, 5718, 5724, 5730, 5736, 5742, 5748, 5754, 5760, 5766, 5772, 5778, 5784, 5790, 5796, 5802, 5808, 5814, 5820, 5826, 5832, 5838, 5844, 5850, 5856, 5862, 5868, 5874, 5880, 5886, 5892, 5898, 5904, 5910, 5916, 5922, 5928, 5934, 5940, 5946, 5952, 5958, 5964, 5970, 5976, 5982, 5988, 5994, 6000, 6006, 6012, 6018, 6024, 6030, 6036, 6042, 6048, 6054, 6060, 6066, 6072, 6078, 6084, 6090, 6096, 6102, 6108, 6114, 6120, 6126, 6132, 6138, 6144, 6150, 6156, 6162, 6168, 6174, 6180, 6186, 6192, 6198, 6204, 6210, 6216, 6222, 6228, 6234, 6240, 6246, 6252, 6258, 6264, 6270, 6276, 6282, 6288, 6294, 6300, 6306, 6312, 6318, 6324, 6330, 6336, 6342, 6348, 6354, 6360, 6366, 6372, 6378, 6384, 6390, 6396, 6402, 6408, 6414, 6420, 6426, 6432, 6438, 6444, 6450, 6456, 6462, 6468, 6474, 6480, 6486, 6492, 6498, 6504, 6510, 6516, 6522, 6528, 6534, 6540, 6546, 6552, 6558, 6564, 6570, 6576, 6582, 6588, 6594, 6600, 6606, 6612, 6618, 6624, 6630, 6636, 6642, 6648, 6654, 6660, 6666, 6672, 6678, 6684, 6690, 6696, 6702, 6708, 6714, 6720, 6726, 6732, 6738, 6744, 6750, 6756, 6762, 6768, 6774, 6780, 6786, 6792, 6798, 6804, 6810, 6816, 6822, 6828, 6834, 6840, 6846, 6852, 6858, 6864, 6870, 6876, 6882, 6888, 6894, 6900, 6906, 6912, 6918, 6924, 6930, 6936, 6942, 6948, 6954, 6960, 6966, 6972, 6978, 6984, 6990, 6996, 7002, 7008, 7014, 7020, 7026, 7032, 7038, 7044, 7050, 7056, 7062, 7068, 7074, 7080, 7086, 7092, 7098, 7104, 7110, 7116, 7122, 7128, 7134, 7140, 7146, 7152, 7158, 7164, 7170, 7176, 7182, 7188, 7194, 7200, 7206, 7212, 7218, 7224, 7230, 7236, 7242, 7248, 7254, 7260, 7266, 7272, 7278, 7284, 7290, 7296, 7302, 7308, 7314, 7320, 7326, 7332, 7338, 7344, 7350, 7356, 7362, 7368, 7374, 7380, 7386, 7392, 7398, 7404, 7410, 7416, 7422, 7428, 7434, 7440, 7446, 7452, 7458, 7464, 7470, 7476, 7482, 7488, 7494, 7500, 7506, 7512, 7518, 7524, 7530, 7536, 7542, 7548, 7554, 7560, 7566, 7572, 7578, 7584, 7590, 7596, 7602, 7608, 7614, 7620, 7626, 7632, 7638, 7644, 7650, 7656, 7662, 7668, 7674, 7680, 7686, 7692, 7698, 7704, 7710, 7716, 7722, 7728, 7734, 7740, 7746, 7752, 7758, 7764, 7770, 7776, 7782, 7788, 7794, 7800, 7806, 7812, 7818, 7824, 7830, 7836, 7842, 7848, 7854, 7860, 7866, 7872, 7878, 7884, 7890, 7896, 7902, 7908, 7914, 7920, 7926, 7932, 7938, 7944, 7950, 7956, 7962, 7968, 7974, 7980, 7986, 7992, 7998, 8004, 8010, 8016, 8022, 8028, 8034, 8040, 8046, 8052, 8058, 8064, 8070, 8076, 8082, 8088, 8094, 8100, 8106, 8112, 8118, 8124, 8130, 8136, 8142, 8148, 8154, 8160, 8166, 8172, 8178, 8184, 8190, 8196, 8202, 8208, 8214, 8220, 8226, 8232, 8238, 8244, 8250, 8256, 8262, 8268, 8274, 8280, 8286, 8292, 8298, 8304, 8310, 8316, 8322, 8328, 8334, 8340, 8346, 8352, 8358, 8364, 8370, 8376, 8382, 8388, 8394, 8400, 8406, 8412, 8418, 8424, 8430, 8436, 8442, 8448, 8454, 8460, 8466, 8472, 8478, 8484, 8490, 8496, 8502, 8508, 8514, 8520, 8526, 8532, 8538, 8544, 8550, 8556, 8562, 8568, 8574, 8580, 8586, 8592, 8598, 8604, 8610, 8616, 8622, 8628, 8634, 8640, 8646, 8652, 8658, 8664, 8670, 8676, 8682, 8688, 8694, 8700, 8706, 8712, 8718, 8724, 8730, 8736, 8742, 8748, 8754, 8760, 8766, 8772, 8778, 8784, 8790, 8796, 8802, 8808, 8814, 8820, 8826, 8832, 8838, 8844, 8850, 8856, 8862, 8868, 8874, 8880, 8886, 8892, 8898, 8904, 8910, 8916, 8922, 8928, 8934, 8940, 8946, 8952, 8958, 8964, 8970, 8976, 8982, 8988, 8994, 9000, 9006, 9012, 9018, 9024, 9030, 9036, 9042, 9048, 9054, 9060, 9066, 9072, 9078, 9084, 9090, 9096, 9102, 9108, 9114, 9120, 9126, 9132, 9138, 9144, 9150, 9156, 9162, 9168, 9174, 9180, 9186, 9192, 9198, 9204, 9210, 9216, 9222, 9228, 9234, 9240, 9246, 9252, 9258, 9264, 9270, 9276, 9282, 9288, 9294, 9300, 9306, 9312, 9318, 9324, 9330, 9336, 9342, 9348, 9354, 9360, 9366, 9372, 9378, 9384, 9390, 9396, 9402, 9408, 9414, 9420, 9426, 9432, 9438, 9444, 9450, 9456, 9462, 9468, 9474, 9480, 9486, 9492, 9498, 9504, 9510, 9516, 9522, 9528, 9534, 9540, 9546, 9552, 9558, 9564, 9570, 9576, 9582, 9588, 9594, 9600, 9606, 9612, 9618, 9624, 9630, 9636, 9642, 9648, 9654, 9660, 9666, 9672, 9678, 9684, 9690, 9696, 9702, 9708, 9714, 9720, 9726, 9732, 9738, 9744, 9750, 9756, 9762, 9768, 9774, 9780, 9786, 9792, 9798, 9804, 9810, 9816, 9822, 9828, 9834, 9840, 9846, 9852, 9858, 9864, 9870, 9876, 9882, 9888, 9894, 9900, 9906, 9912, 9918, 9924, 9930, 9936, 9942, 9948, 9954, 9960, 9966, 9972, 9978, 9984, 9990, 9996]
        if n in arr:
            print(arr.index(n)+2)

        else:
            print(ceil(n/6))

solve()