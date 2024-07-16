
import 'package:flutter/material.dart';

class SilhouetteImage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Image.asset(
        'assets/images/silhouette.png',
        width: 100.0,
        height: 100.0,
      ),
    );
  }
}
