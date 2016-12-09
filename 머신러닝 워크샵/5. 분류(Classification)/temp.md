이제 직접 Naive Bayes Classifier 를 구현해 보겠습니다. 여러 개의 이미 트레이닝된 모델이 있을 때, 주어진 텍스트가 어떤 모델에 더 적합한지 판정 (classify) 하는 방법론을 코딩을 통해 구현해보겠습니다. 우리에게 사탕을 뽑아주는 기계 두 개가 있다고 합시다.

* 첫 번째 기계 <img src="http://bit.ly/2hlmUmJ" align="center" border="0" alt="($M_1$): $\{\theta_{red} = 0.7, \theta_{green} = 0.2, \theta_{blue} = 0.1\}$" width="361" height="21" />
* 두 번째 기계 <img src="http://www.sciweavers.org/tex2img.php?eq=%28%24M_2%24%29%3A%20%24%5C%7B%5Ctheta_%7Bred%7D%20%3D%200.3%2C%20%5Ctheta_%7Bgreen%7D%20%3D%200.4%2C%20%5Ctheta_%7Bblue%7D%20%3D%200.3%5C%7D%24&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="($M_2$): $\{\theta_{red} = 0.3, \theta_{green} = 0.4, \theta_{blue} = 0.3\}$" width="361" height="21" />

그리고 우리에게 첫 번째인지 두 번째 기계에서 뽑았을지는 모르지만, 다음과 같은 10개의 사탕들이 있다고 합시다.

* red: 4
* green: 3
* blue: 3

우리는 일반적으로 첫 번째가 두 번째 기계보다 많이 쓰인다는 것을 알고 있습니다.

* <img src="http://www.sciweavers.org/tex2img.php?eq=%24p%28M_1%29%20%3D%200.7%24&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="$p(M_1) = 0.7$" width="100" height="19" />
* <img src="http://www.sciweavers.org/tex2img.php?eq=%24p%28M_2%29%20%3D%200.3%24&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="$p(M_2) = 0.3$" width="100" height="19" />

우리가 계산하고 싶은 것은, 이미 우리에게 10개의 사탕이 있을 때, 이 사탕을 보고 이것들이 몇 번째 기계에서 나왔을지에 대한 확률을 구하는 것입니다. 이것은 $p(M_k|x)$, $k \in \{1, 2\}$ 로 나타낼 수 있습니다. 이제 Bayes' Rule 을 적용하면,

<img src="http://www.sciweavers.org/tex2img.php?eq=%24p%28M_k%7Cx%29%20%3D%20%5Cfrac%7Bp%28M_k%29p%28x%7CM_k%29%7D%7Bp%28x%29%7D%24&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="$p(M_k|x) = \frac{p(M_k)p(x|M_k)}{p(x)}$" width="175" height="31" /> 이고

여기서 <img src="http://www.sciweavers.org/tex2img.php?eq=%24p%28x%29%24&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="$p(x)$" width="36" height="19" /> 는 기계에 관계없이 같으므로 무시하겠습니다. 우리가 구하고자 하는 것은 사탕들이 이 기계에서 나올 확률의 절대값이 아니고, 1번과 2번 기계 중 어떤 기계인지, 즉 상대적인 확률을 구하고자 하는 것이기 때문입니다. 그러므로

<img src="http://www.sciweavers.org/tex2img.php?eq=%24p%28M_1%7Cx%29%20%5Cpropto%20p%28M_1%29p%28x%7CM_1%29%20%3D%20%24&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="$p(M_1|x) \propto p(M_1)p(x|M_1) = $" width="219" height="19" />
<img src="http://www.sciweavers.org/tex2img.php?eq=%20%240.7%20%2A%20%280.7%5E4%20%2A%200.2%5E3%20%2A%200.1%5E3%29%20%3D%201.345%20%2A%2010%5E%7B-6%7D%24&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt=" $0.7 * (0.7^4 * 0.2^3 * 0.1^3) = 1.345 * 10^{-6}$" width="344" height="21" />

<img src="http://www.sciweavers.org/tex2img.php?eq=%24p%28M_2%7Cx%29%20%5Cpropto%20p%28M_2%29p%28x%7CM_2%29%20%3D%20%24%0A%20%240.3%20%2A%20%280.3%5E4%20%2A%200.4%5E3%20%2A%200.3%5E3%29%20%3D%204.199%20%2A%2010%5E%7B-6%7D%24&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="$p(M_2|x) \propto p(M_2)p(x|M_2) = $ $0.3 * (0.3^4 * 0.4^3 * 0.3^3) = 4.199 * 10^{-6}$" width="571" height="22" />


