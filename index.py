import pickle

models = {}
model_names = ['logistic_regression_model.pkl', 'decision_tree_model.pkl', 'random_forest_model.pkl']

for model_name in model_names:
    with open(model_name, 'rb') as f:
        models[model_name.split('_model.pkl')[0]] = pickle.load(f)

# data = [input("Enter the news data: ")]
data=["So Rachel, now that we re on the subject of taxes President Trump PAID, how about we remind Americans about the tax evaders/MSNBC hosts employed by your leftist network:MSNBC host and perpetual race agitator Al Sharpton certainly gets around quite a bit. Any time there s any sort of Black Lives Matter protest or urban unrest with a race relations twist, Sharpton seems to appear within hours as if by magic. So busy is the man s schedule that he apparently still can t find time to sit down with an accountant and clear up more than a half million dollars in unpaid taxes which the IRS has been pestering him about for some time now. In a follow-up to their previous reports on the subject, the Daily Caller finds that both Sharpton and his MSNBC colleague Joy-Ann Reid are still on the Tax Man s naughty list, despite assurances last year that they were working to settle up their accounts.Watch Jesse Waters confront Al Sharpton and ask him about his unpaid taxes: https://www.youtube.com/watch?v=e9YI5-c1udYMSNBC national correspondent Joy-Ann Reid has yet to pay off her still open nearly $5,000 tax warrant that attracted a good bit of attention last year. Ditto for the nearly $600,000 for two tax warrants that New York lists for MSNBC host Rev. Al Sharpton.In April 2016, New York filed a $4,948.15 tax warrant against Joy-Ann Reid, who serves as managing editor of theGrio.com and until earlier this year hosted MSNBC s The Reid Report, and her husband, Jason. Reid has called taxes on the wealthy  a basic fairness argument,  also arguing for  smart spending and smart tax increases  to create economic growth.   Daily CallerMeanwhile, Sharpton, whose state and federal delinquencies are the stuff of legend, has, according to records accessed Monday evening at least two open New York tax warrants for nearly $600,00. One judgment, dated May 19, 2009, is for $103,156.06. The other, from December 16, 2008, is for $492,612.41.Sharpton insisted to the New York Post and New York Times in 2014 that he was paying down his debts. The Times article noted that his insistence conflicted with  information provided by state officials.   Hot AirMaybe the folks over at MSNBC shouldn t worry so much about the taxes Trump PAID and should focus instead on their host s UNPAID taxes!"]

for model_name, model in models.items():
    predictions = model.predict(data)
    if predictions[0] == 1:
        print(f"{model_name.capitalize()} Prediction: Real News")
    else:
        print(f"{model_name.capitalize()} Prediction: Fake News")