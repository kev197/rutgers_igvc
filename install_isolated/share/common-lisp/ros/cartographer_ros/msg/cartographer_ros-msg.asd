
(cl:in-package :asdf)

(defsystem "cartographer_ros-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "pair" :depends-on ("_package_pair"))
    (:file "_package_pair" :depends-on ("_package"))
  ))