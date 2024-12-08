import pandas  as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

import os
import shutil

from wordcloud import WordCloud
import textwrap
from tabulate import tabulate
from ultils import helper


def GetProductInfoByCode(df_product, product_code):
    # Filter the product data by product name
    df_product_info = df_product.loc[df_product['ma_san_pham'] == product_code]

    # Check if the product exists
    if df_product_info.empty:
        print("Sản phẩm không tồn tại trong dữ liệu.")
        return

    # # Prepare the data
    df_info = GenerateProductDetailTable(df_product_info)
    return df_info


    # df_anlyze, sentiment_data, sentiment_categories = GetProductReview(df_review_new, product_code)
    # # Check if reviews exist
    # if df_anlyze.empty:
    #     print("Không có dữ liệu đánh giá cho sản phẩm này.")
    #     return

    # print("\nPhân tích sản phẩm:")
    # # print("Tổng lượt Reviews: ", df_anlyze['Total_Sentiment'].drop_duplicates().values[0])
    # DrawPieChart(sentiment_data, sentiment_categories)

    # # Generate word clouds for each sentiment category
    # s_positive = df_anlyze[df_anlyze['Categorized'] == 1]
    # s_negative = df_anlyze[df_anlyze['Categorized'] == 0]

    # print("\nTop 50 từ Positive về sản phẩm:")
    # res_wcloud_visualize(s_positive, 'Pos_words', 'Word Cloud - Positive Sentiment')

    # print("\nTop 50 từ Negative về sản phẩm:")
    # res_wcloud_visualize(s_negative, 'Neg_words', 'Word Cloud - Negative Sentiment')

def GenerateProductDetailTable(df_product_info):
    short_desc = ' '.join(df_product_info['mo_ta'].values[0].split()[:100])
    data = {
        'Thông tin': ['Tên sản phẩm', 'Giá bán', 'Giá gốc', 'Phân loại', 'Mô tả', 'Điểm trung bình'],
        'Chi tiết': [
            df_product_info['ten_san_pham'].values[0],
            f"{df_product_info['gia_ban'].values[0]:,} VNĐ",  # Format as currency
            f"{df_product_info['gia_goc'].values[0]:,.0f} VNĐ",  # Format as currency
            df_product_info['phan_loai'].values[0].replace("\n", ", "),  # Replace newlines with commas
            f"{short_desc}...",  # Use first 100 words of description
            f"{df_product_info['diem_trung_binh'].values[0]} *"
        ]
    }
    # Convert to a DataFrame for display
    return pd.DataFrame(data)

def wcloud_visualize(df_sub, column, title):
    # Check if the column has data
    if df_sub[column].str.len().sum() == 0:
        print(f"Không có đủ dữ liệu để tạo Word Cloud cho {title}.")
        return

    # Generate the word cloud
    text = df_sub[column].str.cat(sep=' ')
    wc = WordCloud(
        background_color='white',
        max_words=50,
        width=1600,
        height=900,
        max_font_size=400
    )
    wc.generate(text)

    plt.figure(figsize=(6, 6))
    plt.imshow(wc, interpolation='bilinear')
    plt.title(title, fontsize=16)
    plt.axis('off')
    st.pyplot(plt)

def DrawPieChart(data, categories):
    # Plot the enhanced pie chart
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.pie(data, labels=categories, autopct='%1.1f%%', colors=['salmon', 'skyblue'])
    ax.set_title('Sentiment Rate by Category')
    ax.axis('equal')

    # Show the plot using Streamlit
    st.pyplot(fig)

def GetProductReview(df_review, product_code):

  # Analyze the reviews for the selected product
  df_anlyze = df_review.loc[df_review['ma_san_pham'] == product_code]

  # Prepare data for the pie chart
  sentiment_categories = ['Negative', 'Positive']
  sentiment_data = [0, 0]  # Initialize rates with 0 for all categories

  # Populate sentiment data
  for index, row in df_anlyze.iterrows():
      if row['Categorized'] == 0:  # Negative
          sentiment_data[0] = row['Sentiment_Rate (%)']
      elif row['Categorized'] == 1:  # Positive
          sentiment_data[1] = row['Sentiment_Rate (%)']

  return df_anlyze, sentiment_data, sentiment_categories