# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7294?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7294
- Title: AI for Secure Networks Act
- Congress: 119
- Bill type: HR
- Bill number: 7294
- Origin chamber: House
- Introduced date: 2026-01-30
- Update date: 2026-03-27T08:06:49Z
- Update date including text: 2026-03-27T08:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-30: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-30: Introduced in House

## Actions

- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-30",
    "latestAction": {
      "actionDate": "2026-01-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7294",
    "number": "7294",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001226",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Menendez, Robert [D-NJ-8]",
        "lastName": "Menendez",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "AI for Secure Networks Act",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:49Z",
    "updateDateIncludingText": "2026-03-27T08:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
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
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-30",
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
          "date": "2026-01-30T15:34:10Z",
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
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "TX"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "VA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "OH"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7294ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7294\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 30, 2026 Mr. Menendez (for himself, Mr. Pfluger , Ms. McClellan , and Mr. Landsman ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo study the impacts of artificial intelligence technology with respect to the security of telecommunications networks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AI for Secure Networks Act .\n#### 2. Artificial intelligence technology and the security of telecommunications networks\n##### (a) Study\nThe Secretary shall conduct a study on the impacts of artificial intelligence technology with respect to the security of telecommunications networks, which shall include an analysis of\u2014\n**(1)**\nhow artificial intelligence technology may be used to improve telecommunications networks, including by facilitating\u2014\n**(A)**\nreal-time threat and malware detection and zero trust security solutions;\n**(B)**\nincreased resiliency and interoperability;\n**(C)**\nimproved energy efficiency; and\n**(D)**\nintegrated sensing and communications;\n**(2)**\nhow artificial intelligence technology may be used in connection with Open Radio Access Network technology to increase the security of telecommunications networks;\n**(3)**\nhow artificial intelligence technology may be used in connection with virtualized security technology to increase the security of telecommunications networks;\n**(4)**\nhow artificial intelligence technology may be used to improve network security controls through firewalls and network segmentation; and\n**(5)**\nany risks artificial intelligence technology poses for the security of telecommunications networks.\n##### (b) Consultation\nFor purposes of the study conducted under subsection (a), the Secretary shall consult with the Federal Communications Commission and industry stakeholders with respect to the use of artificial intelligence technology to improve the security of telecommunications networks, including with respect to research and development activities.\n##### (c) Report\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report on the results of the study conducted under subsection (a), which may include legislative recommendations.\n**(2) Opportunity for public comment**\nPrior to the submission of the report under paragraph (1), the Secretary shall provide an opportunity for public comment with respect to such report.\n##### (d) Secretary defined\nIn this section, the term Secretary means the Secretary of Commerce, acting through the Assistant Secretary of Commerce for Communications and Information.",
      "versionDate": "2026-01-30",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-02-19T19:04:30Z"
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
      "date": "2026-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7294ih.xml"
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
      "title": "AI for Secure Networks Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-18T07:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AI for Secure Networks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T07:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To study the impacts of artificial intelligence technology with respect to the security of telecommunications networks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-18T07:49:46Z"
    }
  ]
}
```
