import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image

# 設定 UI 的布景主題（可選 "blue", "green", "dark-blue"）
ctk.set_appearance_mode("dark")  # 內建酷炫深色模式
ctk.set_default_color_theme("blue")

class FaceAnalyzerGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 設定視窗標題與大小
        self.title("人臉情緒與年齡分析系統 - 期末報告專案")
        self.geometry("1100x650")
        self.resizable(False, False) # 固定視窗大小

        # ==========================================
        # 1. 左側控制面板 (Sidebar Frame)
        # ==========================================
        self.sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.pack(side="left", fill="y")

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Face Analyzer\n系統主選單", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(padx=20, pady=(30, 40))

        # 按鈕：上傳照片
        self.btn_upload_img = ctk.CTkButton(self.sidebar_frame, text=" 📂 上傳分析照片 ", font=ctk.CTkFont(size=14), command=self.upload_image)
        self.btn_upload_img.pack(padx=20, pady=15, fill="x")

        # 按鈕：上傳影片
        self.btn_upload_vid = ctk.CTkButton(self.sidebar_frame, text=" 🎬 上傳分析影片 ", font=ctk.CTkFont(size=14), command=self.upload_video)
        self.btn_upload_vid.pack(padx=20, pady=15, fill="x")

        # 狀態顯示文字
        self.status_label = ctk.CTkLabel(self.sidebar_frame, text="系統狀態: 準備就緒", font=ctk.CTkFont(size=12), text_color="gray")
        self.status_label.pack(side="bottom", pady=20)

        # ==========================================
        # 2. 右上：主要顯示區域 (Main Content Frame)
        # ==========================================
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.pack(side="top", fill="both", expand=True, padx=20, pady=(20, 10))

        # 圖片/影片預覽區（初始顯示提示文字）
        self.preview_label = ctk.CTkLabel(self.main_frame, text="請從左側選單選擇照片或影片進行分析\n\n(分析後的結果與方框將會顯示在此處)", font=ctk.CTkFont(size=16))
        self.preview_label.pack(fill="both", expand=True, padx=20, pady=20)

        # ==========================================
        # 3. 右下：數據報告與統計圖表區 (Data Frame)
        # ==========================================
        self.data_frame = ctk.CTkFrame(self, height=180, corner_radius=15)
        self.data_frame.pack(side="bottom", fill="x", padx=20, pady=(10, 20))

        # 在數據區內切分左、右兩個資訊欄
        self.result_title = ctk.CTkLabel(self.data_frame, text="📊 分析報告數據結果", font=ctk.CTkFont(size=14, weight="bold"))
        self.result_title.pack(anchor="w", padx=20, pady=(10, 5))

        # 用一個小容器來橫向排列數據
        self.stats_container = ctk.CTkFrame(self.data_frame, fg_color="transparent")
        self.stats_container.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # 數據欄位 1：年齡預測結果
        self.lbl_age = ctk.CTkLabel(self.stats_container, text="預估年齡： -- 歲", font=ctk.CTkFont(size=16))
        self.lbl_age.pack(side="left", padx=(0, 40))

        # 數據欄位 2：情緒預測結果
        self.lbl_emotion = ctk.CTkLabel(self.stats_container, text="主要情緒： -- ", font=ctk.CTkFont(size=16))
        self.lbl_emotion.pack(side="left", padx=40)

        # 數據欄位 3：影片專用的提示
        self.lbl_info = ctk.CTkLabel(self.stats_container, text="提示：若是分析影片，完成後會自動產生情緒波動圖。", font=ctk.CTkFont(size=12), text_color="gray")
        self.lbl_info.pack(side="right", padx=10)

    # ==========================================
    # 4. 功能事件處理（預留對接點）
    # ==========================================
    def upload_image(self):
        """當使用者按下『上傳照片』按鈕時觸發"""
        file_path = filedialog.askopenfilename(title="選擇照片", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.status_label.configure(text="系統狀態: 已載入照片...")
            print(f"成功選取照片路徑: {file_path}")
            
            # 【下一階段要做的：對接 DeepFace】
            # 1. 讀取並載入圖片
            # 2. 顯示在自訂的 preview_label 上
            # 3. 更新 lbl_age 與 lbl_emotion 標籤
            
            # 這裡先示範更新文字狀態
            self.lbl_age.configure(text="預估年齡： 25 歲 (測試樣式)")
            self.lbl_emotion.configure(text="主要情緒： Happy 😊 (測試樣式)")
            self.status_label.configure(text="系統狀態: 照片分析完成！")

    def upload_video(self):
        """當使用者按下『上傳影片』按鈕時觸發"""
        file_path = filedialog.askopenfilename(title="選擇影片文件", filetypes=[("Video files", "*.mp4 *.avi *.mov")])
        if file_path:
            self.status_label.configure(text="系統狀態: 已載入影片，開始逐幀分析...")
            print(f"成功選取影片路徑: {file_path}")
            
            # 【下一階段要做的：對接 OpenCV 影片讀取與 DeepFace 批次處理】
            # 1. 用 cv2.VideoCapture(file_path) 打開影片
            # 2. 寫迴圈抓取影格
            # 3. 呼叫 Matplotlib 畫出折線圖
            
            self.status_label.configure(text="系統狀態: 影片分析完成！圖表已匯出。")


if __name__ == "__main__":
    app = FaceAnalyzerGUI()
    app.mainloop()