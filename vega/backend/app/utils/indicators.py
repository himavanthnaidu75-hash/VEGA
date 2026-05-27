import pandas as pd
import numpy as np
import pandas_ta as ta

def sma(d, p): return ta.sma(d, length=p)
def ema(d, p): return ta.ema(d, length=p)
def rsi(d, p=14): return ta.rsi(d, length=p)

# Formula (1): fT = ST − S0 − (ST − K)+ + C = K − S0 − (K − ST )+ + C
def f_1(C, K, S0, ST): return ST - S0 - np.maximum(0, ST - K) + C = K - S0 - np.maximum(0, K - ST ) + C

# Formula (2): = S0 − C
def f_2(C, S0): return S0 - C

# Formula (3): Pmax = K − S0 + C
def f_3(C, K, S0): return K - S0 + C

# Formula (4): Lmax = S0 − C
def f_4(C, S0): return S0 - C

# Formula (5): fT = S0 − ST − (K − ST )+ + C = S0 − K − (ST − K)+ + C
def f_5(C, K, S0, ST): return S0 - ST - np.maximum(0, K - ST ) + C = S0 - K - np.maximum(0, ST - K) + C

# Formula (6): = S0 + C
def f_6(C, S0): return S0 + C

# Formula (7): Pmax = S0 − K + C
def f_7(C, K, S0): return S0 - K + C

# Formula (8): Lmax = unlimited
def f_8(unlimited): return unlimited

# Formula (9): fT = ST − S0 + (K − ST )+ − D = K − S0 + (ST − K)+ − D
def f_9(D, K, S0, ST): return ST - S0 + np.maximum(0, K - ST ) - D = K - S0 + np.maximum(0, ST - K) - D

# Formula (10): = S0 + D
def f_10(D, S0): return S0 + D

# Formula (11): Pmax = unlimited
def f_11(unlimited): return unlimited

# Formula (12): Lmax = S0 − K + D
def f_12(D, K, S0): return S0 - K + D

# Formula (13): fT = S0 − ST + (ST − K)+ − D = S0 − K + (K − ST )+ − D
def f_13(D, K, S0, ST): return S0 - ST + np.maximum(0, ST - K) - D = S0 - K + np.maximum(0, K - ST ) - D

# Formula (14): = S0 − D
def f_14(D, S0): return S0 - D

# Formula (15): Pmax = S0 − D
def f_15(D, S0): return S0 - D

# Formula (16): Lmax = K − S0 + D
def f_16(D, K, S0): return K - S0 + D

# Formula (17): fT = (ST − K1 )+ − (ST − K2 )+ − D
def f_17(D, K1, K2, ST): return np.maximum(0, ST - K1 ) - np.maximum(0, ST - K2 ) - D

# Formula (18): = K1 + D
def f_18(D, K1): return K1 + D

# Formula (19): Pmax = K2 − K1 − D
def f_19(D, K1, K2): return K2 - K1 - D

# Formula (20): Lmax = D
def f_20(D): return D

# Formula (21): fT = (K1 − ST )+ − (K2 − ST )+ + C
def f_21(C, K1, K2, ST): return np.maximum(0, K1 - ST ) - np.maximum(0, K2 - ST ) + C

# Formula (22): = K2 − C
def f_22(C, K2): return K2 - C

# Formula (23): Pmax = C
def f_23(C): return C

# Formula (24): Lmax = K2 − K1 − C
def f_24(C, K1, K2): return K2 - K1 - C

# Formula (25): fT = (ST − K1 )+ − (ST − K2 )+ + C
def f_25(C, K1, K2, ST): return np.maximum(0, ST - K1 ) - np.maximum(0, ST - K2 ) + C

# Formula (26): = K2 + C
def f_26(C, K2): return K2 + C

# Formula (27): Pmax = C
def f_27(C): return C

# Formula (28): Lmax = K1 − K2 − C
def f_28(C, K1, K2): return K1 - K2 - C

# Formula (29): fT = (K1 − ST )+ − (K2 − ST )+ − D
def f_29(D, K1, K2, ST): return np.maximum(0, K1 - ST ) - np.maximum(0, K2 - ST ) - D

# Formula (30): = K1 − D
def f_30(D, K1): return K1 - D

# Formula (31): Pmax = K1 − K2 − D
def f_31(D, K1, K2): return K1 - K2 - D

# Formula (32): Lmax = D
def f_32(D): return D

# Formula (33): fT = (ST − K)+ − (K − ST )+ − H = ST − K − H
def f_33(H, K, ST): return np.maximum(0, ST - K) - np.maximum(0, K - ST ) - H = ST - K - H

# Formula (34): = K + H
def f_34(H, K): return K + H

# Formula (35): Pmax = unlimited
def f_35(unlimited): return unlimited

# Formula (36): Lmax = K + H
def f_36(H, K): return K + H

# Formula (37): fT = (K − ST )+ − (ST − K)+ − H = K − ST − H
def f_37(H, K, ST): return np.maximum(0, K - ST ) - np.maximum(0, ST - K) - H = K - ST - H

# Formula (38): = K − H
def f_38(H, K): return K - H

# Formula (39): Pmax = K − H
def f_39(H, K): return K - H

# Formula (40): Lmax = unlimited
def f_40(unlimited): return unlimited

# Formula (41): fT = (ST − K1 )+ − (K2 − ST )+ − H
def f_41(H, K1, K2, ST): return np.maximum(0, ST - K1 ) - np.maximum(0, K2 - ST ) - H

# Formula (42): = K1 + H, H > 0
def f_42(H, K1): return K1 + H, H > 0

# Formula (43): = K2 + H, H < 0
def f_43(H, K2): return K2 + H, H < 0

# Formula (44): H = 0
def f_44(): return 0

# Formula (45): Pmax = unlimited
def f_45(unlimited): return unlimited

# Formula (46): Lmax = K2 + H
def f_46(H, K2): return K2 + H

# Formula (47): fT = (K1 − ST )+ − (ST − K2 )+ − H
def f_47(H, K1, K2, ST): return np.maximum(0, K1 - ST ) - np.maximum(0, ST - K2 ) - H

# Formula (48): = K1 − H, H > 0
def f_48(H, K1): return K1 - H, H > 0

# Formula (49): = K2 − H, H < 0
def f_49(H, K2): return K2 - H, H < 0

# Formula (50): H = 0
def f_50(): return 0

# Formula (51): Pmax = K1 − H
def f_51(H, K1): return K1 - H

# Formula (52): Lmax = unlimited
def f_52(unlimited): return unlimited

# Formula (53): fT = (ST − K1 )+ − (ST − K2 )+ − (ST − K3 )+ − H
def f_53(H, K1, K2, K3, ST): return np.maximum(0, ST - K1 ) - np.maximum(0, ST - K2 ) - np.maximum(0, ST - K3 ) - H

# Formula (54): down = K1 + H, H > 0
def f_54(H, K1): return K1 + H, H > 0

# Formula (55): up = K3 + K2 − K1 − H
def f_55(H, K1, K2, K3): return K3 + K2 - K1 - H

# Formula (56): Pmax = K2 − K1 − H
def f_56(H, K1, K2): return K2 - K1 - H

# Formula (57): Lmax = unlimited
def f_57(unlimited): return unlimited

# Formula (58): fT = (K3 − ST )+ + (K2 − ST )+ − (K1 − ST )+ − H
def f_58(H, K1, K2, K3, ST): return np.maximum(0, K3 - ST ) + np.maximum(0, K2 - ST ) - np.maximum(0, K1 - ST ) - H

# Formula (59): up = K1 + H, H < 0
def f_59(H, K1): return K1 + H, H < 0

