# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/316?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/316
- Title: Of inquiry requesting the President to transmit certain documents relating to the use of insecure electronic communication platforms, including Signal, for official communications and to the compliance of the Administration with all Federal records laws.
- Congress: 119
- Bill type: HRES
- Bill number: 316
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2025-06-05T13:56:07Z
- Update date including text: 2025-06-05T13:56:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-04-09 - IntroReferral: Submitted in House
- 2025-04-09 - IntroReferral: Submitted in House
- 2025-04-30 - Committee: Committee Consideration and Mark-up Session Held
- Latest action: 2025-04-09: Submitted in House

## Actions

- 2025-04-09 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-04-09 - IntroReferral: Submitted in House
- 2025-04-09 - IntroReferral: Submitted in House
- 2025-04-30 - Committee: Committee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/316",
    "number": "316",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000562",
        "district": "8",
        "firstName": "Stephen",
        "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
        "lastName": "Lynch",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Of inquiry requesting the President to transmit certain documents relating to the use of insecure electronic communication platforms, including Signal, for official communications and to the compliance of the Administration with all Federal records laws.",
    "type": "HRES",
    "updateDate": "2025-06-05T13:56:07Z",
    "updateDateIncludingText": "2025-06-05T13:56:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
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
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
            "date": "2025-04-30T15:14:15Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-09T16:05:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "VA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "DC"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NM"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MD"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "OH"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MI"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "FL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "PA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "TX"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "TX"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "WA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "VA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "AZ"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MO"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres316ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 316\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mr. Lynch (for himself, Mr. Connolly , Ms. Norton , Ms. Stansbury , Mr. Krishnamoorthi , Mr. Khanna , Mr. Mfume , Ms. Brown , Ms. Tlaib , Mr. Garcia of California , Mr. Frost , Ms. Lee of Pennsylvania , Mr. Casar , Ms. Crockett , Ms. Randall , Mr. Subramanyam , Ms. Ansari , Mr. Bell , Ms. Simon , Mr. Min , and Ms. Pressley ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nOf inquiry requesting the President to transmit certain documents relating to the use of insecure electronic communication platforms, including Signal, for official communications and to the compliance of the Administration with all Federal records laws.\nThat the President is requested to transmit, to the extent that such documents are in the possession of the President, to the House of Representatives, not later than 14 days after the adoption of this resolution, in a complete and unredacted form, a copy of any document, record, report, memorandum, correspondence, or other communication that refers or relates to the following:\n**(1)**\nThe plan of the Administration to preserve in compliance with Federal recordkeeping requirements all official communications, including any official communications\u2014\n**(A)**\ncontaining highly sensitive national security information; and\n**(B)**\nsent via electronic communication platforms (such as Signal, SMS, iMessage, WhatsApp, Teams, MatterMost, Slack, and Gmail).\n**(2)**\nThe conduct of official business via electronic communication platforms on Federal Government devices, including\u2014\n**(A)**\nvia platforms such as Signal, SMS, iMessage, WhatsApp, Teams, MatterMost, Slack, and Gmail; and\n**(B)**\nsuch official business that involves the communication of highly sensitive national security information.\n**(3)**\nThe conduct of official business via electronic communication platforms on personal devices in violation of Federal law, including\u2014\n**(A)**\nvia platforms such as Signal, SMS, iMessage, WhatsApp, Teams, MatterMost, Slack, and Gmail; and\n**(B)**\nsuch official business that involves the communication of highly sensitive national security information.\n**(4)**\nPlans, procedures, guidance, or practices to ensure that communications involving official business are not set to automatically delete after a period of time in violation of Federal recordkeeping requirements when such communications are sent via electronic communication platforms, including any such communications\u2014\n**(A)**\ncontaining highly sensitive national security information; and\n**(B)**\nsent via such platforms as Signal, SMS, iMessage, WhatsApp, Teams, MatterMost, Slack, and Gmail.",
      "versionDate": "2025-04-09",
      "versionType": "IH"
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
            "name": "Computers and information technology",
            "updateDate": "2025-06-05T13:55:53Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-05T13:55:34Z"
          },
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-06-05T13:55:24Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-05T13:55:40Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-06-05T13:55:48Z"
          },
          {
            "name": "Intelligence activities, surveillance, classified information",
            "updateDate": "2025-06-05T13:56:07Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-06-05T13:55:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-22T18:22:59Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres316ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Of inquiry requesting the President to transmit certain documents relating to the use of insecure electronic communication platforms, including Signal, for official communications and to the compliance of the Administration with all Federal records laws.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T08:48:22Z"
    },
    {
      "title": "Of inquiry requesting the President to transmit certain documents relating to the use of insecure electronic communication platforms, including Signal, for official communications and to the compliance of the Administration with all Federal records laws.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T08:06:38Z"
    }
  ]
}
```
