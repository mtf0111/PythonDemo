"""
将图片和PDF文件合并到一起，合并成一个PDF文件保存
依赖库：img2pdf  PyPDF2 pikepdf

"""
import os
from io import BytesIO
import img2pdf
from PyPDF2 import PdfFileReader,PdfFileWriter
import pikepdf

class MergePDF(object):
	"""docstring for MergePDF"""
	def __init__(self,files):
		super(MergePDF, self).__init__()
		# 需要合并的文件列表：存放文件的完整路径
		self.files = files
		# 支持的图片扩展名集合
		self.img_list = [".jpg",".png"]		
		self.pdfwriter = PdfFileWriter()
	
	def img2bytesio(self,imgs):
		# 利用 img2pdf模块将图片转换成PDF内容的二进制流
		stream = BytesIO()	
		stream.write(img2pdf.convert(imgs))			
		return stream

	def mergePDF(self,only_pageone=False):
		# 开始合并 按照self.files的顺序进行合并
		length = len(self.files)
		for index in range(length):
			# 获取文件
			file = self.files[index]
			extension = os.path.splitext(file)[-1] 
			# 判断扩展名称是图片还是PDF文件
			if extension in self.img_list:
				# 如果是图片就转换成PDF内容的二进制流生成PdfFileReader对象
				stream=self.img2bytesio(imgs=file)
				img_pdfreader = PdfFileReader(stream)							
				self.insert2pdfwriter(img_pdfreader,index)
			elif extension==".pdf":
				# 如果是PDF文件 直接进行生成PdfFileReader对象
				pdfreader = PdfFileReader(stream=file)	
				# 判断PDF文件是否加密
				if pdfreader.getIsEncrypted() is True:
					if not os.path.exists("cache"):
						os.mkdir("cache")					
					cache_file = os.path.join("cache",os.path.basename(file)) 
					# 加密的PDF文件通过pikepdf另存为不加密的文件
					with pikepdf.open(file) as pdf:
						pdf.save(cache_file)

					pdfreader = PdfFileReader(stream=cache_file)
				self.insert2pdfwriter(pdfreader,index)
			else:
				raise TypeError(f"只支持合并 {self.img_list}和PDF文件")
				

	def insert2pdfwriter(self,pdfreader,index):		
		# 循环PDFFileReader对象的所有页面写入到PdfFileWriter对象
		for page in pdfreader.pages:
			pagenum = pdfreader.getPageNumber(page)			
			self.pdfwriter.insertPage(page,index+pagenum)

	def save(self,outPDF="output.pdf"):
		# 合并PDF文件并保存
		#  参数  outPDF 指定保存PDF文件的名称，如果未给值将保存到默认名称
		self.mergePDF()

		with open(outPDF,"wb") as out:
			self.pdfwriter.write(out)

		self.del_cache()

	def del_cache(self):
		# 删除因加密PDF文件而保存的PDF副本文件
		if os.path.exists("cache"):
			for file in os.listdir("cache"):
				os.remove(os.path.join("cache",file))			

		
if __name__=="__main__":
	files = [
	"data/5217275.pdf",
	"data/LFV2A2BU5N4427409.pdf"
	]
	merger = MergePDF(files=files)
	merger.save()