# Formula (60): down = K3 + K2 − K1 − H
def f_60(H, K1, K2, K3): return K3 + K2 - K1 - H

# Formula (61): Pmax = K3 + K2 − K1 − H
def f_61(H, K1, K2, K3): return K3 + K2 - K1 - H

# Formula (62): Lmax = K1 − K2 + H
def f_62(H, K1, K2): return K1 - K2 + H

# Formula (63): fT = (ST − K3 )+ + (ST − K2 )+ − (ST − K1 )+ − H
def f_63(H, K1, K2, K3, ST): return np.maximum(0, ST - K3 ) + np.maximum(0, ST - K2 ) - np.maximum(0, ST - K1 ) - H

# Formula (64): down = K1 − H, H < 0
def f_64(H, K1): return K1 - H, H < 0

# Formula (65): up = K3 + K2 − K1 + H
def f_65(H, K1, K2, K3): return K3 + K2 - K1 + H

# Formula (66): Pmax = unlimited
def f_66(unlimited): return unlimited

# Formula (67): Lmax = K2 − K1 + H
def f_67(H, K1, K2): return K2 - K1 + H

# Formula (68): fT = (K1 − ST )+ − (K2 − ST )+ − (K3 − ST )+ − H
def f_68(H, K1, K2, K3, ST): return np.maximum(0, K1 - ST ) - np.maximum(0, K2 - ST ) - np.maximum(0, K3 - ST ) - H

# Formula (69): up = K1 − H, H > 0
def f_69(H, K1): return K1 - H, H > 0

# Formula (70): down = K3 + K2 − K1 + H
def f_70(H, K1, K2, K3): return K3 + K2 - K1 + H

# Formula (71): Pmax = K1 − K2 − H
def f_71(H, K1, K2): return K1 - K2 - H

# Formula (72): Lmax = K3 + K2 − K1 + H
def f_72(H, K1, K2, K3): return K3 + K2 - K1 + H

# Formula (73): Pmax = V − D
def f_73(D, V): return V - D

# Formula (74): Lmax = D
def f_74(D): return D

# Formula (75): Pmax = V − D
def f_75(D, V): return V - D

# Formula (76): Lmax = D
def f_76(D): return D

# Formula (77): Pmax = V − D
def f_77(D, V): return V - D

# Formula (78): Lmax = D
def f_78(D): return D

# Formula (79): Pmax = V − D
def f_79(D, V): return V - D

# Formula (80): Lmax = D
def f_80(D): return D

# Formula (81): fT = (ST − K)+ + (K − ST )+ − D
def f_81(D, K, ST): return np.maximum(0, ST - K) + np.maximum(0, K - ST ) - D

# Formula (82): up = K + D
def f_82(D, K): return K + D

# Formula (83): down = K − D
def f_83(D, K): return K - D

# Formula (84): Pmax = unlimited
def f_84(unlimited): return unlimited

# Formula (85): Lmax = D
def f_85(D): return D

# Formula (86): fT = (ST − K1 )+ + (K2 − ST )+ − D
def f_86(D, K1, K2, ST): return np.maximum(0, ST - K1 ) + np.maximum(0, K2 - ST ) - D

# Formula (87): up = K1 + D
def f_87(D, K1): return K1 + D

# Formula (88): down = K2 − D
def f_88(D, K2): return K2 - D

# Formula (89): Pmax = unlimited
def f_89(unlimited): return unlimited

# Formula (90): Lmax = D
def f_90(D): return D

# Formula (91): fT = (ST − K1 )+ + (K2 − ST )+ − D
def f_91(D, K1, K2, ST): return np.maximum(0, ST - K1 ) + np.maximum(0, K2 - ST ) - D

# Formula (92): up = K1 + D
def f_92(D, K1): return K1 + D

# Formula (93): down = K2 − D
def f_93(D, K2): return K2 - D

# Formula (94): Pmax = unlimited
def f_94(unlimited): return unlimited

# Formula (95): Lmax = D − (K2 − K1 )
def f_95(D, K1, K2): return D - (K2 - K1 )

# Formula (96): fT = −(ST − K)+ − (K − ST )+ + C
def f_96(C, K, ST): return -np.maximum(0, ST - K) - np.maximum(0, K - ST ) + C

# Formula (97): up = K + C
def f_97(C, K): return K + C

# Formula (98): down = K − C
def f_98(C, K): return K - C

# Formula (99): Pmax = C
def f_99(C): return C

# Formula (100): Lmax = unlimited
def f_100(unlimited): return unlimited

# Formula (101): fT = −(ST − K1 )+ − (K2 − ST )+ + C
def f_101(C, K1, K2, ST): return -np.maximum(0, ST - K1 ) - np.maximum(0, K2 - ST ) + C

# Formula (102): up = K1 + C
def f_102(C, K1): return K1 + C

# Formula (103): down = K2 − C
def f_103(C, K2): return K2 - C

# Formula (104): Pmax = C
def f_104(C): return C

# Formula (105): Lmax = unlimited
def f_105(unlimited): return unlimited

# Formula (106): fT = −(ST − K1 )+ − (K2 − ST )+ + C
def f_106(C, K1, K2, ST): return -np.maximum(0, ST - K1 ) - np.maximum(0, K2 - ST ) + C

# Formula (107): up = K1 + C
def f_107(C, K1): return K1 + C

# Formula (108): down = K2 − C
def f_108(C, K2): return K2 - C

# Formula (109): Pmax = C − (K2 − K1 )
def f_109(C, K1, K2): return C - (K2 - K1 )

# Formula (110): Lmax = unlimited
def f_110(unlimited): return unlimited

# Formula (111): fT = S0 − ST + 2 × (ST − K)+ − D
def f_111(D, K, S0, ST): return S0 - ST + 2 * np.maximum(0, ST - K) - D

# Formula (112): up = 2 × K − S0 + D
def f_112(D, K, S0): return 2 * K - S0 + D

# Formula (113): down = S0 − D
def f_113(D, S0): return S0 - D

# Formula (114): Pmax = unlimited
def f_114(unlimited): return unlimited

# Formula (115): Lmax = D − (S0 − K)
def f_115(D, K, S0): return D - (S0 - K)

# Formula (116): fT = ST − S0 + 2 × (K − ST )+ − D
def f_116(D, K, S0, ST): return ST - S0 + 2 * np.maximum(0, K - ST ) - D

# Formula (117): up = S0 + D
def f_117(D, S0): return S0 + D

# Formula (118): down = 2 × K − S0 − D
def f_118(D, K, S0): return 2 * K - S0 - D

# Formula (119): Pmax = unlimited
def f_119(unlimited): return unlimited

# Formula (120): Lmax = D − (K − S0 )
def f_120(D, K, S0): return D - (K - S0 )

# Formula (121): fT = ST − S0 − 2 × (ST − K)+ + C
def f_121(C, K, S0, ST): return ST - S0 - 2 * np.maximum(0, ST - K) + C

# Formula (122): up = 2 × K − S0 + C
def f_122(C, K, S0): return 2 * K - S0 + C

# Formula (123): down = S0 − C
def f_123(C, S0): return S0 - C

# Formula (124): Pmax = K − S0 + C
def f_124(C, K, S0): return K - S0 + C

# Formula (125): Lmax = unlimited
def f_125(unlimited): return unlimited

# Formula (126): fT = S0 − ST − 2 × (K − ST )+ + C
def f_126(C, K, S0, ST): return S0 - ST - 2 * np.maximum(0, K - ST ) + C

# Formula (127): up = S0 + C
def f_127(C, S0): return S0 + C

# Formula (128): down = 2 × K − S0 − C
def f_128(C, K, S0): return 2 * K - S0 - C

# Formula (129): Pmax = S0 − K + C
def f_129(C, K, S0): return S0 - K + C

