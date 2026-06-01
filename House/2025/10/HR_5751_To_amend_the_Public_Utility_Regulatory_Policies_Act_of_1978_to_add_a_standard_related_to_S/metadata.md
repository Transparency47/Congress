# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5751?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5751
- Title: CPUC Act
- Congress: 119
- Bill type: HR
- Bill number: 5751
- Origin chamber: House
- Introduced date: 2025-10-14
- Update date: 2025-12-09T18:23:50Z
- Update date including text: 2025-12-09T18:23:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-14: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-10-14: Introduced in House

## Actions

- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-14",
    "latestAction": {
      "actionDate": "2025-10-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5751",
    "number": "5751",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "CPUC Act",
    "type": "HR",
    "updateDate": "2025-12-09T18:23:50Z",
    "updateDateIncludingText": "2025-12-09T18:23:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-14",
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
      "actionDate": "2025-10-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-14",
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
          "date": "2025-10-14T18:01:10Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5751ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5751\nIN THE HOUSE OF REPRESENTATIVES\nOctober 14, 2025 Mr. Harder of California introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Utility Regulatory Policies Act of 1978 to add a standard related to State consideration of public disclosure of meetings with lobbyists for, or representatives of, electric utilities.\n#### 1. Short title\nThis Act may be cited as the Curb Private Utilities Corruption Act or the CPUC Act .\n#### 2. Public disclosure of meetings\nSection 111(d) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621(d) ) is amended by adding at the end the following:\n(22) Public disclosure of meetings (A) Standard Each State shall consider requiring public disclosure, on the website of the applicable State regulatory authority, of each meeting between\u2014 (i) an employee or member of the board of the State regulatory authority; and (ii) a lobbyist, executive, or other representative of an electric utility. (B) Prior State actions Notwithstanding section 124 and paragraphs (1) and (2) of section 112(a), each State regulatory authority shall consider and make a determination concerning the standard set out in subparagraph (A) in accordance with the requirements of subsections (a) and (b) of this section, without regard to any proceedings commenced prior to the date of enactment of this paragraph. (C) Time limitation Notwithstanding subsections (b) and (c) of section 112, each State regulatory authority shall consider and make a determination concerning whether it is appropriate to implement the standard set out in subparagraph (A) not later than one year after the date of enactment of this paragraph. .",
      "versionDate": "2025-10-14",
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
        "name": "Energy",
        "updateDate": "2025-12-09T18:23:50Z"
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
      "date": "2025-10-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5751ih.xml"
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
      "title": "CPUC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CPUC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Curb Private Utilities Corruption Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Utility Regulatory Policies Act of 1978 to add a standard related to State consideration of public disclosure of meetings with lobbyists for, or representatives of, electric utilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T11:18:13Z"
    }
  ]
}
```
