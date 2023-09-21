tart_time = time.time()  # 計測開始

 

Pa = pow(code_a, x, n)
Pb = pow(code_b, x, n)

 

end_time = time.time()  # 計測終了
elapsed_time = end_time - start_time

 

print(f"Pa: {Pa}")
print(f"Pb: {Pb}")
print(f"複合にかかる時間: {elapsed_time} 秒")
 