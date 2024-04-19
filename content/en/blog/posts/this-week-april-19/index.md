---
date: 2024-04-19
title: This Week on Minimal 3DP (April 19)
linkTitle: Minimal 3DP April 19
description: >
  I am getting ready to start a new project this week. I am building a Voron 2.4 Pro+
author: Mike Wilson (minimal3dp@gmail.com)
resources:
  - src: "**.{png,jpg}"
    title: "Image #:counter"
    params:
      byline: "Photo: "
draft: true
categories: [This Week]
tags: [voron]
---

{{< imgproc sunset Fill "600x300" >}}
Fetch and scale an image in the upcoming Hugo 0.43.
{{< /imgproc >}}

# Finally!

The front matter of this post specifies properties to be assigned to all image resources:

To include the image in a page, specify its details like this:

```
{{< imgproc sunset Fill "600x300" >}}
Fetch and scale an image in the upcoming Hugo 0.43.
{{< /imgproc >}}
```

The image will be rendered at the size and byline specified in the front matter.
