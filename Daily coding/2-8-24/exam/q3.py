import tensorflow as tf
from tensorflow.keras.losses import Loss

class CustomLoss(Loss):
    def __init__(self, alpha=0.1, **kwargs):
        super().__init__(**kwargs)
        self.alpha = alpha  # Regularization strength

    def call(self, y_true, y_pred):
        # Mean Squared Error
        mse = tf.reduce_mean(tf.square(y_true - y_pred))
        
        # Regularization Term: Penalizes predictions deviating from the mean of y_true
        y_true_mean = tf.reduce_mean(y_true)
        regularization_term = tf.reduce_mean(tf.square(y_pred - y_true_mean))
        
        # Combine MSE with the regularization term
        loss = mse + self.alpha * regularization_term
        return loss

# Example Usage
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss=CustomLoss(alpha=0.5))
