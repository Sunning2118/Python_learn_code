# 最后的行程为：
# LAX --> SFO --> NYC --> ORD --> DNV
# iNPUT: flights = [("ORD", "DNV"), ("SFO", "NYC"), ("LAX", "SFO"), ("NYC","ORD")]
# return: ["LAX" , "SFO" , "NYC" , "ORD" , "DNV"]


# 题目二：其他条件同上，唯一不同在于： 不止存在一个行程
# ORD --> DNV
# SFO --> NYC
# LAX --> SFO
# NYC --> ORD

# DFW --> NJA
# NJA --> BOS

# 最后的行程为：
# (1) LAX --> SFO --> NYC --> ORD --> DNV
# (2) DFW --> NJA --> BOS
# flights = [("ORD", "DNV"), ("SFO", "NYC"), ("NJA", "BOS"), ("LAX", "SFO"), ("NYC","ORD"), ("DFW", "NJA")]
# return: [["LAX" , "SFO" , "NYC" , "ORD" , "DNV"], ["DFW", "NJA", "BOS"]]

# 题目三：其他条件同题目一，唯一不同在于：同一个城市可以去往平行的多个城市
# ORD --> DNV
# SFO --> NYC
# LAX --> SFO
# NYC --> ORD
# SFO --> BOS
# ORD --> NJA
# INPUT: flights = [("ORD", "DNV"), ("SFO", "NYC"), ("LAX", "SFO"), ("NYC","ORD"), ("SFO", "BOS"), ("ORD", "NJA")]
# 如何表达行程 trip =?
