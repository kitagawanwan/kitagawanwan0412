pip install sympy


import streamlit as st
import sympy
import time

def factorize_with_timing(n):
    start_time = time.time()
    factors = sympy.factorint(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return factors, elapsed_time

def main():
    st.title("大きな整数の素因数分解アプリ")

    st.write("このアプリは、与えられた整数の素因数分解を行い、計算時間を表示します。")

    number_to_factorize = st.text_input("素因数分解対象の整数を入力してください:")

    if st.button("素因数分解"):
        try:
            # 文字列を整数に変換
            num = int(number_to_factorize)

            with st.spinner("計算中..."):
                factors, elapsed_time = factorize_with_timing(num)

            st.write(f"素因数分解結果: {factors}")
            st.write(f"素因数分解にかかる時間: {elapsed_time:.4f} 秒")
        except ValueError:
            st.error("無効な整数が入力されました。整数を入力してください。")
        except Exception as e:
            st.error(f"素因数分解中にエラーが発生しました: {str(e)}")

if __name__ == "__main__":
    main()

