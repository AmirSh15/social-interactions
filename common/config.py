import argparse

argparser = argparse.ArgumentParser(description="Evalai challenge: Talking to me")

output_address = "/media/amir_shirian/Amir/Datasets/Ego4D"
argparser.add_argument("--test_data_path", type=str, default="./final_test_data")
argparser.add_argument("--seg_info", type=str, default="./seg_info.json")
# argparser.add_argument(
#     "--img_path",
#     type=str,
#     default="../../social-interactions/data/video_imgs",
#     help="Video image directory",
# )
argparser.add_argument(
    "--img_path",
    type=str,
    default=output_address+"/data/video_imgs",
    help="Video image directory",
)
# argparser.add_argument(
#     "--wave_path",
#     type=str,
#     default="../../social-interactions/data/wave",
#     help="Audio wave directory",
# )
argparser.add_argument(
    "--wave_path",
    type=str,
    default=output_address+"/data/wave",
    help="Audio wave directory",
)
# argparser.add_argument(
#     "--gt_path",
#     type=str,
#     default="../../social-interactions/data/result_TTM",
#     help="Groundtruth directory",
# )
argparser.add_argument(
    "--gt_path",
    type=str,
    default="data/result_TTM",
    help="Groundtruth directory",
)
argparser.add_argument(
    "--json_path",
    type=str,
    default="./data/json_original",
    help="Face tracklets directory",
)
# argparser.add_argument(
#     "--train_file",
#     type=str,
#     default="../../social-interactions/data/split/train.list",
#     help="Train list",
# )
argparser.add_argument(
    "--train_file",
    type=str,
    default="data/split/train.list",
    help="Train list",
)
# argparser.add_argument(
#     "--val_file",
#     type=str,
#     default="../../social-interactions/data/split/val.list",
#     help="Validation list",
# )
argparser.add_argument(
    "--val_file",
    type=str,
    default="data/split/val.list",
    help="Validation list",
)
# argparser.add_argument('--test_file', type=str, default='./test.list', help='Test list')
argparser.add_argument(
    "--train_stride", type=int, default=3, help="Train subsampling rate"
)
argparser.add_argument(
    "--val_stride", type=int, default=1, help="Validation subsampling rate"
)
argparser.add_argument(
    "--test_stride", type=int, default=1, help="Test subsampling rate"
)
argparser.add_argument("--epochs", type=int, default=40, help="Maximum epoch")
argparser.add_argument("--batch_size", type=int, default=100, help="Batch size")
argparser.add_argument("--num_workers", type=int, default=0, help="Num workers")
argparser.add_argument("--lr", type=float, default=5e-4, help="Learning rate")
argparser.add_argument(
    "--weights", type=list, default=[0.266, 0.734], help="Class weight"
)
argparser.add_argument("--eval", action="store_true", help="Running type")
argparser.add_argument(
    "--model", type=str, default="BaselineLSTM", help="Model architecture"
)
argparser.add_argument("--rank", type=int, default=0, help="Rank id")
argparser.add_argument("--device_id", type=int, default=0, help="Device id")
argparser.add_argument(
    "--exp_path", type=str, default="evalai_test/output", help="Path to results"
)
argparser.add_argument(
    "--checkpoint", type=str, default="evalai_test/best.pth", help="Checkpoint to load"
)
