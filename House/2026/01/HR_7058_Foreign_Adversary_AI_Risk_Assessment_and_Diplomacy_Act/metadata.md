# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7058?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7058
- Title: Foreign Adversary AI Risk Assessment and Diplomacy Act
- Congress: 119
- Bill type: HR
- Bill number: 7058
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-05-04T19:15:58Z
- Update date including text: 2026-05-04T19:15:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 45 - 0.
- Latest action: 2026-01-14: Introduced in House

## Actions

- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 45 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7058",
    "number": "7058",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001322",
        "district": "5",
        "firstName": "Michael",
        "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
        "lastName": "Baumgartner",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "Foreign Adversary AI Risk Assessment and Diplomacy Act",
    "type": "HR",
    "updateDate": "2026-05-04T19:15:58Z",
    "updateDateIncludingText": "2026-05-04T19:15:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "text": "Ordered to be Reported by the Yeas and Nays: 45 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-01-14",
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
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-14",
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
            "date": "2026-03-26T16:16:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-14T15:05:10Z",
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
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "AZ"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "FL"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "MS"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "IN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "FL"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "TN"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7058ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7058\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Mr. Baumgartner (for himself, Mr. Hamadeh of Arizona , Ms. Salazar , and Mr. Ezell ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the Secretary of State to conduct assessments of the risks posed to the United States by foreign adversaries who utilize generative artificial intelligence for malicious activities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foreign Adversary AI Risk Assessment and Diplomacy Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nwhile generative artificial intelligence has the potential to provide substantial societal and economic benefits when developed and used responsibly, the increasing use of generative artificial intelligence by foreign adversaries may represent a national security risk, and the challenges posed by such use is not well understood; and\n**(2)**\nthe Department of State, in consultation with the heads of other relevant Federal departments and agencies, must take diplomatic steps to recognize, assess, and address the use of generative artificial intelligence by foreign adversaries, including through bilateral and multilateral engagements and the promotion of responsible state behavior in international fora, to reduce the national security risks to the United States.\n#### 3. Assessments of the risks posed to the United States by foreign adversaries who utilize generative artificial intelligence for malicious activities\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for three years, the Secretary of State, in consultation with the heads of other relevant Federal departments and agencies as appropriate shall submit to the appropriate congressional committees an assessment of the risks posed to the United States by foreign adversaries who utilize generative artificial intelligence for malicious activities.\n##### (b) Contents\nEach assessment under subsection (a) shall include the following:\n**(1)**\nAn analysis of incidents during the preceding calendar year in which foreign adversaries have utilized, or attempted to utilize, generative artificial intelligence for malicious activities against the United States and its allies, including the following:\n**(A)**\nTo disseminate or produce synthetic media, including foreign anti-United States propaganda or conduct foreign malign influence operations targeting the United States, its citizens, or its allies.\n**(B)**\nTo enhance their ability to develop or deploy chemical, biological, radiological, or nuclear weapons.\n**(C)**\nTo facilitate malicious cyber operations.\n**(D)**\nTo develop or enhance other military, surveillance, or intelligence capabilities.\n**(2)**\nAn analysis of emerging trends in the use of generative artificial intelligence by foreign adversaries, including the following:\n**(A)**\nThe extent to which such activities may be attributable to specific foreign adversaries.\n**(B)**\nThe implications of such trends for United States foreign policy, diplomatic engagement, and the development of United States and allied-led international norms and standards.\n**(3)**\nRecommendations to mitigate and counter the risks posed to the United States and allies by foreign adversaries who utilize generative artificial intelligence applications for malicious activities.\n##### (c) Form\nEach assessment under subsection (a) shall be submitted in unclassified form, but may include a classified annex only for the protection of intelligence sources and methods relating to the matters contained in the assessment. The Secretary of State shall post on a publicly available website of the Department of State the unclassified portion of each assessment.\n#### 4. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate.\n**(2) Artificial intelligence**\nThe term artificial intelligence has the meaning given such term in section 5002(3) of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401(3) ).\n**(3) Foreign adversary**\nThe term foreign adversary has the meaning given the term covered nation in section 4872(f) of title 10, United States Code.\n**(4) Generative artificial intelligence applications**\nThe term generative artificial intelligence applications means the class of artificial intelligence models that emulate the structure and characteristics of input data in order to generate derived synthetic content, including images, videos, audio, text, and other digital content.",
      "versionDate": "2026-01-14",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-05-04T19:14:40Z"
          },
          {
            "name": "Chemical and biological weapons",
            "updateDate": "2026-05-04T19:15:27Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-05-04T19:14:48Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-05-04T19:14:56Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-04T19:15:42Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-05-04T19:15:10Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2026-05-04T19:15:51Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2026-05-04T19:15:58Z"
          },
          {
            "name": "Intelligence activities, surveillance, classified information",
            "updateDate": "2026-05-04T19:15:19Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-05-04T19:15:03Z"
          },
          {
            "name": "Nuclear weapons",
            "updateDate": "2026-05-04T19:15:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2026-02-04T23:04:13Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7058ih.xml"
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
      "title": "Foreign Adversary AI Risk Assessment and Diplomacy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T11:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Foreign Adversary AI Risk Assessment and Diplomacy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T11:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of State to conduct assessments of the risks posed to the United States by foreign adversaries who utilize generative artificial intelligence for malicious activities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:59Z"
    }
  ]
}
```
