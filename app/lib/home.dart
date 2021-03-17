import 'package:flutter/material.dart';
import 'package:osint/model/navDrawer.dart';
import 'package:osint/services/sharedPreferences.dart';

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  String _name;
  String searchQuery;
  void fun() async {
    String name = await SharedFunctions.getUserName();
    setState(() {
      _name = name;
    });
    print(_name);
  }

  @override
  void initState() {
    super.initState();
    fun();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Side menu'),
      ),
      drawer: NavDrawer(),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text(
              'Welcome back $_name!',
            ),
            SizedBox(
              height: 30,
            ),
            Text('Add your search query below:'),
            SizedBox(
              height: 10,
            ),
            TextField(
              onChanged: (value) {
                setState(() {
                  searchQuery = value;
                });
              },
            )
          ],
        ),
      ),
    );
  }
}
