# 创建和修改代码库
要点如下：
* 创建代码库，在文件夹下面执行
```bash
git init
```
但初始化并不会产生提交操作；
* 查看当前git状态，显示未被跟踪的文件：
```bash
git status
```
* 关于暂存区的一些指令：
   * 添加文件到暂存区（staged）：
   ```bash
   git add filename
   ```
   * 如果加入到暂存区出错，可使用如下命令将其从暂存区删除：
   ```bash
   git reset
   ```
   或
   ```bash
   git reset filename
   ```
* 提交到repo时，可使用：
```bash
git commit # 此时会弹出编辑器
```
或
```bash
git commit -m "message"
```
提交信息的风格可参见[风格指南](https://gdgdocs.org/document/d/1HZ9Bo1mDKhe3JZzmFvekL5P2WHafpCaEXTymj__FUYw/pub?embedded=true).
* [git命令的速查表](https://services.github.com/on-demand/downloads/zh_CN/github-git-cheat-sheet/)以及一个[思维图](https://github.com/dataanalysisgroup/courses/blob/master/data/%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%20Git%20%E5%92%8C%20GitHub/troubleshooting_guide.pdf)
* 各种文件版本之间的比较：

    * 工作目录与暂存区文件的比较（已修改，但未提交）：
  ```bash
  git diff
  ```
    * 暂存区与最近一次提交的比较（如已提交，则显示为空）：
  ```bash
  git diff --staged
  ```
    * 取消最近本地所做的修改，回到最近的一次提交：
  ```bash
  git reset --hard
  ```
* 关于分支的使用：

   * 显示当前所有的分支以及默认分支：
   ```bash
   git branch
   ```
   * 创建分支：
   ```bash
   git branch branchname
   ```
   * 切换分支：
   ```bash
   git checkout branchname
   ```
