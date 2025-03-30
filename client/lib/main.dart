import 'package:flutter/material.dart';
import 'package:spotify_clone/core/theme/theme.dart';
import 'package:spotify_clone/features/auth/view/login_page.dart';
import 'package:spotify_clone/features/auth/view/singup_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Spotify Clone',
      theme: AppTheme.darkThemeMode,
      home: const LoginPage(),
    );
  }
}
