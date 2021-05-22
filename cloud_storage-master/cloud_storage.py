import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AwvGoBJKMKRAwCvF8MDkDpuYwi5tf5PO6vgrjT4pW8IlBQt-5MxGU4LX-U86sjl6K8MB5tr-rV1v22VjuA6d7SFeczQvzMcfg6mmCBJl78KAUEwLrj1COw1DA566eJuBqn2e9Uc'
    transferData = TransferData(access_token)

    file_from = input("/Users/sudipkdas/Desktop/cloud_storage-master/test2.txt")
    file_to = input("/Game 3/test2.txt ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
