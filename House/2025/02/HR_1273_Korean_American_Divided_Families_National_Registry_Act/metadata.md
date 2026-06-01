# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1273?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1273
- Title: Korean American Divided Families National Registry Act
- Congress: 119
- Bill type: HR
- Bill number: 1273
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-11-01T08:05:39Z
- Update date including text: 2025-11-01T08:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1273",
    "number": "1273",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Korean American Divided Families National Registry Act",
    "type": "HR",
    "updateDate": "2025-11-01T08:05:39Z",
    "updateDateIncludingText": "2025-11-01T08:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:05:50Z",
          "name": "Referred To"
        }
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "VA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-21",
      "state": "PA"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "AS"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "IL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "NY"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "CA"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "MP"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "VA"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "GU"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1273ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1273\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Subramanyam (for himself, Mrs. Kim , Mr. Connolly , and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo direct the Secretary of State to establish a national registry of Korean American divided families, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Korean American Divided Families National Registry Act .\n#### 2. National registry of Korean American divided families\nThe Secretary of State, acting through the Special Envoy on North Korean Human Rights Issues or such other individual as the Secretary may designate, shall\u2014\n**(1)**\ncollate information on Korean American families who wish to be reunited with family members in North Korea from which such Korean American families were divided after the signing of the Agreement Concerning a Military Armistice in Korea, signed at Panmunjom July 27, 1953 (commonly referred to as the Korean War Armistice Agreement ), in anticipation of future reunions for such families and family members, including in-person and video reunions; and\n**(2)**\nestablish a private internal national registry of the names and other relevant information of such Korean American families\u2014\n**(A)**\nto host such future reunions in South Korea, the United States, or third countries; and\n**(B)**\nto provide for a private internal repository of information about such Korean American families and family members in North Korea, including information about individuals who may be deceased.\n#### 3. Actions to facilitate dialogue between the United States and North Korea\n##### (a) In general\nThe Secretary of State shall take such actions as may be necessary to ensure that any direct dialogue between the United States and North Korea includes progress towards holding future reunions for Korean American families and their family members in North Korea as described in section 2.\n##### (b) Consultations\nThe Secretary of State shall consult with the Government of the Republic of Korea in carrying out this section.\n##### (c) Report\nNo later than one year after enactment of this Act, and annually thereafter for 5 years, the Secretary of State shall submit to the appropriate congressional committees a report on\u2014\n**(1)**\nthe status of the national registry established pursuant to section 2(a)(2);\n**(2)**\nthe number of individuals included on the registry who\u2014\n**(A)**\nhave met their family members in North Korea during previous reunions; and\n**(B)**\nhave yet to meet their family members in North Korea during previous reunions;\n**(3)**\na summary of responses by North Korea to requests to hold reunions of divided families; and\n**(4)**\na description of regulations in North Korea and actions taken by North Korea in the year previous to submission of each report that prevent the emigration of family members of Korean American families.\n##### (d) Appropriate congressional committees defined\nIn this Act, appropriate congressional committees means the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate.",
      "versionDate": "2025-02-12",
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
            "name": "Asia",
            "updateDate": "2025-05-14T13:05:02Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-14T13:05:02Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-05-14T13:05:02Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-05-14T13:05:02Z"
          },
          {
            "name": "Family services",
            "updateDate": "2025-05-14T13:05:02Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-14T13:05:02Z"
          },
          {
            "name": "North Korea",
            "updateDate": "2025-05-14T13:05:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-08T15:29:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119hr1273",
          "measure-number": "1273",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-07-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1273v00",
            "update-date": "2025-07-18"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Korean American Divided Families National Registry Act</strong></p><p>This bill establishes a national registry of Korean American families who wish to be reunited with family members living in North Korea. The bill also requires the Department of State to include reunions of such families in any direct dialogue with North Korea.</p><p>Specifically, the bill requires the State Department to (1) collect information on Korean American families, divided from North Korean family members after the Korean War armistice,\u00a0who wish to be reunited with such family members; and (2) establish a national registry of information on those families to facilitate future reunions. The State Department must\u00a0ensure that any direct dialogue with North Korea includes progress towards holding such reunions.</p><p>The State Department must report to Congress periodically on the registry, previous reunions, and on certain North Korean actions related to reunions.</p>"
        },
        "title": "Korean American Divided Families National Registry Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1273.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Korean American Divided Families National Registry Act</strong></p><p>This bill establishes a national registry of Korean American families who wish to be reunited with family members living in North Korea. The bill also requires the Department of State to include reunions of such families in any direct dialogue with North Korea.</p><p>Specifically, the bill requires the State Department to (1) collect information on Korean American families, divided from North Korean family members after the Korean War armistice,\u00a0who wish to be reunited with such family members; and (2) establish a national registry of information on those families to facilitate future reunions. The State Department must\u00a0ensure that any direct dialogue with North Korea includes progress towards holding such reunions.</p><p>The State Department must report to Congress periodically on the registry, previous reunions, and on certain North Korean actions related to reunions.</p>",
      "updateDate": "2025-07-18",
      "versionCode": "id119hr1273"
    },
    "title": "Korean American Divided Families National Registry Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Korean American Divided Families National Registry Act</strong></p><p>This bill establishes a national registry of Korean American families who wish to be reunited with family members living in North Korea. The bill also requires the Department of State to include reunions of such families in any direct dialogue with North Korea.</p><p>Specifically, the bill requires the State Department to (1) collect information on Korean American families, divided from North Korean family members after the Korean War armistice,\u00a0who wish to be reunited with such family members; and (2) establish a national registry of information on those families to facilitate future reunions. The State Department must\u00a0ensure that any direct dialogue with North Korea includes progress towards holding such reunions.</p><p>The State Department must report to Congress periodically on the registry, previous reunions, and on certain North Korean actions related to reunions.</p>",
      "updateDate": "2025-07-18",
      "versionCode": "id119hr1273"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1273ih.xml"
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
      "title": "Korean American Divided Families National Registry Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T15:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Korean American Divided Families National Registry Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T15:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of State to establish a national registry of Korean American divided families, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T15:18:30Z"
    }
  ]
}
```
