import tensorflow as tf

with tf.Session() as sess:
    sess.run(init)

    for epoch in range(n_epochs):
        if epoch % 100 == 0:
            print("에포크", epoch, "MSE = ", mse.eval())
            save_path = sevaer.save(sess, "./tmp/my_model.ckpt")
        sess.run(training_op)

    best_theta = theta.eval()
    save_path = saver.save(sess, "./tmp/my_model_final.ckpt")