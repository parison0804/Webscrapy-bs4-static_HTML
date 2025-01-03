import os 

class DataSave:
    #initializing
    def __init__(self, path):
        self.path = path
    
    def save(self, data):
        if not os.path.exists(self.path):
            #create the file if it is not exist with writing mode
            print('File does not exist. Creating file:{self.path}')
            open(self.path,'w').close()
        
        with open(self.path, 'a') as fp:
            #using appedning mode to save data
            print('Start writing data')
            fp.write(str(data) + '\n')
        fp.close()



if __name__ == '__main__':
    test_data = 'this is a test'
    save_path = '/Users/user000_1/Desktop/Github/cnBeta scrapy/save_test.txt'
    ds = DataSave(save_path)
    ds.save(test_data)  # save data to file