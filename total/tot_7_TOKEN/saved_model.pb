??	
??
B
AssignVariableOp
resource
value"dtype"
dtypetype?
~
BiasAdd

value"T	
bias"T
output"T" 
Ttype:
2	"-
data_formatstringNHWC:
NHWCNCHW
N
Cast	
x"SrcT	
y"DstT"
SrcTtype"
DstTtype"
Truncatebool( 
8
Const
output"dtype"
valuetensor"
dtypetype
.
Identity

input"T
output"T"	
Ttype
q
MatMul
a"T
b"T
product"T"
transpose_abool( "
transpose_bbool( "
Ttype:

2	
?
Mean

input"T
reduction_indices"Tidx
output"T"
	keep_dimsbool( " 
Ttype:
2	"
Tidxtype0:
2	
e
MergeV2Checkpoints
checkpoint_prefixes
destination_prefix"
delete_old_dirsbool(?

NoOp
M
Pack
values"T*N
output"T"
Nint(0"	
Ttype"
axisint 
C
Placeholder
output"dtype"
dtypetype"
shapeshape:
@
ReadVariableOp
resource
value"dtype"
dtypetype?
E
Relu
features"T
activations"T"
Ttype:
2	
?
ResourceGather
resource
indices"Tindices
output"dtype"

batch_dimsint "
validate_indicesbool("
dtypetype"
Tindicestype:
2	?
o
	RestoreV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0?
l
SaveV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0?
?
Select
	condition

t"T
e"T
output"T"	
Ttype
H
ShardedFilename
basename	
shard

num_shards
filename
9
Softmax
logits"T
softmax"T"
Ttype:
2
?
StatefulPartitionedCall
args2Tin
output2Tout"
Tin
list(type)("
Tout
list(type)("	
ffunc"
configstring "
config_protostring "
executor_typestring ?
@
StaticRegexFullMatch	
input

output
"
patternstring
N

StringJoin
inputs*N

output"
Nint(0"
	separatorstring 
?
VarHandleOp
resource"
	containerstring "
shared_namestring "
dtypetype"
shapeshape"#
allowed_deviceslist(string)
 ?"serve*2.4.02v2.4.0-rc4-71-g582c8d236cb8??
?
embedding_6/embeddingsVarHandleOp*
_output_shapes
: *
dtype0*
shape:	? *'
shared_nameembedding_6/embeddings
?
*embedding_6/embeddings/Read/ReadVariableOpReadVariableOpembedding_6/embeddings*
_output_shapes
:	? *
dtype0
z
dense_30/kernelVarHandleOp*
_output_shapes
: *
dtype0*
shape
: * 
shared_namedense_30/kernel
s
#dense_30/kernel/Read/ReadVariableOpReadVariableOpdense_30/kernel*
_output_shapes

: *
dtype0
r
dense_30/biasVarHandleOp*
_output_shapes
: *
dtype0*
shape:*
shared_namedense_30/bias
k
!dense_30/bias/Read/ReadVariableOpReadVariableOpdense_30/bias*
_output_shapes
:*
dtype0
z
dense_31/kernelVarHandleOp*
_output_shapes
: *
dtype0*
shape
: * 
shared_namedense_31/kernel
s
#dense_31/kernel/Read/ReadVariableOpReadVariableOpdense_31/kernel*
_output_shapes

: *
dtype0
r
dense_31/biasVarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_namedense_31/bias
k
!dense_31/bias/Read/ReadVariableOpReadVariableOpdense_31/bias*
_output_shapes
: *
dtype0
z
dense_32/kernelVarHandleOp*
_output_shapes
: *
dtype0*
shape
: @* 
shared_namedense_32/kernel
s
#dense_32/kernel/Read/ReadVariableOpReadVariableOpdense_32/kernel*
_output_shapes

: @*
dtype0
r
dense_32/biasVarHandleOp*
_output_shapes
: *
dtype0*
shape:@*
shared_namedense_32/bias
k
!dense_32/bias/Read/ReadVariableOpReadVariableOpdense_32/bias*
_output_shapes
:@*
dtype0
z
dense_33/kernelVarHandleOp*
_output_shapes
: *
dtype0*
shape
:@* 
shared_namedense_33/kernel
s
#dense_33/kernel/Read/ReadVariableOpReadVariableOpdense_33/kernel*
_output_shapes

:@*
dtype0
r
dense_33/biasVarHandleOp*
_output_shapes
: *
dtype0*
shape:*
shared_namedense_33/bias
k
!dense_33/bias/Read/ReadVariableOpReadVariableOpdense_33/bias*
_output_shapes
:*
dtype0
z
dense_34/kernelVarHandleOp*
_output_shapes
: *
dtype0*
shape
:* 
shared_namedense_34/kernel
s
#dense_34/kernel/Read/ReadVariableOpReadVariableOpdense_34/kernel*
_output_shapes

:*
dtype0
r
dense_34/biasVarHandleOp*
_output_shapes
: *
dtype0*
shape:*
shared_namedense_34/bias
k
!dense_34/bias/Read/ReadVariableOpReadVariableOpdense_34/bias*
_output_shapes
:*
dtype0
f
	Adam/iterVarHandleOp*
_output_shapes
: *
dtype0	*
shape: *
shared_name	Adam/iter
_
Adam/iter/Read/ReadVariableOpReadVariableOp	Adam/iter*
_output_shapes
: *
dtype0	
j
Adam/beta_1VarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_nameAdam/beta_1
c
Adam/beta_1/Read/ReadVariableOpReadVariableOpAdam/beta_1*
_output_shapes
: *
dtype0
j
Adam/beta_2VarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_nameAdam/beta_2
c
Adam/beta_2/Read/ReadVariableOpReadVariableOpAdam/beta_2*
_output_shapes
: *
dtype0
h

Adam/decayVarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_name
Adam/decay
a
Adam/decay/Read/ReadVariableOpReadVariableOp
Adam/decay*
_output_shapes
: *
dtype0
x
Adam/learning_rateVarHandleOp*
_output_shapes
: *
dtype0*
shape: *#
shared_nameAdam/learning_rate
q
&Adam/learning_rate/Read/ReadVariableOpReadVariableOpAdam/learning_rate*
_output_shapes
: *
dtype0
^
totalVarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_nametotal
W
total/Read/ReadVariableOpReadVariableOptotal*
_output_shapes
: *
dtype0
^
countVarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_namecount
W
count/Read/ReadVariableOpReadVariableOpcount*
_output_shapes
: *
dtype0
b
total_1VarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_name	total_1
[
total_1/Read/ReadVariableOpReadVariableOptotal_1*
_output_shapes
: *
dtype0
b
count_1VarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_name	count_1
[
count_1/Read/ReadVariableOpReadVariableOpcount_1*
_output_shapes
: *
dtype0
?
Adam/embedding_6/embeddings/mVarHandleOp*
_output_shapes
: *
dtype0*
shape:	? *.
shared_nameAdam/embedding_6/embeddings/m
?
1Adam/embedding_6/embeddings/m/Read/ReadVariableOpReadVariableOpAdam/embedding_6/embeddings/m*
_output_shapes
:	? *
dtype0
?
Adam/dense_30/kernel/mVarHandleOp*
_output_shapes
: *
dtype0*
shape
: *'
shared_nameAdam/dense_30/kernel/m
?
*Adam/dense_30/kernel/m/Read/ReadVariableOpReadVariableOpAdam/dense_30/kernel/m*
_output_shapes

: *
dtype0
?
Adam/dense_30/bias/mVarHandleOp*
_output_shapes
: *
dtype0*
shape:*%
shared_nameAdam/dense_30/bias/m
y
(Adam/dense_30/bias/m/Read/ReadVariableOpReadVariableOpAdam/dense_30/bias/m*
_output_shapes
:*
dtype0
?
Adam/dense_31/kernel/mVarHandleOp*
_output_shapes
: *
dtype0*
shape
: *'
shared_nameAdam/dense_31/kernel/m
?
*Adam/dense_31/kernel/m/Read/ReadVariableOpReadVariableOpAdam/dense_31/kernel/m*
_output_shapes

: *
dtype0
?
Adam/dense_31/bias/mVarHandleOp*
_output_shapes
: *
dtype0*
shape: *%
shared_nameAdam/dense_31/bias/m
y
(Adam/dense_31/bias/m/Read/ReadVariableOpReadVariableOpAdam/dense_31/bias/m*
_output_shapes
: *
dtype0
?
Adam/dense_32/kernel/mVarHandleOp*
_output_shapes
: *
dtype0*
shape
: @*'
shared_nameAdam/dense_32/kernel/m
?
*Adam/dense_32/kernel/m/Read/ReadVariableOpReadVariableOpAdam/dense_32/kernel/m*
_output_shapes

: @*
dtype0
?
Adam/dense_32/bias/mVarHandleOp*
_output_shapes
: *
dtype0*
shape:@*%
shared_nameAdam/dense_32/bias/m
y
(Adam/dense_32/bias/m/Read/ReadVariableOpReadVariableOpAdam/dense_32/bias/m*
_output_shapes
:@*
dtype0
?
Adam/dense_33/kernel/mVarHandleOp*
_output_shapes
: *
dtype0*
shape
:@*'
shared_nameAdam/dense_33/kernel/m
?
*Adam/dense_33/kernel/m/Read/ReadVariableOpReadVariableOpAdam/dense_33/kernel/m*
_output_shapes

:@*
dtype0
?
Adam/dense_33/bias/mVarHandleOp*
_output_shapes
: *
dtype0*
shape:*%
shared_nameAdam/dense_33/bias/m
y
(Adam/dense_33/bias/m/Read/ReadVariableOpReadVariableOpAdam/dense_33/bias/m*
_output_shapes
:*
dtype0
?
Adam/dense_34/kernel/mVarHandleOp*
_output_shapes
: *
dtype0*
shape
:*'
shared_nameAdam/dense_34/kernel/m
?
*Adam/dense_34/kernel/m/Read/ReadVariableOpReadVariableOpAdam/dense_34/kernel/m*
_output_shapes

:*
dtype0
?
Adam/dense_34/bias/mVarHandleOp*
_output_shapes
: *
dtype0*
shape:*%
shared_nameAdam/dense_34/bias/m
y
(Adam/dense_34/bias/m/Read/ReadVariableOpReadVariableOpAdam/dense_34/bias/m*
_output_shapes
:*
dtype0
?
Adam/embedding_6/embeddings/vVarHandleOp*
_output_shapes
: *
dtype0*
shape:	? *.
shared_nameAdam/embedding_6/embeddings/v
?
1Adam/embedding_6/embeddings/v/Read/ReadVariableOpReadVariableOpAdam/embedding_6/embeddings/v*
_output_shapes
:	? *
dtype0
?
Adam/dense_30/kernel/vVarHandleOp*
_output_shapes
: *
dtype0*
shape
: *'
shared_nameAdam/dense_30/kernel/v
?
*Adam/dense_30/kernel/v/Read/ReadVariableOpReadVariableOpAdam/dense_30/kernel/v*
_output_shapes

: *
dtype0
?
Adam/dense_30/bias/vVarHandleOp*
_output_shapes
: *
dtype0*
shape:*%
shared_nameAdam/dense_30/bias/v
y
(Adam/dense_30/bias/v/Read/ReadVariableOpReadVariableOpAdam/dense_30/bias/v*
_output_shapes
:*
dtype0
?
Adam/dense_31/kernel/vVarHandleOp*
_output_shapes
: *
dtype0*
shape
: *'
shared_nameAdam/dense_31/kernel/v
?
*Adam/dense_31/kernel/v/Read/ReadVariableOpReadVariableOpAdam/dense_31/kernel/v*
_output_shapes

: *
dtype0
?
Adam/dense_31/bias/vVarHandleOp*
_output_shapes
: *
dtype0*
shape: *%
shared_nameAdam/dense_31/bias/v
y
(Adam/dense_31/bias/v/Read/ReadVariableOpReadVariableOpAdam/dense_31/bias/v*
_output_shapes
: *
dtype0
?
Adam/dense_32/kernel/vVarHandleOp*
_output_shapes
: *
dtype0*
shape
: @*'
shared_nameAdam/dense_32/kernel/v
?
*Adam/dense_32/kernel/v/Read/ReadVariableOpReadVariableOpAdam/dense_32/kernel/v*
_output_shapes

: @*
dtype0
?
Adam/dense_32/bias/vVarHandleOp*
_output_shapes
: *
dtype0*
shape:@*%
shared_nameAdam/dense_32/bias/v
y
(Adam/dense_32/bias/v/Read/ReadVariableOpReadVariableOpAdam/dense_32/bias/v*
_output_shapes
:@*
dtype0
?
Adam/dense_33/kernel/vVarHandleOp*
_output_shapes
: *
dtype0*
shape
:@*'
shared_nameAdam/dense_33/kernel/v
?
*Adam/dense_33/kernel/v/Read/ReadVariableOpReadVariableOpAdam/dense_33/kernel/v*
_output_shapes

:@*
dtype0
?
Adam/dense_33/bias/vVarHandleOp*
_output_shapes
: *
dtype0*
shape:*%
shared_nameAdam/dense_33/bias/v
y
(Adam/dense_33/bias/v/Read/ReadVariableOpReadVariableOpAdam/dense_33/bias/v*
_output_shapes
:*
dtype0
?
Adam/dense_34/kernel/vVarHandleOp*
_output_shapes
: *
dtype0*
shape
:*'
shared_nameAdam/dense_34/kernel/v
?
*Adam/dense_34/kernel/v/Read/ReadVariableOpReadVariableOpAdam/dense_34/kernel/v*
_output_shapes

:*
dtype0
?
Adam/dense_34/bias/vVarHandleOp*
_output_shapes
: *
dtype0*
shape:*%
shared_nameAdam/dense_34/bias/v
y
(Adam/dense_34/bias/v/Read/ReadVariableOpReadVariableOpAdam/dense_34/bias/v*
_output_shapes
:*
dtype0

NoOpNoOp
??
ConstConst"/device:CPU:0*
_output_shapes
: *
dtype0*?>
value?>B?> B?>
?
layer_with_weights-0
layer-0
layer-1
layer_with_weights-1
layer-2
layer_with_weights-2
layer-3
layer_with_weights-3
layer-4
layer_with_weights-4
layer-5
layer_with_weights-5
layer-6
	optimizer
		variables

regularization_losses
trainable_variables
	keras_api

signatures
b

embeddings
	variables
regularization_losses
trainable_variables
	keras_api
R
	variables
regularization_losses
trainable_variables
	keras_api
h

kernel
bias
	variables
regularization_losses
trainable_variables
	keras_api
h

kernel
bias
	variables
 regularization_losses
!trainable_variables
"	keras_api
h

#kernel
$bias
%	variables
&regularization_losses
'trainable_variables
(	keras_api
h

)kernel
*bias
+	variables
,regularization_losses
-trainable_variables
.	keras_api
h

/kernel
0bias
1	variables
2regularization_losses
3trainable_variables
4	keras_api
?
5iter

6beta_1

7beta_2
	8decay
9learning_ratemmmnmompmq#mr$ms)mt*mu/mv0mwvxvyvzv{v|#v}$v~)v*v?/v?0v?
N
0
1
2
3
4
#5
$6
)7
*8
/9
010
 
N
0
1
2
3
4
#5
$6
)7
*8
/9
010
?
:layer_metrics

;layers
<metrics
		variables
=layer_regularization_losses
>non_trainable_variables

regularization_losses
trainable_variables
 
fd
VARIABLE_VALUEembedding_6/embeddings:layer_with_weights-0/embeddings/.ATTRIBUTES/VARIABLE_VALUE

0
 

0
?
?layer_metrics

@layers
Ametrics
	variables
Blayer_regularization_losses
Cnon_trainable_variables
regularization_losses
trainable_variables
 
 
 
?
Dlayer_metrics

Elayers
Fmetrics
	variables
Glayer_regularization_losses
Hnon_trainable_variables
regularization_losses
trainable_variables
[Y
VARIABLE_VALUEdense_30/kernel6layer_with_weights-1/kernel/.ATTRIBUTES/VARIABLE_VALUE
WU
VARIABLE_VALUEdense_30/bias4layer_with_weights-1/bias/.ATTRIBUTES/VARIABLE_VALUE

0
1
 

0
1
?
Ilayer_metrics

Jlayers
Kmetrics
	variables
Llayer_regularization_losses
Mnon_trainable_variables
regularization_losses
trainable_variables
[Y
VARIABLE_VALUEdense_31/kernel6layer_with_weights-2/kernel/.ATTRIBUTES/VARIABLE_VALUE
WU
VARIABLE_VALUEdense_31/bias4layer_with_weights-2/bias/.ATTRIBUTES/VARIABLE_VALUE

0
1
 

0
1
?
Nlayer_metrics

Olayers
Pmetrics
	variables
Qlayer_regularization_losses
Rnon_trainable_variables
 regularization_losses
!trainable_variables
[Y
VARIABLE_VALUEdense_32/kernel6layer_with_weights-3/kernel/.ATTRIBUTES/VARIABLE_VALUE
WU
VARIABLE_VALUEdense_32/bias4layer_with_weights-3/bias/.ATTRIBUTES/VARIABLE_VALUE

#0
$1
 

#0
$1
?
Slayer_metrics

Tlayers
Umetrics
%	variables
Vlayer_regularization_losses
Wnon_trainable_variables
&regularization_losses
'trainable_variables
[Y
VARIABLE_VALUEdense_33/kernel6layer_with_weights-4/kernel/.ATTRIBUTES/VARIABLE_VALUE
WU
VARIABLE_VALUEdense_33/bias4layer_with_weights-4/bias/.ATTRIBUTES/VARIABLE_VALUE

)0
*1
 

)0
*1
?
Xlayer_metrics

Ylayers
Zmetrics
+	variables
[layer_regularization_losses
\non_trainable_variables
,regularization_losses
-trainable_variables
[Y
VARIABLE_VALUEdense_34/kernel6layer_with_weights-5/kernel/.ATTRIBUTES/VARIABLE_VALUE
WU
VARIABLE_VALUEdense_34/bias4layer_with_weights-5/bias/.ATTRIBUTES/VARIABLE_VALUE

/0
01
 

/0
01
?
]layer_metrics

^layers
_metrics
1	variables
`layer_regularization_losses
anon_trainable_variables
2regularization_losses
3trainable_variables
HF
VARIABLE_VALUE	Adam/iter)optimizer/iter/.ATTRIBUTES/VARIABLE_VALUE
LJ
VARIABLE_VALUEAdam/beta_1+optimizer/beta_1/.ATTRIBUTES/VARIABLE_VALUE
LJ
VARIABLE_VALUEAdam/beta_2+optimizer/beta_2/.ATTRIBUTES/VARIABLE_VALUE
JH
VARIABLE_VALUE
Adam/decay*optimizer/decay/.ATTRIBUTES/VARIABLE_VALUE
ZX
VARIABLE_VALUEAdam/learning_rate2optimizer/learning_rate/.ATTRIBUTES/VARIABLE_VALUE
 
1
0
1
2
3
4
5
6

b0
c1
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
4
	dtotal
	ecount
f	variables
g	keras_api
D
	htotal
	icount
j
_fn_kwargs
k	variables
l	keras_api
OM
VARIABLE_VALUEtotal4keras_api/metrics/0/total/.ATTRIBUTES/VARIABLE_VALUE
OM
VARIABLE_VALUEcount4keras_api/metrics/0/count/.ATTRIBUTES/VARIABLE_VALUE

d0
e1

f	variables
QO
VARIABLE_VALUEtotal_14keras_api/metrics/1/total/.ATTRIBUTES/VARIABLE_VALUE
QO
VARIABLE_VALUEcount_14keras_api/metrics/1/count/.ATTRIBUTES/VARIABLE_VALUE
 

h0
i1

k	variables
??
VARIABLE_VALUEAdam/embedding_6/embeddings/mVlayer_with_weights-0/embeddings/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
~|
VARIABLE_VALUEAdam/dense_30/kernel/mRlayer_with_weights-1/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
zx
VARIABLE_VALUEAdam/dense_30/bias/mPlayer_with_weights-1/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
~|
VARIABLE_VALUEAdam/dense_31/kernel/mRlayer_with_weights-2/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
zx
VARIABLE_VALUEAdam/dense_31/bias/mPlayer_with_weights-2/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
~|
VARIABLE_VALUEAdam/dense_32/kernel/mRlayer_with_weights-3/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
zx
VARIABLE_VALUEAdam/dense_32/bias/mPlayer_with_weights-3/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
~|
VARIABLE_VALUEAdam/dense_33/kernel/mRlayer_with_weights-4/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
zx
VARIABLE_VALUEAdam/dense_33/bias/mPlayer_with_weights-4/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
~|
VARIABLE_VALUEAdam/dense_34/kernel/mRlayer_with_weights-5/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
zx
VARIABLE_VALUEAdam/dense_34/bias/mPlayer_with_weights-5/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUE
??
VARIABLE_VALUEAdam/embedding_6/embeddings/vVlayer_with_weights-0/embeddings/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
~|
VARIABLE_VALUEAdam/dense_30/kernel/vRlayer_with_weights-1/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
zx
VARIABLE_VALUEAdam/dense_30/bias/vPlayer_with_weights-1/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
~|
VARIABLE_VALUEAdam/dense_31/kernel/vRlayer_with_weights-2/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
zx
VARIABLE_VALUEAdam/dense_31/bias/vPlayer_with_weights-2/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
~|
VARIABLE_VALUEAdam/dense_32/kernel/vRlayer_with_weights-3/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
zx
VARIABLE_VALUEAdam/dense_32/bias/vPlayer_with_weights-3/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
~|
VARIABLE_VALUEAdam/dense_33/kernel/vRlayer_with_weights-4/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
zx
VARIABLE_VALUEAdam/dense_33/bias/vPlayer_with_weights-4/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
~|
VARIABLE_VALUEAdam/dense_34/kernel/vRlayer_with_weights-5/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
zx
VARIABLE_VALUEAdam/dense_34/bias/vPlayer_with_weights-5/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUE
?
!serving_default_embedding_6_inputPlaceholder*'
_output_shapes
:?????????*
dtype0*
shape:?????????
?
StatefulPartitionedCallStatefulPartitionedCall!serving_default_embedding_6_inputembedding_6/embeddingsdense_30/kerneldense_30/biasdense_31/kerneldense_31/biasdense_32/kerneldense_32/biasdense_33/kerneldense_33/biasdense_34/kerneldense_34/bias*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*-
_read_only_resource_inputs
	
*-
config_proto

CPU

GPU 2J 8? *.
f)R'
%__inference_signature_wrapper_3355102
O
saver_filenamePlaceholder*
_output_shapes
: *
dtype0*
shape: 
?
StatefulPartitionedCall_1StatefulPartitionedCallsaver_filename*embedding_6/embeddings/Read/ReadVariableOp#dense_30/kernel/Read/ReadVariableOp!dense_30/bias/Read/ReadVariableOp#dense_31/kernel/Read/ReadVariableOp!dense_31/bias/Read/ReadVariableOp#dense_32/kernel/Read/ReadVariableOp!dense_32/bias/Read/ReadVariableOp#dense_33/kernel/Read/ReadVariableOp!dense_33/bias/Read/ReadVariableOp#dense_34/kernel/Read/ReadVariableOp!dense_34/bias/Read/ReadVariableOpAdam/iter/Read/ReadVariableOpAdam/beta_1/Read/ReadVariableOpAdam/beta_2/Read/ReadVariableOpAdam/decay/Read/ReadVariableOp&Adam/learning_rate/Read/ReadVariableOptotal/Read/ReadVariableOpcount/Read/ReadVariableOptotal_1/Read/ReadVariableOpcount_1/Read/ReadVariableOp1Adam/embedding_6/embeddings/m/Read/ReadVariableOp*Adam/dense_30/kernel/m/Read/ReadVariableOp(Adam/dense_30/bias/m/Read/ReadVariableOp*Adam/dense_31/kernel/m/Read/ReadVariableOp(Adam/dense_31/bias/m/Read/ReadVariableOp*Adam/dense_32/kernel/m/Read/ReadVariableOp(Adam/dense_32/bias/m/Read/ReadVariableOp*Adam/dense_33/kernel/m/Read/ReadVariableOp(Adam/dense_33/bias/m/Read/ReadVariableOp*Adam/dense_34/kernel/m/Read/ReadVariableOp(Adam/dense_34/bias/m/Read/ReadVariableOp1Adam/embedding_6/embeddings/v/Read/ReadVariableOp*Adam/dense_30/kernel/v/Read/ReadVariableOp(Adam/dense_30/bias/v/Read/ReadVariableOp*Adam/dense_31/kernel/v/Read/ReadVariableOp(Adam/dense_31/bias/v/Read/ReadVariableOp*Adam/dense_32/kernel/v/Read/ReadVariableOp(Adam/dense_32/bias/v/Read/ReadVariableOp*Adam/dense_33/kernel/v/Read/ReadVariableOp(Adam/dense_33/bias/v/Read/ReadVariableOp*Adam/dense_34/kernel/v/Read/ReadVariableOp(Adam/dense_34/bias/v/Read/ReadVariableOpConst*7
Tin0
.2,	*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8? *)
f$R"
 __inference__traced_save_3355538
?
StatefulPartitionedCall_2StatefulPartitionedCallsaver_filenameembedding_6/embeddingsdense_30/kerneldense_30/biasdense_31/kerneldense_31/biasdense_32/kerneldense_32/biasdense_33/kerneldense_33/biasdense_34/kerneldense_34/bias	Adam/iterAdam/beta_1Adam/beta_2
Adam/decayAdam/learning_ratetotalcounttotal_1count_1Adam/embedding_6/embeddings/mAdam/dense_30/kernel/mAdam/dense_30/bias/mAdam/dense_31/kernel/mAdam/dense_31/bias/mAdam/dense_32/kernel/mAdam/dense_32/bias/mAdam/dense_33/kernel/mAdam/dense_33/bias/mAdam/dense_34/kernel/mAdam/dense_34/bias/mAdam/embedding_6/embeddings/vAdam/dense_30/kernel/vAdam/dense_30/bias/vAdam/dense_31/kernel/vAdam/dense_31/bias/vAdam/dense_32/kernel/vAdam/dense_32/bias/vAdam/dense_33/kernel/vAdam/dense_33/bias/vAdam/dense_34/kernel/vAdam/dense_34/bias/v*6
Tin/
-2+*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8? *,
f'R%
#__inference__traced_restore_3355674??
?	
?
E__inference_dense_32_layer_call_and_return_conditional_losses_3355340

inputs"
matmul_readvariableop_resource#
biasadd_readvariableop_resource
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOp?
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes

: @*
dtype02
MatMul/ReadVariableOps
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????@2
MatMul?
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
:@*
dtype02
BiasAdd/ReadVariableOp?
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????@2	
BiasAddX
ReluReluBiasAdd:output:0*
T0*'
_output_shapes
:?????????@2
Relu?
IdentityIdentityRelu:activations:0^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*
T0*'
_output_shapes
:?????????@2

Identity"
identityIdentity:output:0*.
_input_shapes
:????????? ::20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:O K
'
_output_shapes
:????????? 
 
_user_specified_nameinputs
?	
?
.__inference_sequential_6_layer_call_fn_3355223

inputs
unknown
	unknown_0
	unknown_1
	unknown_2
	unknown_3
	unknown_4
	unknown_5
	unknown_6
	unknown_7
	unknown_8
	unknown_9
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4	unknown_5	unknown_6	unknown_7	unknown_8	unknown_9*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*-
_read_only_resource_inputs
	
*-
config_proto

CPU

GPU 2J 8? *R
fMRK
I__inference_sequential_6_layer_call_and_return_conditional_losses_33549802
StatefulPartitionedCall?
IdentityIdentity StatefulPartitionedCall:output:0^StatefulPartitionedCall*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*R
_input_shapesA
?:?????????:::::::::::22
StatefulPartitionedCallStatefulPartitionedCall:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?$
?
I__inference_sequential_6_layer_call_and_return_conditional_losses_3354911
embedding_6_input
embedding_6_3354760
dense_30_3354797
dense_30_3354799
dense_31_3354824
dense_31_3354826
dense_32_3354851
dense_32_3354853
dense_33_3354878
dense_33_3354880
dense_34_3354905
dense_34_3354907
identity?? dense_30/StatefulPartitionedCall? dense_31/StatefulPartitionedCall? dense_32/StatefulPartitionedCall? dense_33/StatefulPartitionedCall? dense_34/StatefulPartitionedCall?#embedding_6/StatefulPartitionedCall?
#embedding_6/StatefulPartitionedCallStatefulPartitionedCallembedding_6_inputembedding_6_3354760*
Tin
2*
Tout
2*
_collective_manager_ids
 *+
_output_shapes
:????????? *#
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *Q
fLRJ
H__inference_embedding_6_layer_call_and_return_conditional_losses_33547512%
#embedding_6/StatefulPartitionedCall?
*global_average_pooling1d_6/PartitionedCallPartitionedCall,embedding_6/StatefulPartitionedCall:output:0*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8? *`
f[RY
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_33547682,
*global_average_pooling1d_6/PartitionedCall?
 dense_30/StatefulPartitionedCallStatefulPartitionedCall3global_average_pooling1d_6/PartitionedCall:output:0dense_30_3354797dense_30_3354799*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_30_layer_call_and_return_conditional_losses_33547862"
 dense_30/StatefulPartitionedCall?
 dense_31/StatefulPartitionedCallStatefulPartitionedCall)dense_30/StatefulPartitionedCall:output:0dense_31_3354824dense_31_3354826*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? *$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_31_layer_call_and_return_conditional_losses_33548132"
 dense_31/StatefulPartitionedCall?
 dense_32/StatefulPartitionedCallStatefulPartitionedCall)dense_31/StatefulPartitionedCall:output:0dense_32_3354851dense_32_3354853*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????@*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_32_layer_call_and_return_conditional_losses_33548402"
 dense_32/StatefulPartitionedCall?
 dense_33/StatefulPartitionedCallStatefulPartitionedCall)dense_32/StatefulPartitionedCall:output:0dense_33_3354878dense_33_3354880*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_33_layer_call_and_return_conditional_losses_33548672"
 dense_33/StatefulPartitionedCall?
 dense_34/StatefulPartitionedCallStatefulPartitionedCall)dense_33/StatefulPartitionedCall:output:0dense_34_3354905dense_34_3354907*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_34_layer_call_and_return_conditional_losses_33548942"
 dense_34/StatefulPartitionedCall?
IdentityIdentity)dense_34/StatefulPartitionedCall:output:0!^dense_30/StatefulPartitionedCall!^dense_31/StatefulPartitionedCall!^dense_32/StatefulPartitionedCall!^dense_33/StatefulPartitionedCall!^dense_34/StatefulPartitionedCall$^embedding_6/StatefulPartitionedCall*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*R
_input_shapesA
?:?????????:::::::::::2D
 dense_30/StatefulPartitionedCall dense_30/StatefulPartitionedCall2D
 dense_31/StatefulPartitionedCall dense_31/StatefulPartitionedCall2D
 dense_32/StatefulPartitionedCall dense_32/StatefulPartitionedCall2D
 dense_33/StatefulPartitionedCall dense_33/StatefulPartitionedCall2D
 dense_34/StatefulPartitionedCall dense_34/StatefulPartitionedCall2J
#embedding_6/StatefulPartitionedCall#embedding_6/StatefulPartitionedCall:Z V
'
_output_shapes
:?????????
+
_user_specified_nameembedding_6_input
?
s
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_3354768

inputs
identityr
Mean/reduction_indicesConst*
_output_shapes
: *
dtype0*
value	B :2
Mean/reduction_indiceso
MeanMeaninputsMean/reduction_indices:output:0*
T0*'
_output_shapes
:????????? 2
Meana
IdentityIdentityMean:output:0*
T0*'
_output_shapes
:????????? 2

Identity"
identityIdentity:output:0**
_input_shapes
:????????? :S O
+
_output_shapes
:????????? 
 
_user_specified_nameinputs
?#
?
I__inference_sequential_6_layer_call_and_return_conditional_losses_3355040

inputs
embedding_6_3355010
dense_30_3355014
dense_30_3355016
dense_31_3355019
dense_31_3355021
dense_32_3355024
dense_32_3355026
dense_33_3355029
dense_33_3355031
dense_34_3355034
dense_34_3355036
identity?? dense_30/StatefulPartitionedCall? dense_31/StatefulPartitionedCall? dense_32/StatefulPartitionedCall? dense_33/StatefulPartitionedCall? dense_34/StatefulPartitionedCall?#embedding_6/StatefulPartitionedCall?
#embedding_6/StatefulPartitionedCallStatefulPartitionedCallinputsembedding_6_3355010*
Tin
2*
Tout
2*
_collective_manager_ids
 *+
_output_shapes
:????????? *#
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *Q
fLRJ
H__inference_embedding_6_layer_call_and_return_conditional_losses_33547512%
#embedding_6/StatefulPartitionedCall?
*global_average_pooling1d_6/PartitionedCallPartitionedCall,embedding_6/StatefulPartitionedCall:output:0*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8? *`
f[RY
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_33547682,
*global_average_pooling1d_6/PartitionedCall?
 dense_30/StatefulPartitionedCallStatefulPartitionedCall3global_average_pooling1d_6/PartitionedCall:output:0dense_30_3355014dense_30_3355016*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_30_layer_call_and_return_conditional_losses_33547862"
 dense_30/StatefulPartitionedCall?
 dense_31/StatefulPartitionedCallStatefulPartitionedCall)dense_30/StatefulPartitionedCall:output:0dense_31_3355019dense_31_3355021*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? *$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_31_layer_call_and_return_conditional_losses_33548132"
 dense_31/StatefulPartitionedCall?
 dense_32/StatefulPartitionedCallStatefulPartitionedCall)dense_31/StatefulPartitionedCall:output:0dense_32_3355024dense_32_3355026*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????@*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_32_layer_call_and_return_conditional_losses_33548402"
 dense_32/StatefulPartitionedCall?
 dense_33/StatefulPartitionedCallStatefulPartitionedCall)dense_32/StatefulPartitionedCall:output:0dense_33_3355029dense_33_3355031*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_33_layer_call_and_return_conditional_losses_33548672"
 dense_33/StatefulPartitionedCall?
 dense_34/StatefulPartitionedCallStatefulPartitionedCall)dense_33/StatefulPartitionedCall:output:0dense_34_3355034dense_34_3355036*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_34_layer_call_and_return_conditional_losses_33548942"
 dense_34/StatefulPartitionedCall?
IdentityIdentity)dense_34/StatefulPartitionedCall:output:0!^dense_30/StatefulPartitionedCall!^dense_31/StatefulPartitionedCall!^dense_32/StatefulPartitionedCall!^dense_33/StatefulPartitionedCall!^dense_34/StatefulPartitionedCall$^embedding_6/StatefulPartitionedCall*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*R
_input_shapesA
?:?????????:::::::::::2D
 dense_30/StatefulPartitionedCall dense_30/StatefulPartitionedCall2D
 dense_31/StatefulPartitionedCall dense_31/StatefulPartitionedCall2D
 dense_32/StatefulPartitionedCall dense_32/StatefulPartitionedCall2D
 dense_33/StatefulPartitionedCall dense_33/StatefulPartitionedCall2D
 dense_34/StatefulPartitionedCall dense_34/StatefulPartitionedCall2J
#embedding_6/StatefulPartitionedCall#embedding_6/StatefulPartitionedCall:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?

*__inference_dense_33_layer_call_fn_3355369

inputs
unknown
	unknown_0
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_33_layer_call_and_return_conditional_losses_33548672
StatefulPartitionedCall?
IdentityIdentity StatefulPartitionedCall:output:0^StatefulPartitionedCall*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*.
_input_shapes
:?????????@::22
StatefulPartitionedCallStatefulPartitionedCall:O K
'
_output_shapes
:?????????@
 
_user_specified_nameinputs
?	
?
.__inference_sequential_6_layer_call_fn_3355250

inputs
unknown
	unknown_0
	unknown_1
	unknown_2
	unknown_3
	unknown_4
	unknown_5
	unknown_6
	unknown_7
	unknown_8
	unknown_9
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4	unknown_5	unknown_6	unknown_7	unknown_8	unknown_9*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*-
_read_only_resource_inputs
	
*-
config_proto

CPU

GPU 2J 8? *R
fMRK
I__inference_sequential_6_layer_call_and_return_conditional_losses_33550402
StatefulPartitionedCall?
IdentityIdentity StatefulPartitionedCall:output:0^StatefulPartitionedCall*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*R
_input_shapesA
?:?????????:::::::::::22
StatefulPartitionedCallStatefulPartitionedCall:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?	
?
.__inference_sequential_6_layer_call_fn_3355005
embedding_6_input
unknown
	unknown_0
	unknown_1
	unknown_2
	unknown_3
	unknown_4
	unknown_5
	unknown_6
	unknown_7
	unknown_8
	unknown_9
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallembedding_6_inputunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4	unknown_5	unknown_6	unknown_7	unknown_8	unknown_9*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*-
_read_only_resource_inputs
	
*-
config_proto

CPU

GPU 2J 8? *R
fMRK
I__inference_sequential_6_layer_call_and_return_conditional_losses_33549802
StatefulPartitionedCall?
IdentityIdentity StatefulPartitionedCall:output:0^StatefulPartitionedCall*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*R
_input_shapesA
?:?????????:::::::::::22
StatefulPartitionedCallStatefulPartitionedCall:Z V
'
_output_shapes
:?????????
+
_user_specified_nameembedding_6_input
?

*__inference_dense_34_layer_call_fn_3355389

inputs
unknown
	unknown_0
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_34_layer_call_and_return_conditional_losses_33548942
StatefulPartitionedCall?
IdentityIdentity StatefulPartitionedCall:output:0^StatefulPartitionedCall*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*.
_input_shapes
:?????????::22
StatefulPartitionedCallStatefulPartitionedCall:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?L
?	
"__inference__wrapped_model_3354718
embedding_6_input5
1sequential_6_embedding_6_embedding_lookup_33546758
4sequential_6_dense_30_matmul_readvariableop_resource9
5sequential_6_dense_30_biasadd_readvariableop_resource8
4sequential_6_dense_31_matmul_readvariableop_resource9
5sequential_6_dense_31_biasadd_readvariableop_resource8
4sequential_6_dense_32_matmul_readvariableop_resource9
5sequential_6_dense_32_biasadd_readvariableop_resource8
4sequential_6_dense_33_matmul_readvariableop_resource9
5sequential_6_dense_33_biasadd_readvariableop_resource8
4sequential_6_dense_34_matmul_readvariableop_resource9
5sequential_6_dense_34_biasadd_readvariableop_resource
identity??,sequential_6/dense_30/BiasAdd/ReadVariableOp?+sequential_6/dense_30/MatMul/ReadVariableOp?,sequential_6/dense_31/BiasAdd/ReadVariableOp?+sequential_6/dense_31/MatMul/ReadVariableOp?,sequential_6/dense_32/BiasAdd/ReadVariableOp?+sequential_6/dense_32/MatMul/ReadVariableOp?,sequential_6/dense_33/BiasAdd/ReadVariableOp?+sequential_6/dense_33/MatMul/ReadVariableOp?,sequential_6/dense_34/BiasAdd/ReadVariableOp?+sequential_6/dense_34/MatMul/ReadVariableOp?)sequential_6/embedding_6/embedding_lookup?
sequential_6/embedding_6/CastCastembedding_6_input*

DstT0*

SrcT0*'
_output_shapes
:?????????2
sequential_6/embedding_6/Cast?
)sequential_6/embedding_6/embedding_lookupResourceGather1sequential_6_embedding_6_embedding_lookup_3354675!sequential_6/embedding_6/Cast:y:0",/job:localhost/replica:0/task:0/device:CPU:0*
Tindices0*D
_class:
86loc:@sequential_6/embedding_6/embedding_lookup/3354675*+
_output_shapes
:????????? *
dtype02+
)sequential_6/embedding_6/embedding_lookup?
2sequential_6/embedding_6/embedding_lookup/IdentityIdentity2sequential_6/embedding_6/embedding_lookup:output:0",/job:localhost/replica:0/task:0/device:CPU:0*
T0*D
_class:
86loc:@sequential_6/embedding_6/embedding_lookup/3354675*+
_output_shapes
:????????? 24
2sequential_6/embedding_6/embedding_lookup/Identity?
4sequential_6/embedding_6/embedding_lookup/Identity_1Identity;sequential_6/embedding_6/embedding_lookup/Identity:output:0*
T0*+
_output_shapes
:????????? 26
4sequential_6/embedding_6/embedding_lookup/Identity_1?
>sequential_6/global_average_pooling1d_6/Mean/reduction_indicesConst*
_output_shapes
: *
dtype0*
value	B :2@
>sequential_6/global_average_pooling1d_6/Mean/reduction_indices?
,sequential_6/global_average_pooling1d_6/MeanMean=sequential_6/embedding_6/embedding_lookup/Identity_1:output:0Gsequential_6/global_average_pooling1d_6/Mean/reduction_indices:output:0*
T0*'
_output_shapes
:????????? 2.
,sequential_6/global_average_pooling1d_6/Mean?
+sequential_6/dense_30/MatMul/ReadVariableOpReadVariableOp4sequential_6_dense_30_matmul_readvariableop_resource*
_output_shapes

: *
dtype02-
+sequential_6/dense_30/MatMul/ReadVariableOp?
sequential_6/dense_30/MatMulMatMul5sequential_6/global_average_pooling1d_6/Mean:output:03sequential_6/dense_30/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
sequential_6/dense_30/MatMul?
,sequential_6/dense_30/BiasAdd/ReadVariableOpReadVariableOp5sequential_6_dense_30_biasadd_readvariableop_resource*
_output_shapes
:*
dtype02.
,sequential_6/dense_30/BiasAdd/ReadVariableOp?
sequential_6/dense_30/BiasAddBiasAdd&sequential_6/dense_30/MatMul:product:04sequential_6/dense_30/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
sequential_6/dense_30/BiasAdd?
sequential_6/dense_30/ReluRelu&sequential_6/dense_30/BiasAdd:output:0*
T0*'
_output_shapes
:?????????2
sequential_6/dense_30/Relu?
+sequential_6/dense_31/MatMul/ReadVariableOpReadVariableOp4sequential_6_dense_31_matmul_readvariableop_resource*
_output_shapes

: *
dtype02-
+sequential_6/dense_31/MatMul/ReadVariableOp?
sequential_6/dense_31/MatMulMatMul(sequential_6/dense_30/Relu:activations:03sequential_6/dense_31/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:????????? 2
sequential_6/dense_31/MatMul?
,sequential_6/dense_31/BiasAdd/ReadVariableOpReadVariableOp5sequential_6_dense_31_biasadd_readvariableop_resource*
_output_shapes
: *
dtype02.
,sequential_6/dense_31/BiasAdd/ReadVariableOp?
sequential_6/dense_31/BiasAddBiasAdd&sequential_6/dense_31/MatMul:product:04sequential_6/dense_31/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:????????? 2
sequential_6/dense_31/BiasAdd?
sequential_6/dense_31/ReluRelu&sequential_6/dense_31/BiasAdd:output:0*
T0*'
_output_shapes
:????????? 2
sequential_6/dense_31/Relu?
+sequential_6/dense_32/MatMul/ReadVariableOpReadVariableOp4sequential_6_dense_32_matmul_readvariableop_resource*
_output_shapes

: @*
dtype02-
+sequential_6/dense_32/MatMul/ReadVariableOp?
sequential_6/dense_32/MatMulMatMul(sequential_6/dense_31/Relu:activations:03sequential_6/dense_32/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????@2
sequential_6/dense_32/MatMul?
,sequential_6/dense_32/BiasAdd/ReadVariableOpReadVariableOp5sequential_6_dense_32_biasadd_readvariableop_resource*
_output_shapes
:@*
dtype02.
,sequential_6/dense_32/BiasAdd/ReadVariableOp?
sequential_6/dense_32/BiasAddBiasAdd&sequential_6/dense_32/MatMul:product:04sequential_6/dense_32/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????@2
sequential_6/dense_32/BiasAdd?
sequential_6/dense_32/ReluRelu&sequential_6/dense_32/BiasAdd:output:0*
T0*'
_output_shapes
:?????????@2
sequential_6/dense_32/Relu?
+sequential_6/dense_33/MatMul/ReadVariableOpReadVariableOp4sequential_6_dense_33_matmul_readvariableop_resource*
_output_shapes

:@*
dtype02-
+sequential_6/dense_33/MatMul/ReadVariableOp?
sequential_6/dense_33/MatMulMatMul(sequential_6/dense_32/Relu:activations:03sequential_6/dense_33/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
sequential_6/dense_33/MatMul?
,sequential_6/dense_33/BiasAdd/ReadVariableOpReadVariableOp5sequential_6_dense_33_biasadd_readvariableop_resource*
_output_shapes
:*
dtype02.
,sequential_6/dense_33/BiasAdd/ReadVariableOp?
sequential_6/dense_33/BiasAddBiasAdd&sequential_6/dense_33/MatMul:product:04sequential_6/dense_33/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
sequential_6/dense_33/BiasAdd?
sequential_6/dense_33/ReluRelu&sequential_6/dense_33/BiasAdd:output:0*
T0*'
_output_shapes
:?????????2
sequential_6/dense_33/Relu?
+sequential_6/dense_34/MatMul/ReadVariableOpReadVariableOp4sequential_6_dense_34_matmul_readvariableop_resource*
_output_shapes

:*
dtype02-
+sequential_6/dense_34/MatMul/ReadVariableOp?
sequential_6/dense_34/MatMulMatMul(sequential_6/dense_33/Relu:activations:03sequential_6/dense_34/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
sequential_6/dense_34/MatMul?
,sequential_6/dense_34/BiasAdd/ReadVariableOpReadVariableOp5sequential_6_dense_34_biasadd_readvariableop_resource*
_output_shapes
:*
dtype02.
,sequential_6/dense_34/BiasAdd/ReadVariableOp?
sequential_6/dense_34/BiasAddBiasAdd&sequential_6/dense_34/MatMul:product:04sequential_6/dense_34/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
sequential_6/dense_34/BiasAdd?
sequential_6/dense_34/SoftmaxSoftmax&sequential_6/dense_34/BiasAdd:output:0*
T0*'
_output_shapes
:?????????2
sequential_6/dense_34/Softmax?
IdentityIdentity'sequential_6/dense_34/Softmax:softmax:0-^sequential_6/dense_30/BiasAdd/ReadVariableOp,^sequential_6/dense_30/MatMul/ReadVariableOp-^sequential_6/dense_31/BiasAdd/ReadVariableOp,^sequential_6/dense_31/MatMul/ReadVariableOp-^sequential_6/dense_32/BiasAdd/ReadVariableOp,^sequential_6/dense_32/MatMul/ReadVariableOp-^sequential_6/dense_33/BiasAdd/ReadVariableOp,^sequential_6/dense_33/MatMul/ReadVariableOp-^sequential_6/dense_34/BiasAdd/ReadVariableOp,^sequential_6/dense_34/MatMul/ReadVariableOp*^sequential_6/embedding_6/embedding_lookup*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*R
_input_shapesA
?:?????????:::::::::::2\
,sequential_6/dense_30/BiasAdd/ReadVariableOp,sequential_6/dense_30/BiasAdd/ReadVariableOp2Z
+sequential_6/dense_30/MatMul/ReadVariableOp+sequential_6/dense_30/MatMul/ReadVariableOp2\
,sequential_6/dense_31/BiasAdd/ReadVariableOp,sequential_6/dense_31/BiasAdd/ReadVariableOp2Z
+sequential_6/dense_31/MatMul/ReadVariableOp+sequential_6/dense_31/MatMul/ReadVariableOp2\
,sequential_6/dense_32/BiasAdd/ReadVariableOp,sequential_6/dense_32/BiasAdd/ReadVariableOp2Z
+sequential_6/dense_32/MatMul/ReadVariableOp+sequential_6/dense_32/MatMul/ReadVariableOp2\
,sequential_6/dense_33/BiasAdd/ReadVariableOp,sequential_6/dense_33/BiasAdd/ReadVariableOp2Z
+sequential_6/dense_33/MatMul/ReadVariableOp+sequential_6/dense_33/MatMul/ReadVariableOp2\
,sequential_6/dense_34/BiasAdd/ReadVariableOp,sequential_6/dense_34/BiasAdd/ReadVariableOp2Z
+sequential_6/dense_34/MatMul/ReadVariableOp+sequential_6/dense_34/MatMul/ReadVariableOp2V
)sequential_6/embedding_6/embedding_lookup)sequential_6/embedding_6/embedding_lookup:Z V
'
_output_shapes
:?????????
+
_user_specified_nameembedding_6_input
?

*__inference_dense_30_layer_call_fn_3355309

inputs
unknown
	unknown_0
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_30_layer_call_and_return_conditional_losses_33547862
StatefulPartitionedCall?
IdentityIdentity StatefulPartitionedCall:output:0^StatefulPartitionedCall*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*.
_input_shapes
:????????? ::22
StatefulPartitionedCallStatefulPartitionedCall:O K
'
_output_shapes
:????????? 
 
_user_specified_nameinputs
?	
?
E__inference_dense_34_layer_call_and_return_conditional_losses_3355380

inputs"
matmul_readvariableop_resource#
biasadd_readvariableop_resource
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOp?
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes

:*
dtype02
MatMul/ReadVariableOps
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
MatMul?
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
:*
dtype02
BiasAdd/ReadVariableOp?
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2	
BiasAdda
SoftmaxSoftmaxBiasAdd:output:0*
T0*'
_output_shapes
:?????????2	
Softmax?
IdentityIdentitySoftmax:softmax:0^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*.
_input_shapes
:?????????::20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?
X
<__inference_global_average_pooling1d_6_layer_call_fn_3355278

inputs
identity?
PartitionedCallPartitionedCallinputs*
Tin
2*
Tout
2*
_collective_manager_ids
 *0
_output_shapes
:??????????????????* 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8? *`
f[RY
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_33547342
PartitionedCallu
IdentityIdentityPartitionedCall:output:0*
T0*0
_output_shapes
:??????????????????2

Identity"
identityIdentity:output:0*<
_input_shapes+
):'???????????????????????????:e a
=
_output_shapes+
):'???????????????????????????
 
_user_specified_nameinputs
?W
?
 __inference__traced_save_3355538
file_prefix5
1savev2_embedding_6_embeddings_read_readvariableop.
*savev2_dense_30_kernel_read_readvariableop,
(savev2_dense_30_bias_read_readvariableop.
*savev2_dense_31_kernel_read_readvariableop,
(savev2_dense_31_bias_read_readvariableop.
*savev2_dense_32_kernel_read_readvariableop,
(savev2_dense_32_bias_read_readvariableop.
*savev2_dense_33_kernel_read_readvariableop,
(savev2_dense_33_bias_read_readvariableop.
*savev2_dense_34_kernel_read_readvariableop,
(savev2_dense_34_bias_read_readvariableop(
$savev2_adam_iter_read_readvariableop	*
&savev2_adam_beta_1_read_readvariableop*
&savev2_adam_beta_2_read_readvariableop)
%savev2_adam_decay_read_readvariableop1
-savev2_adam_learning_rate_read_readvariableop$
 savev2_total_read_readvariableop$
 savev2_count_read_readvariableop&
"savev2_total_1_read_readvariableop&
"savev2_count_1_read_readvariableop<
8savev2_adam_embedding_6_embeddings_m_read_readvariableop5
1savev2_adam_dense_30_kernel_m_read_readvariableop3
/savev2_adam_dense_30_bias_m_read_readvariableop5
1savev2_adam_dense_31_kernel_m_read_readvariableop3
/savev2_adam_dense_31_bias_m_read_readvariableop5
1savev2_adam_dense_32_kernel_m_read_readvariableop3
/savev2_adam_dense_32_bias_m_read_readvariableop5
1savev2_adam_dense_33_kernel_m_read_readvariableop3
/savev2_adam_dense_33_bias_m_read_readvariableop5
1savev2_adam_dense_34_kernel_m_read_readvariableop3
/savev2_adam_dense_34_bias_m_read_readvariableop<
8savev2_adam_embedding_6_embeddings_v_read_readvariableop5
1savev2_adam_dense_30_kernel_v_read_readvariableop3
/savev2_adam_dense_30_bias_v_read_readvariableop5
1savev2_adam_dense_31_kernel_v_read_readvariableop3
/savev2_adam_dense_31_bias_v_read_readvariableop5
1savev2_adam_dense_32_kernel_v_read_readvariableop3
/savev2_adam_dense_32_bias_v_read_readvariableop5
1savev2_adam_dense_33_kernel_v_read_readvariableop3
/savev2_adam_dense_33_bias_v_read_readvariableop5
1savev2_adam_dense_34_kernel_v_read_readvariableop3
/savev2_adam_dense_34_bias_v_read_readvariableop
savev2_const

identity_1??MergeV2Checkpoints?
StaticRegexFullMatchStaticRegexFullMatchfile_prefix"/device:CPU:**
_output_shapes
: *
pattern
^s3://.*2
StaticRegexFullMatchc
ConstConst"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B.part2
Constl
Const_1Const"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B
_temp/part2	
Const_1?
SelectSelectStaticRegexFullMatch:output:0Const:output:0Const_1:output:0"/device:CPU:**
T0*
_output_shapes
: 2
Selectt

StringJoin
StringJoinfile_prefixSelect:output:0"/device:CPU:**
N*
_output_shapes
: 2

StringJoinZ

num_shardsConst*
_output_shapes
: *
dtype0*
value	B :2

num_shards
ShardedFilename/shardConst"/device:CPU:0*
_output_shapes
: *
dtype0*
value	B : 2
ShardedFilename/shard?
ShardedFilenameShardedFilenameStringJoin:output:0ShardedFilename/shard:output:0num_shards:output:0"/device:CPU:0*
_output_shapes
: 2
ShardedFilename?
SaveV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:+*
dtype0*?
value?B?+B:layer_with_weights-0/embeddings/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-1/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-1/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-2/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-2/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-3/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-3/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-4/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-4/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-5/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-5/bias/.ATTRIBUTES/VARIABLE_VALUEB)optimizer/iter/.ATTRIBUTES/VARIABLE_VALUEB+optimizer/beta_1/.ATTRIBUTES/VARIABLE_VALUEB+optimizer/beta_2/.ATTRIBUTES/VARIABLE_VALUEB*optimizer/decay/.ATTRIBUTES/VARIABLE_VALUEB2optimizer/learning_rate/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/0/total/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/0/count/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/1/total/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/1/count/.ATTRIBUTES/VARIABLE_VALUEBVlayer_with_weights-0/embeddings/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-1/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-1/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-2/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-2/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-3/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-3/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-4/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-4/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-5/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-5/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBVlayer_with_weights-0/embeddings/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-1/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-1/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-2/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-2/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-3/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-3/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-4/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-4/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-5/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-5/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPH2
SaveV2/tensor_names?
SaveV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:+*
dtype0*i
value`B^+B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B 2
SaveV2/shape_and_slices?
SaveV2SaveV2ShardedFilename:filename:0SaveV2/tensor_names:output:0 SaveV2/shape_and_slices:output:01savev2_embedding_6_embeddings_read_readvariableop*savev2_dense_30_kernel_read_readvariableop(savev2_dense_30_bias_read_readvariableop*savev2_dense_31_kernel_read_readvariableop(savev2_dense_31_bias_read_readvariableop*savev2_dense_32_kernel_read_readvariableop(savev2_dense_32_bias_read_readvariableop*savev2_dense_33_kernel_read_readvariableop(savev2_dense_33_bias_read_readvariableop*savev2_dense_34_kernel_read_readvariableop(savev2_dense_34_bias_read_readvariableop$savev2_adam_iter_read_readvariableop&savev2_adam_beta_1_read_readvariableop&savev2_adam_beta_2_read_readvariableop%savev2_adam_decay_read_readvariableop-savev2_adam_learning_rate_read_readvariableop savev2_total_read_readvariableop savev2_count_read_readvariableop"savev2_total_1_read_readvariableop"savev2_count_1_read_readvariableop8savev2_adam_embedding_6_embeddings_m_read_readvariableop1savev2_adam_dense_30_kernel_m_read_readvariableop/savev2_adam_dense_30_bias_m_read_readvariableop1savev2_adam_dense_31_kernel_m_read_readvariableop/savev2_adam_dense_31_bias_m_read_readvariableop1savev2_adam_dense_32_kernel_m_read_readvariableop/savev2_adam_dense_32_bias_m_read_readvariableop1savev2_adam_dense_33_kernel_m_read_readvariableop/savev2_adam_dense_33_bias_m_read_readvariableop1savev2_adam_dense_34_kernel_m_read_readvariableop/savev2_adam_dense_34_bias_m_read_readvariableop8savev2_adam_embedding_6_embeddings_v_read_readvariableop1savev2_adam_dense_30_kernel_v_read_readvariableop/savev2_adam_dense_30_bias_v_read_readvariableop1savev2_adam_dense_31_kernel_v_read_readvariableop/savev2_adam_dense_31_bias_v_read_readvariableop1savev2_adam_dense_32_kernel_v_read_readvariableop/savev2_adam_dense_32_bias_v_read_readvariableop1savev2_adam_dense_33_kernel_v_read_readvariableop/savev2_adam_dense_33_bias_v_read_readvariableop1savev2_adam_dense_34_kernel_v_read_readvariableop/savev2_adam_dense_34_bias_v_read_readvariableopsavev2_const"/device:CPU:0*
_output_shapes
 *9
dtypes/
-2+	2
SaveV2?
&MergeV2Checkpoints/checkpoint_prefixesPackShardedFilename:filename:0^SaveV2"/device:CPU:0*
N*
T0*
_output_shapes
:2(
&MergeV2Checkpoints/checkpoint_prefixes?
MergeV2CheckpointsMergeV2Checkpoints/MergeV2Checkpoints/checkpoint_prefixes:output:0file_prefix"/device:CPU:0*
_output_shapes
 2
MergeV2Checkpointsr
IdentityIdentityfile_prefix^MergeV2Checkpoints"/device:CPU:0*
T0*
_output_shapes
: 2

Identitym

Identity_1IdentityIdentity:output:0^MergeV2Checkpoints*
T0*
_output_shapes
: 2

Identity_1"!

identity_1Identity_1:output:0*?
_input_shapes?
?: :	? : :: : : @:@:@:::: : : : : : : : : :	? : :: : : @:@:@::::	? : :: : : @:@:@:::: 2(
MergeV2CheckpointsMergeV2Checkpoints:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix:%!

_output_shapes
:	? :$ 

_output_shapes

: : 

_output_shapes
::$ 

_output_shapes

: : 

_output_shapes
: :$ 

_output_shapes

: @: 

_output_shapes
:@:$ 

_output_shapes

:@: 	

_output_shapes
::$
 

_output_shapes

:: 

_output_shapes
::

_output_shapes
: :

_output_shapes
: :

_output_shapes
: :

_output_shapes
: :

_output_shapes
: :

_output_shapes
: :

_output_shapes
: :

_output_shapes
: :

_output_shapes
: :%!

_output_shapes
:	? :$ 

_output_shapes

: : 

_output_shapes
::$ 

_output_shapes

: : 

_output_shapes
: :$ 

_output_shapes

: @: 

_output_shapes
:@:$ 

_output_shapes

:@: 

_output_shapes
::$ 

_output_shapes

:: 

_output_shapes
::% !

_output_shapes
:	? :$! 

_output_shapes

: : "

_output_shapes
::$# 

_output_shapes

: : $

_output_shapes
: :$% 

_output_shapes

: @: &

_output_shapes
:@:$' 

_output_shapes

:@: (

_output_shapes
::$) 

_output_shapes

:: *

_output_shapes
::+

_output_shapes
: 
?
s
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_3355284

inputs
identityr
Mean/reduction_indicesConst*
_output_shapes
: *
dtype0*
value	B :2
Mean/reduction_indiceso
MeanMeaninputsMean/reduction_indices:output:0*
T0*'
_output_shapes
:????????? 2
Meana
IdentityIdentityMean:output:0*
T0*'
_output_shapes
:????????? 2

Identity"
identityIdentity:output:0**
_input_shapes
:????????? :S O
+
_output_shapes
:????????? 
 
_user_specified_nameinputs
?	
?
E__inference_dense_31_layer_call_and_return_conditional_losses_3355320

inputs"
matmul_readvariableop_resource#
biasadd_readvariableop_resource
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOp?
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes

: *
dtype02
MatMul/ReadVariableOps
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:????????? 2
MatMul?
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
: *
dtype02
BiasAdd/ReadVariableOp?
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:????????? 2	
BiasAddX
ReluReluBiasAdd:output:0*
T0*'
_output_shapes
:????????? 2
Relu?
IdentityIdentityRelu:activations:0^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*
T0*'
_output_shapes
:????????? 2

Identity"
identityIdentity:output:0*.
_input_shapes
:?????????::20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?$
?
I__inference_sequential_6_layer_call_and_return_conditional_losses_3354944
embedding_6_input
embedding_6_3354914
dense_30_3354918
dense_30_3354920
dense_31_3354923
dense_31_3354925
dense_32_3354928
dense_32_3354930
dense_33_3354933
dense_33_3354935
dense_34_3354938
dense_34_3354940
identity?? dense_30/StatefulPartitionedCall? dense_31/StatefulPartitionedCall? dense_32/StatefulPartitionedCall? dense_33/StatefulPartitionedCall? dense_34/StatefulPartitionedCall?#embedding_6/StatefulPartitionedCall?
#embedding_6/StatefulPartitionedCallStatefulPartitionedCallembedding_6_inputembedding_6_3354914*
Tin
2*
Tout
2*
_collective_manager_ids
 *+
_output_shapes
:????????? *#
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *Q
fLRJ
H__inference_embedding_6_layer_call_and_return_conditional_losses_33547512%
#embedding_6/StatefulPartitionedCall?
*global_average_pooling1d_6/PartitionedCallPartitionedCall,embedding_6/StatefulPartitionedCall:output:0*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8? *`
f[RY
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_33547682,
*global_average_pooling1d_6/PartitionedCall?
 dense_30/StatefulPartitionedCallStatefulPartitionedCall3global_average_pooling1d_6/PartitionedCall:output:0dense_30_3354918dense_30_3354920*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_30_layer_call_and_return_conditional_losses_33547862"
 dense_30/StatefulPartitionedCall?
 dense_31/StatefulPartitionedCallStatefulPartitionedCall)dense_30/StatefulPartitionedCall:output:0dense_31_3354923dense_31_3354925*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? *$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_31_layer_call_and_return_conditional_losses_33548132"
 dense_31/StatefulPartitionedCall?
 dense_32/StatefulPartitionedCallStatefulPartitionedCall)dense_31/StatefulPartitionedCall:output:0dense_32_3354928dense_32_3354930*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????@*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_32_layer_call_and_return_conditional_losses_33548402"
 dense_32/StatefulPartitionedCall?
 dense_33/StatefulPartitionedCallStatefulPartitionedCall)dense_32/StatefulPartitionedCall:output:0dense_33_3354933dense_33_3354935*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_33_layer_call_and_return_conditional_losses_33548672"
 dense_33/StatefulPartitionedCall?
 dense_34/StatefulPartitionedCallStatefulPartitionedCall)dense_33/StatefulPartitionedCall:output:0dense_34_3354938dense_34_3354940*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_34_layer_call_and_return_conditional_losses_33548942"
 dense_34/StatefulPartitionedCall?
IdentityIdentity)dense_34/StatefulPartitionedCall:output:0!^dense_30/StatefulPartitionedCall!^dense_31/StatefulPartitionedCall!^dense_32/StatefulPartitionedCall!^dense_33/StatefulPartitionedCall!^dense_34/StatefulPartitionedCall$^embedding_6/StatefulPartitionedCall*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*R
_input_shapesA
?:?????????:::::::::::2D
 dense_30/StatefulPartitionedCall dense_30/StatefulPartitionedCall2D
 dense_31/StatefulPartitionedCall dense_31/StatefulPartitionedCall2D
 dense_32/StatefulPartitionedCall dense_32/StatefulPartitionedCall2D
 dense_33/StatefulPartitionedCall dense_33/StatefulPartitionedCall2D
 dense_34/StatefulPartitionedCall dense_34/StatefulPartitionedCall2J
#embedding_6/StatefulPartitionedCall#embedding_6/StatefulPartitionedCall:Z V
'
_output_shapes
:?????????
+
_user_specified_nameembedding_6_input
?

*__inference_dense_31_layer_call_fn_3355329

inputs
unknown
	unknown_0
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? *$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_31_layer_call_and_return_conditional_losses_33548132
StatefulPartitionedCall?
IdentityIdentity StatefulPartitionedCall:output:0^StatefulPartitionedCall*
T0*'
_output_shapes
:????????? 2

Identity"
identityIdentity:output:0*.
_input_shapes
:?????????::22
StatefulPartitionedCallStatefulPartitionedCall:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?	
?
H__inference_embedding_6_layer_call_and_return_conditional_losses_3354751

inputs
embedding_lookup_3354745
identity??embedding_lookup]
CastCastinputs*

DstT0*

SrcT0*'
_output_shapes
:?????????2
Cast?
embedding_lookupResourceGatherembedding_lookup_3354745Cast:y:0",/job:localhost/replica:0/task:0/device:CPU:0*
Tindices0*+
_class!
loc:@embedding_lookup/3354745*+
_output_shapes
:????????? *
dtype02
embedding_lookup?
embedding_lookup/IdentityIdentityembedding_lookup:output:0",/job:localhost/replica:0/task:0/device:CPU:0*
T0*+
_class!
loc:@embedding_lookup/3354745*+
_output_shapes
:????????? 2
embedding_lookup/Identity?
embedding_lookup/Identity_1Identity"embedding_lookup/Identity:output:0*
T0*+
_output_shapes
:????????? 2
embedding_lookup/Identity_1?
IdentityIdentity$embedding_lookup/Identity_1:output:0^embedding_lookup*
T0*+
_output_shapes
:????????? 2

Identity"
identityIdentity:output:0**
_input_shapes
:?????????:2$
embedding_lookupembedding_lookup:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?<
?
I__inference_sequential_6_layer_call_and_return_conditional_losses_3355149

inputs(
$embedding_6_embedding_lookup_3355106+
'dense_30_matmul_readvariableop_resource,
(dense_30_biasadd_readvariableop_resource+
'dense_31_matmul_readvariableop_resource,
(dense_31_biasadd_readvariableop_resource+
'dense_32_matmul_readvariableop_resource,
(dense_32_biasadd_readvariableop_resource+
'dense_33_matmul_readvariableop_resource,
(dense_33_biasadd_readvariableop_resource+
'dense_34_matmul_readvariableop_resource,
(dense_34_biasadd_readvariableop_resource
identity??dense_30/BiasAdd/ReadVariableOp?dense_30/MatMul/ReadVariableOp?dense_31/BiasAdd/ReadVariableOp?dense_31/MatMul/ReadVariableOp?dense_32/BiasAdd/ReadVariableOp?dense_32/MatMul/ReadVariableOp?dense_33/BiasAdd/ReadVariableOp?dense_33/MatMul/ReadVariableOp?dense_34/BiasAdd/ReadVariableOp?dense_34/MatMul/ReadVariableOp?embedding_6/embedding_lookupu
embedding_6/CastCastinputs*

DstT0*

SrcT0*'
_output_shapes
:?????????2
embedding_6/Cast?
embedding_6/embedding_lookupResourceGather$embedding_6_embedding_lookup_3355106embedding_6/Cast:y:0",/job:localhost/replica:0/task:0/device:CPU:0*
Tindices0*7
_class-
+)loc:@embedding_6/embedding_lookup/3355106*+
_output_shapes
:????????? *
dtype02
embedding_6/embedding_lookup?
%embedding_6/embedding_lookup/IdentityIdentity%embedding_6/embedding_lookup:output:0",/job:localhost/replica:0/task:0/device:CPU:0*
T0*7
_class-
+)loc:@embedding_6/embedding_lookup/3355106*+
_output_shapes
:????????? 2'
%embedding_6/embedding_lookup/Identity?
'embedding_6/embedding_lookup/Identity_1Identity.embedding_6/embedding_lookup/Identity:output:0*
T0*+
_output_shapes
:????????? 2)
'embedding_6/embedding_lookup/Identity_1?
1global_average_pooling1d_6/Mean/reduction_indicesConst*
_output_shapes
: *
dtype0*
value	B :23
1global_average_pooling1d_6/Mean/reduction_indices?
global_average_pooling1d_6/MeanMean0embedding_6/embedding_lookup/Identity_1:output:0:global_average_pooling1d_6/Mean/reduction_indices:output:0*
T0*'
_output_shapes
:????????? 2!
global_average_pooling1d_6/Mean?
dense_30/MatMul/ReadVariableOpReadVariableOp'dense_30_matmul_readvariableop_resource*
_output_shapes

: *
dtype02 
dense_30/MatMul/ReadVariableOp?
dense_30/MatMulMatMul(global_average_pooling1d_6/Mean:output:0&dense_30/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
dense_30/MatMul?
dense_30/BiasAdd/ReadVariableOpReadVariableOp(dense_30_biasadd_readvariableop_resource*
_output_shapes
:*
dtype02!
dense_30/BiasAdd/ReadVariableOp?
dense_30/BiasAddBiasAdddense_30/MatMul:product:0'dense_30/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
dense_30/BiasAdds
dense_30/ReluReludense_30/BiasAdd:output:0*
T0*'
_output_shapes
:?????????2
dense_30/Relu?
dense_31/MatMul/ReadVariableOpReadVariableOp'dense_31_matmul_readvariableop_resource*
_output_shapes

: *
dtype02 
dense_31/MatMul/ReadVariableOp?
dense_31/MatMulMatMuldense_30/Relu:activations:0&dense_31/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:????????? 2
dense_31/MatMul?
dense_31/BiasAdd/ReadVariableOpReadVariableOp(dense_31_biasadd_readvariableop_resource*
_output_shapes
: *
dtype02!
dense_31/BiasAdd/ReadVariableOp?
dense_31/BiasAddBiasAdddense_31/MatMul:product:0'dense_31/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:????????? 2
dense_31/BiasAdds
dense_31/ReluReludense_31/BiasAdd:output:0*
T0*'
_output_shapes
:????????? 2
dense_31/Relu?
dense_32/MatMul/ReadVariableOpReadVariableOp'dense_32_matmul_readvariableop_resource*
_output_shapes

: @*
dtype02 
dense_32/MatMul/ReadVariableOp?
dense_32/MatMulMatMuldense_31/Relu:activations:0&dense_32/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????@2
dense_32/MatMul?
dense_32/BiasAdd/ReadVariableOpReadVariableOp(dense_32_biasadd_readvariableop_resource*
_output_shapes
:@*
dtype02!
dense_32/BiasAdd/ReadVariableOp?
dense_32/BiasAddBiasAdddense_32/MatMul:product:0'dense_32/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????@2
dense_32/BiasAdds
dense_32/ReluReludense_32/BiasAdd:output:0*
T0*'
_output_shapes
:?????????@2
dense_32/Relu?
dense_33/MatMul/ReadVariableOpReadVariableOp'dense_33_matmul_readvariableop_resource*
_output_shapes

:@*
dtype02 
dense_33/MatMul/ReadVariableOp?
dense_33/MatMulMatMuldense_32/Relu:activations:0&dense_33/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
dense_33/MatMul?
dense_33/BiasAdd/ReadVariableOpReadVariableOp(dense_33_biasadd_readvariableop_resource*
_output_shapes
:*
dtype02!
dense_33/BiasAdd/ReadVariableOp?
dense_33/BiasAddBiasAdddense_33/MatMul:product:0'dense_33/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
dense_33/BiasAdds
dense_33/ReluReludense_33/BiasAdd:output:0*
T0*'
_output_shapes
:?????????2
dense_33/Relu?
dense_34/MatMul/ReadVariableOpReadVariableOp'dense_34_matmul_readvariableop_resource*
_output_shapes

:*
dtype02 
dense_34/MatMul/ReadVariableOp?
dense_34/MatMulMatMuldense_33/Relu:activations:0&dense_34/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
dense_34/MatMul?
dense_34/BiasAdd/ReadVariableOpReadVariableOp(dense_34_biasadd_readvariableop_resource*
_output_shapes
:*
dtype02!
dense_34/BiasAdd/ReadVariableOp?
dense_34/BiasAddBiasAdddense_34/MatMul:product:0'dense_34/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
dense_34/BiasAdd|
dense_34/SoftmaxSoftmaxdense_34/BiasAdd:output:0*
T0*'
_output_shapes
:?????????2
dense_34/Softmax?
IdentityIdentitydense_34/Softmax:softmax:0 ^dense_30/BiasAdd/ReadVariableOp^dense_30/MatMul/ReadVariableOp ^dense_31/BiasAdd/ReadVariableOp^dense_31/MatMul/ReadVariableOp ^dense_32/BiasAdd/ReadVariableOp^dense_32/MatMul/ReadVariableOp ^dense_33/BiasAdd/ReadVariableOp^dense_33/MatMul/ReadVariableOp ^dense_34/BiasAdd/ReadVariableOp^dense_34/MatMul/ReadVariableOp^embedding_6/embedding_lookup*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*R
_input_shapesA
?:?????????:::::::::::2B
dense_30/BiasAdd/ReadVariableOpdense_30/BiasAdd/ReadVariableOp2@
dense_30/MatMul/ReadVariableOpdense_30/MatMul/ReadVariableOp2B
dense_31/BiasAdd/ReadVariableOpdense_31/BiasAdd/ReadVariableOp2@
dense_31/MatMul/ReadVariableOpdense_31/MatMul/ReadVariableOp2B
dense_32/BiasAdd/ReadVariableOpdense_32/BiasAdd/ReadVariableOp2@
dense_32/MatMul/ReadVariableOpdense_32/MatMul/ReadVariableOp2B
dense_33/BiasAdd/ReadVariableOpdense_33/BiasAdd/ReadVariableOp2@
dense_33/MatMul/ReadVariableOpdense_33/MatMul/ReadVariableOp2B
dense_34/BiasAdd/ReadVariableOpdense_34/BiasAdd/ReadVariableOp2@
dense_34/MatMul/ReadVariableOpdense_34/MatMul/ReadVariableOp2<
embedding_6/embedding_lookupembedding_6/embedding_lookup:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?
X
<__inference_global_average_pooling1d_6_layer_call_fn_3355289

inputs
identity?
PartitionedCallPartitionedCallinputs*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8? *`
f[RY
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_33547682
PartitionedCalll
IdentityIdentityPartitionedCall:output:0*
T0*'
_output_shapes
:????????? 2

Identity"
identityIdentity:output:0**
_input_shapes
:????????? :S O
+
_output_shapes
:????????? 
 
_user_specified_nameinputs
??
?
#__inference__traced_restore_3355674
file_prefix+
'assignvariableop_embedding_6_embeddings&
"assignvariableop_1_dense_30_kernel$
 assignvariableop_2_dense_30_bias&
"assignvariableop_3_dense_31_kernel$
 assignvariableop_4_dense_31_bias&
"assignvariableop_5_dense_32_kernel$
 assignvariableop_6_dense_32_bias&
"assignvariableop_7_dense_33_kernel$
 assignvariableop_8_dense_33_bias&
"assignvariableop_9_dense_34_kernel%
!assignvariableop_10_dense_34_bias!
assignvariableop_11_adam_iter#
assignvariableop_12_adam_beta_1#
assignvariableop_13_adam_beta_2"
assignvariableop_14_adam_decay*
&assignvariableop_15_adam_learning_rate
assignvariableop_16_total
assignvariableop_17_count
assignvariableop_18_total_1
assignvariableop_19_count_15
1assignvariableop_20_adam_embedding_6_embeddings_m.
*assignvariableop_21_adam_dense_30_kernel_m,
(assignvariableop_22_adam_dense_30_bias_m.
*assignvariableop_23_adam_dense_31_kernel_m,
(assignvariableop_24_adam_dense_31_bias_m.
*assignvariableop_25_adam_dense_32_kernel_m,
(assignvariableop_26_adam_dense_32_bias_m.
*assignvariableop_27_adam_dense_33_kernel_m,
(assignvariableop_28_adam_dense_33_bias_m.
*assignvariableop_29_adam_dense_34_kernel_m,
(assignvariableop_30_adam_dense_34_bias_m5
1assignvariableop_31_adam_embedding_6_embeddings_v.
*assignvariableop_32_adam_dense_30_kernel_v,
(assignvariableop_33_adam_dense_30_bias_v.
*assignvariableop_34_adam_dense_31_kernel_v,
(assignvariableop_35_adam_dense_31_bias_v.
*assignvariableop_36_adam_dense_32_kernel_v,
(assignvariableop_37_adam_dense_32_bias_v.
*assignvariableop_38_adam_dense_33_kernel_v,
(assignvariableop_39_adam_dense_33_bias_v.
*assignvariableop_40_adam_dense_34_kernel_v,
(assignvariableop_41_adam_dense_34_bias_v
identity_43??AssignVariableOp?AssignVariableOp_1?AssignVariableOp_10?AssignVariableOp_11?AssignVariableOp_12?AssignVariableOp_13?AssignVariableOp_14?AssignVariableOp_15?AssignVariableOp_16?AssignVariableOp_17?AssignVariableOp_18?AssignVariableOp_19?AssignVariableOp_2?AssignVariableOp_20?AssignVariableOp_21?AssignVariableOp_22?AssignVariableOp_23?AssignVariableOp_24?AssignVariableOp_25?AssignVariableOp_26?AssignVariableOp_27?AssignVariableOp_28?AssignVariableOp_29?AssignVariableOp_3?AssignVariableOp_30?AssignVariableOp_31?AssignVariableOp_32?AssignVariableOp_33?AssignVariableOp_34?AssignVariableOp_35?AssignVariableOp_36?AssignVariableOp_37?AssignVariableOp_38?AssignVariableOp_39?AssignVariableOp_4?AssignVariableOp_40?AssignVariableOp_41?AssignVariableOp_5?AssignVariableOp_6?AssignVariableOp_7?AssignVariableOp_8?AssignVariableOp_9?
RestoreV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:+*
dtype0*?
value?B?+B:layer_with_weights-0/embeddings/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-1/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-1/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-2/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-2/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-3/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-3/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-4/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-4/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-5/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-5/bias/.ATTRIBUTES/VARIABLE_VALUEB)optimizer/iter/.ATTRIBUTES/VARIABLE_VALUEB+optimizer/beta_1/.ATTRIBUTES/VARIABLE_VALUEB+optimizer/beta_2/.ATTRIBUTES/VARIABLE_VALUEB*optimizer/decay/.ATTRIBUTES/VARIABLE_VALUEB2optimizer/learning_rate/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/0/total/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/0/count/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/1/total/.ATTRIBUTES/VARIABLE_VALUEB4keras_api/metrics/1/count/.ATTRIBUTES/VARIABLE_VALUEBVlayer_with_weights-0/embeddings/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-1/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-1/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-2/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-2/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-3/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-3/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-4/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-4/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-5/kernel/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-5/bias/.OPTIMIZER_SLOT/optimizer/m/.ATTRIBUTES/VARIABLE_VALUEBVlayer_with_weights-0/embeddings/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-1/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-1/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-2/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-2/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-3/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-3/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-4/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-4/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBRlayer_with_weights-5/kernel/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEBPlayer_with_weights-5/bias/.OPTIMIZER_SLOT/optimizer/v/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPH2
RestoreV2/tensor_names?
RestoreV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:+*
dtype0*i
value`B^+B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B B 2
RestoreV2/shape_and_slices?
	RestoreV2	RestoreV2file_prefixRestoreV2/tensor_names:output:0#RestoreV2/shape_and_slices:output:0"/device:CPU:0*?
_output_shapes?
?:::::::::::::::::::::::::::::::::::::::::::*9
dtypes/
-2+	2
	RestoreV2g
IdentityIdentityRestoreV2:tensors:0"/device:CPU:0*
T0*
_output_shapes
:2

Identity?
AssignVariableOpAssignVariableOp'assignvariableop_embedding_6_embeddingsIdentity:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOpk

Identity_1IdentityRestoreV2:tensors:1"/device:CPU:0*
T0*
_output_shapes
:2

Identity_1?
AssignVariableOp_1AssignVariableOp"assignvariableop_1_dense_30_kernelIdentity_1:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_1k

Identity_2IdentityRestoreV2:tensors:2"/device:CPU:0*
T0*
_output_shapes
:2

Identity_2?
AssignVariableOp_2AssignVariableOp assignvariableop_2_dense_30_biasIdentity_2:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_2k

Identity_3IdentityRestoreV2:tensors:3"/device:CPU:0*
T0*
_output_shapes
:2

Identity_3?
AssignVariableOp_3AssignVariableOp"assignvariableop_3_dense_31_kernelIdentity_3:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_3k

Identity_4IdentityRestoreV2:tensors:4"/device:CPU:0*
T0*
_output_shapes
:2

Identity_4?
AssignVariableOp_4AssignVariableOp assignvariableop_4_dense_31_biasIdentity_4:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_4k

Identity_5IdentityRestoreV2:tensors:5"/device:CPU:0*
T0*
_output_shapes
:2

Identity_5?
AssignVariableOp_5AssignVariableOp"assignvariableop_5_dense_32_kernelIdentity_5:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_5k

Identity_6IdentityRestoreV2:tensors:6"/device:CPU:0*
T0*
_output_shapes
:2

Identity_6?
AssignVariableOp_6AssignVariableOp assignvariableop_6_dense_32_biasIdentity_6:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_6k

Identity_7IdentityRestoreV2:tensors:7"/device:CPU:0*
T0*
_output_shapes
:2

Identity_7?
AssignVariableOp_7AssignVariableOp"assignvariableop_7_dense_33_kernelIdentity_7:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_7k

Identity_8IdentityRestoreV2:tensors:8"/device:CPU:0*
T0*
_output_shapes
:2

Identity_8?
AssignVariableOp_8AssignVariableOp assignvariableop_8_dense_33_biasIdentity_8:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_8k

Identity_9IdentityRestoreV2:tensors:9"/device:CPU:0*
T0*
_output_shapes
:2

Identity_9?
AssignVariableOp_9AssignVariableOp"assignvariableop_9_dense_34_kernelIdentity_9:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_9n
Identity_10IdentityRestoreV2:tensors:10"/device:CPU:0*
T0*
_output_shapes
:2
Identity_10?
AssignVariableOp_10AssignVariableOp!assignvariableop_10_dense_34_biasIdentity_10:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_10n
Identity_11IdentityRestoreV2:tensors:11"/device:CPU:0*
T0	*
_output_shapes
:2
Identity_11?
AssignVariableOp_11AssignVariableOpassignvariableop_11_adam_iterIdentity_11:output:0"/device:CPU:0*
_output_shapes
 *
dtype0	2
AssignVariableOp_11n
Identity_12IdentityRestoreV2:tensors:12"/device:CPU:0*
T0*
_output_shapes
:2
Identity_12?
AssignVariableOp_12AssignVariableOpassignvariableop_12_adam_beta_1Identity_12:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_12n
Identity_13IdentityRestoreV2:tensors:13"/device:CPU:0*
T0*
_output_shapes
:2
Identity_13?
AssignVariableOp_13AssignVariableOpassignvariableop_13_adam_beta_2Identity_13:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_13n
Identity_14IdentityRestoreV2:tensors:14"/device:CPU:0*
T0*
_output_shapes
:2
Identity_14?
AssignVariableOp_14AssignVariableOpassignvariableop_14_adam_decayIdentity_14:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_14n
Identity_15IdentityRestoreV2:tensors:15"/device:CPU:0*
T0*
_output_shapes
:2
Identity_15?
AssignVariableOp_15AssignVariableOp&assignvariableop_15_adam_learning_rateIdentity_15:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_15n
Identity_16IdentityRestoreV2:tensors:16"/device:CPU:0*
T0*
_output_shapes
:2
Identity_16?
AssignVariableOp_16AssignVariableOpassignvariableop_16_totalIdentity_16:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_16n
Identity_17IdentityRestoreV2:tensors:17"/device:CPU:0*
T0*
_output_shapes
:2
Identity_17?
AssignVariableOp_17AssignVariableOpassignvariableop_17_countIdentity_17:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_17n
Identity_18IdentityRestoreV2:tensors:18"/device:CPU:0*
T0*
_output_shapes
:2
Identity_18?
AssignVariableOp_18AssignVariableOpassignvariableop_18_total_1Identity_18:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_18n
Identity_19IdentityRestoreV2:tensors:19"/device:CPU:0*
T0*
_output_shapes
:2
Identity_19?
AssignVariableOp_19AssignVariableOpassignvariableop_19_count_1Identity_19:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_19n
Identity_20IdentityRestoreV2:tensors:20"/device:CPU:0*
T0*
_output_shapes
:2
Identity_20?
AssignVariableOp_20AssignVariableOp1assignvariableop_20_adam_embedding_6_embeddings_mIdentity_20:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_20n
Identity_21IdentityRestoreV2:tensors:21"/device:CPU:0*
T0*
_output_shapes
:2
Identity_21?
AssignVariableOp_21AssignVariableOp*assignvariableop_21_adam_dense_30_kernel_mIdentity_21:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_21n
Identity_22IdentityRestoreV2:tensors:22"/device:CPU:0*
T0*
_output_shapes
:2
Identity_22?
AssignVariableOp_22AssignVariableOp(assignvariableop_22_adam_dense_30_bias_mIdentity_22:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_22n
Identity_23IdentityRestoreV2:tensors:23"/device:CPU:0*
T0*
_output_shapes
:2
Identity_23?
AssignVariableOp_23AssignVariableOp*assignvariableop_23_adam_dense_31_kernel_mIdentity_23:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_23n
Identity_24IdentityRestoreV2:tensors:24"/device:CPU:0*
T0*
_output_shapes
:2
Identity_24?
AssignVariableOp_24AssignVariableOp(assignvariableop_24_adam_dense_31_bias_mIdentity_24:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_24n
Identity_25IdentityRestoreV2:tensors:25"/device:CPU:0*
T0*
_output_shapes
:2
Identity_25?
AssignVariableOp_25AssignVariableOp*assignvariableop_25_adam_dense_32_kernel_mIdentity_25:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_25n
Identity_26IdentityRestoreV2:tensors:26"/device:CPU:0*
T0*
_output_shapes
:2
Identity_26?
AssignVariableOp_26AssignVariableOp(assignvariableop_26_adam_dense_32_bias_mIdentity_26:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_26n
Identity_27IdentityRestoreV2:tensors:27"/device:CPU:0*
T0*
_output_shapes
:2
Identity_27?
AssignVariableOp_27AssignVariableOp*assignvariableop_27_adam_dense_33_kernel_mIdentity_27:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_27n
Identity_28IdentityRestoreV2:tensors:28"/device:CPU:0*
T0*
_output_shapes
:2
Identity_28?
AssignVariableOp_28AssignVariableOp(assignvariableop_28_adam_dense_33_bias_mIdentity_28:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_28n
Identity_29IdentityRestoreV2:tensors:29"/device:CPU:0*
T0*
_output_shapes
:2
Identity_29?
AssignVariableOp_29AssignVariableOp*assignvariableop_29_adam_dense_34_kernel_mIdentity_29:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_29n
Identity_30IdentityRestoreV2:tensors:30"/device:CPU:0*
T0*
_output_shapes
:2
Identity_30?
AssignVariableOp_30AssignVariableOp(assignvariableop_30_adam_dense_34_bias_mIdentity_30:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_30n
Identity_31IdentityRestoreV2:tensors:31"/device:CPU:0*
T0*
_output_shapes
:2
Identity_31?
AssignVariableOp_31AssignVariableOp1assignvariableop_31_adam_embedding_6_embeddings_vIdentity_31:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_31n
Identity_32IdentityRestoreV2:tensors:32"/device:CPU:0*
T0*
_output_shapes
:2
Identity_32?
AssignVariableOp_32AssignVariableOp*assignvariableop_32_adam_dense_30_kernel_vIdentity_32:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_32n
Identity_33IdentityRestoreV2:tensors:33"/device:CPU:0*
T0*
_output_shapes
:2
Identity_33?
AssignVariableOp_33AssignVariableOp(assignvariableop_33_adam_dense_30_bias_vIdentity_33:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_33n
Identity_34IdentityRestoreV2:tensors:34"/device:CPU:0*
T0*
_output_shapes
:2
Identity_34?
AssignVariableOp_34AssignVariableOp*assignvariableop_34_adam_dense_31_kernel_vIdentity_34:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_34n
Identity_35IdentityRestoreV2:tensors:35"/device:CPU:0*
T0*
_output_shapes
:2
Identity_35?
AssignVariableOp_35AssignVariableOp(assignvariableop_35_adam_dense_31_bias_vIdentity_35:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_35n
Identity_36IdentityRestoreV2:tensors:36"/device:CPU:0*
T0*
_output_shapes
:2
Identity_36?
AssignVariableOp_36AssignVariableOp*assignvariableop_36_adam_dense_32_kernel_vIdentity_36:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_36n
Identity_37IdentityRestoreV2:tensors:37"/device:CPU:0*
T0*
_output_shapes
:2
Identity_37?
AssignVariableOp_37AssignVariableOp(assignvariableop_37_adam_dense_32_bias_vIdentity_37:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_37n
Identity_38IdentityRestoreV2:tensors:38"/device:CPU:0*
T0*
_output_shapes
:2
Identity_38?
AssignVariableOp_38AssignVariableOp*assignvariableop_38_adam_dense_33_kernel_vIdentity_38:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_38n
Identity_39IdentityRestoreV2:tensors:39"/device:CPU:0*
T0*
_output_shapes
:2
Identity_39?
AssignVariableOp_39AssignVariableOp(assignvariableop_39_adam_dense_33_bias_vIdentity_39:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_39n
Identity_40IdentityRestoreV2:tensors:40"/device:CPU:0*
T0*
_output_shapes
:2
Identity_40?
AssignVariableOp_40AssignVariableOp*assignvariableop_40_adam_dense_34_kernel_vIdentity_40:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_40n
Identity_41IdentityRestoreV2:tensors:41"/device:CPU:0*
T0*
_output_shapes
:2
Identity_41?
AssignVariableOp_41AssignVariableOp(assignvariableop_41_adam_dense_34_bias_vIdentity_41:output:0"/device:CPU:0*
_output_shapes
 *
dtype02
AssignVariableOp_419
NoOpNoOp"/device:CPU:0*
_output_shapes
 2
NoOp?
Identity_42Identityfile_prefix^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_10^AssignVariableOp_11^AssignVariableOp_12^AssignVariableOp_13^AssignVariableOp_14^AssignVariableOp_15^AssignVariableOp_16^AssignVariableOp_17^AssignVariableOp_18^AssignVariableOp_19^AssignVariableOp_2^AssignVariableOp_20^AssignVariableOp_21^AssignVariableOp_22^AssignVariableOp_23^AssignVariableOp_24^AssignVariableOp_25^AssignVariableOp_26^AssignVariableOp_27^AssignVariableOp_28^AssignVariableOp_29^AssignVariableOp_3^AssignVariableOp_30^AssignVariableOp_31^AssignVariableOp_32^AssignVariableOp_33^AssignVariableOp_34^AssignVariableOp_35^AssignVariableOp_36^AssignVariableOp_37^AssignVariableOp_38^AssignVariableOp_39^AssignVariableOp_4^AssignVariableOp_40^AssignVariableOp_41^AssignVariableOp_5^AssignVariableOp_6^AssignVariableOp_7^AssignVariableOp_8^AssignVariableOp_9^NoOp"/device:CPU:0*
T0*
_output_shapes
: 2
Identity_42?
Identity_43IdentityIdentity_42:output:0^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_10^AssignVariableOp_11^AssignVariableOp_12^AssignVariableOp_13^AssignVariableOp_14^AssignVariableOp_15^AssignVariableOp_16^AssignVariableOp_17^AssignVariableOp_18^AssignVariableOp_19^AssignVariableOp_2^AssignVariableOp_20^AssignVariableOp_21^AssignVariableOp_22^AssignVariableOp_23^AssignVariableOp_24^AssignVariableOp_25^AssignVariableOp_26^AssignVariableOp_27^AssignVariableOp_28^AssignVariableOp_29^AssignVariableOp_3^AssignVariableOp_30^AssignVariableOp_31^AssignVariableOp_32^AssignVariableOp_33^AssignVariableOp_34^AssignVariableOp_35^AssignVariableOp_36^AssignVariableOp_37^AssignVariableOp_38^AssignVariableOp_39^AssignVariableOp_4^AssignVariableOp_40^AssignVariableOp_41^AssignVariableOp_5^AssignVariableOp_6^AssignVariableOp_7^AssignVariableOp_8^AssignVariableOp_9*
T0*
_output_shapes
: 2
Identity_43"#
identity_43Identity_43:output:0*?
_input_shapes?
?: ::::::::::::::::::::::::::::::::::::::::::2$
AssignVariableOpAssignVariableOp2(
AssignVariableOp_1AssignVariableOp_12*
AssignVariableOp_10AssignVariableOp_102*
AssignVariableOp_11AssignVariableOp_112*
AssignVariableOp_12AssignVariableOp_122*
AssignVariableOp_13AssignVariableOp_132*
AssignVariableOp_14AssignVariableOp_142*
AssignVariableOp_15AssignVariableOp_152*
AssignVariableOp_16AssignVariableOp_162*
AssignVariableOp_17AssignVariableOp_172*
AssignVariableOp_18AssignVariableOp_182*
AssignVariableOp_19AssignVariableOp_192(
AssignVariableOp_2AssignVariableOp_22*
AssignVariableOp_20AssignVariableOp_202*
AssignVariableOp_21AssignVariableOp_212*
AssignVariableOp_22AssignVariableOp_222*
AssignVariableOp_23AssignVariableOp_232*
AssignVariableOp_24AssignVariableOp_242*
AssignVariableOp_25AssignVariableOp_252*
AssignVariableOp_26AssignVariableOp_262*
AssignVariableOp_27AssignVariableOp_272*
AssignVariableOp_28AssignVariableOp_282*
AssignVariableOp_29AssignVariableOp_292(
AssignVariableOp_3AssignVariableOp_32*
AssignVariableOp_30AssignVariableOp_302*
AssignVariableOp_31AssignVariableOp_312*
AssignVariableOp_32AssignVariableOp_322*
AssignVariableOp_33AssignVariableOp_332*
AssignVariableOp_34AssignVariableOp_342*
AssignVariableOp_35AssignVariableOp_352*
AssignVariableOp_36AssignVariableOp_362*
AssignVariableOp_37AssignVariableOp_372*
AssignVariableOp_38AssignVariableOp_382*
AssignVariableOp_39AssignVariableOp_392(
AssignVariableOp_4AssignVariableOp_42*
AssignVariableOp_40AssignVariableOp_402*
AssignVariableOp_41AssignVariableOp_412(
AssignVariableOp_5AssignVariableOp_52(
AssignVariableOp_6AssignVariableOp_62(
AssignVariableOp_7AssignVariableOp_72(
AssignVariableOp_8AssignVariableOp_82(
AssignVariableOp_9AssignVariableOp_9:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix
?	
?
E__inference_dense_33_layer_call_and_return_conditional_losses_3354867

inputs"
matmul_readvariableop_resource#
biasadd_readvariableop_resource
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOp?
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes

:@*
dtype02
MatMul/ReadVariableOps
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
MatMul?
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
:*
dtype02
BiasAdd/ReadVariableOp?
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2	
BiasAddX
ReluReluBiasAdd:output:0*
T0*'
_output_shapes
:?????????2
Relu?
IdentityIdentityRelu:activations:0^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*.
_input_shapes
:?????????@::20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:O K
'
_output_shapes
:?????????@
 
_user_specified_nameinputs
?
?
%__inference_signature_wrapper_3355102
embedding_6_input
unknown
	unknown_0
	unknown_1
	unknown_2
	unknown_3
	unknown_4
	unknown_5
	unknown_6
	unknown_7
	unknown_8
	unknown_9
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallembedding_6_inputunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4	unknown_5	unknown_6	unknown_7	unknown_8	unknown_9*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*-
_read_only_resource_inputs
	
*-
config_proto

CPU

GPU 2J 8? *+
f&R$
"__inference__wrapped_model_33547182
StatefulPartitionedCall?
IdentityIdentity StatefulPartitionedCall:output:0^StatefulPartitionedCall*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*R
_input_shapesA
?:?????????:::::::::::22
StatefulPartitionedCallStatefulPartitionedCall:Z V
'
_output_shapes
:?????????
+
_user_specified_nameembedding_6_input
?	
?
E__inference_dense_32_layer_call_and_return_conditional_losses_3354840

inputs"
matmul_readvariableop_resource#
biasadd_readvariableop_resource
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOp?
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes

: @*
dtype02
MatMul/ReadVariableOps
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????@2
MatMul?
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
:@*
dtype02
BiasAdd/ReadVariableOp?
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????@2	
BiasAddX
ReluReluBiasAdd:output:0*
T0*'
_output_shapes
:?????????@2
Relu?
IdentityIdentityRelu:activations:0^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*
T0*'
_output_shapes
:?????????@2

Identity"
identityIdentity:output:0*.
_input_shapes
:????????? ::20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:O K
'
_output_shapes
:????????? 
 
_user_specified_nameinputs
?	
?
E__inference_dense_31_layer_call_and_return_conditional_losses_3354813

inputs"
matmul_readvariableop_resource#
biasadd_readvariableop_resource
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOp?
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes

: *
dtype02
MatMul/ReadVariableOps
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:????????? 2
MatMul?
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
: *
dtype02
BiasAdd/ReadVariableOp?
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:????????? 2	
BiasAddX
ReluReluBiasAdd:output:0*
T0*'
_output_shapes
:????????? 2
Relu?
IdentityIdentityRelu:activations:0^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*
T0*'
_output_shapes
:????????? 2

Identity"
identityIdentity:output:0*.
_input_shapes
:?????????::20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?
s
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_3355273

inputs
identityr
Mean/reduction_indicesConst*
_output_shapes
: *
dtype0*
value	B :2
Mean/reduction_indicesx
MeanMeaninputsMean/reduction_indices:output:0*
T0*0
_output_shapes
:??????????????????2
Meanj
IdentityIdentityMean:output:0*
T0*0
_output_shapes
:??????????????????2

Identity"
identityIdentity:output:0*<
_input_shapes+
):'???????????????????????????:e a
=
_output_shapes+
):'???????????????????????????
 
_user_specified_nameinputs
?	
?
E__inference_dense_30_layer_call_and_return_conditional_losses_3355300

inputs"
matmul_readvariableop_resource#
biasadd_readvariableop_resource
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOp?
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes

: *
dtype02
MatMul/ReadVariableOps
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
MatMul?
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
:*
dtype02
BiasAdd/ReadVariableOp?
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2	
BiasAddX
ReluReluBiasAdd:output:0*
T0*'
_output_shapes
:?????????2
Relu?
IdentityIdentityRelu:activations:0^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*.
_input_shapes
:????????? ::20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:O K
'
_output_shapes
:????????? 
 
_user_specified_nameinputs
?#
?
I__inference_sequential_6_layer_call_and_return_conditional_losses_3354980

inputs
embedding_6_3354950
dense_30_3354954
dense_30_3354956
dense_31_3354959
dense_31_3354961
dense_32_3354964
dense_32_3354966
dense_33_3354969
dense_33_3354971
dense_34_3354974
dense_34_3354976
identity?? dense_30/StatefulPartitionedCall? dense_31/StatefulPartitionedCall? dense_32/StatefulPartitionedCall? dense_33/StatefulPartitionedCall? dense_34/StatefulPartitionedCall?#embedding_6/StatefulPartitionedCall?
#embedding_6/StatefulPartitionedCallStatefulPartitionedCallinputsembedding_6_3354950*
Tin
2*
Tout
2*
_collective_manager_ids
 *+
_output_shapes
:????????? *#
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *Q
fLRJ
H__inference_embedding_6_layer_call_and_return_conditional_losses_33547512%
#embedding_6/StatefulPartitionedCall?
*global_average_pooling1d_6/PartitionedCallPartitionedCall,embedding_6/StatefulPartitionedCall:output:0*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8? *`
f[RY
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_33547682,
*global_average_pooling1d_6/PartitionedCall?
 dense_30/StatefulPartitionedCallStatefulPartitionedCall3global_average_pooling1d_6/PartitionedCall:output:0dense_30_3354954dense_30_3354956*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_30_layer_call_and_return_conditional_losses_33547862"
 dense_30/StatefulPartitionedCall?
 dense_31/StatefulPartitionedCallStatefulPartitionedCall)dense_30/StatefulPartitionedCall:output:0dense_31_3354959dense_31_3354961*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? *$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_31_layer_call_and_return_conditional_losses_33548132"
 dense_31/StatefulPartitionedCall?
 dense_32/StatefulPartitionedCallStatefulPartitionedCall)dense_31/StatefulPartitionedCall:output:0dense_32_3354964dense_32_3354966*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????@*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_32_layer_call_and_return_conditional_losses_33548402"
 dense_32/StatefulPartitionedCall?
 dense_33/StatefulPartitionedCallStatefulPartitionedCall)dense_32/StatefulPartitionedCall:output:0dense_33_3354969dense_33_3354971*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_33_layer_call_and_return_conditional_losses_33548672"
 dense_33/StatefulPartitionedCall?
 dense_34/StatefulPartitionedCallStatefulPartitionedCall)dense_33/StatefulPartitionedCall:output:0dense_34_3354974dense_34_3354976*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_34_layer_call_and_return_conditional_losses_33548942"
 dense_34/StatefulPartitionedCall?
IdentityIdentity)dense_34/StatefulPartitionedCall:output:0!^dense_30/StatefulPartitionedCall!^dense_31/StatefulPartitionedCall!^dense_32/StatefulPartitionedCall!^dense_33/StatefulPartitionedCall!^dense_34/StatefulPartitionedCall$^embedding_6/StatefulPartitionedCall*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*R
_input_shapesA
?:?????????:::::::::::2D
 dense_30/StatefulPartitionedCall dense_30/StatefulPartitionedCall2D
 dense_31/StatefulPartitionedCall dense_31/StatefulPartitionedCall2D
 dense_32/StatefulPartitionedCall dense_32/StatefulPartitionedCall2D
 dense_33/StatefulPartitionedCall dense_33/StatefulPartitionedCall2D
 dense_34/StatefulPartitionedCall dense_34/StatefulPartitionedCall2J
#embedding_6/StatefulPartitionedCall#embedding_6/StatefulPartitionedCall:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?
s
-__inference_embedding_6_layer_call_fn_3355267

inputs
unknown
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputsunknown*
Tin
2*
Tout
2*
_collective_manager_ids
 *+
_output_shapes
:????????? *#
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *Q
fLRJ
H__inference_embedding_6_layer_call_and_return_conditional_losses_33547512
StatefulPartitionedCall?
IdentityIdentity StatefulPartitionedCall:output:0^StatefulPartitionedCall*
T0*+
_output_shapes
:????????? 2

Identity"
identityIdentity:output:0**
_input_shapes
:?????????:22
StatefulPartitionedCallStatefulPartitionedCall:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?	
?
H__inference_embedding_6_layer_call_and_return_conditional_losses_3355260

inputs
embedding_lookup_3355254
identity??embedding_lookup]
CastCastinputs*

DstT0*

SrcT0*'
_output_shapes
:?????????2
Cast?
embedding_lookupResourceGatherembedding_lookup_3355254Cast:y:0",/job:localhost/replica:0/task:0/device:CPU:0*
Tindices0*+
_class!
loc:@embedding_lookup/3355254*+
_output_shapes
:????????? *
dtype02
embedding_lookup?
embedding_lookup/IdentityIdentityembedding_lookup:output:0",/job:localhost/replica:0/task:0/device:CPU:0*
T0*+
_class!
loc:@embedding_lookup/3355254*+
_output_shapes
:????????? 2
embedding_lookup/Identity?
embedding_lookup/Identity_1Identity"embedding_lookup/Identity:output:0*
T0*+
_output_shapes
:????????? 2
embedding_lookup/Identity_1?
IdentityIdentity$embedding_lookup/Identity_1:output:0^embedding_lookup*
T0*+
_output_shapes
:????????? 2

Identity"
identityIdentity:output:0**
_input_shapes
:?????????:2$
embedding_lookupembedding_lookup:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?

*__inference_dense_32_layer_call_fn_3355349

inputs
unknown
	unknown_0
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????@*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8? *N
fIRG
E__inference_dense_32_layer_call_and_return_conditional_losses_33548402
StatefulPartitionedCall?
IdentityIdentity StatefulPartitionedCall:output:0^StatefulPartitionedCall*
T0*'
_output_shapes
:?????????@2

Identity"
identityIdentity:output:0*.
_input_shapes
:????????? ::22
StatefulPartitionedCallStatefulPartitionedCall:O K
'
_output_shapes
:????????? 
 
_user_specified_nameinputs
?	
?
.__inference_sequential_6_layer_call_fn_3355065
embedding_6_input
unknown
	unknown_0
	unknown_1
	unknown_2
	unknown_3
	unknown_4
	unknown_5
	unknown_6
	unknown_7
	unknown_8
	unknown_9
identity??StatefulPartitionedCall?
StatefulPartitionedCallStatefulPartitionedCallembedding_6_inputunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4	unknown_5	unknown_6	unknown_7	unknown_8	unknown_9*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*-
_read_only_resource_inputs
	
*-
config_proto

CPU

GPU 2J 8? *R
fMRK
I__inference_sequential_6_layer_call_and_return_conditional_losses_33550402
StatefulPartitionedCall?
IdentityIdentity StatefulPartitionedCall:output:0^StatefulPartitionedCall*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*R
_input_shapesA
?:?????????:::::::::::22
StatefulPartitionedCallStatefulPartitionedCall:Z V
'
_output_shapes
:?????????
+
_user_specified_nameembedding_6_input
?<
?
I__inference_sequential_6_layer_call_and_return_conditional_losses_3355196

inputs(
$embedding_6_embedding_lookup_3355153+
'dense_30_matmul_readvariableop_resource,
(dense_30_biasadd_readvariableop_resource+
'dense_31_matmul_readvariableop_resource,
(dense_31_biasadd_readvariableop_resource+
'dense_32_matmul_readvariableop_resource,
(dense_32_biasadd_readvariableop_resource+
'dense_33_matmul_readvariableop_resource,
(dense_33_biasadd_readvariableop_resource+
'dense_34_matmul_readvariableop_resource,
(dense_34_biasadd_readvariableop_resource
identity??dense_30/BiasAdd/ReadVariableOp?dense_30/MatMul/ReadVariableOp?dense_31/BiasAdd/ReadVariableOp?dense_31/MatMul/ReadVariableOp?dense_32/BiasAdd/ReadVariableOp?dense_32/MatMul/ReadVariableOp?dense_33/BiasAdd/ReadVariableOp?dense_33/MatMul/ReadVariableOp?dense_34/BiasAdd/ReadVariableOp?dense_34/MatMul/ReadVariableOp?embedding_6/embedding_lookupu
embedding_6/CastCastinputs*

DstT0*

SrcT0*'
_output_shapes
:?????????2
embedding_6/Cast?
embedding_6/embedding_lookupResourceGather$embedding_6_embedding_lookup_3355153embedding_6/Cast:y:0",/job:localhost/replica:0/task:0/device:CPU:0*
Tindices0*7
_class-
+)loc:@embedding_6/embedding_lookup/3355153*+
_output_shapes
:????????? *
dtype02
embedding_6/embedding_lookup?
%embedding_6/embedding_lookup/IdentityIdentity%embedding_6/embedding_lookup:output:0",/job:localhost/replica:0/task:0/device:CPU:0*
T0*7
_class-
+)loc:@embedding_6/embedding_lookup/3355153*+
_output_shapes
:????????? 2'
%embedding_6/embedding_lookup/Identity?
'embedding_6/embedding_lookup/Identity_1Identity.embedding_6/embedding_lookup/Identity:output:0*
T0*+
_output_shapes
:????????? 2)
'embedding_6/embedding_lookup/Identity_1?
1global_average_pooling1d_6/Mean/reduction_indicesConst*
_output_shapes
: *
dtype0*
value	B :23
1global_average_pooling1d_6/Mean/reduction_indices?
global_average_pooling1d_6/MeanMean0embedding_6/embedding_lookup/Identity_1:output:0:global_average_pooling1d_6/Mean/reduction_indices:output:0*
T0*'
_output_shapes
:????????? 2!
global_average_pooling1d_6/Mean?
dense_30/MatMul/ReadVariableOpReadVariableOp'dense_30_matmul_readvariableop_resource*
_output_shapes

: *
dtype02 
dense_30/MatMul/ReadVariableOp?
dense_30/MatMulMatMul(global_average_pooling1d_6/Mean:output:0&dense_30/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
dense_30/MatMul?
dense_30/BiasAdd/ReadVariableOpReadVariableOp(dense_30_biasadd_readvariableop_resource*
_output_shapes
:*
dtype02!
dense_30/BiasAdd/ReadVariableOp?
dense_30/BiasAddBiasAdddense_30/MatMul:product:0'dense_30/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
dense_30/BiasAdds
dense_30/ReluReludense_30/BiasAdd:output:0*
T0*'
_output_shapes
:?????????2
dense_30/Relu?
dense_31/MatMul/ReadVariableOpReadVariableOp'dense_31_matmul_readvariableop_resource*
_output_shapes

: *
dtype02 
dense_31/MatMul/ReadVariableOp?
dense_31/MatMulMatMuldense_30/Relu:activations:0&dense_31/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:????????? 2
dense_31/MatMul?
dense_31/BiasAdd/ReadVariableOpReadVariableOp(dense_31_biasadd_readvariableop_resource*
_output_shapes
: *
dtype02!
dense_31/BiasAdd/ReadVariableOp?
dense_31/BiasAddBiasAdddense_31/MatMul:product:0'dense_31/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:????????? 2
dense_31/BiasAdds
dense_31/ReluReludense_31/BiasAdd:output:0*
T0*'
_output_shapes
:????????? 2
dense_31/Relu?
dense_32/MatMul/ReadVariableOpReadVariableOp'dense_32_matmul_readvariableop_resource*
_output_shapes

: @*
dtype02 
dense_32/MatMul/ReadVariableOp?
dense_32/MatMulMatMuldense_31/Relu:activations:0&dense_32/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????@2
dense_32/MatMul?
dense_32/BiasAdd/ReadVariableOpReadVariableOp(dense_32_biasadd_readvariableop_resource*
_output_shapes
:@*
dtype02!
dense_32/BiasAdd/ReadVariableOp?
dense_32/BiasAddBiasAdddense_32/MatMul:product:0'dense_32/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????@2
dense_32/BiasAdds
dense_32/ReluReludense_32/BiasAdd:output:0*
T0*'
_output_shapes
:?????????@2
dense_32/Relu?
dense_33/MatMul/ReadVariableOpReadVariableOp'dense_33_matmul_readvariableop_resource*
_output_shapes

:@*
dtype02 
dense_33/MatMul/ReadVariableOp?
dense_33/MatMulMatMuldense_32/Relu:activations:0&dense_33/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
dense_33/MatMul?
dense_33/BiasAdd/ReadVariableOpReadVariableOp(dense_33_biasadd_readvariableop_resource*
_output_shapes
:*
dtype02!
dense_33/BiasAdd/ReadVariableOp?
dense_33/BiasAddBiasAdddense_33/MatMul:product:0'dense_33/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
dense_33/BiasAdds
dense_33/ReluReludense_33/BiasAdd:output:0*
T0*'
_output_shapes
:?????????2
dense_33/Relu?
dense_34/MatMul/ReadVariableOpReadVariableOp'dense_34_matmul_readvariableop_resource*
_output_shapes

:*
dtype02 
dense_34/MatMul/ReadVariableOp?
dense_34/MatMulMatMuldense_33/Relu:activations:0&dense_34/MatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
dense_34/MatMul?
dense_34/BiasAdd/ReadVariableOpReadVariableOp(dense_34_biasadd_readvariableop_resource*
_output_shapes
:*
dtype02!
dense_34/BiasAdd/ReadVariableOp?
dense_34/BiasAddBiasAdddense_34/MatMul:product:0'dense_34/BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
dense_34/BiasAdd|
dense_34/SoftmaxSoftmaxdense_34/BiasAdd:output:0*
T0*'
_output_shapes
:?????????2
dense_34/Softmax?
IdentityIdentitydense_34/Softmax:softmax:0 ^dense_30/BiasAdd/ReadVariableOp^dense_30/MatMul/ReadVariableOp ^dense_31/BiasAdd/ReadVariableOp^dense_31/MatMul/ReadVariableOp ^dense_32/BiasAdd/ReadVariableOp^dense_32/MatMul/ReadVariableOp ^dense_33/BiasAdd/ReadVariableOp^dense_33/MatMul/ReadVariableOp ^dense_34/BiasAdd/ReadVariableOp^dense_34/MatMul/ReadVariableOp^embedding_6/embedding_lookup*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*R
_input_shapesA
?:?????????:::::::::::2B
dense_30/BiasAdd/ReadVariableOpdense_30/BiasAdd/ReadVariableOp2@
dense_30/MatMul/ReadVariableOpdense_30/MatMul/ReadVariableOp2B
dense_31/BiasAdd/ReadVariableOpdense_31/BiasAdd/ReadVariableOp2@
dense_31/MatMul/ReadVariableOpdense_31/MatMul/ReadVariableOp2B
dense_32/BiasAdd/ReadVariableOpdense_32/BiasAdd/ReadVariableOp2@
dense_32/MatMul/ReadVariableOpdense_32/MatMul/ReadVariableOp2B
dense_33/BiasAdd/ReadVariableOpdense_33/BiasAdd/ReadVariableOp2@
dense_33/MatMul/ReadVariableOpdense_33/MatMul/ReadVariableOp2B
dense_34/BiasAdd/ReadVariableOpdense_34/BiasAdd/ReadVariableOp2@
dense_34/MatMul/ReadVariableOpdense_34/MatMul/ReadVariableOp2<
embedding_6/embedding_lookupembedding_6/embedding_lookup:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?	
?
E__inference_dense_30_layer_call_and_return_conditional_losses_3354786

inputs"
matmul_readvariableop_resource#
biasadd_readvariableop_resource
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOp?
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes

: *
dtype02
MatMul/ReadVariableOps
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
MatMul?
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
:*
dtype02
BiasAdd/ReadVariableOp?
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2	
BiasAddX
ReluReluBiasAdd:output:0*
T0*'
_output_shapes
:?????????2
Relu?
IdentityIdentityRelu:activations:0^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*.
_input_shapes
:????????? ::20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:O K
'
_output_shapes
:????????? 
 
_user_specified_nameinputs
?	
?
E__inference_dense_34_layer_call_and_return_conditional_losses_3354894

inputs"
matmul_readvariableop_resource#
biasadd_readvariableop_resource
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOp?
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes

:*
dtype02
MatMul/ReadVariableOps
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
MatMul?
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
:*
dtype02
BiasAdd/ReadVariableOp?
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2	
BiasAdda
SoftmaxSoftmaxBiasAdd:output:0*
T0*'
_output_shapes
:?????????2	
Softmax?
IdentityIdentitySoftmax:softmax:0^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*.
_input_shapes
:?????????::20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
?	
?
E__inference_dense_33_layer_call_and_return_conditional_losses_3355360

inputs"
matmul_readvariableop_resource#
biasadd_readvariableop_resource
identity??BiasAdd/ReadVariableOp?MatMul/ReadVariableOp?
MatMul/ReadVariableOpReadVariableOpmatmul_readvariableop_resource*
_output_shapes

:@*
dtype02
MatMul/ReadVariableOps
MatMulMatMulinputsMatMul/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2
MatMul?
BiasAdd/ReadVariableOpReadVariableOpbiasadd_readvariableop_resource*
_output_shapes
:*
dtype02
BiasAdd/ReadVariableOp?
BiasAddBiasAddMatMul:product:0BiasAdd/ReadVariableOp:value:0*
T0*'
_output_shapes
:?????????2	
BiasAddX
ReluReluBiasAdd:output:0*
T0*'
_output_shapes
:?????????2
Relu?
IdentityIdentityRelu:activations:0^BiasAdd/ReadVariableOp^MatMul/ReadVariableOp*
T0*'
_output_shapes
:?????????2

Identity"
identityIdentity:output:0*.
_input_shapes
:?????????@::20
BiasAdd/ReadVariableOpBiasAdd/ReadVariableOp2.
MatMul/ReadVariableOpMatMul/ReadVariableOp:O K
'
_output_shapes
:?????????@
 
_user_specified_nameinputs
?
s
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_3354734

inputs
identityr
Mean/reduction_indicesConst*
_output_shapes
: *
dtype0*
value	B :2
Mean/reduction_indicesx
MeanMeaninputsMean/reduction_indices:output:0*
T0*0
_output_shapes
:??????????????????2
Meanj
IdentityIdentityMean:output:0*
T0*0
_output_shapes
:??????????????????2

Identity"
identityIdentity:output:0*<
_input_shapes+
):'???????????????????????????:e a
=
_output_shapes+
):'???????????????????????????
 
_user_specified_nameinputs"?L
saver_filename:0StatefulPartitionedCall_1:0StatefulPartitionedCall_28"
saved_model_main_op

NoOp*>
__saved_model_init_op%#
__saved_model_init_op

NoOp*?
serving_default?
O
embedding_6_input:
#serving_default_embedding_6_input:0?????????<
dense_340
StatefulPartitionedCall:0?????????tensorflow/serving/predict:??
?9
layer_with_weights-0
layer-0
layer-1
layer_with_weights-1
layer-2
layer_with_weights-2
layer-3
layer_with_weights-3
layer-4
layer_with_weights-4
layer-5
layer_with_weights-5
layer-6
	optimizer
		variables

regularization_losses
trainable_variables
	keras_api

signatures
+?&call_and_return_all_conditional_losses
?__call__
?_default_save_signature"?5
_tf_keras_sequential?5{"class_name": "Sequential", "name": "sequential_6", "trainable": true, "expects_training_arg": true, "dtype": "float32", "batch_input_shape": null, "must_restore_from_config": false, "config": {"name": "sequential_6", "layers": [{"class_name": "InputLayer", "config": {"batch_input_shape": {"class_name": "__tuple__", "items": [null, 7]}, "dtype": "float32", "sparse": false, "ragged": false, "name": "embedding_6_input"}}, {"class_name": "Embedding", "config": {"name": "embedding_6", "trainable": true, "batch_input_shape": {"class_name": "__tuple__", "items": [null, 7]}, "dtype": "float32", "input_dim": 1000, "output_dim": 32, "embeddings_initializer": {"class_name": "RandomUniform", "config": {"minval": -0.05, "maxval": 0.05, "seed": null}}, "embeddings_regularizer": null, "activity_regularizer": null, "embeddings_constraint": null, "mask_zero": false, "input_length": 7}}, {"class_name": "GlobalAveragePooling1D", "config": {"name": "global_average_pooling1d_6", "trainable": true, "dtype": "float32", "data_format": "channels_last"}}, {"class_name": "Dense", "config": {"name": "dense_30", "trainable": true, "dtype": "float32", "units": 16, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "Dense", "config": {"name": "dense_31", "trainable": true, "dtype": "float32", "units": 32, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "Dense", "config": {"name": "dense_32", "trainable": true, "dtype": "float32", "units": 64, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "Dense", "config": {"name": "dense_33", "trainable": true, "dtype": "float32", "units": 16, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "Dense", "config": {"name": "dense_34", "trainable": true, "dtype": "float32", "units": 2, "activation": "softmax", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}]}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 7]}, "is_graph_network": true, "keras_version": "2.4.0", "backend": "tensorflow", "model_config": {"class_name": "Sequential", "config": {"name": "sequential_6", "layers": [{"class_name": "InputLayer", "config": {"batch_input_shape": {"class_name": "__tuple__", "items": [null, 7]}, "dtype": "float32", "sparse": false, "ragged": false, "name": "embedding_6_input"}}, {"class_name": "Embedding", "config": {"name": "embedding_6", "trainable": true, "batch_input_shape": {"class_name": "__tuple__", "items": [null, 7]}, "dtype": "float32", "input_dim": 1000, "output_dim": 32, "embeddings_initializer": {"class_name": "RandomUniform", "config": {"minval": -0.05, "maxval": 0.05, "seed": null}}, "embeddings_regularizer": null, "activity_regularizer": null, "embeddings_constraint": null, "mask_zero": false, "input_length": 7}}, {"class_name": "GlobalAveragePooling1D", "config": {"name": "global_average_pooling1d_6", "trainable": true, "dtype": "float32", "data_format": "channels_last"}}, {"class_name": "Dense", "config": {"name": "dense_30", "trainable": true, "dtype": "float32", "units": 16, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "Dense", "config": {"name": "dense_31", "trainable": true, "dtype": "float32", "units": 32, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "Dense", "config": {"name": "dense_32", "trainable": true, "dtype": "float32", "units": 64, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "Dense", "config": {"name": "dense_33", "trainable": true, "dtype": "float32", "units": 16, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"class_name": "Dense", "config": {"name": "dense_34", "trainable": true, "dtype": "float32", "units": 2, "activation": "softmax", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}]}}, "training_config": {"loss": "sparse_categorical_crossentropy", "metrics": [[{"class_name": "MeanMetricWrapper", "config": {"name": "accuracy", "dtype": "float32", "fn": "sparse_categorical_accuracy"}}]], "weighted_metrics": null, "loss_weights": null, "optimizer_config": {"class_name": "Adam", "config": {"name": "Adam", "learning_rate": 0.0010000000474974513, "decay": 0.0, "beta_1": 0.8999999761581421, "beta_2": 0.9990000128746033, "epsilon": 1e-07, "amsgrad": false}}}}
?

embeddings
	variables
regularization_losses
trainable_variables
	keras_api
+?&call_and_return_all_conditional_losses
?__call__"?
_tf_keras_layer?{"class_name": "Embedding", "name": "embedding_6", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": {"class_name": "__tuple__", "items": [null, 7]}, "stateful": false, "must_restore_from_config": false, "config": {"name": "embedding_6", "trainable": true, "batch_input_shape": {"class_name": "__tuple__", "items": [null, 7]}, "dtype": "float32", "input_dim": 1000, "output_dim": 32, "embeddings_initializer": {"class_name": "RandomUniform", "config": {"minval": -0.05, "maxval": 0.05, "seed": null}}, "embeddings_regularizer": null, "activity_regularizer": null, "embeddings_constraint": null, "mask_zero": false, "input_length": 7}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 7]}}
?
	variables
regularization_losses
trainable_variables
	keras_api
+?&call_and_return_all_conditional_losses
?__call__"?
_tf_keras_layer?{"class_name": "GlobalAveragePooling1D", "name": "global_average_pooling1d_6", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "config": {"name": "global_average_pooling1d_6", "trainable": true, "dtype": "float32", "data_format": "channels_last"}, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": 3, "max_ndim": null, "min_ndim": null, "axes": {}}}}
?

kernel
bias
	variables
regularization_losses
trainable_variables
	keras_api
+?&call_and_return_all_conditional_losses
?__call__"?
_tf_keras_layer?{"class_name": "Dense", "name": "dense_30", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "config": {"name": "dense_30", "trainable": true, "dtype": "float32", "units": 16, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": null, "max_ndim": null, "min_ndim": 2, "axes": {"-1": 32}}}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 32]}}
?

kernel
bias
	variables
 regularization_losses
!trainable_variables
"	keras_api
+?&call_and_return_all_conditional_losses
?__call__"?
_tf_keras_layer?{"class_name": "Dense", "name": "dense_31", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "config": {"name": "dense_31", "trainable": true, "dtype": "float32", "units": 32, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": null, "max_ndim": null, "min_ndim": 2, "axes": {"-1": 16}}}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 16]}}
?

#kernel
$bias
%	variables
&regularization_losses
'trainable_variables
(	keras_api
+?&call_and_return_all_conditional_losses
?__call__"?
_tf_keras_layer?{"class_name": "Dense", "name": "dense_32", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "config": {"name": "dense_32", "trainable": true, "dtype": "float32", "units": 64, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": null, "max_ndim": null, "min_ndim": 2, "axes": {"-1": 32}}}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 32]}}
?

)kernel
*bias
+	variables
,regularization_losses
-trainable_variables
.	keras_api
+?&call_and_return_all_conditional_losses
?__call__"?
_tf_keras_layer?{"class_name": "Dense", "name": "dense_33", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "config": {"name": "dense_33", "trainable": true, "dtype": "float32", "units": 16, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": null, "max_ndim": null, "min_ndim": 2, "axes": {"-1": 64}}}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 64]}}
?

/kernel
0bias
1	variables
2regularization_losses
3trainable_variables
4	keras_api
+?&call_and_return_all_conditional_losses
?__call__"?
_tf_keras_layer?{"class_name": "Dense", "name": "dense_34", "trainable": true, "expects_training_arg": false, "dtype": "float32", "batch_input_shape": null, "stateful": false, "must_restore_from_config": false, "config": {"name": "dense_34", "trainable": true, "dtype": "float32", "units": 2, "activation": "softmax", "use_bias": true, "kernel_initializer": {"class_name": "GlorotUniform", "config": {"seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}, "input_spec": {"class_name": "InputSpec", "config": {"dtype": null, "shape": null, "ndim": null, "max_ndim": null, "min_ndim": 2, "axes": {"-1": 16}}}, "build_input_shape": {"class_name": "TensorShape", "items": [null, 16]}}
?
5iter

6beta_1

7beta_2
	8decay
9learning_ratemmmnmompmq#mr$ms)mt*mu/mv0mwvxvyvzv{v|#v}$v~)v*v?/v?0v?"
	optimizer
n
0
1
2
3
4
#5
$6
)7
*8
/9
010"
trackable_list_wrapper
 "
trackable_list_wrapper
n
0
1
2
3
4
#5
$6
)7
*8
/9
010"
trackable_list_wrapper
?
:layer_metrics

;layers
<metrics
		variables
=layer_regularization_losses
>non_trainable_variables

regularization_losses
trainable_variables
?__call__
?_default_save_signature
+?&call_and_return_all_conditional_losses
'?"call_and_return_conditional_losses"
_generic_user_object
-
?serving_default"
signature_map
):'	? 2embedding_6/embeddings
'
0"
trackable_list_wrapper
 "
trackable_list_wrapper
'
0"
trackable_list_wrapper
?
?layer_metrics

@layers
Ametrics
	variables
Blayer_regularization_losses
Cnon_trainable_variables
regularization_losses
trainable_variables
?__call__
+?&call_and_return_all_conditional_losses
'?"call_and_return_conditional_losses"
_generic_user_object
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
?
Dlayer_metrics

Elayers
Fmetrics
	variables
Glayer_regularization_losses
Hnon_trainable_variables
regularization_losses
trainable_variables
?__call__
+?&call_and_return_all_conditional_losses
'?"call_and_return_conditional_losses"
_generic_user_object
!: 2dense_30/kernel
:2dense_30/bias
.
0
1"
trackable_list_wrapper
 "
trackable_list_wrapper
.
0
1"
trackable_list_wrapper
?
Ilayer_metrics

Jlayers
Kmetrics
	variables
Llayer_regularization_losses
Mnon_trainable_variables
regularization_losses
trainable_variables
?__call__
+?&call_and_return_all_conditional_losses
'?"call_and_return_conditional_losses"
_generic_user_object
!: 2dense_31/kernel
: 2dense_31/bias
.
0
1"
trackable_list_wrapper
 "
trackable_list_wrapper
.
0
1"
trackable_list_wrapper
?
Nlayer_metrics

Olayers
Pmetrics
	variables
Qlayer_regularization_losses
Rnon_trainable_variables
 regularization_losses
!trainable_variables
?__call__
+?&call_and_return_all_conditional_losses
'?"call_and_return_conditional_losses"
_generic_user_object
!: @2dense_32/kernel
:@2dense_32/bias
.
#0
$1"
trackable_list_wrapper
 "
trackable_list_wrapper
.
#0
$1"
trackable_list_wrapper
?
Slayer_metrics

Tlayers
Umetrics
%	variables
Vlayer_regularization_losses
Wnon_trainable_variables
&regularization_losses
'trainable_variables
?__call__
+?&call_and_return_all_conditional_losses
'?"call_and_return_conditional_losses"
_generic_user_object
!:@2dense_33/kernel
:2dense_33/bias
.
)0
*1"
trackable_list_wrapper
 "
trackable_list_wrapper
.
)0
*1"
trackable_list_wrapper
?
Xlayer_metrics

Ylayers
Zmetrics
+	variables
[layer_regularization_losses
\non_trainable_variables
,regularization_losses
-trainable_variables
?__call__
+?&call_and_return_all_conditional_losses
'?"call_and_return_conditional_losses"
_generic_user_object
!:2dense_34/kernel
:2dense_34/bias
.
/0
01"
trackable_list_wrapper
 "
trackable_list_wrapper
.
/0
01"
trackable_list_wrapper
?
]layer_metrics

^layers
_metrics
1	variables
`layer_regularization_losses
anon_trainable_variables
2regularization_losses
3trainable_variables
?__call__
+?&call_and_return_all_conditional_losses
'?"call_and_return_conditional_losses"
_generic_user_object
:	 (2	Adam/iter
: (2Adam/beta_1
: (2Adam/beta_2
: (2
Adam/decay
: (2Adam/learning_rate
 "
trackable_dict_wrapper
Q
0
1
2
3
4
5
6"
trackable_list_wrapper
.
b0
c1"
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
?
	dtotal
	ecount
f	variables
g	keras_api"?
_tf_keras_metricj{"class_name": "Mean", "name": "loss", "dtype": "float32", "config": {"name": "loss", "dtype": "float32"}}
?
	htotal
	icount
j
_fn_kwargs
k	variables
l	keras_api"?
_tf_keras_metric?{"class_name": "MeanMetricWrapper", "name": "accuracy", "dtype": "float32", "config": {"name": "accuracy", "dtype": "float32", "fn": "sparse_categorical_accuracy"}}
:  (2total
:  (2count
.
d0
e1"
trackable_list_wrapper
-
f	variables"
_generic_user_object
:  (2total
:  (2count
 "
trackable_dict_wrapper
.
h0
i1"
trackable_list_wrapper
-
k	variables"
_generic_user_object
.:,	? 2Adam/embedding_6/embeddings/m
&:$ 2Adam/dense_30/kernel/m
 :2Adam/dense_30/bias/m
&:$ 2Adam/dense_31/kernel/m
 : 2Adam/dense_31/bias/m
&:$ @2Adam/dense_32/kernel/m
 :@2Adam/dense_32/bias/m
&:$@2Adam/dense_33/kernel/m
 :2Adam/dense_33/bias/m
&:$2Adam/dense_34/kernel/m
 :2Adam/dense_34/bias/m
.:,	? 2Adam/embedding_6/embeddings/v
&:$ 2Adam/dense_30/kernel/v
 :2Adam/dense_30/bias/v
&:$ 2Adam/dense_31/kernel/v
 : 2Adam/dense_31/bias/v
&:$ @2Adam/dense_32/kernel/v
 :@2Adam/dense_32/bias/v
&:$@2Adam/dense_33/kernel/v
 :2Adam/dense_33/bias/v
&:$2Adam/dense_34/kernel/v
 :2Adam/dense_34/bias/v
?2?
I__inference_sequential_6_layer_call_and_return_conditional_losses_3355149
I__inference_sequential_6_layer_call_and_return_conditional_losses_3354911
I__inference_sequential_6_layer_call_and_return_conditional_losses_3355196
I__inference_sequential_6_layer_call_and_return_conditional_losses_3354944?
???
FullArgSpec1
args)?&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults?
p 

 

kwonlyargs? 
kwonlydefaults? 
annotations? *
 
?2?
.__inference_sequential_6_layer_call_fn_3355250
.__inference_sequential_6_layer_call_fn_3355005
.__inference_sequential_6_layer_call_fn_3355223
.__inference_sequential_6_layer_call_fn_3355065?
???
FullArgSpec1
args)?&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults?
p 

 

kwonlyargs? 
kwonlydefaults? 
annotations? *
 
?2?
"__inference__wrapped_model_3354718?
???
FullArgSpec
args? 
varargsjargs
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *0?-
+?(
embedding_6_input?????????
?2?
H__inference_embedding_6_layer_call_and_return_conditional_losses_3355260?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
-__inference_embedding_6_layer_call_fn_3355267?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_3355284
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_3355273?
???
FullArgSpec%
args?
jself
jinputs
jmask
varargs
 
varkw
 
defaults?

 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
<__inference_global_average_pooling1d_6_layer_call_fn_3355278
<__inference_global_average_pooling1d_6_layer_call_fn_3355289?
???
FullArgSpec%
args?
jself
jinputs
jmask
varargs
 
varkw
 
defaults?

 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
E__inference_dense_30_layer_call_and_return_conditional_losses_3355300?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
*__inference_dense_30_layer_call_fn_3355309?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
E__inference_dense_31_layer_call_and_return_conditional_losses_3355320?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
*__inference_dense_31_layer_call_fn_3355329?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
E__inference_dense_32_layer_call_and_return_conditional_losses_3355340?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
*__inference_dense_32_layer_call_fn_3355349?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
E__inference_dense_33_layer_call_and_return_conditional_losses_3355360?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
*__inference_dense_33_layer_call_fn_3355369?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
E__inference_dense_34_layer_call_and_return_conditional_losses_3355380?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?2?
*__inference_dense_34_layer_call_fn_3355389?
???
FullArgSpec
args?
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 
?B?
%__inference_signature_wrapper_3355102embedding_6_input"?
???
FullArgSpec
args? 
varargs
 
varkwjkwargs
defaults
 

kwonlyargs? 
kwonlydefaults
 
annotations? *
 ?
"__inference__wrapped_model_3354718~#$)*/0:?7
0?-
+?(
embedding_6_input?????????
? "3?0
.
dense_34"?
dense_34??????????
E__inference_dense_30_layer_call_and_return_conditional_losses_3355300\/?,
%?"
 ?
inputs????????? 
? "%?"
?
0?????????
? }
*__inference_dense_30_layer_call_fn_3355309O/?,
%?"
 ?
inputs????????? 
? "???????????
E__inference_dense_31_layer_call_and_return_conditional_losses_3355320\/?,
%?"
 ?
inputs?????????
? "%?"
?
0????????? 
? }
*__inference_dense_31_layer_call_fn_3355329O/?,
%?"
 ?
inputs?????????
? "?????????? ?
E__inference_dense_32_layer_call_and_return_conditional_losses_3355340\#$/?,
%?"
 ?
inputs????????? 
? "%?"
?
0?????????@
? }
*__inference_dense_32_layer_call_fn_3355349O#$/?,
%?"
 ?
inputs????????? 
? "??????????@?
E__inference_dense_33_layer_call_and_return_conditional_losses_3355360\)*/?,
%?"
 ?
inputs?????????@
? "%?"
?
0?????????
? }
*__inference_dense_33_layer_call_fn_3355369O)*/?,
%?"
 ?
inputs?????????@
? "???????????
E__inference_dense_34_layer_call_and_return_conditional_losses_3355380\/0/?,
%?"
 ?
inputs?????????
? "%?"
?
0?????????
? }
*__inference_dense_34_layer_call_fn_3355389O/0/?,
%?"
 ?
inputs?????????
? "???????????
H__inference_embedding_6_layer_call_and_return_conditional_losses_3355260_/?,
%?"
 ?
inputs?????????
? ")?&
?
0????????? 
? ?
-__inference_embedding_6_layer_call_fn_3355267R/?,
%?"
 ?
inputs?????????
? "?????????? ?
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_3355273{I?F
??<
6?3
inputs'???????????????????????????

 
? ".?+
$?!
0??????????????????
? ?
W__inference_global_average_pooling1d_6_layer_call_and_return_conditional_losses_3355284`7?4
-?*
$?!
inputs????????? 

 
? "%?"
?
0????????? 
? ?
<__inference_global_average_pooling1d_6_layer_call_fn_3355278nI?F
??<
6?3
inputs'???????????????????????????

 
? "!????????????????????
<__inference_global_average_pooling1d_6_layer_call_fn_3355289S7?4
-?*
$?!
inputs????????? 

 
? "?????????? ?
I__inference_sequential_6_layer_call_and_return_conditional_losses_3354911x#$)*/0B??
8?5
+?(
embedding_6_input?????????
p

 
? "%?"
?
0?????????
? ?
I__inference_sequential_6_layer_call_and_return_conditional_losses_3354944x#$)*/0B??
8?5
+?(
embedding_6_input?????????
p 

 
? "%?"
?
0?????????
? ?
I__inference_sequential_6_layer_call_and_return_conditional_losses_3355149m#$)*/07?4
-?*
 ?
inputs?????????
p

 
? "%?"
?
0?????????
? ?
I__inference_sequential_6_layer_call_and_return_conditional_losses_3355196m#$)*/07?4
-?*
 ?
inputs?????????
p 

 
? "%?"
?
0?????????
? ?
.__inference_sequential_6_layer_call_fn_3355005k#$)*/0B??
8?5
+?(
embedding_6_input?????????
p

 
? "???????????
.__inference_sequential_6_layer_call_fn_3355065k#$)*/0B??
8?5
+?(
embedding_6_input?????????
p 

 
? "???????????
.__inference_sequential_6_layer_call_fn_3355223`#$)*/07?4
-?*
 ?
inputs?????????
p

 
? "???????????
.__inference_sequential_6_layer_call_fn_3355250`#$)*/07?4
-?*
 ?
inputs?????????
p 

 
? "???????????
%__inference_signature_wrapper_3355102?#$)*/0O?L
? 
E?B
@
embedding_6_input+?(
embedding_6_input?????????"3?0
.
dense_34"?
dense_34?????????