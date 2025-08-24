---
date: 2025-08-24
title: OrcaSlicer 2.3.1 Alpha Just Dropped & How to Use the New Flow Rate Calibration
linkTitle: orcaslicer-2.3.1-alpha-flow-test
description: >
  This guide provides a deep dive into the new Archimedean flow calibration feature in OrcaSlicer 2.3.1 Alpha, which replaces subjective guesswork with a visually precise test. Follow our step-by-step instructions to interpret the results and perfectly dial in your filament's flow rate for higher quality 3D prints.
author: Mike Wilson (minimal3dp@gmail.com)
resources:
  - src: "**.{png,jpg}"
    title: "OrcaSlicer 2.3.1 Alpha"
    params:
      byline: "Photo: Mike Wilson"
draft: false
---
## Mastering Extrusion: A Deep Dive into OrcaSlicer’s New Archimedean Flow Calibration

### From Subjective Guesswork to Visual Precision: A Step-by-Step Guide to Perfecting Your Flow Rate with the OrcaSlicer 2.3.1 Alpha Feature

## The Next Evolution in Slicing: Introducing OrcaSlicer 2.3.1 Alpha

### The Relentless Pursuit of Perfection

If you're like me, you're constantly on the lookout for the latest and greatest features to elevate your 3D prints from good to flawless.[1] This relentless pursuit of perfection is the lifeblood of the 3D printing community, and it's a spirit embodied by the team behind OrcaSlicer. More than just a piece of software, OrcaSlicer has established itself as a dynamic, open-source project at the vanguard of Fused Deposition Modeling (FDM) technology.[2] It's a slicer built by and for the community, characterized by a rapid development cycle that consistently delivers powerful, cutting-edge tools into our hands.

It is in this spirit of continuous innovation that the developers have released OrcaSlicer version 2.3.1 Alpha.[1] This isn't just a minor update; it's a significant leap forward, offering an exciting glimpse into the future of slicing. This release is packed with enhancements that promise to refine our workflows and improve our print quality in tangible ways.

### A Glimpse of the Future: What's New in Version 2.3.1 Alpha?

The 2.3.1 Alpha release is a treasure trove of new functionalities that address various aspects of the printing process. While this guide will focus on one revolutionary feature, it's worth taking a moment to appreciate the breadth of improvements included in this update.[1] The key additions are:

* A new sparse infill rotation system for stronger, more efficient internal structures.
* Substantial changes and improvements to the fuzzy skin feature, offering more creative control over surface textures.
* Integrated input shaping calibration for printers running Klipper firmware.
* A new junction deviation calibration test for users with Marlin-based machines.
* And, the focus of our deep dive today, a completely redesigned and more intuitive method for flow rate calibration.[1]

Each of these features deserves its own detailed exploration, and I plan to cover them in future articles and videos. However, the new flow calibration method represents such a fundamental shift in approach and offers such a significant improvement in accuracy and ease of use that it warrants a dedicated, comprehensive guide. My goal here is to provide a focused, exhaustive walkthrough that will empower you to master this new tool immediately, without wasting your time.[1]

### Multimedia Integration: Watch the Guide in Action

For those who prefer a visual demonstration, I have created a complete video walkthrough that complements this written guide. You can watch it to see the entire process in action, from launching the test in OrcaSlicer to analyzing the physical prints.

<iframe width="560" height="315" src="https://www.youtube.com/embed/afuKB8T133s?si=2DOHzn_8XdObTpyZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### The Philosophy of Alpha Releases in Open Source

Before we dive into the technical details, it's important to understand the context of an "Alpha" release. In the world of open-source software, an alpha version is far more than just an early, potentially unstable preview. It represents a philosophical choice that lies at the heart of community-driven development.[2] Unlike the closed, internal testing of proprietary software, a public alpha is a transparent invitation for the most engaged users to become active participants in the development process.

The OrcaSlicer project thrives on this collaborative model, offering not just stable releases but also "Nightly Builds" for those who want to test the absolute latest code.[2] When you download and use OrcaSlicer 2.3.1 Alpha, you are not merely a consumer; you are a collaborator. The feedback you provide, particularly through well-documented bug reports, is invaluable data that helps the developers refine, debug, and perfect these new features before they are rolled into a stable release.[1] This guide will not only show you how to use the new flow calibration but also how to responsibly contribute back to the project that provides these powerful tools for free.

## From Subjective Feel to Objective Data: A Paradigm Shift in Flow Calibration

### The Old Way: Limitations of the Diagonal Surface Test

