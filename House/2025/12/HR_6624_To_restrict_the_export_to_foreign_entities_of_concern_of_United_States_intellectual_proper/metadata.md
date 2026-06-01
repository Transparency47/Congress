# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6624?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6624
- Title: Biological Intellectual Property Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6624
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-04-24T08:07:35Z
- Update date including text: 2026-04-24T08:07:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 30 - 14.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 30 - 14.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6624",
    "number": "6624",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Biological Intellectual Property Protection Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-24T08:07:35Z",
    "updateDateIncludingText": "2026-04-24T08:07:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
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
      "text": "Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 30 - 14.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
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
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
            "date": "2026-04-22T20:20:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-11T16:03:40Z",
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
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "PA"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "OK"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "NC"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MD"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "NC"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "AK"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6624ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6624\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Davidson (for himself, Ms. Houlahan , Mrs. Bice , Mr. McCaul , Mr. Sessions , and Mr. Harrigan ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo restrict the export to foreign entities of concern of United States intellectual property and sensitive information related to synthetic biology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Biological Intellectual Property Protection Act of 2025 .\n#### 2. Sense of congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe People\u2019s Republic of China is conducting a systematic campaign to access and exploit sensitive United States data and intellectual property to modernize its military, intelligence, and other security apparatuses, enable human rights abuses, and develop dual-use strategic technologies;\n**(2)**\naccess by the People\u2019s Republic of China to sensitive United States data and intellectual property poses grave and direct threats to United States national security;\n**(3)**\nthe efforts of the People\u2019s Republic of China to access such data and intellectual property are supported by a military-civil fusion strategy, through which the People\u2019s Republic of China increases the size of its military-industrial complex by compelling civilian Chinese companies and research institutions to support its military and intelligence activities, which results in ostensibly private and civilian companies that access United States capital supporting the modernization of the People\u2019s Liberation Army;\n**(4)**\nthe law of the People\u2019s Republic of China requires that all citizens of the People\u2019s Republic of China cooperate with national security priorities, enabling the modernization of the People\u2019s Liberation Army, including through\u2014\n**(A)**\nthe National Security Law of 2015, which states that citizens of the People\u2019s Republic of China shall have duties and obligations to maintain national security ;\n**(B)**\nthe National Intelligence Law of 2017, which states that all organizations and citizens shall support, assist, and cooperate with national intelligence work ;\n**(C)**\nthe Data Security Law of 2021, which states that where a public security organ or national security organ needs to obtain data for the sake of national security or for investigating crimes in accordance with the law . . . the relevant organizations and individuals shall cooperate ; and\n**(D)**\nthe Counterespionage Law, revised in 2023, which states that citizens of the People\u2019s Republic of China have the duty to maintain the security, honor and interests of the state, and shall not engage in any act that endangers the security, honor or interests of the state ;\n**(5)**\nthe export of novel synthetic DNA and RNA sequences provides insight into the designs and research of biotechnology entities, leading to a high potential for intellectual property theft by foreign adversaries; and\n**(6)**\nthe United States should therefore control the export of synthetic DNA and RNA sequences to foreign adversaries.\n#### 3. License requirement to protect united states intellectual property and sensitive information related to synthetic biology\nPart I of the Export Control Reform Act of 2018 ( 50 U.S.C. 4811 et seq. ) is amended by inserting after section 1758 the following:\n1758A. License requirement to protect united states intellectual property and sen- sitive information related to syn- thetic biology (a) License requirement Not later than 1 year after the date of the enactment of this section, the Secretary shall, except as provided for in subsection (b), require a license for the export, reexport, or in-country transfer to a foreign entity of concern of a digital sequence of synthetic DNA or RNA designed by humans or artificial intelligence systems. (b) Exception The requirement for a license under subsection (a) shall not apply with respect to information described in section 734.3(b) of the Export Administration Regulations. (c) Definitions In this section: (1) Digital sequence The term digital sequence means a binary file or other digital representation containing symbols representing the identity, order, and any chemical modification for each position in a DNA or RNA molecule. (2) Foreign country of concern The term foreign country of concern has the meaning given that term in section 10612(a) of the Research and Development, Competition, and Innovation Act ( 42 U.S.C. 19221(a) ). (3) Foreign entity of concern The term foreign entity of concern means\u2014 (A) a government entity of a foreign country of concern; (B) a foreign person subject to the jurisdiction of, or organized under the laws of, a foreign country of concern; or (C) a foreign person owned, directed, or controlled by an entity described in subparagraph (A) or (B). (4) Synthetic DNA or RNA The term synthetic DNA or RNA means\u2014 (A) molecules that are constructed by joining nucleic acid molecules and can replicate in a living cell, such as recombinant nucleic acids; (B) nucleic acid molecules that are chemically or by other means synthesized, including such molecules that are chemically or otherwise modified but can base pair with naturally occurring nucleic acid molecules, such as synthetic nucleic acids; or (C) molecules that result from the replication of molecules described in subparagraph (A) or (B). .",
      "versionDate": "2025-12-11",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-11",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "3452",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Biological Intellectual Property Protection Act of 2025",
      "type": "S"
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
        "updateDate": "2026-01-08T16:27:30Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6624ih.xml"
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
      "title": "Biological Intellectual Property Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-03T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Biological Intellectual Property Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To restrict the export to foreign entities of concern of United States intellectual property and sensitive information related to synthetic biology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-03T05:48:22Z"
    }
  ]
}
```