두 번째 기계가 첫 번째 기계보다 적게 사용된다는 사실을 고려하더라도 <img src="http://www.sciweavers.org/tex2img.php?eq=%28%24p%28M_2%29%20%3D%200.3%24%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="($p(M_2) = 0.3$)" width="112" height="19" />, 두 번째 기계일 확률이 훨씬 더 높은 것을 알 수 있습니다. 이제 두 확률을 normalize 하겠습니다.

<img src="http://www.sciweavers.org/tex2img.php?eq=%24%281.345%20%2A%2010%5E%7B-6%7D%2C%204.199%20%2A%2010%5E%7B-6%7D%29%20%5Crightarrow%20%280.243%2C%200.757%29%24&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="$(1.345 * 10^{-6}, 4.199 * 10^{-6}) \rightarrow (0.243, 0.757)$" width="389" height="21" />

그러므로 10개의 사탕 샘플을 통해, Naive Bayes Classifier를 사용했을 때 이것들이 두 번째 기계에서 뽑혔을 확률이 <img src="http://www.sciweavers.org/tex2img.php?eq=%2475.7%5C%25%24&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="$75.7\%$" width="56" height="14" />임을 알아낼 수 있습니다.

<hr>

**과제**

세 개의 문장을 입력받을 것입니다. 먼저 텍스트 모델을 트레이닝하겠습니다. 첫 번째 및 두 번째 문장을 이용해 각각 하나씩 두 개의 텍스트 모델을 만듭니다. 그 뒤, 베이즈 법칙을 이용해 세 번째 문장이 첫 번째 문장에서 생성될 확률과 두 번째 문장에서 생성될 확률을 구한 뒤 리턴합니다.

`naive_bayes` 함수를 제외한 나머지 함수들은 모두 구현되어 있습니다. `log_likelihood` 함수를 사용해서 training model에서 testing 데이터를 생성할 (Laplace smoothing이 적용된) 확률을 계산할 수 있습니다. `log_likelihood(training, testing, alpha)` 함수는 testing 문서가 training 문서를 통해 만들어진 모델에서 생성될 확률의 로그값을 리턴합니다. 즉, $\mathrm{log} P(\mathrm{testing}|\mathrm{training})$ 값을 의미합니다.

그 다음으로 나이브 베이즈 분류를 수행합니다. 첫 번째 문장에서 생성된 모델은 위의 예제에서 첫 번째 기계, 두 번째 문장에서 생성된 모델은 두 번째 기계, 그리고 테스트할 문장은 사탕들이라고 생각하면 됩니다.

### 입력

문장 세 줄과 $\alpha$ 값, 그리고 세 번째 문장이 첫 번째 클래스에 속할 확률, 그리고 두 번째 클래스에 속할 확률이 차례대로 입력됩니다. 즉,

* 첫 번째 줄: $C_1$ (사탕 문제에서 $M_1$, 기계 1)
* 두 번째 줄: $C_2$ (사탕 문제에서 $M_2$, 기계 2)
* 세 번째 줄: $x$ (사탕 문제에서 사탕 10개)
* 네 번째 줄: $\alpha$ (laplace smoothing에 사용되는 숫자)
* 다섯 번째 줄: $p(C_1)$ (사탕 문제에서 $p(M_1)$)
* 여섯 번째 줄: $p(C_2)$ (사탕 문제에서 $p(M_2)$)

### 출력

이전 과제에서 연습한 bag-of-words 및 likelihood 함수를 사용하여, $p(C_1|x)$ 및 $p(C_2|x)$ 의 normalize된 값을 계산하여 출력합니다. 중간에 확률 계산을 위해 확률의 로그값을 리턴해야 합니다. 이전 과제와 같이, 로그값을 계산하는 이유는 확률이 매우 작아지면 underflow 현상으로 인해 숫자가 제대로 표현되지 않고 오차가 커지기 때문입니다.

### 테스트 입력

    John likes to watch movies. Mary likes movies too.
    In the machine learning, naive Bayes classifiers are a family of simple probabilistic classifiers.
    John also likes to watch football games.
    0.1
    0.5
    0.5

### 테스트 출력

    (0.9999985271309568, 1.4728690432649586e-06)
