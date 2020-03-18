# IBM Watson Machine Learning sp20-516-252 Jessica Zhu

## Introduction 

IBM Watson Machine Learning is a set of tools to build, train and deploy machine
 learning models and neural networks using users' own data. These tools range
  from completely automating training process for quick prototyping to total
   control on specifications of a model. These models can be deployed in
    applications or at scale.
  
  A typical process for machine learning model is shown below:
![Process for Machine Learning Model[@sp20-516-252-machine-learning-process]](image/ml_process.png){#fig:sp20-516-252-machine-learning-process} 

## Features

### Watson Studio Tools

IBM Watson Studio offers a set of tools for model design, training
, deployment and management. We introduce a few of them here:

- AutoAI experiments
 
 It allows users to select the best performing pipeline as a machine
  learning model from a set of automatically generated pipeline options. Several steps are automated, which includes data pre
 -processing, best estimator selection and the generation of model candidate pipelines
  for review and compare.

![AutoAI Features[@AutoAI-2020-sp20-516-252]](image/autoai_overview.png){#fig
:sp20-516-252-auto-ai-features} [@sp20-516-252-machine-learning-process]

- Spark MLlib modeler

Its flow editor allows users to create a machine learning flow, which is a
 graphical representation of a data model. A machine learning flow presents a
  graphical view of a model during the building process by combining nodes that
   represent algorithm nodes. Each node represents a transformation or
    processing step on data.

- SPSS modeler

It can present a graphical view of a model while it is being built by
 combining nodes representing objects or actions. This modeler is designed based
  upon established SPSS Modeler client software and the industry standard CRISP
  -DM model.

- Neural network modeler

Its flow editor helps create a deep learning flow, which is a graphical
 representation of a neural network design. This modeler can be used to design
  and run experiments.   
  
![Fig 3 - Neural Network Workflow [@Neural Workflow-2020-sp20-516
-252]](image/neural-workflow.png){#fig:sp20-516-252-neural-workflow}

- Experiment Builder

In the case that thousands of models need to be trained to identify the
 right combination of data and hyperparameters, the experiment builder
  simplifies the model training process along with an auto-allocated GPU
   compute containers. [sp20-516-252-watson-ml-overview]
   
### Architecture and Services

Watson Machine Learning is built upon Kubernetes and Docker components
. It supports the following infrastructure and services:

- Programming Interfaces:

**Python client library**
**Command Line Interface**
**REST API**

- Training Infrastructure 

**Distributed training** that can have training jobs run among multiple servers

**Common frameworks** allows users to work with their preferred frameworks

**GPU** 

**Hyperparameter optimization** 

- Deployment Infrastructure

**Trained models** can be deployed for batch processing, as a web service
 or with streaming data;
 
**Python functions** can be deployed to simplify AI solutions.

## Getting Started

Here we are giving you a brief demonstration of Watson Machine Learning
 features to show how simple it is to train and deploy a model.
 
- Create an IBM Cloud account (free) and sign in

<https://cloud.ibm.com/login>

![Fig 4 - Sign In Page [@sign-in-page-2020-sp20-516
-252
]](image/sign_in_page.png){#fig:sp20-516-252-sign-in-page
}

- Access to Watson Machine Learning

You will be directed to the `Dashboard` page. Click `Services` on `Resource
 Summary` section. Type in `Machine Learning` in the search section to search
  for Watson Machine Learning among many other tools. Then click `Machine
   Learning-lb`.

Now you should be directed to the Watson Machine Learning page like below:
![Fig 5 - Watson Machine Learning Page [@machine-learning-page-2020-sp20-516
-252]](image/machine-learning-page.png){#fig:sp20-516-252-machine-learning-page}

We are using `Production Line Prediction` as sample data. Go to the bottom
 of the page to the `Sample Applications` section, and click `+` sign on
  `Product Line Prediction` section. 
  
Instructions on the following steps to build, train and deploy a model can be
 found [here](https://developer.ibm.com/technologies/data-science/tutorials/watson-studio-auto-ai/).
Watson studio allows you to complete the whole process in just a minute.

### Deployment 

There are four supported deployment methods: 

* Watson Studio project

Simply use the *Deployments* tab of the project in Watson Studio. Test data
 can be submitted either in a typed form, JSON-formatted code, or as a data
  source. It is very simple that you don't even have to write a line of code
  . [sp20-516-252-model-deployment]

* Python Client 

Models can be deployed using Python client if you are working on a local
 Python development environment or a Python notebook. 
 
You can train a model by submitting a training job to IBM Cloud
 infrastructure with a few lines of code on your local Python notebook. During training, you can run commands to get updates on its
  training progress. 
  
  After training, you can store the model in Watson Machine Learning
   repository. Then you can deploy the model by applying test data to the
    stored model. A prediction and the actual result will be returned. [sp20-516-252-model-deployment]
    
An example and code that demonstrate the use of Python client can be
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
  training and storing a model in your Watson Machine Learning repository
  , you can deploy model using command lines:
  
```bash
$ bx ml deploy MODEL-ID DEPLOYMENT-NAME<full path to test data>
$ bx ml deploy -b MODEL-ID DEVELOPMENT-NAME<path to batch json>
  -b - Enable batch deployment mode
```
[sp20-516-252-model-deployment]

An example and sample code using CLI can be found [here](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-deploy_new.html?linkInPage=true#rest).  

## Pricing

In terms of the region of the United States, there are three pricing plans: Lite
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
 used, more details of which can be found on [IBM pricing website](https
 ://cloud.ibm.com/catalog/services/machine-learning). Lite is a free plan
  that is a good starter for new users to test out Watson
  Machine Learning Services. [sp20-516-252-pricing1]
  
  This [tutorial page](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/track-runtime-usage-wml.html?audience=wdp) 
  also provides more details regarding pricing. It also explains how to track
   runtime usage on your account.
  
After a model is deployed, a *score* refers to one prediction made by a
 trained model. Notice that you will be billed for any *event* that involves
  the use of the Cloud Service. So you will be billed for a prediction, an
   *scoring event*. [sp20-516-252-pricing2]
   
## Further Readings

This [playlist](https://www.youtube.com/watch?v=DBRGlAHdj48&list=PLzpeuWUENMK2PYtasCaKK4bZjaYzhW23L&index=1) has videos giving concrete examples on how to build, train and
 deploy different models using Watson Machine Learning. It is a good resource
  for interested users. 