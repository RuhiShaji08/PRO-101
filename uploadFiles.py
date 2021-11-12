import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        db = dropbox.Dropbox()
        f =open(file_from,'rb')
        db.files_upload(f.read(), file_to)        

def main():
    access_token = 'sl.A7XX3nfLdEQ9Zl297nbQnKmsFCzLxAl1R7VNK24v9Sqfisu7lOP1370ndoZjVGfmZ4tNHY5KBuKsaqIwerjTZBUVKcForA-LehOblYeoBjGUOK7TsOxx3IfLDxwQutnPf1h_G2gv-7WT'
    transferData = TransferData(access_token)
    file_from = input('Enter file path to transfer :')
    file_to = input('Enter full file path to upload to dropbox')

    transferData.upload_file(file_from,file_to)
    print('file has been moved')

main()