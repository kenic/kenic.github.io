import os
import glob
from git import Repo # GitPythonを使う

def define_env(env):
    # Gitリポジトリの読み込み
    try:
        repo = Repo(env.project_dir)
    except:
        repo = None

    def get_git_date(filepath):
        if repo is None: return 0
        try:
            rel_path = os.path.relpath(filepath, env.project_dir)
            commits = list(repo.iter_commits(paths=rel_path, max_count=1))
            if commits:
                return commits[0].committed_datetime.timestamp()
        except:
            pass
        return os.path.getmtime(filepath)

    @env.macro
    def latest_article_url(directory="blog"):
        # 記事を探す
        search_path = os.path.join(env.project_dir, 'docs', directory, '*.md')
        files = glob.glob(search_path)
        
        if not files: return "#"

        # Gitの日付順で並べ替え（一番新しいものを取得）
        latest_file = max(files, key=get_git_date)
        
        # URLに変換
        rel_path = os.path.relpath(latest_file, os.path.join(env.project_dir, 'docs'))
        return f"/{rel_path.replace(os.sep, '/').replace('.md', '/')}"
