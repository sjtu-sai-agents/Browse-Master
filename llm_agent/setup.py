from setuptools import setup, find_packages

setup(
    name='llm_agent',  
    version='0.1.0',          
    description='implementation of the llm agnet framework',  
    packages=find_packages(), 
    install_requires=[        
        'openai>=1.13.0',
    ],
    classifiers=[             # 元数据，描述包的分类
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',  
)