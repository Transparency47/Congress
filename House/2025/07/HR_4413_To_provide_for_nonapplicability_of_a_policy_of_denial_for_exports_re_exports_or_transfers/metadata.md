# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4413?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4413
- Title: End the Cyprus Embargo Act
- Congress: 119
- Bill type: HR
- Bill number: 4413
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2026-05-07T08:05:25Z
- Update date including text: 2026-05-07T08:05:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported by the Yeas and Nays: 47 - 2.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported by the Yeas and Nays: 47 - 2.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4413",
    "number": "4413",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "End the Cyprus Embargo Act",
    "type": "HR",
    "updateDate": "2026-05-07T08:05:25Z",
    "updateDateIncludingText": "2026-05-07T08:05:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 47 - 2.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
        "item": [
          {
            "date": "2025-12-03T16:12:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-15T14:04:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "FL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NV"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "NY"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "NJ"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NJ"
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
      "sponsorshipDate": "2025-08-05",
      "state": "PA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NJ"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NJ"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "NY"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4413ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4413\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Mr. Pappas (for himself, Mr. Bilirakis , Ms. Titus , Ms. Malliotakis , and Mr. Kean ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo provide for nonapplicability of a policy of denial for exports, re-exports, or transfers of defense articles and defense services destined for or originating in the Republic of Cyprus.\n#### 1. Short title\nThis Act may be cited as the End the Cyprus Embargo Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nallowing for the export, re-export, or transfer of arms subject to the United States Munitions List to the Republic of Cyprus would advance United States security interests in Europe by helping to reduce the dependence of the Government of the Republic of Cyprus on other countries, including countries that pose challenges to United States interests around the world, for defense-related materiel;\n**(2)**\nthe Republic of Cyprus has successfully complied with the conditions set forth in the Eastern Mediterranean Security and Energy Partnership Act of 2019 (title X of division J of Public Law 116\u201394 ) for the purposes of modifying the prohibitions of the sale or other provisions of any defense article or defense service to the Government of the Republic of Cyprus and modifying the policy of denial for exports, re-exports, or transfers of defense articles on the United States Munitions List to the Republic of Cyprus; and\n**(3)**\nit is in the interest of the United States\u2014\n**(A)**\nto continue to support United Nations-facilitated efforts toward a comprehensive solution to the division of Cyprus;\n**(B)**\nto enhance the strategic partnership and security relationship between the United States and Republic of Cyprus as provided for in the Eastern Mediterranean Security and Energy Partnership Act of 2019;\n**(C)**\nto enhance the cooperation between the United States Armed Forces and the National Guard of the Republic of Cyprus and to enhance existing programs such as the joint training between the National Guards of the Republic of Cyprus and the State of New Jersey under the auspices of the Department of Defense\u2019s State Partnership Program; and\n**(D)**\nfor the Republic of Cyprus to join NATO\u2019s Partnership for Peace program.\n#### 3. Nonapplicability of a policy of denial for exports, re-exports, or transfers of defense articles and defense services destined for or originating in the Republic of Cyprus\n##### (a) In general\nSubject to subsection (d) and except as provided in subsection (b), beginning on the date of the enactment of this Act, the Secretary of State shall not apply a policy of denial for exports, re-exports, or transfers of defense articles and defense services destined for or originating in the Republic of Cyprus if\u2014\n**(1)**\nthe request is made by or on behalf of the Government of the Republic of Cyprus; and\n**(2)**\nthe end-user of such defense articles or defense services is the Government of the Republic of Cyprus.\n##### (b) Exception\nThe exclusion provided for in subsection (a) shall not apply with respect to the application of a policy of denial based upon credible human rights concerns.\n##### (c) Waiver\nThe President may waive the exclusion provided for in subsection (a) for a period of one fiscal year if the President determines that it is essential to the national security interests of the United States to do so.\n##### (d) Termination\n**(1) In general**\nThe President may terminate the exclusion provided for in subsection (a) for the 5-year period beginning on the date that is 5 years after the date of the enactment of this Act, and may renew such termination for subsequent 5-year periods, if, prior to each such 5-year period, the President submits to the appropriate congressional committees a certification that the Government of the Republic of Cyprus is no longer\u2014\n**(A)**\ncooperating with the United States Government in efforts to implement reforms on anti-money laundering regulations and financial regulatory oversight; and\n**(B)**\ndenying Russian military vessels access to ports for refueling and servicing.\n**(2) Appropriate congressional committees defined**\nIn this subsection, the term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs and the Committee on Armed Services of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations and the Committee on Armed Services of the Senate.",
      "versionDate": "2025-07-15",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-07-29T22:09:36Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4413ih.xml"
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
      "title": "End the Cyprus Embargo Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T07:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End the Cyprus Embargo Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T07:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for nonapplicability of a policy of denial for exports, re-exports, or transfers of defense articles and defense services destined for or originating in the Republic of Cyprus.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T07:48:20Z"
    }
  ]
}
```
