from modules.file_handler import load_csv
from modules.analyzer import get_summary

from modules.report_generator import generate_pdf
import tempfile

st.set_page_config(page_title="📊 Smart Sales Dashboard", layout="wide")
st.title("📊 Smart Sales Dashboard")

file = st.file_uploader("Upload your sales CSV", type=["csv"])
if file:
    df = load_csv(file)
    st.success("File loaded successfully!")

   

    st.subheader("📄 Generate PDF Report")
    if st.button("Generate Report"):
        stats = get_summary(df)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            generate_pdf(df, stats, tmp.name)
            with open(tmp.name, "rb") as f:
                st.download_button("📥 Download Report", data=f, file_name="Sales_Report.pdf", mime="application/pdf")
