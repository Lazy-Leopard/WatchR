import 'package:firebase_auth/firebase_auth.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:osint/home.dart';
import 'package:osint/authentication/login.dart';
import 'package:osint/services/sharedPreferences.dart';

class Root extends StatefulWidget {
  @override
  _RootState createState() => _RootState();
}

class _RootState extends State<Root> {
  bool signedIn = false;
  Future<void> checkStatus() async {
    String uid = await SharedFunctions.getUserUid();
    if (uid != null)
      signedIn = true;
    else
      signedIn = false;
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    checkStatus();
  }

  @override
  Widget build(BuildContext context) {
    if (signedIn) {
      return Home();
    } else {
      return Login();
    }
  }
}
