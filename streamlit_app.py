tart_time = time.time()  # 計測開始

 

Pa = pow(code_a, x, n)
Pb = pow(code_b, x, n)

 

end_time = time.time()  # 計測終了
elapsed_time = end_time - start_time

 

st.write(f"Pa: {Pa}")
st.write(f"Pb: {Pb}")
st.write(f"複合にかかる時間: {elapsed_time} 秒")
 