To fully appreciate the brilliance of the new flow calibration method, we must first understand the limitations of the one it replaces. For a long time, flow rate calibration in OrcaSlicer (and many other slicers) involved printing a series of square patches, each with a different flow modifier.[4, 5] The top surface of these squares was printed with a simple diagonal line pattern, moving back and forth at a 45-degree angle.[1]

The process for determining the correct flow rate was almost entirely subjective. The official instruction was to run your fingers across the printed squares and select the one that felt the smoothest to the touch.[1] While this method can work, its effectiveness is heavily dependent on the user's experience and tactile sensitivity. A beginner might struggle to discern the subtle differences between patches, while even an expert's judgment could be influenced by lighting or the specific texture of the filament. This subjectivity was the primary weakness of the old system, creating a barrier to achieving consistent, repeatable results.

### Introducing the Archimedean Chord: A Smarter Pattern for a Smarter Slicer

The 2.3.1 Alpha release replaces the ambiguous diagonal pattern with a far more intelligent design: a concentric pattern based on an Archimedean chord.[1] This isn't just a cosmetic change; it's a fundamental re-engineering of the test based on geometric principles.

An Archimedean spiral is a shape defined by a path that moves away from a central point at a constant angular velocity. In simpler terms, the distance between each successive turn of the spiral remains constant. When the toolhead of a 3D printer traces this path, it should lay down a series of perfectly concentric lines with a uniform gap between them. This geometric purity is the key to the test's effectiveness. Any deviation from the ideal amount of extruded filament—either too much or too little—will immediately disrupt this perfect, repeating pattern in a way that is visually and tactically obvious.

Unlike the old diagonal pattern, where over-extrusion might simply result in a slightly rougher surface, the Archimedean pattern provides clear, unmistakable evidence. This new test, as highlighted in the updated OrcaSlicer wiki, is now the recommended method for dialing in your flow rate.[1]

### The Democratization of Precision

This evolution from a tactile, experience-based method to a visually explicit one represents more than just a technical upgrade; it's a move that democratizes precision in 3D printing. It effectively lowers the barrier to entry for achieving one of the most critical calibrations, empowering users of all skill levels to diagnose and resolve extrusion issues with a newfound level of confidence.

The old method relied on an acquired skill—a developed "feel" for surface smoothness that created a knowledge gap between newcomers and seasoned veterans.[1] The new test replaces this subjectivity with objective, observable data. Over-extrusion presents itself as distinct ridges where "the edge of the circle is really sticking out," while under-extrusion creates clear "valleys" or gaps between the lines.[1] These are not matters of opinion; they are measurable physical artifacts.

This aligns perfectly with OrcaSlicer's overarching mission: to package "advanced calibration tools" within a "user-friendly interface" that supports a "wide printer compatibility".[2] By making a foundational calibration process like flow rate easier to perform and more reliable to interpret, the software empowers a much broader range of users to achieve superior print quality. It removes the gatekeeper of subjective "feel" and replaces it with the clarity of visual evidence. This new feature is a perfect encapsulation of the project's philosophy: it doesn't just add power for experts; it engineers that power in a way that elevates the entire community.

## A Practical Guide: Dialing in Your Flow Rate with the New Test

### Prerequisites and Setup

Before you jump into printing the new calibration test, a little preparation will ensure you get the most accurate results possible.

First, this test is designed to refine an existing flow rate, not to establish one from absolute zero. It is most effective when you start with a filament profile that is already reasonably well-configured. The calibration test works by applying small positive and negative modifiers to your filament's *current* flow ratio setting. As the transcript notes, "it doesn't reset it back to one. It's based on what it's currently set at".[1] So, if your filament profile's flow ratio is already set to 0.98, the test chips will be modifiers based on that value.

Second, for the most scientifically accurate calibration, it's crucial to follow the recommended order of operations. According to the official OrcaSlicer wiki, you should always calibrate temperature *before* calibrating flow rate.[4] The temperature of your nozzle directly affects the viscosity of the filament, which in turn impacts how it flows. Dialing in your temperature first ensures that you are calibrating flow under the correct thermal conditions.

### Step 1: Launching the Calibration Test

With your slicer open and your printer profile selected, launching the new test is straightforward.

1. Navigate to the top menu bar.
2. Click on the "Calibration" dropdown.
3. Select "Flow Rate." A new test plate will be automatically generated in your workspace.

You will see a series of small, square chips laid out on the build plate. Each chip is labeled with a modifier value, such as `0`, `-0.01`, `+0.01`, etc. This is the new, recommended test that utilizes the Archimedean pattern.[1]

### Step 2: Printing and Initial Observation

