# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4906?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4906
- Title: USA Act
- Congress: 119
- Bill type: HR
- Bill number: 4906
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2025-09-18T18:19:20Z
- Update date including text: 2025-09-18T18:19:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4906",
    "number": "4906",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "W000806",
        "district": "11",
        "firstName": "Daniel",
        "fullName": "Rep. Webster, Daniel [R-FL-11]",
        "lastName": "Webster",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "USA Act",
    "type": "HR",
    "updateDate": "2025-09-18T18:19:20Z",
    "updateDateIncludingText": "2025-09-18T18:19:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4906ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4906\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Mr. Webster of Florida (for himself and Mr. Self ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend the Research and Development, Competition, and Innovation Act to require the Director of the National Institute of Standards and Technology to advance the principles of openness, transparency, due process, appeals, and consensus in the development of international standards, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Utilize Standards for All Act or the USA Act .\n#### 2. Importance of international standards development\nSection 10245 of the Research and Development, Competition, and Innovation Act ( Public Law 117\u2013167 ; 42 U.S.C. 18951 ) is amended by amending subsection (a) to read as follows:\n(a) Importance of international standards development The Director shall carry out the following: (1) Advance the principles of openness, transparency, due process, appeals, and consensus in the development of international standards. (2) Shall promote voluntary consensus standards, developed through a private sector-led process (domestically and internationally) in accordance with the National Institute of Standards and Technology Act ( 15 U.S.C. 271 et seq. ), as in effect on the day before the date of the enactment of this subsection, which are the cornerstone of the United States standardization system and serve as the basis for a sound national economy and the key to global market access. (3) Strengthen the unique United States public-private partnerships approach to advance United States interests in standards development, as such is critical to United States economic competitiveness. (4) In coordination with the heads of relevant Federal agencies, ensure cooperation and coordination across Federal agencies to partner with and support private sector stakeholders regarding standards development for emerging technologies. .",
      "versionDate": "2025-08-05",
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
        "updateDate": "2025-09-18T18:19:20Z"
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
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4906ih.xml"
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
      "title": "USA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Utilize Standards for All Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Research and Development, Competition, and Innovation Act to require the Director of the National Institute of Standards and Technology to advance the principles of openness, transparency, due process, appeals, and consensus in the development of international standards, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:54Z"
    }
  ]
}
```
