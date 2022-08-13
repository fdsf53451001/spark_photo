import requests
import json
import numpy as np
import matplotlib.pyplot as plt

class YTSpider():
    def __init__(self, vid):
        self.vid = vid

    def get_most_replayed(self):
        request_url = "https://yt.lemnoslife.com/videos?part=mostReplayed&id="+self.vid
        response = requests.get(request_url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('request failed')
            exit(1)
    
    def decode_data(self,data):
        heatMarkers = data['items'][0]['mostReplayed']['heatMarkers']
        result = np.array([])
        for row in heatMarkers:
            t = len(result)
            # pad 0 if timeline missing
            if t<row['heatMarkerRenderer']['timeRangeStartMillis']:
                result=np.pad(result,(0,0),'constant', constant_values=(0,row['heatMarkerRenderer']['timeRangeStartMillis']-t)) 

            value = row['heatMarkerRenderer']['heatMarkerIntensityScoreNormalized']
            count = row['heatMarkerRenderer']['markerDurationMillis']
            result = np.append(result,[value for _ in range(count)])

        return result

    def draw_graph(self,result):
        # time metric = milis
        x = [i/1000 for i in range(len(result))]
        plt.plot(x,result)
        plt.show()
    
    def analyze(self,result,threshold):
        map = result>threshold
        print('most view times :',np.count_nonzero(map==True)/1000)
        return map

if __name__ == '__main__':
    ytspider = YTSpider('i5nb0VvktN8')
    data = ytspider.get_most_replayed()
    result = ytspider.decode_data(data)
    ytspider.draw_graph(result)
    threshold = 0.9
    ytspider.analyze(result,threshold)