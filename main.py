import fitz
import pytesseract
from PIL import Image
import io, re, csv, os
from PIL import Image, ImageEnhance, ImageFilter
from nanonets import NANONETSOCR
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import ttkbootstrap as tb

model = NANONETSOCR()
model.set_token('')

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

index=2
folder_path = "./pdf" 
csv_path = "./output.csv"
file_exists = os.path.exists(csv_path)

# columns = ["Name","Relative's Name", "House No","Age","Gender"]

# patterns = {
#     "Name": r"(?:नाव|चाव|नाबर|नाब|नावर|जाब)\s*[:!;.,|।ः]?\s*([^\n|]*)",
#     "Relative's Name": r"(?:वडिलांचे नाव|पतीचे नाव|पत्नीचे नाव|पत्तीचे नाव|पत्तीचे नान|पतींचे नाव|आईचे नाव|बडिलांचे नाव|चडिलांचे नाव|यंडिलांचे नाव|बंडिलांचे नाव|यडिलांचे नाय|बंडिलांचे नाब)\s*[:!;.,|।ः]?\s*(.*)",
#     "House No": r"(?:घर\s*क्रमांक|घरं\s*क्रमांक)\s*[:!;.,|।ः]?\s*([^\n|]*)",
#     "Age": r"(?:वस|चय|ब्रय|बस|बय|यय|वय|वप|वस|वयं|वयन|व|वग्न|वगय|वपन|वदय|वषय|वष|वव|वग)\s*[:!;.,|।ः]?\s*(\d+)",
#     "Gender": r"(?:लिंग)\s*[:!;.,|।ः]?\s*(पुरुष|महिला)"
# }



# def extract_values_from_pdf(pdf_path, writer):
#     doc = fitz.open(pdf_path)
#     all_text = ""
#     i=0

#     for page in doc:
#         i+=1
#         pix = page.get_pixmap(dpi=300)  
#         img = Image.open(io.BytesIO(pix.tobytes("png")))
#         for j in range(3):
#             w, h = img.size
#             col_width = w // 3
#             left = j * col_width
#             right = (j + 1) * col_width
#             col_img = img.crop((left, 125, right, h - 125))
            
#             col_img = col_img.resize((int(col_img.width * 0.5), int(col_img.height * 0.5)), Image.LANCZOS)
#             enhancer = ImageEnhance.Brightness(col_img) 
#             col_img = enhancer.enhance(0.5)
#             col_img = col_img.convert("L")
#             col_img = col_img.filter(ImageFilter.SHARPEN)
            
#             col_img = col_img.resize((int(col_img.width * 3), int(col_img.height * 3)), Image.LANCZOS)
#             # col_img = col_img.filter(ImageFilter.SHARPEN)
#             cw, ch = col_img.size
#             cell_height = ch // 10

#             for k in range(10):
#                 top = k * cell_height
#                 bottom = (k + 1) * cell_height
#                 cell_img = col_img.crop((0, top, cw, bottom))

#                 # cell_img.save(f"./output_images/{i}_{j}_{k}.png")

#                 custom_config = r'--oem 3 --psm 6'
#                 text = pytesseract.image_to_string(cell_img, lang="mar", config=custom_config)

#                 text = re.sub(r'[ ]{2,}', ' ', text)
#                 lines = [line.strip() for line in text.splitlines() if line.strip()]
#                 text = "\n".join(lines)
                
              
#                 row = {}
#                 for field, regex in patterns.items():
#                     match = re.search(regex, text)
#                     row[field] = match.group(1).strip() if match else ""
                
             
#                 writer.writerow(row)

#                 all_text += text + "\n\n"

                 

    # with open("./output.txt", "w", encoding="utf-8") as f:
    #     f.write(all_text)

    # values = {col: "" for col in columns}

    # for col, pat in patterns.items():
    #     m = re.search(pat, all_text, re.IGNORECASE)
    #     if m:
    #         values[col] = m.group(1)

    # return values


# Process all PDFs and save into CSV
# with open(csv_path, "a", newline="", encoding="utf-8-sig") as f:
#     writer = csv.DictWriter(f, fieldnames=columns)

