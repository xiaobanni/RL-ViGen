import os
import imageio

def create_gif_from_images(folder_path, output_filename):
    # 获取文件夹中的所有文件
    all_files = os.listdir(folder_path)
    
    # 仅选取以"display"开头的jpg文件
    display_files = [f for f in all_files if f.startswith("display") and f.endswith(".jpg")]
    
    # 对文件名进行排序，确保图像按正确的顺序添加
    display_files.sort()
    
    # 读取图像并存储为列表
    images = [imageio.imread(os.path.join(folder_path, filename)) for filename in display_files]
    
    # 使用imageio.mimsave将图像列表存储为GIF
    output_path = os.path.join(folder_path, output_filename)
    imageio.mimsave(output_path, images)

# 要读取图像的文件夹路径
folder_path = "exp_local/2023.09.11/025712_action_repeat=2,feature_dim=50,lr=1e-4,nstep=1,num_train_frames=1001000,save_snapshot=True,save_video=False,seed=3,task=carla,use_tb=True,use_wandb=False,wandb_group=/images-2023-09-11-02-57-16"

# 输出的GIF文件名
output_filename = "display_images.mp4"

# 执行函数
create_gif_from_images(folder_path, output_filename)
