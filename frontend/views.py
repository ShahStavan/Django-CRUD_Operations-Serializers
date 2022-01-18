from multiprocessing import context
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

posts = [
    {
        'id': 1,
        'title': 'What is Fundamental Analysis in Stock Market🙄?',
        'content_1': "Fundamental analysis (FA) is a method of measuring a security's intrinsic value by examining related economic and financial factors. Fundamental analysts study anything that can affect the security's value, from macroeconomic factors such as the state of the economy and industry conditions to microeconomic factors like the effectiveness of the company's management. ",
        'content_2': '''All stock analysis tries to determine whether a security is correctly valued within the broader market. Fundamental analysis is usually done from a macro to micro perspective in order to identify securities that are not correctly priced by the market. 
        <hr>Analysts typically study, in order, the overall state of the economy and then the strength of the specific industry before concentrating on individual company performance to arrive at a fair market value for the stock.

        <hr><br>Fundamental analysis uses public data to evaluate the value of a stock or any other type of security. For example, an investor can perform fundamental analysis on a bond's value by looking at economic factors such as interest rates and the overall state of the economy, then studying information about the bond issuer, such as potential changes in its credit rating.

        <hr><br>For stocks, fundamental analysis uses revenues, earnings, future growth, return on equity, profit margins, and other data to determine a company's underlying value and potential for future growth. All of this data is available in a company's financial statements (more on that below). 
        ''',
        'author': 'Shah Stavan',
        'date_posted': 'January 18, 2022'
    },
    {
        'id': 2,
        'title': 'What is Technical Analysis in Stock Market🙄?',
        'content_1': "Technical analysis is a trading discipline employed to evaluate investments and identify trading opportunities by analyzing statistical trends gathered from trading activity, such as price movement and volume. ",
        'content_2': ''' Unlike fundamental analysis, which attempts to evaluate a security's value based on business results such as sales and earnings, technical analysis focuses on the study of price and volume. Technical analysis tools are used to scrutinize the ways supply and demand for a security will affect changes in price, volume, and implied volatility.

<hr>Technical analysis is often used to generate short-term trading signals from various charting tools, but can also help improve the evaluation of a security's strength or weakness relative to the broader market or one of its sectors. This information helps analysts improve their overall valuation estimate.

<hr>Technical analysis can be used on any security with historical trading data. This includes stocks, futures, commodities, fixed-income, currencies, and other securities. In this tutorial, we’ll usually analyze stocks in our examples, but keep in mind that these concepts can be applied to any type of security. In fact, technical analysis is far more prevalent in commodities and forex markets where traders focus on short-term price movements. 
 <hr>Technical analysis as we know it today was first introduced by Charles Dow and the Dow Theory in the late 1800s.1 Several noteworthy researchers including William P. Hamilton, Robert Rhea, Edson Gould, and John Magee further contributed to Dow Theory concepts helping to form its basis. Nowadays technical analysis has evolved to include hundreds of patterns and signals developed through years of research.

<hr>Technical analysis operates from the assumption that past trading activity and price changes of a security can be valuable indicators of the security's future price movements when paired with appropriate investing or trading rules. Professional analysts often use technical analysis in conjunction with other forms of research. Retail traders may make decisions based solely on the price charts of a security and similar statistics, but practicing equity analysts rarely limit their research to fundamental or technical analysis alone.

<hr>Among professional analysts, the CMT Association supports the largest collection of chartered or certified analysts using technical analysis professionally around the world. The association's Chartered Market Technician (CMT) designation can be obtained after three levels of exams that cover both a broad and deep look at technical analysis tools. The association now waives Level 1 of the CMT exam for those who are Certified Financial Analyst (CFA) charterholders. This demonstrates how well the two disciplines reinforce each other.

 <hr>Technical analysis attempts to forecast the price movement of virtually any tradable instrument that is generally subject to forces of supply and demand, including stocks, bonds, futures, and currency pairs. In fact, some view technical analysis as simply the study of supply and demand forces as reflected in the market price movements of a security. Technical analysis most commonly applies to price changes, but some analysts track numbers other than just price, such as trading volume or open interest figures.

<hr>Across the industry, there are hundreds of patterns and signals that have been developed by researchers to support technical analysis trading. Technical analysts have also developed numerous types of trading systems to help them forecast and trade on price movements. Some indicators are focused primarily on identifying the current market trend, including support and resistance areas, while others are focused on determining the strength of a trend and the likelihood of its continuation. Commonly used technical indicators and charting patterns include trendlines, channels, moving averages, and momentum indicators. 
        ''',
        'author': 'Shah Stavan',
        'date_posted': 'January 18, 2022'
    }
]

# Create your views here.
def list(request):
    return render(request, 'frontend/list.html')
def login(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            response = redirect('frontend/list.html')
            return response

    else:
        form = UserCreationForm()
    
    return render(request, 'userapp/index.html', {'form':form})
    return render(request, 'frontend/login.html')
def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'frontend/blog.html',context)
