import requests
url = 'https://baidu.com'

#生成一个requests对象 使用get方法
# r = requests.get(url)

# 用post请求数据
# r = requests.post(url,data = {'key':'value'})

# 其他请求方式：
# r = delete(url)
# r = put(url)
# r = options(url)
# r = head(url)

# 传入需要的参数，用：
payload = {'key1':'value1', 'key2':'value2'}
r = requests.get(url, params=payload)




r"""Sends a GET request.

    :param url: URL for the new :class:`Request` object.    url地址，必须
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the body of the :class:`Request`. 字典类型的参数，可选
    :param \*\*kwargs: Optional arguments that ``request`` takes. 可选参数 
    :return: :class:`Response <Response>` object  返回一个response对象
    :rtype: requests.Response 
    
    kwargs.setdefault('allow_redirects', True) 
    return request('get', url, params=params, **kwargs)
    """

def main():
# 返回请求的url
    print(r.url)
# 返回状态码
    print(r.status_code)
# 返回headers信息
    print(r.headers)
#返回字符集
    print(r.encoding)
# 制定返回的内容的编码
    r.encoding = 'utf8'
# 返回网页内容
    print(r.text)
# 返回二进制数据
    print(r.content)
# 返回cookie信息
    print(r.cookies)
# 返回json
    print(r.json())

if __name__ == '__main__':
    main()