Once the test plate is generated, simply slice it using the filament profile you wish to calibrate and send it to your printer. While it's printing, prepare a well-lit area for inspection. Good lighting is critical for visually identifying the subtle surface differences between the test chips.

### Step 3: Interpreting the Print – The Art of Sight and Touch

This is the most critical part of the process. Once the print is finished and has cooled, carefully remove it from the build plate. You will now analyze each chip, using both your eyes and your fingertips, to find the one that represents the "Goldilocks" zone of perfect extrusion.

#### Identifying Over-extrusion

Over-extrusion occurs when the printer pushes out too much filament. On the Archimedean pattern, this is incredibly easy to spot.

* **Visual Cues:** Look for concentric circles where the edges are raised and pronounced. As the transcript describes, "the edge of the circle is really sticking out".[1] This happens because the excess plastic has nowhere to go and is forced upwards, creating distinct ridges. The surface may look overly glossy and lose fine detail.
* **Tactile Cues:** When you run your finger across an over-extruded chip, it will feel bumpy and rough. You will be able to clearly feel the ridges formed by the excess filament. The chips with positive modifiers (e.g., `+0.03`, `+0.05`) are most likely to exhibit these characteristics.

#### Identifying Under-extrusion

Under-extrusion is the opposite problem: the printer is not pushing out enough filament to fill the toolpath completely.

* **Visual Cues:** Look for visible gaps between the concentric lines. You may be able to see the layer below through these gaps. The transcript refers to these as "valleys" in the surface.[1] The surface might also have a dull, matte, or unfinished appearance because the lines are not properly squishing together.
* **Tactile Cues:** An under-extruded chip will feel textured or even hollow. Your finger will catch on the gaps between the lines, giving it a rough or scratchy feel. The chips with negative modifiers (e.g., `-0.03`, `-0.05`) are the primary candidates for this issue.

#### The "Goldilocks" Zone – Identifying the Optimal Result

Your goal is to find the single chip that is perfectly smooth, both visually and by feel.[1]

* **The Ideal Chip:** The best chip will have a uniform, smooth top surface with a consistent, healthy shine.[1] The concentric lines should be laid down perfectly next to each other with very little to no visible gaps. When you run your finger across it, it should feel almost like a single, solid surface. In my own testing for the video, the chip labeled `0` was the best, indicating my existing flow rate was already well-calibrated.[1]
* **An Important Nuance:** It is crucial to understand one key detail from the official documentation: "it is okay to have a visible line between the inner and outer spiral".[1] The goal is not to create a completely fused, monolithic surface where the lines are indistinguishable. The perfect result is one that shows distinct lines laid down with "very little gap between" them.[1] Do not mistake the faint line between toolpaths for under-extrusion. You are looking for the smoothest possible surface that is free of ridges (over-extrusion) and significant valleys (under-extrusion).

### Step 4: Applying the Results and Updating Your Profile

Once you have identified the best chip, updating your filament profile is incredibly simple. The value printed on the chip is the exact modifier you need to apply to your current flow ratio.

The logic is simple addition or subtraction:

* If you picked a chip with a **positive** value (e.g., `+0.02`), you **add** that value to your current flow ratio.
* If you picked a chip with a **negative** value (e.g., `-0.03`), you **subtract** that value from your current flow ratio.
* If you picked the `0` chip, no changes are needed.

Let's use the concrete example from the transcript: imagine your filament's flow ratio was set to `0.98` and you determined that the chip labeled `+0.01` was the smoothest. Your new flow ratio would be $0.98 + 0.01 = 0.99$.[1] This direct arithmetic is a significant improvement in user experience over older, more complex percentage-based formulas.[4, 5]

To make the change in OrcaSlicer:

1. Go to the "Filament" tab in the left-hand panel.
2. Click the "Edit preset" icon next to your chosen filament profile.
3. In the filament settings window, scroll down until you find the "Flow Ratio" parameter.
4. Enter your newly calculated value.
5. **Crucially, click the "Save" icon at the top of the window to save your changes to the profile.** Forgetting this last step is a common mistake that will cause you to lose your newly calibrated value.

## The Enabler's Guide: Responsible Use of Alpha Software

### You Are Now Part of the Development Team

Choosing to use alpha software is choosing to step onto the front lines of development. It's a decision that reframes your role from a passive user to an active tester and contributor. Every print you run, every setting you tweak, provides real-world data that is impossible to replicate in a controlled lab environment. By engaging with these new features early, you are providing an invaluable service to the developers and the entire OrcaSlicer community. You are helping to forge the tools that everyone will be using in the next stable release.