# Formula (130): Lmax = unlimited
def f_130(unlimited): return unlimited

# Formula (131): fT = ST − S0 − (ST − K)+ − (K − ST )+ + C
def f_131(C, K, S0, ST): return ST - S0 - np.maximum(0, ST - K) - np.maximum(0, K - ST ) + C

# Formula (132): = (S0 + K − C)
def f_132(C, K, S0): return (S0 + K - C)

# Formula (133): Pmax = K − S0 + C
def f_133(C, K, S0): return K - S0 + C

# Formula (134): Lmax = S0 + K − C
def f_134(C, K, S0): return S0 + K - C

# Formula (135): fT = ST − S0 − (ST − K)+ − (K 0 − ST )+ + C
def f_135(C, K, S0, ST): return ST - S0 - np.maximum(0, ST - K) - np.maximum(0, K 0 - ST ) + C

# Formula (136): Pmax = K − S0 + C
def f_136(C, K, S0): return K - S0 + C

# Formula (137): Lmax = S0 + K 0 − C
def f_137(C, K, S0): return S0 + K 0 - C

# Formula (138): fT = 2 × (ST − K)+ + (K − ST )+ − D
def f_138(D, K, ST): return 2 * np.maximum(0, ST - K) + np.maximum(0, K - ST ) - D

# Formula (139): up = K +
def f_139(K): return K +

# Formula (140): down = K − D
def f_140(D, K): return K - D

# Formula (141): Pmax = unlimited
def f_141(unlimited): return unlimited

# Formula (142): Lmax = D
def f_142(D): return D

# Formula (143): fT = (ST − K)+ + 2 × (K − ST )+ − D
def f_143(D, K, ST): return np.maximum(0, ST - K) + 2 * np.maximum(0, K - ST ) - D

# Formula (144): up = K + D
def f_144(D, K): return K + D

# Formula (145): down = K −
def f_145(K): return K -

# Formula (146): Pmax = unlimited
def f_146(unlimited): return unlimited

# Formula (147): Lmax = D
def f_147(D): return D

# Formula (148): fT = NL × (ST − K2 )+ − NS × (ST − K1 )+ − H
def f_148(H, K1, K2, NL, NS, ST): return NL * np.maximum(0, ST - K2 ) - NS * np.maximum(0, ST - K1 ) - H

# Formula (149): down = K1 − H/NS , H < 0
def f_149(H, K1, NS): return K1 - H/NS , H < 0

# Formula (150): up = (NL × K2 − NS × K1 + H)/(NL − NS )
def f_150(H, K1, K2, NL, NS): return (NL * K2 - NS * K1 + H)/(NL - NS )

# Formula (151): Pmax = unlimited
def f_151(unlimited): return unlimited

# Formula (152): Lmax = NS × (K2 − K1 ) + H
def f_152(H, K1, K2, NS): return NS * (K2 - K1 ) + H

# Formula (153): fT = NL × (K2 − ST )+ − NS × (K1 − ST )+ − H
def f_153(H, K1, K2, NL, NS, ST): return NL * np.maximum(0, K2 - ST ) - NS * np.maximum(0, K1 - ST ) - H

# Formula (154): up = K1 + H/NS , H < 0
def f_154(H, K1, NS): return K1 + H/NS , H < 0

# Formula (155): down = (NL × K2 − NS × K1 − H)/(NL − NS )
def f_155(H, K1, K2, NL, NS): return (NL * K2 - NS * K1 - H)/(NL - NS )

# Formula (156): Pmax = NL × K2 − NS × K1 − H
def f_156(H, K1, K2, NL, NS): return NL * K2 - NS * K1 - H

# Formula (157): Lmax = NS × (K1 − K2 ) + H
def f_157(H, K1, K2, NS): return NS * (K1 - K2 ) + H

# Formula (158): fT = NL × (ST − K2 )+ − NS × (ST − K1 )+ − H
def f_158(H, K1, K2, NL, NS, ST): return NL * np.maximum(0, ST - K2 ) - NS * np.maximum(0, ST - K1 ) - H

# Formula (159): down = K2 + H/NL , H > 0
def f_159(H, K2, NL): return K2 + H/NL , H > 0

# Formula (160): up = (NS × K1 − NL × K2 − H)/(NS − NL )
def f_160(H, K1, K2, NL, NS): return (NS * K1 - NL * K2 - H)/(NS - NL )

# Formula (161): Pmax = NL × (K1 − K2 ) − H
def f_161(H, K1, K2, NL): return NL * (K1 - K2 ) - H

# Formula (162): Lmax = unlimited
def f_162(unlimited): return unlimited

# Formula (163): fT = NL × (K2 − ST )+ − NS × (K1 − ST )+ − H
def f_163(H, K1, K2, NL, NS, ST): return NL * np.maximum(0, K2 - ST ) - NS * np.maximum(0, K1 - ST ) - H

# Formula (164): up = K2 − H/NL , H > 0
def f_164(H, K2, NL): return K2 - H/NL , H > 0

# Formula (165): down = (NS × K1 − NL × K2 + H)/(NS − NL )
def f_165(H, K1, K2, NL, NS): return (NS * K1 - NL * K2 + H)/(NS - NL )

# Formula (166): Pmax = NL × (K2 − K1 ) − H
def f_166(H, K1, K2, NL): return NL * (K2 - K1 ) - H

# Formula (167): Lmax = NS × K1 − NL × K2 + H
def f_167(H, K1, K2, NL, NS): return NS * K1 - NL * K2 + H

# Formula (168): fT = (ST − K1 )+ + (ST − K3 )+ − 2 × (ST − K2 )+ − D
def f_168(D, K1, K2, K3, ST): return np.maximum(0, ST - K1 ) + np.maximum(0, ST - K3 ) - 2 * np.maximum(0, ST - K2 ) - D

# Formula (169): down = K3 + D
def f_169(D, K3): return K3 + D

# Formula (170): up = K1 − D
def f_170(D, K1): return K1 - D

# Formula (171): Pmax = κ − D
def f_171(D): return κ - D

# Formula (172): Lmax = D
def f_172(D): return D

# Formula (173): fT = (ST − K1 )+ + (ST − K3 )+ − 2 × (ST − K2 )+ − D
def f_173(D, K1, K2, K3, ST): return np.maximum(0, ST - K1 ) + np.maximum(0, ST - K3 ) - 2 * np.maximum(0, ST - K2 ) - D

# Formula (174): = K3 + D
def f_174(D, K3): return K3 + D

# Formula (175): Pmax = K2 − K3 − D
def f_175(D, K2, K3): return K2 - K3 - D

# Formula (176): Lmax = D
def f_176(D): return D

# Formula (177): fT = (K1 − ST )+ + (K3 − ST )+ − 2 × (K2 − ST )+ − D
def f_177(D, K1, K2, K3, ST): return np.maximum(0, K1 - ST ) + np.maximum(0, K3 - ST ) - 2 * np.maximum(0, K2 - ST ) - D

# Formula (178): up = K3 − D
def f_178(D, K3): return K3 - D

# Formula (179): down = K1 + D
def f_179(D, K1): return K1 + D

# Formula (180): Pmax = κ − D
def f_180(D): return κ - D

# Formula (181): Lmax = D
def f_181(D): return D

# Formula (182): fT = (K1 − ST )+ + (K3 − ST )+ − 2 × (K2 − ST )+ − H
def f_182(H, K1, K2, K3, ST): return np.maximum(0, K1 - ST ) + np.maximum(0, K3 - ST ) - 2 * np.maximum(0, K2 - ST ) - H

# Formula (183): down = 2 × K2 − K3 + H
def f_183(H, K2, K3): return 2 * K2 - K3 + H

