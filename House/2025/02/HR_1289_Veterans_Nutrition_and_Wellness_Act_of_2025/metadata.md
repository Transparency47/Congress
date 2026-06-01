# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1289?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1289
- Title: Veterans Nutrition and Wellness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1289
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2025-10-04T08:05:28Z
- Update date including text: 2025-10-04T08:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-14 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-14 - Committee: Referred to the Subcommittee on Health.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1289",
    "number": "1289",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Veterans Nutrition and Wellness Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-04T08:05:28Z",
    "updateDateIncludingText": "2025-10-04T08:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
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
          "date": "2025-02-13T14:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-14T17:52:09Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "WI"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1289ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1289\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Buchanan (for himself and Ms. Moore of Wisconsin ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to establish and carry out a pilot program to administer to eligible veterans medically-tailored meals and groceries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Nutrition and Wellness Act of 2025 .\n#### 2. Department of Veterans Affairs pilot program to administer medically-tailored meals and groceries to certain eligible veterans\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall establish and carry out a pilot program (to be known as the Food is Medicine program ).\n##### (b) Functions\nUnder the Food is Medicine program, the Secretary shall,\n**(1)**\nwith respect to eligible veterans described in subsection (c)\u2014\n**(A)**\nadminister medically-tailored meals and medically-tailored groceries; and\n**(B)**\nfurnish nutrition education and cooking classes through a registered dieticians, nutritionists, and community health workers;\n**(2)**\ndevelop and seek to implement training programs for health care providers employed by the Department of Veterans Affairs with respect to the integration of the Food is Medicine program in the treatment plans of veterans receiving health care under the laws administered by the Secretary; and\n**(3)**\nseek to collaborate with community-based organizations, including food banks and local agriculture programs, to\u2014\n**(A)**\nprocure fresh and locally-sourced produce; and\n**(B)**\nexpand the availability of medically-tailored meals and medically-tailored groceries.\n##### (c) Eligibility\nAn eligible veteran described in this subsection is a veteran (as defined in section 101 of title 38, United States Code) who is enrolled in the system of annual patient enrollment established and operated under section 1705 of such section and\u2014\n**(1)**\nreceives health care furnished by the Department with respect to multiple chronic conditions, including diabetes, cancer, or heart failure; or\n**(2)**\nreceives such health care with respect to maternal health, including prenatal care, labor and delivery care, postpartum care, and is at risk of preeclampsia or gestational diabetes.\n##### (d) Regional balance\nIn carrying out the Food is Medicine program, the Secretary shall, to the maximum extent practicable ensure geographic diversity of the pilot program offices of the Food is Medicine program.\n##### (e) Report\nDuring the period the authority to carry out the Food is Medicine program is effective, the Secretary shall submit to Congress an annual report on such program that includes\u2014\n**(1)**\nthe number of eligible veterans participating in such program;\n**(2)**\nwith respect to such eligible veterans, a summary of\u2014\n**(A)**\nhealth outcomes;\n**(B)**\neffects on physical and mental health;\n**(C)**\nquality of life; and\n**(D)**\nthe extent of utilization of health care under the laws administered by the Secretary;\n**(3)**\nan evaluation of the effectiveness of such program, including estimated cost savings to the Department of Veterans Affairs; and\n**(4)**\nrecommendations of the Secretary with respect to potential improvements to such program.\n##### (f) Authorization of appropriations\n**(1) In general**\nSubject to paragraph (2), there are authorized to be appropriated to the Secretary for fiscal years 2025 through 2028 such sums as may be necessary to carry out the Food is Medicine program.\n**(2) Use of funds**\nAny amounts appropriated pursuant to paragraph (1) shall be used for\u2014\n**(A)**\ndeveloping and operating the Food is Medicine program;\n**(B)**\nhiring registered dieticians and nutrition specialists;\n**(C)**\nconducting research and evaluations; and\n**(D)**\nestablishing partnerships with local organizations pursuant to subsection (b)(3).\n##### (g) Termination date\nThe authority of the Secretary to carry out the Food is Medicine program shall terminate on the date that is three years after the date of the enactment of this Act.\n##### (h) Definitions\nIn this Act:\n**(1)**\nThe term medically-tailored groceries means nutritious food for an individual with a diet-sensitive condition curated to the treatment plan of such individual.\n**(2)**\nThe term medically-tailored meals means nutritious meals customized for an individual with a severe chronic condition or limitation in activities of daily living.",
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
            "name": "Community life and organization",
            "updateDate": "2025-06-13T18:54:20Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-13T18:54:26Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-06-13T18:54:14Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-06-13T18:54:02Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-06-13T18:53:58Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-06-13T18:54:08Z"
          },
          {
            "name": "Nutrition and diet",
            "updateDate": "2025-06-13T18:53:53Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-13T18:53:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T16:36:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1289",
          "measure-number": "1289",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1289v00",
            "update-date": "2025-04-08"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Nutrition and Wellness Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish and implement the Food is Medicine pilot program, under which the VA must provide medically\u00a0tailored meals and groceries, nutrition education, and cooking classes to certain veterans who are enrolled in the VA health care system. Specifically, the program is for veterans enrolled in the VA health care system who receive VA care for (1) multiple chronic conditions, or (2) maternal health and are at risk of\u00a0preeclampsia or gestational diabetes.</p><p>The three-year pilot program also requires the VA to (1) develop and seek to implement training programs for VA health care providers in integrating the program into the treatment plans of veterans, and (2) seek to collaborate with community-based organizations to procure\u00a0locally\u00a0sourced produce and expand the availability of medically\u00a0tailored meals and groceries.</p>"
        },
        "title": "Veterans Nutrition and Wellness Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1289.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Nutrition and Wellness Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish and implement the Food is Medicine pilot program, under which the VA must provide medically\u00a0tailored meals and groceries, nutrition education, and cooking classes to certain veterans who are enrolled in the VA health care system. Specifically, the program is for veterans enrolled in the VA health care system who receive VA care for (1) multiple chronic conditions, or (2) maternal health and are at risk of\u00a0preeclampsia or gestational diabetes.</p><p>The three-year pilot program also requires the VA to (1) develop and seek to implement training programs for VA health care providers in integrating the program into the treatment plans of veterans, and (2) seek to collaborate with community-based organizations to procure\u00a0locally\u00a0sourced produce and expand the availability of medically\u00a0tailored meals and groceries.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr1289"
    },
    "title": "Veterans Nutrition and Wellness Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Nutrition and Wellness Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to establish and implement the Food is Medicine pilot program, under which the VA must provide medically\u00a0tailored meals and groceries, nutrition education, and cooking classes to certain veterans who are enrolled in the VA health care system. Specifically, the program is for veterans enrolled in the VA health care system who receive VA care for (1) multiple chronic conditions, or (2) maternal health and are at risk of\u00a0preeclampsia or gestational diabetes.</p><p>The three-year pilot program also requires the VA to (1) develop and seek to implement training programs for VA health care providers in integrating the program into the treatment plans of veterans, and (2) seek to collaborate with community-based organizations to procure\u00a0locally\u00a0sourced produce and expand the availability of medically\u00a0tailored meals and groceries.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr1289"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1289ih.xml"
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
      "title": "Veterans Nutrition and Wellness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Nutrition and Wellness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to establish and carry out a pilot program to administer to eligible veterans medically-tailored meals and groceries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:20:57Z"
    }
  ]
}
```
