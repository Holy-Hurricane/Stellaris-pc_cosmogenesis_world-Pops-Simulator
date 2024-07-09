def F(x):    #净化基础速度（神经过载）
    if x>40:
        return (x-40)*4
    else:
        return 0
def A(c,b):    #修正函数
    return c*(1+0.01*b)
def R(z):    #规划修正——定居点飞升函数(结果还需根据情况乘1/2/3)
    return 5*(1+0.25*z)
def S(n):    #神经之门数量对岗位产出的研究点加成
    return 0.75*(n)    
def H(n):    #扩充思维区队岗位产出的超然逻辑加成
    return 0.02*(n)    
def G(n):    #输入生效核心建筑等级，输出其对产出和维护修正
    return 10*n
def Y(st):    #输入附加建筑代号组合输出修正效果，考虑到的建筑有五种（每种建筑不能超过两个，总数不能超过六个）
    e=st.count("e")    #拓展反应堆数量
    m=st.count("m")    #突触共振器数量
    s=st.count("s")    #突触保存器数量
    o=st.count("o")    #突触超频器数量
    m0=st.count("g")    #突触沉思器数量
    z=75*o-15*s
    return m,-m0*35,100*m-15*e,z,o    #共振器对产出修正系数，产出固定修正，维护费修正，人口净化速度修正，超频系数
def P(x):    #人口产值与维护（效率）函数
    return 0.0375*x,0.00125*x,0.05*x    #研究点，超然逻辑，能量币维护
print("欢迎使用烧人口模拟器，目前适配群星版本3.12.5，仅计量岗位的产出和维护！")
print("这个小版本添加了粗略的人口增长机制，人口会达到一个动态平衡值，因此也有模拟时限的设置！")
print("首先是配置突触凝练机，以下输入非法值或空值都会当做取默认值！")
try:
    i=eval(input("请输入生效的核心建筑等级，或者其对产出/维护修正量的首位（0~3，默认为3）："))
    i=G(i)
except:
    i=G(3)
    print("输入无效值，取用默认值3")
finally:
    print("核心建筑修正量："+str(i)+"%")
try:
    a=eval(input("请输入定居点飞升等效等级（默认为0），采用升格假设类国民理念需要乘1.5："))
    a=R(a)
except:
    a=R(0)
    print("输入无效值，取用默认值0")
finally:
    print("规划类型修正基准值："+str(a)+"%")
try:
    s=eval(input("请输入神经之门的数量（默认为6）："))
    s1=S(s)
except:
    s=6
    s1=S(s)
    print("输入无效值，取用默认值6")
finally:
    print("神经之门数量："+str(s))
try:
    h=eval(input("请输入扩充思维区数量（默认为0）："))
    h1=H(h)
except:
    h=0
    h1=H(h)
    print("输入无效值，取用默认值0")
finally:
    print("扩充思维区数量："+str(h))
print("请准备输入附加建筑情况，本程序仅考虑其中四种，每种都有其对应的代号")
print("拓展反应堆——e；突触共振器——m；突触保存器——s；突触超频器——o；突触沉思器——g。")
print("请输入相应数量和种类的代号，例如“eessmm”代表拓展反应堆、突触共振器和突触保存器各两个：")
try:
    y=input()
    y=y.lower()
    if y=="":
        y+=1
except:
    y="eessmm"
    print("输入无效，取用默认值！")
finally:
    print("拓展反应堆数量："+str(y.count("e")))
    print("突触共振器数量："+str(y.count("m")))
    print("突触保存器数量："+str(y.count("s")))
    print("突触超频器数量："+str(y.count("o")))
    print("突触沉思器数量："+str(y.count("g")))
    pass
try:
    st=eval(input("请输入稳定度对产出修正（默认为0，以“%”为单位）："))
except:
    st=0
    print("输入无效，取用默认值0")
finally:
    print("稳定度对产出修正："+str(st)+"%")
try:
    v1=eval(input("请输入全局产出修正，可以将物种特质加成计入，默认为15%，单位为“%”："))
except:
    v1=15
    print("输入无效，取用默认值15%")
finally:
    print("全局及物种特质产出修正："+str(v1)+"%")
try:
    v2=eval(input("请输入全局维护修正，默认为-5%（和谐/同调传统），单位为“%”："))
except:
    v2=-5
    print("输入无效，取用默认值-5%")
finally:
    print("全局维护修正："+str(v2)+"%")
m=eval(input("请输入初始人口数："))
try:
    u=eval(input("请输入初始净化进度，默认为0："))
except:
    u=0
    print("输入无效，取用默认值0")
finally:
    print("初始净化进度："+str(u))
try:
    gth=eval(input("如有多余人口持续供给突触凝练机，请输入月增长进度之和："))
    if gth=="":
        gth=0
except:
    gth=0
    print("输入无效，取用默认值0！")
