"""
Bài 3: Điểm trung bình
	  	Bạn Nam vừa tham gia cuộc thi kiểm tra kiến thức môn Tin học, nội dung kiểm tra gồm hai phần:
	  	phần thi lý thực hành (viết tắt TH) và phần thi lý thuyết (viết tắt LT). Điểm trung bình (viết tắt DTB) được tính như sau:
              	DTB = (TH*3 + LT)/4
              	Nếu DTB  thì đạt, ngược lại không đạt
Yêu cầu: cho hai số nguyên X và Y  lần lượt là điểm thi thực hành và lý thuyết của Nam.
Em hãy viết chương trình giúp bạn Nam tính ra kết quả đạt hay không đạt (nếu đạt ghi 1, không đạt ghi 0)
"""
file_input=open("DTB.INP","r")
file_output=open("DTB.OUT","w")
output=""
for i in range(2):
    x,y = map(int,file_input.readline().split())
    DTB = (x*3 + y)/4
    if DTB >=5:
        output+= "1 \n"
    else:
        output+= "0 \n"
file_output.write(output)