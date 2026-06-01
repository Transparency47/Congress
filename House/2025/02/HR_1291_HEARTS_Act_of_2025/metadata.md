# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1291?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1291
- Title: HEARTS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1291
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-01-14T09:06:47Z
- Update date including text: 2026-01-14T09:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1291",
    "number": "1291",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C000059",
        "district": "41",
        "firstName": "Ken",
        "fullName": "Rep. Calvert, Ken [R-CA-41]",
        "lastName": "Calvert",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "HEARTS Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-14T09:06:47Z",
    "updateDateIncludingText": "2026-01-14T09:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-02-13T14:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NH"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MI"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "MI"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "HI"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CT"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "NJ"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NV"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "VA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "NV"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "PA"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "FL"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NC"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1291ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1291\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Calvert (for himself, Mr. Pappas , Ms. Malliotakis , Ms. Scholten , Mr. Goldman of New York , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to ensure that nonanimal methods are prioritized, where applicable and feasible, in proposals for all research to be conducted or supported by the National Institutes of Health, to provide for the establishment of the National Center for Alternatives to Animals in Research and Testing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Humane and Existing Alternatives in Research and Testing Sciences Act of 2025 or the HEARTS Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe National Institutes of Health (NIH) has supported life-saving research that has greatly improved the health and well-being not only of Americans but also of people around the world.\n**(2)**\nMuch of this research has relied on animals. It is estimated that between 17,000,000 and 100,000,000 animals are used annually in the United States in research, education, and testing. However, the precise number of animals used in research in the United States is unknown. Such imprecise numbers make it impossible to effectively track and reduce the numbers of animals used.\n**(3)**\nAccording to the NIH, approximately 30 percent of promising medications have failed in human clinical trials because they are found to be toxic despite promising pre-clinical studies in animal models. About 60 percent of candidate drugs fail due to lack of efficacy. . These statistics indicate that new, human-focused biology is needed.\n**(4)**\nThe laboratory use of animals has also long been a matter of public concern because, among other things, there is very little publicly available data provided by the NIH about the number and species of animals used in research.\n**(5)**\nEffective alternatives to animals are becoming available, and their number is growing. Cutting-edge technologies have forged new frontiers in toxicology, biology, and medicine that have produced human-relevant models, including organoid cell cultures, multiphysiological systems, genomics, induced pluripotent adult stem cells, 3D modeling with human cells, molecular imaging, computer models, in silico trials, digital imaging, artificial intelligence, and other innovative methods, all of which have launched a technological revolution in biomedical research.\n**(6)**\nThe Animal Welfare Act ( Public Law 89\u2013544 ) requires researchers to consider alternatives to animal use for painful procedures and stresses that researchers should not unnecessarily duplicate previous experiments. However, oversight is lacking, and these provisions are not implemented the way that Congress intended. As a result, researchers are not capitalizing on nonanimal models that might more effectively recapitulate human biology.\n**(7)**\nA system of active incentives is needed to encourage researchers to develop and utilize humane, cost-effective, and scientifically suitable nonanimal methods based on human biology.\n**(8)**\nFurther, under the National Institutes of Health Revitalization Act of 1993 ( Public Law 103\u201343 ), the NIH is supposed to outline a plan for reducing the use of animals in research. Section 404C(a)(1) of the Public Health Service Act ( 42 U.S.C. 283e(a)(1) ), as added by section 205 of the National Institutes of Health Revitalization Act of 1993, calls for the NIH to conduct or support research into\u2026 methods of biomedical research and experimentation that do not require the use of animals [and] methods of such research and experimentation that reduce the number of animals used in such research .\n**(9)**\nA dedicated center that provides resources, funding, and training to encourage researchers to utilize humane, cost-effective, and scientifically suitable nonanimal methods based on human biology will result in more progress toward understanding human diseases and their treatments and cures. It will complete the vision that Congress set out in the National Institutes of Health Revitalization Act of 1993 ( Public Law 103\u201343 ), which has been thwarted because of lack of oversight.\n#### 3. Animals in research\nSection 495 of the Public Health Service Act ( 42 U.S.C. 289d ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking paragraph and inserting subparagraph ; and\n**(ii)**\nby redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and moving the margins of such clauses (as so redesignated) two ems to the right;\n**(B)**\nby redesignating paragraphs (1), (2) (as so amended), and (3) as subparagraphs (A), (B), and (C), respectively, and moving the margins of such subparagraphs (as so redesignated) two ems to the right;\n**(C)**\nin the matter preceding subparagraph (A) (as so redesignated), by striking establish guidelines for the following: and inserting the following:\n, with respect to all research conducted or supported by the National Institutes of Health, do the following: (1) Establish and maintain animal care guidelines for the following: ; and\n**(D)**\nby adding at the end the following:\n(2) Establish a system of meaningful incentives to encourage the use of existing humane and scientifically satisfactory nonanimal methods in research proposals. (3) Ensure that, before any research involving the use of animals is approved or performed, all scientifically satisfactory nonanimal methods for obtaining the results sought have been fully evaluated. (4) Ensure that\u2014 (A) research proposals are reviewed by at least one person who has expertise in nonanimal research methods; and (B) reviewers of the research proposals have access to a reference librarian with expertise in evaluating the adequacy of the searches for nonanimal methods described in the research proposals. (5) Establish and maintain research proposal guidelines for conducting thorough searches for nonanimal alternatives to the use of animals for biomedical and behavioral research. ;\n**(2)**\nin subsection (b)(1), by striking subsection (a)(3) and inserting subsection (a)(1)(C) ; and\n**(3)**\nin subsection (c)(1)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking paragraphs (1) and (2) of ; and\n**(ii)**\nby striking and at the end; and\n**(B)**\nby adding at the end the following:\n(C) a statement of assurance that a scientifically satisfactory nonanimal method of obtaining the result sought is not available; and .\n#### 4. National Center for Alternatives to Animals in Research and Testing\n##### (a) Addition to list of institutes and centers\nSection 401(b) of the Public Health Service Act ( 42 U.S.C. 281(b) ) is amended\u2014\n**(1)**\nby redesignating paragraph (25) as paragraph (26); and\n**(2)**\nby inserting after paragraph (24) the following new paragraph:\n(25) The National Center for Alternatives to Animals in Research and Testing. .\n##### (b) Conforming change to number of institutes and centers\nSection 401(d)(1) of the Public Health Service Act ( 42 U.S.C. 281(d)(1) ) is amended by striking 27 and inserting 28 .\n##### (c) Establishment; duties\nPart E of title IV of the Public Health Service Act ( 42 U.S.C. 287 et seq. ) is amended by inserting after subpart 5 of such part E ( 42 U.S.C. 287c\u201321 ) the following new subpart:\n6 National Center for Alternatives to Animals in Research and Testing 485E. Establishment; duties (a) Establishment Not later than one year after the date of enactment of the Humane and Existing Alternatives in Research and Testing Sciences Act of 2025 , the Secretary shall establish a National Center for Alternatives to Animals in Research and Testing (in this subpart referred to as the National Center ) within the National Institutes of Health. The Center shall be headed by a director, who shall be appointed by the Secretary. (b) Purpose The general purpose of the National Center shall be\u2014 (1) developing, promoting, and funding alternatives to animal research and testing; and (2) developing a plan for reducing the number of animals used in federally funded research and testing. (c) Duties The Director of the National Center shall\u2014 (1) provide assistance (including funding) to federally funded researchers to incentivize the development and qualification of nonanimal methods, such as advanced cell cultures or technology such as 3D organoids, microphysiological systems, induced pluripotent adult stem cell models, in silico modeling, advanced imaging systems, artificial intelligence, and other innovative methods; (2) train and inform scientists about the methods developed pursuant to paragraph (1); (3) establish collaborations among research institutions so that scientists who lack resources (such as bioengineering and advanced bio-imaging equipment) can develop and use methods developed pursuant to paragraph (1); and (4) collect information regarding the numbers of animals used in federally funded research and testing, and make such information available to the public in a timely manner. .\n#### 5. Reporting by federally funded research entities on numbers of animals used in research and testing\n##### (a) In general\nEach covered reporting entity shall do the following:\n**(1)**\nNot later than 2 years after the date of enactment of this Act, report to the National Center for Alternatives to Animals in Research and Testing and make publicly available\u2014\n**(A)**\nthe number of animals used by the covered reporting entity in federally funded research and testing at facilities of the covered reporting entity, disaggregated by species; and\n**(B)**\nthe total number of such animals that were bred or acquired by the covered reporting entity for research or testing purposes, disaggregated by species.\n**(2)**\nEvery 2 years thereafter\u2014\n**(A)**\nupdate the latest report of the covered reporting entity under this section and make publicly available such updated report to measure the progress of the covered reporting entity in reducing the number of animals used in federally funded research and testing; and\n**(B)**\ndevelop and submit to the National Center for Alternatives to Animals in Research and Testing and make publicly available a plan for reducing the numbers described in subparagraphs (A) and (B) of paragraph (1).\n##### (b) Standardized process\nThe Director of the National Center for Alternatives to Animals in Research and Testing shall establish a standardized process for submitting and updating reports and plans under subsection (a), including for making such reports and plans publicly available.\n##### (c) Definition\nIn this section:\n**(1) Animal**\nThe term animal means any live, nonhuman vertebrate animal or cephalopod used or intended for use in research, research training, experimentation, or biological testing, or for related purposes.\n**(2) Covered reporting entity**\nThe term covered reporting entity means\u2014\n**(A)**\nany entity that\u2014\n**(i)**\nreceives Federal funds for research or testing; and\n**(ii)**\nuses animals in research and testing; and\n**(B)**\nany Federal department or agency that uses animals in research or testing.",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2025-07-08T12:32:12Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-07-08T12:32:06Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-08T12:32:25Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-07-08T12:32:02Z"
          },
          {
            "name": "National Institutes of Health (NIH)",
            "updateDate": "2025-07-08T12:31:58Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2025-07-08T12:32:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-14T12:50:18Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1291ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "HEARTS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEARTS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Humane and Existing Alternatives in Research and Testing Sciences Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to ensure that nonanimal methods are prioritized, where applicable and feasible, in proposals for all research to be conducted or supported by the National Institutes of Health, to provide for the establishment of the National Center for Alternatives to Animals in Research and Testing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:20:34Z"
    }
  ]
}
```
