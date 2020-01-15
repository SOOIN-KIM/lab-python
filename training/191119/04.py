def add(v,w):
    '''
    주어진 두개의 n차원 벡터에서 성분별로 더하기를 해서,
    새로운  n차원 벡터를 리턴

    :param v: n차원 벡터(성분이 n개인 벡터)
    :param w: n차원 벡터(성분이 n개인 벡터)
    :return: 각 성분별로 더하기 결과를 갖는 벡터
    '''

    result= []
    for i in range(len(v)):
        result.append(v[i] + w[i])
    return result

if __name__=='__main__':
    v = [1,2,4,5,6]
    w = [3,4,6,4,7]
    result =add(v,w)
    print('add=', result)