'''This file holds the links for each filter specification. It was written in order to avoid polluting
the class files with long addresses'''

filtering_choice = {'ranking':1, 'manufacturer':2, 'screen':3 , 'RAM':4, 'Weight':5, 'HD type':6}

default_url = 'https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108&dc&qid=1595345193&rnid=13896617011&ref=sr_nr_n_2'

ranking = {'ranking_1 ':"""https://www.amazon.com/s?k=laptop&i=computers&rh=n%3A541966%2Cn%3A565108%2Cp_72%3A1248882011&dc&qid=1594229352&rnid=1248877011&ref=sr_nr_p_72_4""",
           'ranking_2':"""https://www.amazon.com/s?k=laptop&i=computers&rh=n%3A541966%2Cn%3A565108%2Cp_72%3A1248881011&dc&qid=1594229331&rnid=1248877011&ref=sr_nr_p_72_3""",
           'ranking_3':"""https://www.amazon.com/s?k=laptop&i=computers&rh=n%3A541966%2Cn%3A565108%2Cp_72%3A1248880011&dc&qid=1594229321&rnid=1248877011&ref=sr_nr_p_72_2""",
           'ranking_4':"""https://www.amazon.com/s?k=laptop&i=computers&rh=n%3A541966%2Cn%3A565108%2Cp_72%3A1248879011&dc&qid=1594229300&rnid=1248877011&ref=sr_nr_p_72_1"""}

manufactures_list = ['Acer', 'DELL','HP', 'Samsung','Lenovo','Asus','Apple']

manufacture = {'manufacture_Acer':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AAcer&dc&qid=1594230281&rnid=2528832011&ref=sr_nr_p_89_1""",
'manufacture_Asus':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AASUS&dc&qid=1594230452&rnid=13896617011&ref=sr_nr_n_2""",
'manufacture_HP':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AHP&dc&qid=1594230424&rnid=13896617011&ref=sr_nr_n_2""",
'manufacture_Apple':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AApple&dc&qid=1594230378&rnid=13896617011&ref=sr_nr_n_2""",
'manufacture_Samsung':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ASAMSUNG&dc&qid=1594230499&rnid=2528832011&ref=sr_nr_p_89_5""",
'manufacture_DELL':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ADell&dc&qid=1594230529&rnid=2528832011&ref=sr_nr_p_89_7""",
'manufacture_Lenovo':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3ALenovo&dc&qid=1594230563&rnid=2528832011&ref=sr_nr_p_89_4"""}

screen_sizes = ['11', '11-12','12-13', '13-14','14-15', '15-16', '17']

screen = {'screen_11': """https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_size_browse-bin%3A13580786011&dc&qid=1594230619&rnid=2242797011&ref=sr_nr_p_n_size_browse-bin_8""",
'screen_11_2_12':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_size_browse-bin%3A13580785011&dc&qid=1594230813&rnid=2242797011&ref=sr_nr_p_n_size_browse-bin_7""",
'screen_12_2_13':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_size_browse-bin%3A13580784011&dc&qid=1594230883&rnid=2242797011&ref=sr_nr_p_n_size_browse-bin_6""",
'screen_13_2_14':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_size_browse-bin%3A3545275011&dc&qid=1594230915&rnid=2242797011&ref=sr_nr_p_n_size_browse-bin_5""",
'screen_14_2_15':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_size_browse-bin%3A2423840011&dc&qid=1594230944&rnid=2242797011&ref=sr_nr_p_n_size_browse-bin_4""",
'screen_15_2_16':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_size_browse-bin%3A2423841011&dc&qid=1594230989&rnid=2242797011&ref=sr_nr_p_n_size_browse-bin_3""",
'screen_17':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_size_browse-bin%3A7817234011&dc&qid=1594231073&rnid=2242797011&ref=sr_nr_p_n_size_browse-bin_1"""}

RAM_sizes = ['4', '8', '12', '16','32']

RAM = {'RAM_4':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_five_browse-bin%3A7817222011&dc&qid=1594231142&rnid=2257851011&ref=sr_nr_p_n_feature_five_browse-bin_8""",
'RAM_8':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_five_browse-bin%3A7817224011&dc&qid=1594231177&rnid=2257851011&ref=sr_nr_p_n_feature_five_browse-bin_6""",
'RAM_12':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_five_browse-bin%3A13580791011&dc&qid=1594231211&rnid=2257851011&ref=sr_nr_p_n_feature_five_browse-bin_5""",
'RAM_16':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_five_browse-bin%3A13580790011&dc&qid=1594231233&rnid=2257851011&ref=sr_nr_p_n_feature_five_browse-bin_4""",
'RAM_32':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_five_browse-bin%3A13580788011&dc&qid=1594231260&rnid=2257851011&ref=sr_nr_p_n_feature_five_browse-bin_2"""}

weights_list = ['3-', '3-4', '4-5', '5-6', '7-8', '8']

weight = {'weight_2_3':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_eleven_browse-bin%3A9521903011&dc&qid=1594231338&rnid=9521902011&ref=sr_nr_p_n_feature_eleven_browse-bin_1""",
'weight_3_2_4':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_eleven_browse-bin%3A13580795011&dc&qid=1594231405&rnid=9521902011&ref=sr_nr_p_n_feature_eleven_browse-bin_2""",
'weight_4_2_5':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_eleven_browse-bin%3A13580796011&dc&qid=1594231443&rnid=9521902011&ref=sr_nr_p_n_feature_eleven_browse-bin_3""",
'weight_5_2_6':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_eleven_browse-bin%3A13580797011&dc&qid=1594231480&rnid=9521902011&ref=sr_nr_p_n_feature_eleven_browse-bin_4""",
'weight_7_2_8':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_eleven_browse-bin%3A13580799011&dc&qid=1594231514&rnid=9521902011&ref=sr_nr_p_n_feature_eleven_browse-bin_6""",
'weight_8':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_eleven_browse-bin%3A9521906011&dc&qid=1594231545&rnid=9521902011&ref=sr_nr_p_n_feature_eleven_browse-bin_7"""}

HD_type_list = ['SSD', 'HDD', 'Hybrid']

HD_type = {'HD_type_HDD':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_twelve_browse-bin%3A9521909011&dc&qid=1594231648&rnid=9521907011&ref=sr_nr_p_n_feature_twelve_browse-bin_2""",
'HD_type_SSD':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_twelve_browse-bin%3A9521908011&dc&qid=1594231758&rnid=9521907011&ref=sr_nr_p_n_feature_twelve_browse-bin_1""",
'HD_type_Hybrid':"""https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565108%2Cp_n_feature_twelve_browse-bin%3A9521910011&dc&qid=1594231785&rnid=9521907011&ref=sr_nr_p_n_feature_twelve_browse-bin_3"""}