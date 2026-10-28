class Report:
    def generate(self): raise NotImplementedError
class PDFReport(Report):
    def generate(self): print("Generating PDF report")
class ExcelReport(Report):
    def generate(self): print("Generating Excel report")
class HTMLReport(Report):
    def generate(self): print("Generating HTML report")
def create_report(report): report.generate()
for r in [PDFReport(), ExcelReport(), HTMLReport()]: create_report(r)
