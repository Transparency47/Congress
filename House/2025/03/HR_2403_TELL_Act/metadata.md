# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2403?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2403
- Title: TELL Act
- Congress: 119
- Bill type: HR
- Bill number: 2403
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2025-11-18T09:05:40Z
- Update date including text: 2025-11-18T09:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2403",
    "number": "2403",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "A000372",
        "district": "12",
        "firstName": "Rick",
        "fullName": "Rep. Allen, Rick W. [R-GA-12]",
        "lastName": "Allen",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "TELL Act",
    "type": "HR",
    "updateDate": "2025-11-18T09:05:40Z",
    "updateDateIncludingText": "2025-11-18T09:05:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:06:30Z",
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
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "OH"
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
      "sponsorshipDate": "2025-11-17",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2403ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2403\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Allen (for himself and Ms. Kaptur ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require that any person that maintains an internet website or that sells or distributes a mobile application that stores and maintains information collected from such website or application in the People\u2019s Republic of China to disclose that such information is stored and maintained in the People\u2019s Republic of China and whether the Chinese Communist Party or a Chinese State-owned entity has access to such information.\n#### 1. Short title\nThis Act may be cited as the Telling Everyone the Location of data Leaving the U.S. Act or the TELL Act .\n#### 2. Country disclosure requirements\n##### (a) Disclosure requirements\nAny person that maintains an internet website or that sells or distributes a mobile application that stores and maintains information collected from such website or application in the People\u2019s Republic of China shall disclose to any individual who downloads or otherwise uses such website or application, in a clear and conspicuous manner, the following:\n**(1)**\nThat such information is stored and maintained in the People\u2019s Republic of China.\n**(2)**\nWhether the Chinese Communist Party or a Chinese State-owned entity has access to such information.\n##### (b) False information\nIt shall be unlawful for a person required to disclose information under subsection (a) to knowingly disclose false information under such subsection.\n#### 3. Enforcement\n##### (a) Unfair or deceptive acts or practices\nA violation of this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n##### (b) Powers of Federal Trade Commission\n**(1) In general**\nThe Federal Trade Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(2) Privileges and immunities**\nAny person that violates this Act shall be subject to the penalties, and entitled to the privileges and immunities, provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).",
      "versionDate": "2025-03-27",
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
        "name": "Commerce",
        "updateDate": "2025-05-19T15:55:58Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2403ih.xml"
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
      "title": "TELL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-05T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TELL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Telling Everyone the Location of data Leaving the U.S. Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require that any person that maintains an internet website or that sells or distributes a mobile application that stores and maintains information collected from such website or application in the People's Republic of China to disclose that such information is stored and maintained in the People's Republic of China and whether the Chinese Communist Party or a Chinese State-owned entity has access to such information.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T05:48:28Z"
    }
  ]
}
```
