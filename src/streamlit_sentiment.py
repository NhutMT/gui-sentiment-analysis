import streamlit as st
from PIL import Image
import pickle
import pandas as pd
import numpy as np
import scipy.sparse as sp

from ultils import helper, product_analysis

st.set_page_config(page_title="Sentiment Analysis System", page_icon=":shopping_cart:", layout="wide")

menu = ["Project Summary", "Sentiment Analysis", "Product Analysis", ]
st.sidebar.title("Đồ Án Tốt Nghiệp")
st.sidebar.markdown(
    """
    <h2 style="display: flex; align-items: center; font-size: 18px;">
        <span style="margin-left: 8px;">Sentiment Analysis Project</span>
    </h2>
    """,
    unsafe_allow_html=True,
)

page = st.sidebar.selectbox("Chức Năng", menu)

# Subheader with an icon for "Giảng viên hướng dẫn"
st.sidebar.markdown(
    """
    <h3 style="display: flex; align-items: center; font-size: 18px;">
        <span style="margin-left: 8px;">Giảng viên hướng dẫn</span>
    </h3>
    """,
    unsafe_allow_html=True,
)
st.sidebar.markdown("👩‍🏫 [Thạc Sĩ Khuất Thùy Phương](https://csc.edu.vn/giao-vien~37#)")

# Subheader with an icon for "Thành Viên"
st.sidebar.markdown(
    """
    <style>
        .footer {
            text-align: center;
            font-size: 12px;
        }
        hr {
            border: 0.5px solid gray;
        }
    </style>
    <div class="footer">
        <hr>
    </div>
    """,
    unsafe_allow_html=True,
)
st.sidebar.markdown(
    """
    <h3 style="display: flex; align-items: center; font-size: 18px;">
        <span style="margin-left: 8px;">Thành Viên</span>
    </h3>
    """,
    unsafe_allow_html=True,
)
st.sidebar.markdown(" :boy: Mã Thế Nhựt")
st.sidebar.markdown(" :girl: Từ Thị Thanh Xuân")

