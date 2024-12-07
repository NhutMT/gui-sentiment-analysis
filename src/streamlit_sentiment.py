import streamlit as st
from PIL import Image
import pickle
import pandas as pd
import numpy as np
import scipy.sparse as sp

st.set_page_config(page_title="Sentiment Analysis System", page_icon=":shopping_cart:", layout="wide")

# Sidebar for navigation
menu = ["Home", "Hasaki",'Project Summary', "Sentiment Analysis"]

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", menu)

# Subheader with an icon for "Giảng viên hướng dẫn"
st.sidebar.markdown(
    """
    <h3 style="display: flex; align-items: center; font-size: 18px;">
        👩‍🏫 <span style="margin-left: 8px;">Giảng viên hướng dẫn</span>
    </h3>
    """,
    unsafe_allow_html=True,
)
st.sidebar.markdown("* [Cô Khuất Thùy Phương](https://csc.edu.vn/giao-vien~37#)")


# Subheader with an icon for "Ngày báo cáo tốt nghiệp"
st.sidebar.markdown(
    """
    <h3 style="display: flex; align-items: center; font-size: 18px;">
        📅 <span style="margin-left: 8px;">Ngày báo cáo tốt nghiệp:</span>
    </h3>
    """,
    unsafe_allow_html=True,
)
st.sidebar.write("16/12/2024")

# Add spacer for footer positioning
st.sidebar.markdown("<div style='height: 200px;'></div>", unsafe_allow_html=True)