# Formula (184): Pmax = K3 − K2 − H
def f_184(H, K2, K3): return K3 - K2 - H

# Formula (185): Lmax = 2 × K2 − K1 − K3 + H
def f_185(H, K1, K2, K3): return 2 * K2 - K1 - K3 + H

# Formula (186): fT = 2 × (ST − K2 )+ − (ST − K1 )+ − (ST − K3 )+ + C
def f_186(C, K1, K2, K3, ST): return 2 * np.maximum(0, ST - K2 ) - np.maximum(0, ST - K1 ) - np.maximum(0, ST - K3 ) + C

# Formula (187): up = K3 − C
def f_187(C, K3): return K3 - C

# Formula (188): down = K1 + C
def f_188(C, K1): return K1 + C

# Formula (189): Pmax = C
def f_189(C): return C

# Formula (190): Lmax = κ − C
def f_190(C): return κ - C

# Formula (191): fT = 2 × (K2 − ST )+ − (K1 − ST )+ − (K3 − ST )+ + C
def f_191(C, K1, K2, K3, ST): return 2 * np.maximum(0, K2 - ST ) - np.maximum(0, K1 - ST ) - np.maximum(0, K3 - ST ) + C

# Formula (192): down = K3 + C
def f_192(C, K3): return K3 + C

# Formula (193): up = K1 − C
def f_193(C, K1): return K1 - C

# Formula (194): Pmax = C
def f_194(C): return C

# Formula (195): Lmax = κ − C
def f_195(C): return κ - C

# Formula (196): fT = (K1 − ST )+ − (K2 − ST )+ − (ST − K2 )+ + (ST − K3 )+ + C
def f_196(C, K1, K2, K3, ST): return np.maximum(0, K1 - ST ) - np.maximum(0, K2 - ST ) - np.maximum(0, ST - K2 ) + np.maximum(0, ST - K3 ) + C

# Formula (197): up = K2 + C
def f_197(C, K2): return K2 + C

# Formula (198): down = K2 − C
def f_198(C, K2): return K2 - C

# Formula (199): Pmax = C
def f_199(C): return C

# Formula (200): Lmax = κ − C
def f_200(C): return κ - C

# Formula (201): fT = (K2 − ST )+ + (ST − K2 )+ − (K1 − ST )+ − (ST − K3 )+ − D
def f_201(D, K1, K2, K3, ST): return np.maximum(0, K2 - ST ) + np.maximum(0, ST - K2 ) - np.maximum(0, K1 - ST ) - np.maximum(0, ST - K3 ) - D

# Formula (202): up = K2 + D
def f_202(D, K2): return K2 + D

# Formula (203): down = K2 − D
def f_203(D, K2): return K2 - D

# Formula (204): Pmax = κ − D
def f_204(D): return κ - D

# Formula (205): Lmax = D
def f_205(D): return D

# Formula (206): fT = (ST − K1 )+ − (ST − K2 )+ − (ST − K3 )+ + (ST − K4 )+ − D
def f_206(D, K1, K2, K3, K4, ST): return np.maximum(0, ST - K1 ) - np.maximum(0, ST - K2 ) - np.maximum(0, ST - K3 ) + np.maximum(0, ST - K4 ) - D

# Formula (207): up = K4 − D
def f_207(D, K4): return K4 - D

# Formula (208): down = K1 + D
def f_208(D, K1): return K1 + D

# Formula (209): Pmax = κ − D
def f_209(D): return κ - D

# Formula (210): Lmax = D
def f_210(D): return D

# Formula (211): fT = (K1 − ST )+ − (K2 − ST )+ − (K3 − ST )+ + (K4 − ST )+ − D
def f_211(D, K1, K2, K3, K4, ST): return np.maximum(0, K1 - ST ) - np.maximum(0, K2 - ST ) - np.maximum(0, K3 - ST ) + np.maximum(0, K4 - ST ) - D

# Formula (212): up = K4 − D
def f_212(D, K4): return K4 - D

# Formula (213): down = K1 + D
def f_213(D, K1): return K1 + D

# Formula (214): Pmax = κ − D
def f_214(D): return κ - D

# Formula (215): Lmax = D
def f_215(D): return D

# Formula (216): fT = (ST − K2 )+ + (ST − K3 )+ − (ST − K1 )+ − (ST − K4 )+ + C
def f_216(C, K1, K2, K3, K4, ST): return np.maximum(0, ST - K2 ) + np.maximum(0, ST - K3 ) - np.maximum(0, ST - K1 ) - np.maximum(0, ST - K4 ) + C

# Formula (217): up = K4 − C
def f_217(C, K4): return K4 - C

# Formula (218): down = K1 + C
def f_218(C, K1): return K1 + C

# Formula (219): Pmax = C
def f_219(C): return C

# Formula (220): Lmax = κ − C
def f_220(C): return κ - C

# Formula (221): fT = (K2 − ST )+ + (K3 − ST )+ − (K1 − ST )+ − (K4 − ST )+ + C
def f_221(C, K1, K2, K3, K4, ST): return np.maximum(0, K2 - ST ) + np.maximum(0, K3 - ST ) - np.maximum(0, K1 - ST ) - np.maximum(0, K4 - ST ) + C

# Formula (222): up = K4 − C
def f_222(C, K4): return K4 - C

# Formula (223): down = K1 + C
def f_223(C, K1): return K1 + C

# Formula (224): Pmax = C
def f_224(C): return C

# Formula (225): Lmax = κ − C
def f_225(C): return κ - C

# Formula (226): fT = (K1 − ST )+ + (ST − K4 )+ − (K2 − ST )+ − (ST − K3 )+ + C
def f_226(C, K1, K2, K3, K4, ST): return np.maximum(0, K1 - ST ) + np.maximum(0, ST - K4 ) - np.maximum(0, K2 - ST ) - np.maximum(0, ST - K3 ) + C

# Formula (227): up = K3 + C
def f_227(C, K3): return K3 + C

# Formula (228): down = K2 − C
def f_228(C, K2): return K2 - C

# Formula (229): Pmax = C
def f_229(C): return C

# Formula (230): Lmax = κ − C
def f_230(C): return κ - C

# Formula (231): fT = (K2 − ST )+ + (ST − K3 )+ − (K1 − ST )+ − (ST − K4 )+ − D
def f_231(D, K1, K2, K3, K4, ST): return np.maximum(0, K2 - ST ) + np.maximum(0, ST - K3 ) - np.maximum(0, K1 - ST ) - np.maximum(0, ST - K4 ) - D

# Formula (232): up = K3 + D
def f_232(D, K3): return K3 + D

# Formula (233): down = K2 − D
def f_233(D, K2): return K2 - D

# Formula (234): Pmax = κ − D
def f_234(D): return κ - D

# Formula (235): Lmax = D
def f_235(D): return D

# Formula (236): D
            = K1 − K 2 − D
def f_236(D, K, K1): return K1 - K 2 - D

# Formula (237): Pmax = (K1 − K2 ) − D
def f_237(D, K1, K2): return (K1 - K2 ) - D

# Formula (238): fT = ST − S0 + (K1 − ST )+ − (ST − K2 )+ − H
def f_238(H, K1, K2, S0, ST): return ST - S0 + np.maximum(0, K1 - ST ) - np.maximum(0, ST - K2 ) - H

# Formula (239): = S0 + H
def f_239(H, S0): return S0 + H

# Formula (240): Pmax = K2 − S0 − H
def f_240(H, K2, S0): return K2 - S0 - H

# Formula (241): Lmax = S0 − K1 + H
def f_241(H, K1, S0): return S0 - K1 + H

