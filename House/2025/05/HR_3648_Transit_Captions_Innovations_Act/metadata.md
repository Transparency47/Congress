# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3648?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3648
- Title: Transit Captions Innovations Act
- Congress: 119
- Bill type: HR
- Bill number: 3648
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2025-07-15T08:06:11Z
- Update date including text: 2025-07-15T08:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-30 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-30 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3648",
    "number": "3648",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001225",
        "district": "15",
        "firstName": "Kevin",
        "fullName": "Rep. Mullin, Kevin [D-CA-15]",
        "lastName": "Mullin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Transit Captions Innovations Act",
    "type": "HR",
    "updateDate": "2025-07-15T08:06:11Z",
    "updateDateIncludingText": "2025-07-15T08:06:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-30",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:07:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-30T19:46:01Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3648ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3648\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Mullin introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to make grants for the deployment of innovative real-time transcription and translation technology to improve the transit rider experience for deaf, hard of hearing, and limited English proficient individuals.\n#### 1. Short title\nThis Act may be cited as the Transit Captions Innovations Act .\n#### 2. Innovations in language accessibility\nSection 5312(e)(3) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (B), by striking or at the end;\n**(2)**\nin paragraph (C), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(D) the deployment of real-time transcription and translation technology to improve the rider experience for deaf, hard of hearing, and limited English proficient individuals. .\n#### 3. Authorization of appropriations\nSection 5338(a)(2)(G) of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (i), by striking and at the end;\n**(2)**\nin paragraph (ii), by inserting and at the end; and\n**(3)**\nby adding at the end the following:\n(iii) $4,000,000 for fiscal year 2027, $4,100,000 for fiscal year 2028, $4,202,500 for fiscal year 2029, $4,307,562 for fiscal year 2030, and $4,415,251 for fiscal year 2031 shall be available to carry out projects eligible under section 5312(e)(3)(D); .",
      "versionDate": "2025-05-29",
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
        "updateDate": "2025-06-03T14:46:55Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3648ih.xml"
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
      "title": "Transit Captions Innovations Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transit Captions Innovations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to make grants for the deployment of innovative real-time transcription and translation technology to improve the transit rider experience for deaf, hard of hearing, and limited English proficient individuals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T05:18:43Z"
    }
  ]
}
```
