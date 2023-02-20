# some training parameters
EPOCHS = 10
BATCH_SIZE = 32
NUM_CLASSES = 2
image_height = 45
image_width = 45
channels = 3

model_save_name = "EfficientNetV2B0_ivy"
model_dir = "trained_models/ivy/"+model_save_name+"/" # = save_dir

dir_base = "/home/mirap/0_DATABASE/ivy_coverage/cropped/"
train_dir = dir_base + "set1"
valid_dir = dir_base + "5_fold/fold1"
test_dir = dir_base + "test"
test_image_path = test_dir + "/ivy/resultsivy_002_018.jpg"