# Subheader with an icon for "Ngày báo cáo tốt nghiệp"
st.sidebar.markdown(
    """
    <style>
        .footer {
            text-align: center;
            font-size: 12px;
        }
        hr {
            border: 0.5px solid gray;
        }
    </style>
    <div class="footer">
        <hr>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    """
    <h3 style="display: flex; align-items: center; font-size: 18px;">
        <span style="margin-left: 8px;">Ngày báo cáo tốt nghiệp:</span>
    </h3>
    """,
    unsafe_allow_html=True,
)
st.sidebar.write('📅 16/12/2024')

# Add spacer for footer positioning
st.sidebar.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

# Sidebar footer
st.sidebar.write("© 2024 Hasaki Sentiment Analysis System")


# Main page logic
if page == "Project Summary":
    # Banner Image
    image = Image.open("src/images/hasaki_banner.jpg")
    st.image(image)

    tab_containers = st.tabs(['Hasaki Project', 'Thực Hiện Dự Án'])

    with tab_containers[0]:
        # Title Section
        st.title("Dự án HASAKI: Phân tích phản hồi khách hàng 🛍️")

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

        # Problem Section
        st.subheader("2. Vấn đề đặt ra 🚩")
        st.markdown("""
        🧐 **Câu hỏi đặt ra:**  
        - Làm thế nào để **các nhãn hàng hiểu rõ hơn về khách hàng**?  
        - Làm sao để biết **khách hàng đánh giá gì về sản phẩm**?  
        - Làm cách nào để từ phản hồi đó, các nhãn hàng có thể:  
            - **Cải thiện chất lượng sản phẩm.**  
            - **Nâng cấp dịch vụ đi kèm.**  

        **Hasaki.vn sở hữu lượng lớn dữ liệu từ các bình luận và đánh giá của khách hàng, tuy nhiên:**
        - 🚫 **Không thể xử lý phản hồi nhanh chóng và chính xác.**  
        - 🤔 **Khó xác định phản hồi tích cực, tiêu cực hay trung tính.**  
        - 🕒 **Tốn thời gian để sử dụng phản hồi cho việc cải thiện sản phẩm/dịch vụ.**
        """)

        # Objective Section
        st.subheader("3. Mục tiêu 🎯")
        st.markdown("""
        🛠️ **Xây dựng hệ thống dự đoán cảm xúc trong phản hồi khách hàng**:
        1. **Phân loại các bình luận thành 2 loại**: Tích Cực, Tiêu Cực.
        2. **Đánh giá chi tiết từng sản phẩm dựa vào các bình luận.** 
        3. **Giúp Hasaki và đối tác**:
            - Hiểu nhanh ý kiến khách hàng.
            - **Cải thiện sản phẩm/dịch vụ** dựa trên phản hồi thực tế.
            - **Tăng mức độ hài lòng và trung thành** của khách hàng.
        """)

        # Expected Outcomes Section
        st.subheader("4. Kết quả kỳ vọng ✅")
        st.markdown("""
        - **Chính xác ≥90%** trong phân loại phản hồi khách hàng.  
        - **Cung cấp phân tích thời gian thực** cho Hasaki và đối tác.  
        - Tăng sự **hài lòng** và **lòng trung thành** của khách hàng thông qua các cải tiến.
        """)

    with tab_containers[1]:  # Assuming the second tab is for the project process
        st.subheader("Quy trình thực hiện 💡")

        # Step 1: Data Collection
        st.subheader("1. Thu thập dữ liệu 📝")
        st.markdown("""
        - **Nguồn dữ liệu:** Bình luận và đánh giá từ khách hàng trên Hasaki.vn.  
        - **Mục tiêu:** Tạo tập dữ liệu chất lượng cao để đào tạo và đánh giá mô hình học máy.
        """)
        image = Image.open("src/images/rv2.png")
        st.image(image, caption="Đánh giá về sản phẩm nước Hoa Hồng Klairs Không Mùi Cho Da Nhạy Cảm 180ml Supple Preparation Unscented Toner")
    
        # Step 2: Data Processing Section
        st.subheader("2. Xử lý dữ liệu 🔄")
        st.markdown("""
        ### Mục tiêu:
        Chuẩn bị và làm sạch dữ liệu bình luận để sẵn sàng cho các bước phân tích và xây dựng mô hình.

        ### Quy trình xử lý:
        1. **Làm sạch dữ liệu:**
        - Loại bỏ ký tự đặc biệt (ví dụ: `!`, `@`, `#`, ...).
        - Xóa số và các từ không mang ý nghĩa ngữ nghĩa (stop words).
        2. **Chuẩn hóa văn bản:**
        - Chuyển toàn bộ văn bản về chữ thường.
        - Chuẩn hóa ký tự lặp lại (ví dụ: `"đẹp quáaaa"` → `"đẹp quá"`).
        - Sử dụng công cụ NLP để tách từ và chuẩn bị dữ liệu.
        3. **Chuyển đổi ngôn ngữ:**
        - Thay thế các từ teencode thành dạng chuẩn (ví dụ: `"hok"` → `"không"`).
        - Dịch từ tiếng Anh sang tiếng Việt (nếu có).
        4. **Xử lý ngữ pháp (POS Tagging):**
        - Phân tích từ loại và gán nhãn từ vựng để hiểu cấu trúc câu.
        5. **Tạo phân đoạn (Chunking):**
        - Chia nhỏ văn bản thành các khối thông tin có ý nghĩa để dễ dàng xử lý và phân tích.

        ### Kết quả kỳ vọng:
        - Dữ liệu sạch và chuẩn hóa, lưu trữ dưới dạng cột văn bản đã xử lý và phân đoạn.
        """)
        image = Image.open("src/images/output1.png")
        st.image(image, caption="Nội dung bình luận trước và sau khi xử lý")
        
        # Step 3: Labeling and Sentiment Analysis Section
        st.subheader("3. Gắn nhãn và phân tích cảm xúc 🏷️📊")
        st.markdown("""
        ### Mục tiêu:
        - Gắn nhãn (label) cho dữ liệu bình luận để sử dụng trong phân tích cảm xúc hoặc các mô hình học máy giám sát.
        - Phân tích số lượng đánh giá theo sản phẩm và cảm xúc (tích cực hoặc tiêu cực), đồng thời tính tỷ lệ cảm xúc để hiểu rõ phản hồi của khách hàng.

        ### Quy trình thực hiện:
        1. **Gắn nhãn bình luận:**
        - **Xác định từ tích cực và tiêu cực:** Tìm và đếm các từ tích cực (ví dụ: `tốt`, `đẹp`, `thích`) và tiêu cực (ví dụ: `xấu`, `tệ`, `thất vọng`) trong bình luận.
        - **Tính toán tỷ lệ từ:**
            - **Tỷ lệ từ tích cực:** Tổng số từ tích cực chia cho tổng số từ trong bình luận.
            - **Tỷ lệ từ tiêu cực:** Tổng số từ tiêu cực chia cho tổng số từ trong bình luận.
        - **Phân loại bình luận:**
            - **Tích cực:** Khi tỷ lệ từ tích cực cao hơn tiêu cực và >= 2.
            - **Tiêu cực:** Các trường hợp còn lại.

        2. **Phân tích cảm xúc theo sản phẩm:**
        - **Tổng hợp đánh giá theo sản phẩm và cảm xúc:**
            - Đếm số lượng đánh giá tích cực và tiêu cực theo từng sản phẩm.
            - Gộp tất cả các bình luận, từ tích cực, và từ tiêu cực thành chuỗi văn bản.
        - **Tính tổng số lượng đánh giá mỗi sản phẩm:** Tổng số lượng đánh giá từ tất cả các cảm xúc cho từng sản phẩm.
        - **Tính tỷ lệ cảm xúc:**
            - **Công thức:** `(Số lượng đánh giá theo cảm xúc / Tổng số đánh giá) * 100`.
            - Kết quả được lưu trong cột `Sentiment_Rate (%)`.

        ### Kết quả kỳ vọng:
        - Dữ liệu bình luận được gắn nhãn:
        - `1` cho bình luận **tích cực**.
        - `0` cho bình luận **tiêu cực**.
        - Thống kê số lượng đánh giá tích cực, tiêu cực, và tổng số đánh giá theo từng sản phẩm.
        - Tính tỷ lệ phần trăm cảm xúc tích cực hoặc tiêu cực cho mỗi sản phẩm, hỗ trợ phân tích xu hướng cảm xúc của khách hàng.
        """)
        image = Image.open("src/images/label.png")
        st.image(image, caption="Dữ liệu sau khi được label")
        
        # Step 4: Detailed Product Analysis Section
        st.subheader("4. Phân tích chi tiết sản phẩm 🛍️")
        st.markdown("""
        ### Mục tiêu:
        Cung cấp thông tin chi tiết về sản phẩm, bao gồm:
        - Thông tin cơ bản (tên sản phẩm, giá bán, mô tả, điểm đánh giá trung bình).
        - Phân tích đánh giá cảm xúc (tích cực và tiêu cực).
        - Hình dung dữ liệu thông qua biểu đồ và Word Cloud.

        ### Quy trình:
        1. **Hiển thị thông tin cơ bản về sản phẩm**:
        - Tên sản phẩm, giá bán, giá gốc, phân loại, mô tả, điểm đánh giá trung bình.
        2. **Phân tích đánh giá cảm xúc**:
        - Hiển thị tỷ lệ cảm xúc tích cực và tiêu cực bằng biểu đồ hình tròn.
        - Tạo Word Cloud cho các từ tích cực và tiêu cực.
        3. **Kiểm tra dữ liệu**:
        - Nếu không có dữ liệu, thông báo sẽ được hiển thị để người dùng biết.
        """)
        image = Image.open("src/images/info.png")
        st.image(image)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            image = Image.open("src/images/pie.png")
            st.image(image)

        # Center the title using HTML
        st.markdown(
            """
            <h3 style="text-align: center;">Word Cloud - Positive and Negative Sentiment:</h3>
            """,
            unsafe_allow_html=True
        )

        # Display Positive and Negative Word Cloud Images Side-by-Side
        cols = st.columns(2)

        # Positive Word Cloud
        with cols[0]:
            image = Image.open("src/images/pos.png")
            st.image(image)

        # Negative Word Cloud
        with cols[1]:
            image = Image.open("src/images/neg.png")
            st.image(image)

        # Step 5: Data Preparation for Machine Learning
        st.subheader("5. Chuẩn bị dữ liệu cho Mô hình Học máy 🤖")

        st.markdown("""
        ### Mục tiêu:
        Chuẩn bị dữ liệu đầu vào chất lượng cao cho các mô hình học máy bằng cách:
        - Biến đổi văn bản thành đặc trưng số sử dụng TF-IDF.
        - Bổ sung các đặc trưng hỗ trợ phân tích (độ dài đánh giá).
        - Xử lý mất cân bằng lớp để cải thiện hiệu suất mô hình.

        ### Quy trình:
        1. **Phân chia dữ liệu:**
            - Tách dữ liệu thành tập huấn luyện (80%) và tập kiểm tra (20%).
        2. **Biến đổi văn bản bằng TF-IDF:**
            - Sử dụng `TfidfVectorizer` để tạo đặc trưng từ văn bản (giữ lại 5000 từ quan trọng nhất).
        3. **Thêm đặc trưng hỗ trợ:**
            - Tính độ dài văn bản và chuẩn hóa bằng `MinMaxScaler`.
        4. **Kết hợp đặc trưng:**
            - Kết hợp TF-IDF và đặc trưng độ dài thành một ma trận đầu vào duy nhất.
        5. **Xử lý mất cân bằng lớp:**
            - Áp dụng SMOTE để tạo thêm dữ liệu cho lớp nhỏ, đảm bảo dữ liệu cân bằng.
        """)

        # Step 6: Evaluation and Improvement
        st.subheader("6. Đánh giá và cải thiện 📊")

        st.markdown("""
        ### Tiêu chí đánh giá:
        1. **Độ chính xác (Accuracy):** Xác định tỷ lệ dự đoán đúng.
        2. **F1-Score:** Đo lường cân bằng giữa Precision và Recall.
        3. **ROC-AUC:** Hiệu quả phân loại dựa trên đường cong ROC.

        ### Quy trình cải thiện:
        - Dựa trên các chỉ số và phản hồi từ người dùng hệ thống.
        - Thử nghiệm thêm các mô hình hoặc đặc trưng bổ sung.
        """)
        # Step 7: Model Comparison and Recommendation
        st.subheader("7. So sánh và lựa chọn mô hình tối ưu 📊")
        st.markdown("""
        ### Mục tiêu:
        So sánh hiệu suất của các mô hình Logistic Regression, Multinomial Naive Bayes, XGBoost, và SVM.
        Đưa ra lựa chọn mô hình tối ưu cho bài toán phân loại cảm xúc.
        """)

        # Display Comparison Table
        st.markdown("### Bảng so sánh hiệu suất các mô hình:")
        comparison_data = {
            "Metric": ["Accuracy", "Precision (Class 0)", "Precision (Class 1)", "Recall (Class 0)", "Recall (Class 1)", "F1-Score (Class 0)", "F1-Score (Class 1)", "ROC-AUC Score"],
            "Logistic Regression": [0.9778, 0.63, 1.00, 0.96, 0.98, 0.76, 0.99, 0.99],
            "Multinomial Naive Bayes": [0.9639, 0.50, 1.00, 0.96, 0.96, 0.66, 0.98, 0.99],
            "XGBoost": [0.9849, 0.73, 1.00, 0.93, 0.99, 0.82, 0.99, 0.99],
            "SVM": [0.9776, 0.62, 1.00, 0.97, 0.98, 0.76, 0.99, 0.99]
        }

        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(df_comparison)

        # Recommendation Section
        st.markdown("### Lựa chọn mô hình tối ưu 📌")
        st.markdown("""
        #### Lý do lựa chọn Logistic Regression:
        1. **Dễ hiểu và giải thích**:
            - Logistic Regression giúp xác định rõ ràng tầm quan trọng của từng đặc trưng (từ khóa) trong dự đoán.
            - Thích hợp cho các bài toán cần minh bạch kết quả.

        2. **Hiệu suất ổn định**:
            - Độ chính xác đạt **97.78%**, gần tương đương XGBoost.
            - F1-Score cho cả hai lớp (Tích cực, Tiêu cực) rất tốt.

        3. **Đơn giản và hiệu quả**:
            - Yêu cầu ít tài nguyên tính toán.
            - Dễ dàng triển khai vào hệ thống thực tế.

        4. **Khả năng mở rộng**:
            - Thích hợp với dữ liệu lớn và dễ dàng nâng cấp khi có thêm dữ liệu mới.

        #### So sánh với các mô hình khác:
        - **XGBoost**: Mặc dù chính xác hơn nhưng phức tạp và đòi hỏi nhiều tài nguyên.
        - **SVM**: Cân bằng hiệu suất nhưng mất thời gian trong huấn luyện khi dữ liệu lớn.
        - **Multinomial Naive Bayes**: Nhanh nhưng hiệu suất thấp hơn Logistic Regression.
        """)

        # Step 8: System Deployment
        st.subheader("8. Triển khai hệ thống 🚀")
        st.markdown("""
        ### Mục tiêu:
        Triển khai mô hình học máy vào hệ thống thực tế để hỗ trợ quản lý sản phẩm và dịch vụ.

        ### Nội dung triển khai:
        1. **Tích hợp mô hình trên nền tảng Hasaki.vn:**
            - Phân loại phản hồi của khách hàng theo thời gian thực.
            - Phân tích cảm xúc để cung cấp thông tin hữu ích cho nhà quản lý.
        2. **Hiển thị báo cáo chi tiết:**
            - Số lượng bình luận tích cực/tiêu cực.
            - Xu hướng cảm xúc theo sản phẩm/dịch vụ.
        """)

#####################################

elif page == "Sentiment Analysis":
    image = Image.open("src/images/process.png")
    st.image(image, caption="Hasaki.VN - Quality & Trust")

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
        caption="✨ **Discover customer insights for flawless skincare experiences**"
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
            # contents = content.split("\n")
            lines = content.split("\n")
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
elif page == "Product Analysis":
    st.title("Phân Tích Sản Phẩm")
    st.write("Dựa vào kết quả phân tích, Hasaki và các đối tác sẽ hiểu được cảm nhận của khách hàng về sản phẩm.")
    
    df_products = helper.read_csv("src/data/San_pham.csv")

    # Chọn phương thức nhập liệu (Mã sản phẩm hoặc Tên sản phẩm)
    input_method = st.radio("Chọn phương thức nhập liệu:", ["Chọn tên sản phẩm", "Nhập mã/tên sản phẩm"])

    product_code = None
    
    if input_method == "Nhập mã/tên sản phẩm":
        # Nhập mã sản phẩm hoặc tên sản phẩm
        search_criteria = st.text_input("Nhập mã hoặc tên sản phẩm:")
        
        if (search_criteria != "" and search_criteria.isdigit()):
            result = df_products[df_products["ma_san_pham"] == eval(search_criteria)]
            if not result.empty:
                product_code = result["ma_san_pham"].iloc[0]
            else:
                st.write("Không tìm thấy sản phẩm!")
            
        elif (search_criteria != ""):
            result = df_products[df_products["ten_san_pham"] == search_criteria]
            if not result.empty:
                product_code = result["ma_san_pham"].iloc[0]
            else:
                st.write("Không tìm thấy sản phẩm!")
        else:
            st.write("Nhập mã hoặc tên sản phẩm!")
    else:   
        # Chọn tên sản phẩm từ dropdown
        selected_item = st.selectbox("Chọn tên sản phẩm:", df_products['ten_san_pham'].unique())
        product_code = df_products[df_products["ten_san_pham"] == selected_item]["ma_san_pham"].iloc[0]
    
    # Hiển thị thông tin sản phẩm
    if st.button("Phân Tích"):
        if not product_code:
            st.error("Mã sản phẩm không tồn tại trong cơ sở dữ liệu. Vui lòng chọn hoặc nhập mã sản phẩm hợp lệ.")
        else:
            df_review = helper.read_csv("src/data/step2_full_review_result.csv")
            st.subheader("Kết quả phân tích sản phẩm")
            
            st.write("Thông tin sản phẩm:")
            df_info = product_analysis.GetProductInfoByCode(df_products, product_code)
            st.markdown(
                df_info.to_html(index=False, justify='center', classes='table table-striped'),
                unsafe_allow_html=True
            )

            st.write("Thông tin nhận xét:")
            df_anlyze, sentiment_data, sentiment_categories = product_analysis.GetProductReview(df_review, product_code)

            # Draw Pie chart
            st.write("Thống kê cảm xúc:")
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                product_analysis.DrawPieChart(sentiment_data, sentiment_categories)

            # Generate word clouds for each sentiment category
            s_positive = df_anlyze[df_anlyze['Categorized'] == 1]
            s_negative = df_anlyze[df_anlyze['Categorized'] == 0]

            col1, col2 = st.columns(2)
            with col1:
                st.write("\nTop 50 từ Positive về sản phẩm:")
                product_analysis.wcloud_visualize(s_positive, 'Pos_words', 'Word Cloud - Positive')
            with col2:
                st.write("\nTop 50 từ Negative về sản phẩm:")
                product_analysis.wcloud_visualize(s_negative, 'Neg_words', 'Word Cloud - Negative')