#     if not file_exists or os.path.getsize(csv_path) == 0:
#         writer.writeheader()

#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.lower().endswith(".pdf"):
#                 pdf_file = os.path.join(root, file)
#                 try:
#                     row = extract_values_from_pdf(pdf_file)

#                     if any(v for v in row.values()):
#                         writer.writerow(row)
#                         f.flush()          
#                         print(f"{index} Processed: {pdf_file}")                        
#                         index += 1
#                     else:
#                         # Debug: print file that had no recognizable data
#                         print(f"Skipped (no recognizable values): {pdf_file}")
#                 except Exception as e:
#                     print(f"Error with {pdf_file}: {e}")



                    
# with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
#     writer = csv.DictWriter(f, fieldnames=columns)
#     f.seek(0, os.SEEK_END)
#     # if f.tell() == 0:
#     writer.writeheader()

#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.lower().endswith(".pdf"):
#                 pdf_file = os.path.join(root, file)
#                 try:
#                     extract_values_from_pdf(pdf_file, writer)
#                     print(f"{index} Processed: {pdf_file}")                        
#                     index += 1
#                 except Exception as e:
#                     print(f"Error with {pdf_file}: {e}")



class PDFToCSVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF → CSV/XLSX Preview")
        self.root.geometry("900x600")
        self.style = tb.Style("darkly")

        # Top frame
        top_frame = ttk.Frame(root, padding=10)
        top_frame.pack(fill="x")
        self.choose_btn = ttk.Button(top_frame, text="📄 Select PDF(s)", bootstyle="primary", command=self.select_pdfs)
        self.choose_btn.pack(side="left")
        self.status_lbl = ttk.Label(top_frame, text="No file selected", bootstyle="secondary")
        self.status_lbl.pack(side="left", padx=10)

        # Table frame
        table_frame = ttk.Frame(root, padding=10)
        table_frame.pack(fill="both", expand=True)
        self.tree = ttk.Treeview(table_frame, show="headings", bootstyle="dark")
        self.tree.pack(fill="both", expand=True, side="left")
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview, bootstyle="round-dark")
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Bottom buttons
        bottom_frame = ttk.Frame(root, padding=10)
        bottom_frame.pack(fill="x")
        self.copy_btn = ttk.Button(bottom_frame, text="📋 Copy Snippet", bootstyle="success", command=self.copy_to_clipboard)
        self.copy_btn.pack(side="right", padx=5)
        self.export_btn = ttk.Button(bottom_frame, text="💾 Save as CSV/XLSX", bootstyle="info", command=self.export_file)
        self.export_btn.pack(side="right", padx=5)

        self.data_preview = []

    def select_pdfs(self):
        filepaths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if not filepaths:
            return
        self.status_lbl.configure(text=f"{len(filepaths)} PDF(s) selected ✔")
        self.data_preview = []


        for pdf in filepaths:            
            import pandas as pd
            model.convert_to_csv(pdf, output_file_name='temp_output.csv')
            df = pd.read_csv("temp_output.csv")            
            self.data_preview.extend(df.to_dict(orient="records"))  

        self.show_preview()

    def show_preview(self):
        self.tree.delete(*self.tree.get_children())
        if not self.data_preview:
            return
        self.tree["columns"] = list(self.data_preview[0].keys())
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200, anchor="center")
        for row in self.data_preview:
            self.tree.insert("", "end", values=list(row.values()))

    def copy_to_clipboard(self):
        if not self.data_preview:
            messagebox.showwarning("No Data", "No data to copy")
            return
        import pandas as pd
        df = pd.DataFrame(self.data_preview)
        tb.clipboard_clear()
        self.root.clipboard_append(df.to_csv(index=False))
        messagebox.showinfo("Copied", "Snippet copied to clipboard")

    def export_file(self):
        messagebox.showinfo("Export", "You can implement Save as CSV/XLSX here")


if __name__ == "__main__":
    root = tb.Window(themename="darkly")
    app = PDFToCSVApp(root)
    root.mainloop()
