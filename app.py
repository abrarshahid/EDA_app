import streamlit as st
import pandas as pd
import codecs
import streamlit.components.v1 as components
import numpy as np
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sweetviz as sv
#custom functions

def st_display_sweetviz(report_html,width=1300,height=500):
	report_file = codecs.open(report_html,'r')
	page = report_file.read()
	components.html(page,width=width,height=height,scrolling= True)




def main():
	menu = ["Home","Pandas Profile","SweetViz"]
	choice = st.sidebar.selectbox("Menu",menu)
	
	if choice == "Pandas Profile":
		st.subheader("EDA with Pandas Profile")
		data_file = st.file_uploader("Upload CSV",type=['CSV'])
		if data_file is not None:
			df = pd.read_csv(data_file)
			st.header('**Input DataFrame**')
			st.write(df)
			profile=ProfileReport(df)
			st.header('**Pandas Profiling Report**')
			st_profile_report(profile)
		else:
			st.info('Awaiting for CSV file to be uploaded.')
			if st.button('Press to use Example Dataset'):
				# Example data
				@st.cache
				def load_data():
					a = pd.DataFrame(
						np.random.rand(100, 5),
						columns=['a', 'b', 'c', 'd', 'e']
					)
					return a
				df = load_data()
				pr = ProfileReport(df, explorative=True)
				st.header('**Input DataFrame**')
				st.write(df)
				st.write('---')
				st.header('**Pandas Profiling Report**')
				st_profile_report(pr)		
	elif choice == "SweetViz":
		st.subheader("EDA with Sweetviz")
		data_file = st.file_uploader("Upload CSV",type=['CSV'])
		if data_file is not None:
			df = pd.read_csv(data_file)
			st.header('**Input DataFrame**')
			st.write(df)
			st.header('**SweetViz Report**')
			if st.button("Generate Sweetviz Report"):
				st_display_sweetviz("SWEETVIZ_REPORT.html")
	
	else:
		
		html_temp = """
		<div style="background-color:#549dc7;padding:3px;border-radius:10px;font-family:'Dosis', sans-serif">
		<h1 style="color:white;text-align:center;">DataWay</h1>
		
		</div>
		<div class = "lol" style="padding:-5px;font-family:'Dosis', sans-serif">
		<h2 style="color:#292726;text-align:center;">More than EDA Website</h2>
		</div>
		
		"""
		
		components.html(html_temp)
		st.image("datapic.png",use_column_width=True)
		chart_data = pd.DataFrame(
		np.random.randn(20, 3),
		columns=['a', 'b', 'c'])
		st.area_chart(chart_data)
		st.write('Graphs are The base here :sunglasses:')
		st.write('Copyright: Abrar Shahid :wink:')
		
if __name__ == '__main__':
	main()	
