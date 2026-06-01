# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4082?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4082
- Title: Industrial Certification for Coast Guard Veterans Act
- Congress: 119
- Bill type: HR
- Bill number: 4082
- Origin chamber: House
- Introduced date: 2025-06-23
- Update date: 2025-07-17T15:48:24Z
- Update date including text: 2025-07-17T15:48:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-24 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-06-23: Introduced in House

## Actions

- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-24 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4082",
    "number": "4082",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001077",
        "district": "3",
        "firstName": "Clay",
        "fullName": "Rep. Higgins, Clay [R-LA-3]",
        "lastName": "Higgins",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Industrial Certification for Coast Guard Veterans Act",
    "type": "HR",
    "updateDate": "2025-07-17T15:48:24Z",
    "updateDateIncludingText": "2025-07-17T15:48:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-23",
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
          "date": "2025-06-23T16:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-24T20:55:52Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4082ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4082\nIN THE HOUSE OF REPRESENTATIVES\nJune 23, 2025 Mr. Higgins of Louisiana (for himself and Mr. Ezell ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require a report on Coast Guard personnel skills transfer to the dredging sector and the importance of certain waterways to national security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Industrial Certification for Coast Guard Veterans Act .\n#### 2. Report on Coast Guard personnel skills transfer to the dredging sector and the importance of certain waterways to national security\nRecognizing the critical role of Federal channels and other channels determined by the Secretary of Homeland Security to be strategically important in supporting national security and economic prosperity, and the essential function of the United States dredging industry in maintaining such waterways, not later than 180 days after the date of the enactment of this Act, the Secretary shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report that includes the following:\n**(1)**\nAn analysis of the skills and experience of Coast Guard personnel, particularly such personnel with backgrounds in engineering, navigation, heavy equipment operation, and maintenance, that are directly transferable to the dredging industry, which is vital for the upkeep of Federal channels and other channels determined by the Secretary to be strategically important.\n**(2)**\nA plan for developing and implementing targeted outreach and recruitment strategies to connect separating or retiring Coast Guard personnel with employment opportunities in the dredging industry, thereby strengthening the workforce that supports national security interests.\n**(3)**\nAn evaluation of the potential for establishing credentialing or certification programs to recognize and validate the skills of Coast Guard personnel for employment in the dredging industry, ensuring a skilled workforce for maintaining Federal channels and other channels determined by the Secretary to be strategically important.\n**(4)**\nA description of any existing or planned coordination with the Army Corps of Engineers and other relevant agencies to facilitate the transition of Coast Guard personnel into the dredging industry, reinforcing the capacity of the United States to ensure the readiness and reliability of Federal channels and other channels determined by the Secretary to be strategically important.",
      "versionDate": "2025-06-23",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-17T15:48:24Z"
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
      "date": "2025-06-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4082ih.xml"
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
      "title": "Industrial Certification for Coast Guard Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Industrial Certification for Coast Guard Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a report on Coast Guard personnel skills transfer to the dredging sector and the importance of certain waterways to national security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T05:18:31Z"
    }
  ]
}
```