# Formula (242): fT = −(K1 − ST )+ + (ST − K2 )+ − (ST − K3 )+ − H
def f_242(H, K1, K2, K3, ST): return -np.maximum(0, K1 - ST ) + np.maximum(0, ST - K2 ) - np.maximum(0, ST - K3 ) - H

# Formula (243): = K2 + H, H > 0
def f_243(H, K2): return K2 + H, H > 0

# Formula (244): = K1 + H, H < 0
def f_244(H, K1): return K1 + H, H < 0

# Formula (245): H = 0
def f_245(): return 0

# Formula (246): Pmax = K3 − K2 − H
def f_246(H, K2, K3): return K3 - K2 - H

# Formula (247): Lmax = K1 + H
def f_247(H, K1): return K1 + H

# Formula (248): fT = (K1 − ST )+ − (ST − K2 )+ + (ST − K3 )+ − H
def f_248(H, K1, K2, K3, ST): return np.maximum(0, K1 - ST ) - np.maximum(0, ST - K2 ) + np.maximum(0, ST - K3 ) - H

# Formula (249): = K1 − H, H > 0
def f_249(H, K1): return K1 - H, H > 0

# Formula (250): = K2 − H, H < 0
def f_250(H, K2): return K2 - H, H < 0

# Formula (251): H = 0
def f_251(): return 0

# Formula (252): Pmax = K1 − H
def f_252(H, K1): return K1 - H

# Formula (253): Lmax = K3 − K2 + H
def f_253(H, K2, K3): return K3 - K2 + H

# Formula (254): fT = −(K1 − ST )+ + (K2 − ST )+ − (ST − K3 )+ − H
def f_254(H, K1, K2, K3, ST): return -np.maximum(0, K1 - ST ) + np.maximum(0, K2 - ST ) - np.maximum(0, ST - K3 ) - H

# Formula (255): = K2 − H, H > 0
def f_255(H, K2): return K2 - H, H > 0

# Formula (256): = K3 − H, H < 0
def f_256(H, K3): return K3 - H, H < 0

# Formula (257): H = 0
def f_257(): return 0

# Formula (258): Pmax = K2 − K1 − H
def f_258(H, K1, K2): return K2 - K1 - H

# Formula (259): Lmax = unlimited
def f_259(unlimited): return unlimited

# Formula (260): fT = (K1 − ST )+ − (K2 − ST )+ + (ST − K3 )+ − H
def f_260(H, K1, K2, K3, ST): return np.maximum(0, K1 - ST ) - np.maximum(0, K2 - ST ) + np.maximum(0, ST - K3 ) - H

# Formula (261): = K3 + H, H > 0
def f_261(H, K3): return K3 + H, H > 0

# Formula (262): = K2 + H, H < 0
def f_262(H, K2): return K2 + H, H < 0

# Formula (263): H = 0
def f_263(): return 0

# Formula (264): Pmax = unlimited
def f_264(unlimited): return unlimited

# Formula (265): Lmax = K2 − K1 + H
def f_265(H, K1, K2): return K2 - K1 + H

# Formula (266): =           −1
def f_266(): return -1

# Formula (267): Ricum =             −1
def f_267(): return -1

# Formula (268): Ri     =            Ri (t)
def f_268(Ri, t): return Ri (t)

# Formula (269): adj =
def f_269(): return

# Formula (270): σi2 =             (Ri (t) − Rimean )2
def f_270(Ri, Rimean, t): return (Ri (t) - Rimean )2

# Formula (271): wi = 1
def f_271(): return 1

# Formula (0): Qi = I × wi /Pi
def f_0(I, Pi, wi): return I * wi /Pi

# Formula (272): = 1
def f_272(): return 1

# Formula (273): wi = 0
def f_273(): return 0

# Formula (274): SUEi =
def f_274(): return

# Formula (275): wA = 1
def f_275(): return 1

# Formula (276): sAi = rank(fAi ) −           rank(fAj )
def f_276(fAi, fAj, rank): return rank(fAi ) -           rank(fAj )

# Formula (277): si =       sAi
def f_277(sAi): return sAi

# Formula (278): = αi + β1,i MKT(t) + β2,i SMB(t) + β3,i HML(t) + i (t)
def f_278(HML, MKT, SMB, i, t): return αi + β1,i MKT(t) + β2,i SMB(t) + β3,i HML(t) + i (t)

# Formula (279): = Ri (t) − β1,i MKT(t) − β2,i SMB(t) − β3,i HML(t)
def f_279(HML, MKT, Ri, SMB, i, t): return Ri (t) - β1,i MKT(t) - β2,i SMB(t) - β3,i HML(t)

# Formula (280): i    =                   i (t)
def f_280(i, t): return i (t)

# Formula (283): RA =          −1
def f_283(): return -1

# Formula (284): RB =          −1
def f_284(): return -1

# Formula (285): RA = ln
def f_285(ln): return ln

# Formula (286): RB = ln
def f_286(ln): return ln

# Formula (287): R=     (RA + RB )
def f_287(RA, RB): return (RA + RB )

# Formula (290): = I
def f_290(I): return I

# Formula (291): QB = 0
def f_291(): return 0

# Formula (292): Ri = ln
def f_292(ln): return ln

# Formula (293): R=          Ri
def f_293(Ri): return Ri

# Formula (295): = I
def f_295(I): return I

# Formula (296): Qi = 0
def f_296(): return 0

# Formula (298): γ=P
def f_298(P): return P

# Formula (299): NA =           ΛiA > 0
def f_299(iA): return ΛiA > 0

# Formula (300): N=            NA
def f_300(NA): return NA

# Formula (301): ΛiA = δG(i),A
def f_301(A, G, i): return δG(i),A

# Formula (303): Ri =         ΛiA fA + εi
def f_303(fA, i, iA): return ΛiA fA + εi

# Formula (304): f = Q−1 ΛT R
def f_304(Q, R, T): return Q-1 ΛT R

# Formula (305): Q = ΛT Λ
def f_305(T): return ΛT Λ

# Formula (306): ε = R − Λ Q−1 ΛT R
def f_306(Q, R, T): return R - Λ Q-1 ΛT R

# Formula (307): QAB = NA δAB
def f_307(AB, NA): return NA δAB

# Formula (308): RA =         Rj
def f_308(Rj): return Rj

# Formula (310): ΛiA = 0,        A = 1, . . . , K
def f_310(A, K): return 0,        A = 1, . . . , K

# Formula (311): νi = 0
def f_311(): return 0

# Formula (312): ΛiA = νi
def f_312(i): return νi

# Formula (313): A = 1, . . . , K
def f_313(K): return 1, . . . , K

# Formula (314): e=Z ε
def f_314(Z): return Z ε

# Formula (315): ε = R − Ω Q−1 ΩT Z R
def f_315(Q, R, T, Z): return R - Ω Q-1 ΩT Z R

# Formula (316): Z = diag(zi )
def f_316(diag, zi): return diag(zi )

# Formula (317): Q = ΩT Z Ω
def f_317(T, Z): return ΩT Z Ω

# Formula (318): ei = 0
def f_318(): return 0

# Formula (319): =       P (t)
def f_319(P, t): return P (t)

# Formula (321): Signal =
def f_321(): return

# Formula (322): Signal =
def f_322(): return

# Formula (323): Signal =                                      0
def f_323(): return 0

# Formula (324): Signal =
def f_324(): return

# Formula (325): C=
def f_325(): return

# Formula (326): R = 2 × C − PL
def f_326(C, PL): return 2 * C - PL

# Formula (327): S = 2 × C − PH
def f_327(C, PH): return 2 * C - PH

# Formula (328): Signal =
def f_328(): return

# Formula (331): Signal =
def f_331(): return

# Formula (332): =              −1
def f_332(): return -1

