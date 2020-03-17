# IBM Watson Machine Learning 
## sp20-516-252 Jessica Zhu

## Introduction 

IBM Watson Machine Learning has features for training and deploying machine
 learning models and neural networks using users' own data. The models can be
  deployed in applications. 

Watson Machine Learning offers a range of tools for model building, training
 and deployment. Tools range from completely automating training process for
  quick prototyping to total control on specifications of a model.
  
  A typical process for machine learning model is shown below:
![Fig 1 - Process for Machine Learning Model [#fig1:sp20-516-252-machine-learning-process
]](image/ml_process.png){#fig1:sp20-516-252-machine-learning-process} Fig. 1
 Typical Process for Machine Learning Model

## Features

### Watson Studio tools

IBM Watson Studio offers a set of tools for model design, training, deployment and management.

- AutoAI experiments
 
 It allows to select the best performing pipeline as a
 machine learning model. Several automated steps include data preprocessing
 , best estimator selection and the generation of model candidate pipelines
  for review and compare.

![Fig 2 - AutoAI Features [@AutoAI-2020-sp20-516
-252
]](image/autoai_overview.png){#fig2:sp20-516-252-auto-ai-features
} Fig. 2 AutoAI Experiment Features

- Spark MLlib modeler

Its flow editor can create a machine learning flow, which is a graphical
 representation of a data model. It presents a graphical view of model while
  building it by combining nodes that represent algorithm nodes. These nodes
   represent a transformation or processing step on data.

- SPSS modeler

It shows a graphical view of the model while it is being built by combining
 nodes representing objects or actions. It is designed based upon established
  SPSS Modeler client software and the industry0strandard CRISP-DM model.

- Neural network modeler

Its flow editor helps to create a deep learning flow, which is a graphical
 representation of a neural network design. It can be used to design and run
  experiments.   
  
![Fig 4 - Neural Workflow [@Neural Workflow-2020-sp20-516
-252
]](image/neural-workflow.png){#fig2:sp20-516-252-neural-workflow
} Fig. 3 A Sample Neural Network Design


- Experiment Builder

In the case that thousands of models need to be trained to identify the
 right combination of data and hyperparameters, the experiment builder
  simplify the model training process along with an auto-allocated GPU
   compute containers. [sp20-516-252-watson-ml-overview]
   
### architecture and services

Watson Machine Learning is built based upon Kubernetes and Docker components
. It supports the following infrastructure and services:

- Programming Interfaces:

Python client library, Command Line Interface and REST API.

- Training Infrastructure 

Distributed training that allows to run training jobs among multiple servers
Common frameworks
GPU
Hyperparameter optimization 

- Deployment Infrastructure

Trained models: they can be deployed for batch processing, as a web service
 or with streaming data;
 
Python functions: they can be deployed to simplify AI solutions.

## Getting Started

Here we are giving you a brief demonstration of Waston Machine Learning to
 show how simple it is to train and deploy a model.
 
- Create an IBM Cloud account (free) and sign in

<https://cloud.ibm.com/login>

![Fig 3 - Sign In Page [@sign-in-page-2020-sp20-516
-252
]](image/sign_in_page.png){#fig2:sp20-516-252-sign-in-page
} Fig. 3 Sign In Page

- Access to Watson Machine Learning

You will be directed to the `Dashboard` page. Click `Services` on `Resource
 Summary` section. Type in `Machine Learning` in the search section to search
  for Watson Machine Learning among many other tools. Then click `Machine
   Learning-lb`.

Now you should be directed to the Watson Machine Learning page like below:
![Fig 4 - Watson Machine Learning Page [@machine-learning-page-2020-sp20-516
-252
]](image/machine-learning-page.png){#fig2:sp20-516-252-machine-learning-page
} Fig. 3 Watson Machine Learning Page

We are using `Production Line Prediction` as sample data. Go to the bottom
 of the page to the `Sample Applications` part, and click `+` sign on `Product
  Line Prediction` section. 
  
Instructions on the following steps can be found [here](https://developer.ibm.com/technologies/data-science/tutorials/watson-studio-auto-ai/).
Waston studio allows you to train, build and deploy a model in just a minute.

### Deployment 

There are four supported deployment methods: 

* Watson Studio project

Simply use the *Deployments* tab of the project in Watson Studio. Test data
 can be sumbitted either in a typed form, JSON-formatted code, or as a data
  sources. It is very simple that you don't have to write a line of code. [sp20-516-252
    -model-deployment]

* Python Client 

Models can be deployed using the Python client if you are working on a local
 Python development environment or a Python notebook. 
 
In fact, you can train your model by submitting a training job to IBM Cloud
 infrastructure by writing a few lines of code on your local Python notebook
 . During the training process, you can run command to get updates on its
  training progress. 
  
  After training, you can store the model in Watson Machine Learning
   repository. Then you can deploy the model by applying the test data to the
    stored model. A prediction and actual result will be returned. [sp20-516-252
    -model-deployment]
    
An full example and code that demonstrate the use of Python client can be
 found [here](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-python-mnist-tutorial.html).  

* REST API

This method offers the ultimate flexibility. A model can be deployed from
 your local machine without having Watson Machine Learning CLI installed. You
  can also deploy a model without having a Watson Machine Learning client
   library imported.
   
   To achieve this, you need the endpoint URL from the *Implementation* tab
    of the model's deployment page. The page also provides sample code to
     help structure the payload for the deployment. You need to manually
      input a set of parameters to the payload. [sp20-516-252-model-deployment]
      
A sample code using REST API can be found [here](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-deploy_new.html?linkInPage=true#rest).  

* Command Line Interface (CLI)

CLI allows you to fully automate training and deployment process on your
 local machine. Or you can use it if you simply prefer CLI. 
 
 You need to install Watson Machine Learning CLI on your computer. After
  training and storing the model in your Watson Machine Learning repository
  , you can deploy model using command lines:
  
  ```
bx ml deploy MODEL-ID DEPLOYMENT-NAME<full path to test data>
bx ml deploy -b MODEL-ID DEVELOPMENT-NAME<path to batch json>
-b - Enable batch deployment mode
```
[sp20-516-252-model-deployment]

An example and sample code using CLI can be found [here](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-deploy_new.html?linkInPage=true#rest).  

## Pricing

For United States, there are three pricing plans: Lite
, Standard and Professional.
 
 - Lite - Free of Charge
 
 It provides up to five deployed models, 5000 predictions per month, and 50
  capacity unit-hours per month.
  
- Standard

$0.50 USD/ 1000 predictions, $0.50 USA/capacity unit-hour

- Professional

$1,000 USD/instance, $0.40 USD/1000 predictions, $0.40 USD/capacity unit-hour

The prices listed are valid as of March 2020. This list provides a general
guide for each plan. Capacity unit-hour also depends upon CPU and RAM being
 used, more details of which can be found on [IBM pricing website](https://cloud.ibm.com/catalog/services/machine-learning).
  
  This [tutorial page](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/track-runtime-usage-wml.html?audience=wdp) 
  also provides more details regarding pricing. It also explains how to track
   runtime usage on your account.

 Lite is a free plan that is a good starter for new users to test out Watson
  Machine Learning Services. [sp20-516-252-pricing1]
  
When a model is deployed, a *score* refers to one prediction made by a
 trained model. Notice that you will be billed for any *event* that involves
  the use of the Cloud Service. So you will be billed for a prediction, an
   *scoring event*. [sp20-516-252-pricing2]
   
## Further Readings

This [playlist](https://www.youtube.com/watch?v=DBRGlAHdj48&list=PLzpeuWUENMK2PYtasCaKK4bZjaYzhW23L&index=1) has videos giving concrete examples on how to build, train and
 deploy different models using Watson Machine Learning. It is a good source
  for interested users. 