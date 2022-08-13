import os

class SearchKeyword():
    def __init__(self,dataset):
        self.dataset = dataset
        self.actions = { 'no_action':0,'standing':1,'falling':2,'moving':3,'setting':4,'digging':5,
                    'blocking':6,'spiking':7,'jumping':8,'waiting':9
                }
        self.type_of_actions = len(self.actions) # one with no action
        self.people_count_in_picture = 20
    
    def search(self,keyword):
        try:
            keyword = self.actions[keyword]
        except KeyError:
            print('keyword not found!')
            return []
        
        file_list = []
        search_count = 0
        for no in os.listdir(self.dataset):
            for action_series in os.listdir(os.path.join(self.dataset,no)):
                with open(os.path.join(self.dataset,no,action_series),'r') as f:
                    search_count += 1
                    line = f.readline()
                    line = line.split(' ')
                    for person in range(self.people_count_in_picture):
                        if line[person] == str(keyword):
                            file_list.append(str(os.path.join(no,action_series))[:-4])
                            break
        print('search finish!')
        print('search files :',search_count)
        print('found :',len(file_list))

        return file_list

if __name__ == '__main__':
    dataset = 'G:\Github\LSTM-action-detection\dataset_lstm'
    sk = SearchKeyword(dataset)
    res = sk.search('jumping')
    # print(res)