# Sidebar footer
st.sidebar.markdown(
    """
    <style>
        .footer {
            text-align: center;
            font-size: 12px;
        }
        hr {
            border: 1px solid gray;
        }
    </style>
    <div class="footer">
        <hr>
        <p>© 2024 Hasaki Sentiment Analysis System</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Main page logic
if page == "Home":
    # Banner Image
    image = Image.open("src/images/hasaki_banner_2.jpg")
    st.image(image, caption="Sentiment Analysis - Understand Your Customers", use_container_width=True)

    # Project Objective
    st.header("Project Objective")
    st.markdown("""
        This project focuses on developing a **Sentiment Analysis System** to:
        - Analyze customer feedback and reviews.
        - Classify sentiments into categories: **Positive**, **Negative**.
        - Provide actionable insights to improve products and services.
    """)

    # Display Lottie Animation
    image = Image.open("src/images/home.png")
    st.image(image, caption="Sentiment Analysis - Understand Your Customers", use_container_width=True)

    # Methodology
    st.header("Methodology 📋")
    st.markdown("""
    🤖 **Steps to Build the Sentiment Analysis System**:  
    1. **Data Collection**: Collect feedback and reviews from various platforms.  
    2. **Data Preprocessing**: Clean and preprocess the text data using NLP techniques.  
    3. **Model Training**: Train machine learning or deep learning models to classify sentiments.  
    4. **Deployment**: Integrate the sentiment classifier into a real-time system for actionable insights.
    """)

    # Team Section
    st.header("Our Team")
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Mã Thế Nhựt")
        image1 = Image.open("src/images/A.jpg")
        st.image(image1, caption="Mã Thế Nhựt - Data Scientist", use_container_width=True)

    with col2:
        st.write("### Từ Thị Thanh Xuân")
        image2 = Image.open("src/images/B.jpg")
        st.image(image2, caption="Từ Thị Thanh Xuân - Machine Learning Engineer", use_container_width=True)

    # Footer
    st.markdown("""
    ---
    **© 2024 Sentiment Analysis System** | Developed with ❤️ by [Mã Thế Nhựt & Từ Thị Thanh Xuân]
    """)

#####################################

elif page == "Hasaki":
    
    # Title
    st.title("🌟 **Giới thiệu về HASAKI.VN** 🌟")
    # Banner Image
    image = Image.open("src/images/hasaki_banner_2.jpg")
    st.image(image, caption="Hasaki.VN - Quality & Trust", use_container_width=True)
    # Introduction Section
    st.subheader("1. Tổng quan về HASAKI")
    st.markdown("""
    **HASAKI.VN** là hệ thống cửa hàng mỹ phẩm chính hãng và dịch vụ chăm sóc sắc đẹp chuyên sâu, với:  
    - 🛒 **Hệ thống cửa hàng trải dài trên toàn quốc.**  
    - 🤝 **Là đối tác phân phối chiến lược tại Việt Nam** của hàng loạt thương hiệu mỹ phẩm lớn.  
    - 🌐 **Nền tảng trực tuyến** giúp khách hàng dễ dàng:
        - Lựa chọn sản phẩm.  
        - Xem đánh giá/nhận xét thực tế.  
        - Đặt mua hàng nhanh chóng.  
    """)

    # Divider
    st.divider()

    # Problem Section
    st.subheader("2. Vấn đề đặt ra 🚩")
    st.markdown("""
    🧐 **Câu hỏi đặt ra:**  
    - Làm thế nào để **các nhãn hàng hiểu rõ hơn về khách hàng**?  
    - Làm sao để biết **khách hàng đánh giá gì về sản phẩm**?  
    - Làm cách nào để từ phản hồi đó, các nhãn hàng có thể:  
        - **Cải thiện chất lượng sản phẩm.**  
        - **Nâng cấp dịch vụ đi kèm.**  
    """)

    # Divider
    st.divider()

    # Goal Section
    st.subheader("3. Mục tiêu 🎯")
    st.markdown("""
    - 💡 **Thu thập và phân tích đánh giá của khách hàng** để cung cấp thông tin giá trị cho các nhãn hàng.  
    - 📊 Giúp các nhãn hàng hiểu sâu hơn về **sở thích, nhu cầu và trải nghiệm thực tế** của khách hàng.  
    - 🚀 Tăng sự hài lòng và trung thành của khách hàng thông qua việc cải tiến sản phẩm và dịch vụ.
    """)

    # Divider
    st.divider()

    # Methodology Section
    st.subheader("4. Phương pháp 📋")
    st.markdown("""
    🤖 **Xây dựng hệ thống phân loại bình luận tích cực/tiêu cực**  
    1. **Thu thập dữ liệu đánh giá** từ khách hàng trên nền tảng HASAKI.  
    2. **Xử lý dữ liệu (Data Preprocessing)**:
        - Loại bỏ các ký tự đặc biệt và từ dư thừa.
        - Tách từ và chuẩn hóa văn bản bằng công cụ NLP như `underthesea` hoặc ``.  
    3. **Huấn luyện mô hình học máy**:
        - Sử dụng các thuật toán như Logistic Regression, Random Forest.  
    4. **Phân loại cảm xúc**:
        - Dán nhãn bình luận: **Tích cực** hoặc **Tiêu cực**.  
    5. **Triển khai hệ thống**:
        - Tích hợp mô hình vào nền tảng để xử lý bình luận trong thời gian thực.  
    """)


    st.image(
    "src/images/1.jpg", 
    caption="✨ **Phân loại bình luận tích cực và tiêu cực** giúp nhãn hàng hiểu rõ hơn cảm xúc của khách hàng và cải thiện chất lượng sản phẩm.",
    use_container_width=True,
    )

    st.markdown("""
    💡 **Minh họa**:  
    - Bình luận tích cực được phân tích để xác định những điểm nổi bật mà khách hàng yêu thích.  
    - Bình luận tiêu cực được khai thác để tìm ra các vấn đề cần cải thiện.  
    📊 **Tăng khả năng hành động:** Giải pháp này giúp nhãn hàng tối ưu hóa sản phẩm và dịch vụ.
    """)

    # Divider
    st.divider()

    # Call-to-Action
    st.markdown("""
    💡 **Kết quả kỳ vọng**:  
    - Phân loại chính xác >90% bình luận của khách hàng.  
    - Cung cấp thông tin giá trị cho nhãn hàng để cải thiện sản phẩm và dịch vụ.  
    - Tăng sự hài lòng và lòng trung thành của khách hàng.
    """)

#####################################

elif page == "Project Summary":

    st.image(
        'src/images/intro.png',use_container_width=True,
    )
    # Title
    st.title("🌟 **Phân Loại Phản Hồi Khách Hàng Hasaki.vn** 🌟")

    # Problem Section
    st.subheader("1. Vấn đề 🚩")
    st.markdown("""
    Hasaki.vn sở hữu lượng lớn dữ liệu từ các bình luận và đánh giá của khách hàng, tuy nhiên:
    - 🚫 **Không thể xử lý phản hồi nhanh chóng và chính xác.**  
    - 🤔 **Khó xác định phản hồi tích cực, tiêu cực hay trung tính.**  
    - 🕒 **Tốn thời gian để sử dụng phản hồi cho việc cải thiện sản phẩm/dịch vụ.**
    """)

    # Objective Section
    st.subheader("2. Mục tiêu 🎯")
    st.markdown("""
    **Xây dựng hệ thống dự đoán cảm xúc trong phản hồi khách hàng** nhằm:
    - 📊 **Phân loại các bình luận** thành 2 loại: **tích cực, tiêu cực**.  
    - 💡 Giúp Hasaki và đối tác:
        - Hiểu nhanh ý kiến khách hàng.
        - **Cải thiện sản phẩm/dịch vụ** dựa trên phản hồi thực tế.
        - **Tăng mức độ hài lòng và trung thành** của khách hàng.
    """)

    # Solution Section
    st.subheader("3. Giải pháp 💡")
    st.markdown("""
    🛠️ **Hệ thống dự đoán phản hồi** sẽ được phát triển với các bước:
    1. **Thu thập dữ liệu**: Từ phần bình luận và đánh giá của khách hàng trên Hasaki.vn.  
    2. **Xử lý dữ liệu**:
        - Làm sạch dữ liệu (loại bỏ ký tự đặc biệt, stop words).
        - Chuẩn hóa văn bản (chuyển về chữ thường, tách từ bằng NLP).  
    3. **Xây dựng mô hình học máy/học sâu**:
        - Logistic Regression, Random Forest, hoặc mô hình transformer như BERT.  
    4. **Triển khai hệ thống**:
        - Tích hợp mô hình trên website để phân loại phản hồi theo thời gian thực.
    5. **Đánh giá và cải thiện**:
        - Dựa trên chỉ số Precision, Recall, F1-Score.
    """)

    # Add Image/Diagram to Illustrate the Solution
    st.image(
        "src/images/process.png",
        caption="Minh họa quy trình phân loại phản hồi khách hàng.",
        use_container_width=True,
    )

    # Expected Outcomes Section
    st.subheader("4. Kết quả kỳ vọng ✅")
    st.markdown("""
    - **Chính xác ≥90%** trong phân loại phản hồi khách hàng.  
    - **Cung cấp phân tích thời gian thực** cho Hasaki và đối tác.  
    - Tăng sự hài lòng và lòng trung thành của khách hàng thông qua các cải tiến.
    """)

    # # Interactive Demo Placeholder (Optional)
    # st.subheader("5. Trải nghiệm mẫu 💻")
    # st.markdown("**Nhập bình luận của bạn bên dưới để kiểm tra dự đoán cảm xúc (tích cực/tiêu cực):**")
    # user_input = st.text_area("Nhập bình luận khách hàng:")
    # if user_input:
    #     # Placeholder Prediction Logic
    #     # Replace this logic with your trained model's prediction
    #     sentiment = "Tích cực" if "tốt" in user_input.lower() else "Tiêu cực"
    #     st.success(f"🌟 **Dự đoán cảm xúc**: {sentiment}")

#####################################

elif page == "Sentiment Analysis":
    image = Image.open("src/images/process.png")
    st.image(image, caption="Hasaki.VN - Quality & Trust", use_container_width=True)

    pkl_filemodel = "src/models/logreg_model.pkl" 
    with open(pkl_filemodel, 'rb') as file:  
        lgr_model_sentiment = pickle.load(file)
    # doc model count len
    pkl_count = "src/models/tfidf_vectorizer.pkl"  
    with open(pkl_count, 'rb') as file:  
        tfidf_vectorizer = pickle.load(file)

    plk_scaler = "src/models/minmax_scaler.pkl"
    with open(plk_scaler, 'rb') as file:
        scaler = pickle.load(file)

    # Header
    st.title("🌟 Skincare Feedback Analyzer 🌟")
    st.write("Is your product **glowing up** your customers or causing a **breakout**? Let's find out!")

    # Add Banner Image
    st.image(
        "src/images/classify.png", 
        caption="✨ **Discover customer insights for flawless skincare experiences**",
        use_container_width=True,
    )

    # Introductory Text
    st.markdown("""
        🧖‍♀️ **What does this app do?**  
        - Analyzes customer reviews on your skincare products.  
        - Detects if the feedback is **Positive** 💖 (smooth skin ahead!) or **Negative** 💔 (time to rethink).  
        - Helps you make data-driven decisions to keep your customers glowing!  
    """)

    # Streamlit App
    st.subheader("🚀 Input Customer Feedback for Sentiment Analysis")

    flag = False
    lines = None
    data_type = st.radio("How would you like to provide customer feedback?", options=("📝 Type it manually", "📁 Upload a file"))

    if data_type == "📁 Upload a file":
        # Upload file
        uploaded_file = st.file_uploader("Upload a CSV or TXT file with customer feedback", type=['txt', 'csv'])
        if uploaded_file is not None:
            try:
                # Read data
                if uploaded_file.name.endswith('.csv'):
                    lines = pd.read_csv(uploaded_file, header=None)
                else:
                    lines = pd.read_table(uploaded_file, header=None)
                
                st.write("📂 **Uploaded Data Preview:**")
                st.dataframe(lines)
                lines = lines[0]  # Select the first column for processing
                flag = True
            except Exception as e:
                st.error(f"🚨 Oops! Couldn’t read the file: {e}")

    if data_type == "📝 Type it manually":
        content = st.text_area(label="Write a customer's feedback:", placeholder="e.g., This moisturizer is life-changing!")
        if content != "":
            lines = np.array([content])  # Convert input to a NumPy array
            flag = True

    if flag:
        st.subheader("🧐 Processed Feedback")
        if len(lines) > 0:
            st.code(lines, language="plaintext")

            new_reviews = [str(line) for line in lines]
            
            # Transform data using the vectorizer
            x_new = tfidf_vectorizer.transform(new_reviews)

            # Create a DataFrame for the new reviews
            df_new_review = pd.DataFrame(x_new.toarray(), columns=tfidf_vectorizer.get_feature_names_out())

            # Add and scale the 'content_length' feature like you did during training
            df_new_review['content_length'] = [len(review) for review in new_reviews]
            df_new_review['content_length_scaled'] = scaler.transform(df_new_review[['content_length']]) # Use the same scaler from training

            # Combine features
            new_reviews_combined = sp.hstack((x_new, df_new_review[['content_length_scaled']]))

            # Predict sentiment
            y_pred_new = lgr_model_sentiment.predict(new_reviews_combined)
            
            # Map predictions to sentiment labels
            sentiment_labels = {0: "💔 Negative", 1: "💖 Positive"}
            predictions = [sentiment_labels[pred] for pred in y_pred_new]
            
            # Display predictions
            st.subheader("🎯 Feedback Analysis Results:")
            for i, line in enumerate(lines):
                st.markdown(f"""
                - **Feedback**: {line}  
                - **Sentiment**: {predictions[i]}  
                """)
                # Add fun reactions based on sentiment
                if predictions[i] == "💖 Positive":
                    st.success("✨ Skincare success! Your customers are glowing!")
                else:
                    st.error("🛑 Skincare alert! Looks like there’s room for improvement.")