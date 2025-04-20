;; Auto-generated. Do not edit!


(when (boundp 'cartographer_ros::pair)
  (if (not (find-package "CARTOGRAPHER_ROS"))
    (make-package "CARTOGRAPHER_ROS"))
  (shadow 'pair (find-package "CARTOGRAPHER_ROS")))
(unless (find-package "CARTOGRAPHER_ROS::PAIR")
  (make-package "CARTOGRAPHER_ROS::PAIR"))

(in-package "ROS")
;;//! \htmlinclude pair.msg.html


(defclass cartographer_ros::pair
  :super ros::object
  :slots (_x_avg _width ))

(defmethod cartographer_ros::pair
  (:init
   (&key
    ((:x_avg __x_avg) 0)
    ((:width __width) 0)
    )
   (send-super :init)
   (setq _x_avg (round __x_avg))
   (setq _width (round __width))
   self)
  (:x_avg
   (&optional __x_avg)
   (if __x_avg (setq _x_avg __x_avg)) _x_avg)
  (:width
   (&optional __width)
   (if __width (setq _width __width)) _width)
  (:serialization-length
   ()
   (+
    ;; int64 _x_avg
    8
    ;; int64 _width
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _x_avg
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _x_avg (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _x_avg) (= (length (_x_avg . bv)) 2)) ;; bignum
              (write-long (ash (elt (_x_avg . bv) 0) 0) s)
              (write-long (ash (elt (_x_avg . bv) 1) -1) s))
             ((and (class _x_avg) (= (length (_x_avg . bv)) 1)) ;; big1
              (write-long (elt (_x_avg . bv) 0) s)
              (write-long (if (>= _x_avg 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _x_avg s)(write-long (if (>= _x_avg 0) 0 #xffffffff) s)))
     ;; int64 _width
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _width (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _width) (= (length (_width . bv)) 2)) ;; bignum
              (write-long (ash (elt (_width . bv) 0) 0) s)
              (write-long (ash (elt (_width . bv) 1) -1) s))
             ((and (class _width) (= (length (_width . bv)) 1)) ;; big1
              (write-long (elt (_width . bv) 0) s)
              (write-long (if (>= _width 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _width s)(write-long (if (>= _width 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _x_avg
#+(or :alpha :irix6 :x86_64)
      (setf _x_avg (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _x_avg (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _width
#+(or :alpha :irix6 :x86_64)
      (setf _width (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _width (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(setf (get cartographer_ros::pair :md5sum-) "e422f6ba709537d0cc32d10fc4426744")
(setf (get cartographer_ros::pair :datatype-) "cartographer_ros/pair")
(setf (get cartographer_ros::pair :definition-)
      "int64 x_avg
int64 width
")



(provide :cartographer_ros/pair "e422f6ba709537d0cc32d10fc4426744")