### How to Submit an Effective Bug Report: A Checklist

Finding a bug in alpha software is not a failure; it's a success. It's an opportunity to contribute directly to the project's improvement. However, the usefulness of your discovery depends entirely on the quality of your bug report. A vague or incomplete report is often unusable. To help you make the most impactful contributions, here is a checklist for submitting an effective bug report on the OrcaSlicer GitHub page, based directly on best practices.[1]

| Step | Action | Why It's Important |
|------|--------|-------------------|
| 1 | **Search First** | Go to the OrcaSlicer GitHub "Issues" page and search to see if your bug has already been reported. | This prevents creating duplicate reports, which saves developers valuable time. You might also find an existing thread with a workaround or solution.[1] |
| 2 | **Provide Context** | State the exact OrcaSlicer version (e.g., 2.3.1 Alpha), your Operating System (e.g., Windows 11, macOS Sonoma), and OS version. | This helps developers immediately isolate whether the problem is specific to a certain platform, version, or environment.[1] |
| 3 | **Document Steps** | Write a clear, numbered list of the exact steps required to reproduce the error. Be as specific as possible. | This is the single most critical part of any bug report. If the developers cannot reliably reproduce the bug, they have almost no chance of fixing it.[1] |
| 4 | **Include Your Setup** | Mention the specific 3D printer profile you are using (e.g., Voron 2.4, Bambu Lab X1C, Creality Ender 3). | The bug could be unique to a certain printer's configuration, G-code flavor, or start/end scripts.[1] |
| 5 | **Add Visuals & Logs** | Attach screenshots that clearly show the issue. If the slicer crashes, include the debug log file it generates. | Visual evidence is powerful and provides immense clarity. Log files contain detailed technical information that can point developers directly to the source of the crash.[1] |

### The Power of Community Feedback

A well-structured bug report is one of the most powerful contributions a user can make to an open-source project. It transforms a moment of frustration into a constructive step toward a more robust and reliable piece of software for everyone. Despite its "Alpha" status, my own experience with version 2.3.1 has been that it "seems rock solid," a testament to the quality of the developers' work and likely the result of excellent community feedback during the nightly build phase.[1]

## Conclusion, Community, and Further Resources

### Summary: A Step Forward for Precision

The introduction of the Archimedean chord flow calibration in OrcaSlicer 2.3.1 Alpha is a definitive step forward for precision 3D printing. By replacing a subjective, tactile test with a visually objective and geometrically intelligent one, OrcaSlicer has made a critical calibration process more accessible, repeatable, and accurate for users of all experience levels. It is a smarter test for a smarter slicer, and a perfect example of the thoughtful innovation that defines the project.

### Join the Conversation: A Call to Action

Your experience and feedback are what make the 3D printing community thrive. Now that you've learned about this new feature, I encourage you to join the conversation.

* Have you tried the new flow test? What were your results? Is there another new feature in the 2.3.1 Alpha release that you feel I should highlight in a future guide? As I always say, "just leave me a comment and I'll get back to you as soon as I can".[1]
* If you found this guide valuable, please consider giving it a few 'claps' here on Medium. This is a simple, free way to show your support, and it helps the platform's algorithm show this article to more people who might benefit from it.
* For more deep dives, tutorials, and the latest updates in 3D printing and OrcaSlicer, be sure to subscribe to my YouTube channel and follow me here on Medium.[1]

### The OrcaSlicer Ecosystem: References and Further Reading

To continue your journey and become more involved with the OrcaSlicer project, here are the essential official resources. I strongly recommend bookmarking these to ensure you are always getting information from the primary source.

* **Official OrcaSlicer GitHub Repository:** This is the home of the project. Here you can download the latest stable and alpha releases, read the full release notes, and report bugs.[2]
* **Official OrcaSlicer Wiki:** An invaluable resource for detailed documentation on all of OrcaSlicer's features, including the main Calibration page which provides a broader overview of the entire tuning process.[4]
* **Official OrcaSlicer Discord Server:** The best place to engage with the community in real-time, ask questions, and get support from fellow users and the developers themselves.[2]

Finally, I want to extend a heartfelt thank you to all of my subscribers and members. Your support is what makes it possible for me to create in-depth content like this guide. Thank you for being a part of this community.[1]

[1]: https://www.youtube.com/watch?v=afuKB8T133s
[2]: https://github.com/OrcaSlicer/OrcaSlicer
[3]: https://github.com/SoftFever/OrcaSlicer#main-features
[4]: https://github.com/OrcaSlicer/OrcaSlicer/wiki/Calibration
