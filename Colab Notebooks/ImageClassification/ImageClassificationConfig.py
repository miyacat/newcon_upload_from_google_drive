#ファイルパスの設定
PATH = '/content/drive/MyDrive/MLData'
DATA_NAME = 'images_dogcat'

#分類の設定。上記のパスの中のフォルダ名を列挙
CLASSES = ['dog', 'cat']
NUM_CLASSES = len(CLASSES)

#学習・検証時の画像サイズを指定
#このサイズに変換して利用する
IMAGE_SIZE = 224
INPUT_CHANNELS = 3