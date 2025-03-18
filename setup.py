from setuptools import setup, find_packages

setup(
    name='pyyorozuya',  # パッケージ名（pip listで表示される）
    version="1.0.0",
    description="Useful tools for you",
    author='akilasatolu',
    packages=find_packages(),  # 使うモジュール一覧を指定する
    license='MIT',
    python_requires='>=3.12.7',
)