# Formula (333): =        V (t + s)
def f_333(V, s, t): return V (t + s)

# Formula (334): =           P (t + s)
def f_334(P, s, t): return P (t + s)

# Formula (335): =           P (t + s)
def f_335(P, s, t): return P (t + s)

# Formula (338): =          (X
def f_338(X): return (X

# Formula (339): =           Y (t0α (t))
def f_339(Y, t, t0): return Y (t0α (t))

# Formula (340): =            Y (t0α (t)) wα + v
def f_340(Y, t, t0, v, w): return Y (t0α (t)) wα + v

# Formula (341): Signal =
def f_341(): return

# Formula (342): P =         Ei Di
def f_342(Di, Ei): return Ei Di

# Formula (343): V2 =             Cij Di Dj
def f_343(Cij, Di, Dj): return Cij Di Dj

# Formula (344): S = P/V
def f_344(P, V): return P/V

# Formula (345): wi = Di /I
def f_345(Di, I): return Di /I

# Formula (346): = 1
def f_346(): return 1

# Formula (347): Pe =        E i wi
def f_347(E, i, wi): return E i wi

# Formula (348): 2 =           Cij wi wj
def f_348(Cij, wi, wj): return Cij wi wj

# Formula (350): wi = γ            Cij−1 Ej
def f_350(Cij, Ej): return γ            Cij-1 Ej

# Formula (351): =         Cij wi wj −     E i wi
def f_351(Cij, E, i, wi, wj): return Cij wi wj -     E i wi

# Formula (353): wi =      C Ej
def f_353(C, Ej): return C Ej

# Formula (354): =         Cij wi wj −     E i wi − µ     wi
def f_354(Cij, E, i, wi, wj): return Cij wi wj -     E i wi - µ     wi

# Formula (356): wj = Ei + µ
def f_356(Ei): return Ei + µ

# Formula (357): wi = 0
def f_357(): return 0

# Formula (358): wi =         C Ej −        Cij−1 PN
def f_358(C, Cij, Ej, PN): return C Ej -        Cij-1 PN

# Formula (359): Rule =
def f_359(): return

# Formula (360): Ei =       Ris
def f_360(Ris): return Ris

# Formula (361): =               −1
def f_361(): return -1

# Formula (362): Rule =
def f_362(): return

# Formula (363): Rule =
def f_363(): return

# Formula (364): = αi + β1,i MKT(t) + β2,i SMB(t) + β3,i HML(t) + i (t)
def f_364(HML, MKT, SMB, i, t): return αi + β1,i MKT(t) + β2,i SMB(t) + β3,i HML(t) + i (t)

# Formula (365): = αi + β1,i MKT(t) + β2,i SMB(t) + β3,i HML(t) + β4,i MOM(t) + i (t)
def f_365(HML, MKT, MOM, SMB, i, t): return αi + β1,i MKT(t) + β2,i SMB(t) + β3,i HML(t) + β4,i MOM(t) + i (t)

# Formula (366): R2 = 1 −
def f_366(): return 1 -

# Formula (367): SSres =     2i (t)
def f_367(i, t): return 2i (t)

# Formula (368): SStot =         (Ri (t) − R(t))2
def f_368(R, Ri, t): return (Ri (t) - R(t))2

# Formula (369): =       Ri (t)
def f_369(Ri, t): return Ri (t)

# Formula (370): IBS =
def f_370(): return

# Formula (371): wi = γ1 Ricum
def f_371(Ricum): return γ1 Ricum

# Formula (372): wi = γ2 Ricum /σi
def f_372(Ricum, i): return γ2 Ricum /σi

# Formula (373): wi = γ3 Ricum /σi2
def f_373(Ricum, i2): return γ3 Ricum /σi2

# Formula (374): = −
def f_374(): return -

# Formula (375): = P (t, T ) + kδ            P (t, Ti )
def f_375(P, T, Ti, k, t): return P (t, T ) + kδ            P (t, Ti )

# Formula (376): = P (T0 , T ) + kδ          P (T0 , Ti )
def f_376(P, T, T0, Ti, k): return P (T0 , T ) + kδ          P (T0 , Ti )

# Formula (377): k=     Pn
def f_377(Pn): return Pn

# Formula (378): =                  −1
def f_378(): return -1

# Formula (379): Xi = L(Ti−1 )δ =                     −1
def f_379(L, Ti): return L(Ti-1 )δ =                     -1

# Formula (380): V0 = 1 − [P (T0 , Tn ) − P (T0 , T )]
def f_380(P, T, T0, Tn): return 1 - [P (T0 , Tn ) - P (T0 , T )]

# Formula (381): V0 = P (T0 , T ) + V0coupons
def f_381(P, T, T0, V0coupons): return P (T0 , T ) + V0coupons

# Formula (382): V0coupons = 1
def f_382(): return 1

# Formula (383): k = Pn
def f_383(Pn): return Pn

# Formula (384): =                                      (Ti − t) P (t, Ti )
def f_384(P, Ti, t): return (Ti - t) P (t, Ti )

# Formula (385): = −
def f_385(): return -

# Formula (386): = MacD(t, T )/(1 + Y δ)
def f_386(MacD, T, Y, t): return MacD(t, T )/(1 + Y δ)

# Formula (387): = −                = ModD(t, T ) Pc (t, T )
def f_387(ModD, Pc, T, t): return -                = ModD(t, T ) Pc (t, T )

# Formula (388): = −
def f_388(): return -

# Formula (390): D=
def f_390(): return

# Formula (391): = D∗ = D
def f_391(D): return D∗ = D

# Formula (392): C=
def f_392(): return

# Formula (393): = T∗
def f_393(T): return T∗

# Formula (394): =               (T2 − T1 )2 > 0
def f_394(T1, T2): return (T2 - T1 )2 > 0

# Formula (395): T =       Ti
def f_395(Ti): return Ti

# Formula (396): P = F/(1 + Y δ)T∗ /δ
def f_396(F, T, Y): return F/(1 + Y δ)T∗ /δ

# Formula (397): 2 = P
def f_397(P): return P

# Formula (398): D2 = P D
def f_398(D, P): return P D

# Formula (399): D = T∗ /(1 + Y δ)
def f_399(T, Y): return T∗ /(1 + Y δ)

# Formula (400): 3 = P
def f_400(P): return P

# Formula (401): D3 = P D
def f_401(D, P): return P D

# Formula (402): 3 = P C
def f_402(C, P): return P C

# Formula (403): C = T∗ (T∗ + δ)/(1 + Y δ)2
def f_403(T, Y): return T∗ (T∗ + δ)/(1 + Y δ)2

# Formula (404): P3 = P 2
def f_404(P): return P 2

# Formula (405): D3 = P2 D2
def f_405(D2, P2): return P2 D2

# Formula (406): D1 = P3 D3 =         P2 D2
def f_406(D2, D3, P2, P3): return P3 D3 =         P2 D2

# Formula (407): D3 = P2 D2
def f_407(D2, P2): return P2 D2

# Formula (408): D1 = β P3 D3
def f_408(D3, P3): return β P3 D3

# Formula (409): β=
def f_409(): return

# Formula (410): Si =         βr Iir + γ Ti + i
def f_410(Iir, Ti, i, r): return βr Iir + γ Ti + i

# Formula (411): = Si − i
def f_411(Si, i): return Si - i

# Formula (412): Iir = 1
def f_412(): return 1

# Formula (413): =
def f_413(): return

# Formula (414): = R(t, T ) ∆t + Croll (t, t + ∆t, T )
def f_414(Croll, R, T, t): return R(t, T ) ∆t + Croll (t, t + ∆t, T )

# Formula (416): Rule =
def f_416(): return

# Formula (417): basis = CDS spread − bond spread
def f_417(CDS, bond, spread): return CDS spread - bond spread

# Formula (418): = ±[C1 − C2 (t)]
def f_418(C1, C2, t): return +-[C1 - C2 (t)]

# Formula (419): C1 = rswap − YT reasury
def f_419(YT, reasury, rswap): return rswap - YT reasury

# Formula (420): = L(t) − r(t)
def f_420(L, r, t): return L(t) - r(t)

# Formula (421): = [S(t) − D(t, T )] exp (r (T − t))
def f_421(D, S, T, r, t): return [S(t) - D(t, T )] exp (r (T - t))

# Formula (422): =
def f_422(): return

# Formula (423): σI2 =           wi wj σi σj ρij
def f_423(i, ij, j, wi, wj): return wi wj σi σj ρij

# Formula (424): i = PN
def f_424(PN): return PN

# Formula (425): ψij = ξi2 δij +          λ(A) Vi     Vj
def f_425(A, Vi, Vj, i2, ij): return ξi2 δij +          λ(A) Vi     Vj

# Formula (426): ξi2 = 1 −         λ(A) Vi
def f_426(A, Vi): return 1 -         λ(A) Vi

# Formula (427): σI2 =     wi wj σi σj ψij =   wi2 σi2 ξi2 +       λ(A) Vi wi σi
def f_427(A, Vi, i, i2, ij, j, wi, wi2, wj): return wi wj σi σj ψij =   wi2 σi2 ξi2 +       λ(A) Vi wi σi

# Formula (428): Rule =
def f_428(): return

# Formula (429): IX = PU X1 − PV IX
def f_429(IX, PU, PV, X1): return PU X1 - PV IX

# Formula (430): D=
def f_430(): return

# Formula (431): Rule =
def f_431(): return

# Formula (432): wi = σ X          Cij−1 σj ρj
def f_432(Cij, X, j): return σ X          Cij-1 σj ρj

# Formula (433): wi = 1
def f_433(): return 1

# Formula (434): = N × (v(T ) − K)
def f_434(K, N, T, v): return N * (v(T ) - K)

# Formula (435): =        R (t)
def f_435(R, t): return R (t)

# Formula (436): = ln
def f_436(ln): return ln

# Formula (437): = S ∗ (t) + ν(t)
def f_437(S, t): return S ∗ (t) + ν(t)

# Formula (438): g=      [S(t) − S ∗ (t)]2 + λ      [S ∗ (t + 1) − 2S ∗ (t) + S ∗ (t − 1)]2
def f_438(S, t): return [S(t) - S ∗ (t)]2 + λ      [S ∗ (t + 1) - 2S ∗ (t) + S ∗ (t - 1)]2

# Formula (440): =                  (1 + rf )
def f_440(rf): return (1 + rf )

# Formula (441): = S(t)
def f_441(S, t): return S(t)

# Formula (442): = s(t) − f (t, T )
def f_442(T, f, s, t): return s(t) - f (t, T )

# Formula (443): = ln            ≈ rf − rd
def f_443(ln, rd, rf): return ln            ≈ rf - rd

# Formula (444): =       Di (t, T )
def f_444(Di, T, t): return Di (t, T )

# Formula (445): σ12 = Var(R1 (ts ))
def f_445(R1, Var, ts): return Var(R1 (ts ))

# Formula (446): σ22 = Var(R2 (ts ))
def f_446(R2, Var, ts): return Var(R2 (ts ))

# Formula (447): ρ = Cor(R1 (ts ), R2 (ts ))
def f_447(Cor, R1, R2, ts): return Cor(R1 (ts ), R2 (ts ))

# Formula (448): = w1 R1 (ts ) + w2 R2 (ts )
def f_448(R1, R2, ts, w1, w2): return w1 R1 (ts ) + w2 R2 (ts )

# Formula (449): w2 = 1
def f_449(): return 1

# Formula (451): w1 = 2 2 2
def f_451(): return 2 2 2

# Formula (452): w2 = 2 1 2
def f_452(): return 2 1 2

# Formula (453): = Bid(A → B) × Bid(B → C) ×
def f_453(A, B, Bid, C): return Bid(A → B) * Bid(B → C) *

# Formula (454): φ = P1 /P2
def f_454(P1, P2): return P1 /P2

# Formula (455): v = P5 /P0
def f_455(P0, P5): return P5 /P0

# Formula (456): Si =               Ris − Ri
def f_456(Ri, Ris): return Ris - Ri

# Formula (457): Ri =       Ris
def f_457(Ris): return Ris

# Formula (459): = κ [a − X(t)] dt + σ dW (t)
def f_459(X, a, dW, dt, t): return κ [a - X(t)] dt + σ dW (t)

# Formula (460): = Et (S(T ))
def f_460(Et, S, T): return Et (S(T ))

# Formula (461): = Et (X(T )) + Vt (X(T ))
def f_461(Et, T, Vt, X): return Et (X(T )) + Vt (X(T ))

# Formula (463): =
                         [S∗ (T ) − F (T, T )] + [S(T ) − S∗ (T )] + F (t, T )
def f_463(F, S, T, t): return [S∗ (T ) - F (T, T )] + [S(T ) - S∗ (T )] + F (t, T )

# Formula (464): = B(0, T ) − B(t, T )
def f_464(B, T, t): return B(0, T ) - B(t, T )

# Formula (465): = B(t, T ) − B(0, T )
def f_465(B, T, t): return B(t, T ) - B(0, T )

# Formula (466): = S(t) − F (t, T )
def f_466(F, S, T, t): return S(t) - F (t, T )

# Formula (467): hC = C
def f_467(C): return C

# Formula (468): hD = β
def f_468(): return β

# Formula (469): Rm =       Ri
def f_469(Ri): return Ri

# Formula (470): wi = −γ [Ri − Rm ]
def f_470(Ri, Rm): return -γ [Ri - Rm ]

# Formula (471): = 1
def f_471(): return 1

# Formula (472): vi = ln(Vi /Vi0 )
def f_472(Vi, Vi0, ln): return ln(Vi /Vi0 )

# Formula (473): ui = ln(Ui /Ui0 )
def f_473(Ui, Ui0, ln): return ln(Ui /Ui0 )

# Formula (474): wi = γ
def f_474(): return γ

# Formula (475): ηi = sign(Ri )
def f_475(Ri, sign): return sign(Ri )

# Formula (476): = 1
def f_476(): return 1

# Formula (477): wi = γ         −
def f_477(): return γ         -

# Formula (478): wi = γ+   ,       i ∈ H+
def f_478(H, i): return γ+   ,       i ∈ H+

# Formula (479): wi = γ− ,         i ∈ H−
def f_479(H, i): return γ- ,         i ∈ H-

# Formula (480): wi = 0
def f_480(): return 0

# Formula (481): =         pα (t) max(min(`α , Ld ) − La , 0)
def f_481(La, Ld, max, min, p, t): return pα (t) max(min(`α , Ld ) - La , 0)

# Formula (482): M=P −C
def f_482(C, P): return P -C

# Formula (483): P =S   Di ∆i [Mtr − L(ti )]
def f_483(Di, L, Mtr, S, i, ti): return S   Di ∆i [Mtr - L(ti )]

# Formula (484): C=           Di [L(ti ) − L(ti−1 )]
def f_484(Di, L, ti): return Di [L(ti ) - L(ti-1 )]

# Formula (485): = (S − S∗ )             Di ∆i [Mtr − L(ti )]
def f_485(Di, L, Mtr, S, i, ti): return (S - S∗ )             Di ∆i [Mtr - L(ti )]

# Formula (486): D = ∂M/∂S =                Di ∆i [Mtr − L(ti )]
def f_486(Di, L, M, Mtr, S, i, ti): return ∂M/∂S =                Di ∆i [Mtr - L(ti )]

# Formula (487): ix =
def f_487(): return

# Formula (488): high =
def f_488(): return

# Formula (489): CDS =
def f_489(): return

# Formula (490): = (Mlong Slong − Mshort Sshort ) ∆t
def f_490(Mlong, Mshort, Slong, Sshort, t): return (Mlong Slong - Mshort Sshort ) ∆t

# Formula (491): L = Mlong − Mshort
def f_491(Mlong, Mshort): return Mlong - Mshort

# Formula (492): h=∆×C
def f_492(C): return ∆*C

# Formula (493): = ∂V /∂S
def f_493(S, V): return ∂V /∂S

# Formula (494): PC = PB + V
def f_494(PB, V): return PB + V

# Formula (495): R = rlong − rshort (1 − τ )
def f_495(rlong, rshort): return rlong - rshort (1 - τ )

# Formula (496): income = It = D + C = 1−τ     c
def f_496(C, D, It, c): return It = D + C = 1-τ     c

# Formula (498): = K − [S0 − D (1 + κ)]
def f_498(D, K, S0): return K - [S0 - D (1 + κ)]

# Formula (499): L = S0 + Vput (K, T ) − K = D (1 + κ)
def f_499(D, K, S0, T, Vput): return S0 + Vput (K, T ) - K = D (1 + κ)

# Formula (500): ixed = (1 + K)T − 1
def f_500(K, T): return (1 + K)T - 1

# Formula (501): loating = I(T )/I(0) − 1
def f_501(I, T): return I(T )/I(0) - 1

# Formula (502): = K
def f_502(K): return K

# Formula (503): = I(t)/I(t − 1) − 1
def f_503(I, t): return I(t)/I(t - 1) - 1

# Formula (504): = Ni I(ti )/I(0)
def f_504(I, Ni, ti): return Ni I(ti )/I(0)

# Formula (506): = Cswap (ti ) + CT IP S (ti ) = Ni (1 + K)ti
def f_506(CT, Cswap, IP, K, Ni, S, ti): return Cswap (ti ) + CT IP S (ti ) = Ni (1 + K)ti

# Formula (508): = PT reasury − PT IP S −           S(ti )
def f_508(IP, PT, S, reasury, ti): return PT reasury - PT IP S -           S(ti )

# Formula (509): ICDD =          max(0, Ti − Tbase )
def f_509(Tbase, Ti, max): return max(0, Ti - Tbase )

# Formula (510): IHDD =           max(0, Tbase − Ti )
def f_510(Tbase, Ti, max): return max(0, Tbase - Ti )

# Formula (511): Ti =
def f_511(): return

# Formula (512): utures = Cov(qw , IHDD )/Var(IHDD )
def f_512(Cov, IHDD, Var, qw): return Cov(qw , IHDD )/Var(IHDD )

# Formula (513): put = −Cov (qw , max(K − IHDD , 0)) /Var (max(K − IHDD , 0))
def f_513(Cov, IHDD, K, Var, max, qw): return -Cov (qw , max(K - IHDD , 0)) /Var (max(K - IHDD , 0))

# Formula (514): utures = Cov(qw , ICDD )/Var(ICDD )
def f_514(Cov, ICDD, Var, qw): return Cov(qw , ICDD )/Var(ICDD )

# Formula (515): call = Cov (qw , max(ICDD − K, 0)) /Var (max(ICDD − K, 0))
def f_515(Cov, ICDD, K, Var, max, qw): return Cov (qw , max(ICDD - K, 0)) /Var (max(ICDD - K, 0))

# Formula (516): H = QF /QE
def f_516(QE, QF): return QF /QE

# Formula (517): S = PE − H PF
def f_517(H, PE, PF): return PE - H PF

# Formula (518): h = H FE /FF
def f_518(FE, FF, H): return H FE /FF

# Formula (519): =                HMD
def f_519(HMD): return HMD

# Formula (520): =                         −1
def f_520(): return -1

# Formula (521): =              −1
def f_521(): return -1

# Formula (523): =            R(t0 )
def f_523(R, t0): return R(t0 )

# Formula (525): =               [R(t,
def f_525(R, t): return [R(t,

# Formula (528): =
def f_528(): return

# Formula (529): =       max(±R(t  b 0 ), 0)
def f_529(R, b, max, t): return max(+-R(t  b 0 ), 0)

# Formula (531): = 1
def f_531(): return 1

# Formula (532): = hi(`) (Y~ (`) ),       ` = 2, . . . , L
def f_532(L, Y, hi): return hi(`) (Y~ (`) ),       ` = 2, . . . , L

# Formula (533): =                Ai(`) j (`−1) Xj (`−1) + Bi(`)
def f_533(Ai, Bi, Xj, j): return Ai(`) j (`-1) Xj (`-1) + Bi(`)

# Formula (534): = max Yi(`) , 0 , ` = 2, . . . , L − 1 (ReLU)
def f_534(L, ReLU, Yi, max): return max Yi(`) , 0 , ` = 2, . . . , L - 1 (ReLU)

# Formula (535): = Yi(L)         Yj (L)    (softmax)
def f_535(L, Yi, Yj, softmax): return Yi(L)         Yj (L)    (softmax)

# Formula (536): E=−                     Sα (t) ln(pα (t))
def f_536(S, ln, p, t): return -                     Sα (t) ln(pα (t))

# Formula (537): Signal =
def f_537(): return

# Formula (538): =
def f_538(): return

# Formula (539): =
def f_539(): return

# Formula (540): = P (Xi |Cα )
def f_540(C, P, Xi): return P (Xi |Cα )

# Formula (541): = γ P (Cα )          P (Xi |Cα )
def f_541(C, P, Xi): return γ P (Cα )          P (Xi |Cα )

# Formula (542): γ = 1/P (X1 , . . . , XN )
def f_542(P, X1, XN): return 1/P (X1 , . . . , XN )

# Formula (543): =          Qiaα
def f_543(Qia): return Qiaα

# Formula (544): Qiaα = P (wa |Cα ), Xia = 1
def f_544(C, P, Xia, wa): return P (wa |Cα ), Xia = 1

# Formula (545): Qiaα = 1 − P (wa |Cα ), Xia = 0
def f_545(C, P, Xia, wa): return 1 - P (wa |Cα ), Xia = 0

# Formula (546): Cpred = argmax Cα∈{1,...,K} P (Cα )               [P (wa |Cα )]Xia [1 − P (wa |Cα )]1−Xia
def f_546(C, K, P, Xia, argmax, wa): return argmax Cα∈{1,...,K} P (Cα )               [P (wa |Cα )]Xia [1 - P (wa |Cα )]1-Xia

# Formula (547): CA = max 0, min                       ,1
def f_547(max, min): return max 0, min                       ,1

# Formula (549): Eport =         E i wi
def f_549(E, i, wi): return E i wi

# Formula (550): Eport =         [Ei wi − τi |wi |]
def f_550(Ei, i, wi): return [Ei wi - τi |wi |]

# Formula (551): f = sign(Ei ) max(|Ei | − τi , 0)
def f_551(Ei, i, max, sign): return sign(Ei ) max(|Ei | - τi , 0)

# Formula (552): Eport =          Eief f wi
def f_552(Eief, f, wi): return Eief f wi

# Formula (553): Ti = ζ σi
def f_553(i): return ζ σi

# Formula (554): τi = ζ
def f_554(): return ζ

# Formula (555): = ln
def f_555(ln): return ln

# Formula (556): = γiadj (t) PiO (t)
def f_556(PiO, iadj, t): return γiadj (t) PiO (t)

# Formula (557): = C
def f_557(C): return C