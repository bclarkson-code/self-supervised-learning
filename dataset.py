import pytorch_lightning as pl
import os
from urllib.request import urlopen
from shutil import copyfileobj 
from tqdm import tqdm

class XRayDataset(pl.LightningDataModule):
    data_urls = [
        'https://nihcc.box.com/shared/static/vfk49d74nhbxq3nqjg0900w5nvkorp5c.gz',
        'https://nihcc.box.com/shared/static/i28rlmbvmfjbl8p2n3ril0pptcmcu9d1.gz',
        'https://nihcc.box.com/shared/static/f1t00wrtdk94satdfb9olcolqx20z2jp.gz',
        'https://nihcc.box.com/shared/static/0aowwzs5lhjrceb3qp67ahp0rd1l1etg.gz',
        'https://nihcc.box.com/shared/static/v5e3goj22zr6h8tzualxfsqlqaygfbsn.gz',
        'https://nihcc.box.com/shared/static/asi7ikud9jwnkrnkj99jnpfkjdes7l6l.gz',
        'https://nihcc.box.com/shared/static/jn1b4mw4n6lnh74ovmcjb8y48h8xj07n.gz',
        'https://nihcc.box.com/shared/static/tvpxmn7qyrgl0w8wfh9kqfjskv6nmm1j.gz',
        'https://nihcc.box.com/shared/static/upyy3ml7qdumlgk2rfcvlb9k6gvqq2pj.gz',
        'https://nihcc.box.com/shared/static/l6nilvfa9cg3s28tqv1qc1olm3gnz54p.gz',
        'https://nihcc.box.com/shared/static/hhq8fkdgvcari67vfhs7ppg2w6ni4jze.gz',
        'https://nihcc.box.com/shared/static/ioqwiy20ihqwyr8pf4c24eazhh281pbu.gz'
    ]
    def __init__(self):
        super().__init__()
        self.download_dir = 'tmp'
        self.data_dir = 'images'

    def _download_file(self, url, dest_path):
        '''
        Download a file from a url
        '''
        with urlopen(url) as in_stream, open(dest_path, 'wb') as out_file:
            copyfileobj(in_stream, out_file)

    def _download_dataset(self):
        # Download the files
        for idx, url in tqdm(enumerate(self.data_urls), desc='Downloading Data', total=len(self.data_urls)):
            index_string = str(idx+1).zfill(2)
            filename = f'images_{index_string}.tar.gz'
            dest_path = os.path.join(self.download_dir, filename)
            self._download_file(url, dest_path)
        

    def setup(self):
        if not os.path.exists('tmp'):
            # Make a directory to store the downloaded files
            os.mkdir('tmp')

            self._download_dataset()
        
        

        