finally:
    print("月人口增长量："+str(gth))
try:
    gne=eval(input("如有需要，请输入人口增长需求（默认为100）"))
except:
    gne=100
    print("输入无效，取用默认值100")
finally:
    print("人口增长需求："+str(gne))
print("数据输入完毕，现在开始模拟！")
try:
    T=eval(input("请输入模拟月数，默认为360月（30年）"))
except:
    T=360
    input("输入无效，取用默认值360，点击回车键确认！")
D=Y(y)
g,j,k,l,o=D[0],D[1],D[2],D[3],D[4]    #共振器对产出修正系数，产出固定修正，维护费修正，人口净化速度修正，超频系数
g0=g    #备份一个共振器系数
s,h=s1,h1
w=0    #准备开始第一个月
u1=u
f=l-a    #人口净化速度总修正
u2=A(F(m),f)    #当月产生人口净化进度
gh0=0    #初始人口增长进度
gh1=gh0    #当月人口增长进度
gh2=gth    #当月人口增长量
fl=open("gehult.csv",'w')    #打开文件备用
fl.writelines("月数,人口,单岗研究,总研究,单岗超然逻辑,总超然逻辑,单岗能量币维护,总岗能量币维护,人口净化进度,产生人口净化进度,人口增长进度,产生人口增长进度\n")
while u2>0:
    w=w+1
    g=g0*m    #共振器产出修正
    b0=i+3*a+g+j+st+v1    #产出固定修正之和
    b=b0+g    #总修正
    tk1=A(P(m)[0]+s+o,b)    #单岗研究点产出
    tk2=m*tk1    #总科研点产出
    lg1=A(P(m)[1]+h+0.5*o,b)    #单岗超然逻辑产出
    lg2=m*lg1    #总超然逻辑产出
    p0=i-a+k+v2    #（固定）维护修正
    mt1=A(P(m)[2],p0)    #单岗能量币维护
    mt2=m*mt1    #总岗能量币维护
    f=l-a    #人口净化速度总修正
    u2=A(F(m),f)    #当月产生人口净化进度
    d1=u1+u2
    d=d1//100    #当月净化人口数
    gth1=gh1+gh2
    gth=gth1//gne    #当月人口增长数
    d=int(d)
    m=int(m)    
    gth=int(gth)    #对这三个值取整，打印出来好看些
    ls=[str(w-1),str(m),str(tk1),str(tk2),str(lg1),str(lg2),str(mt1),str(mt2),str(u1),str(u2),str(gh1),str(gh2)]
    fl.writelines(",".join(ls))
    fl.writelines("\n")    #换行
    print("第"+str(w)+"个月，"+str(m)+"(-"+str(d)+"+"+str(gth)+")人口，产出研究"+str(tk2)+"、超然逻辑"+str(lg2)+"，岗位维护费"+str(mt2)+"能量币")
    u1=d1%100    #下一个月的已完成净化进度
    gh1=gth1%gne    #下个月的已完成人口增长进度
    m=m-d+gth    #下一个月的人口
    if w>=T:
        break
print("模拟停止！当前人口"+str(m)+"，经过了"+str(w)+"个月")
w=w+1
g=g0*m    #共振器产出修正
b0=i+3*a+g+j+st+v1    #产出固定修正之和
b=b0+g    #总修正
tk1=A(P(m)[0]+s+o,b)    #单岗研究点产出
tk2=m*tk1    #总科研点产出
lg1=A(P(m)[1]+h+0.5*o,b)    #单岗超然逻辑产出
lg2=m*lg1    #总超然逻辑产出
p0=i-a+k+v2    #（固定）维护修正
mt1=A(P(m)[2],p0)    #单岗能量币维护
mt2=m*mt1    #总岗能量币维护
f=l-a    #人口净化速度总修正
u2=A(F(m),f)    #当月产生人口净化进度
d1=u1+u2
d=d1//100    #当月净化人口数
gth1=gh1+gh2
gth=gth1//gne    #当月人口增长数
d=int(d)
m=int(m)    
gth=int(gth)    #对这三个值取整，打印出来好看些
ls=[str(w-1),str(m),str(tk1),str(tk2),str(lg1),str(lg2),str(mt1),str(mt2),str(u1),str(u2),str(gh1),str(gh2)]
fl.writelines(",".join(ls))
fl.writelines("\n")    #换行
print("第"+str(w)+"个月，"+str(m)+"(-"+str(d)+"+"+str(gth)+")人口，产出研究"+str(tk2)+"、超然逻辑"+str(lg2)+"，岗位维护费"+str(mt2)+"能量币")
u1=d1%100    #下一个月的已完成净化进度
gh1=gth1%gne    #下个月的已完成人口增长进度
m=m-d+gth    #下一个月的人口
fl.close()    #关闭文件
