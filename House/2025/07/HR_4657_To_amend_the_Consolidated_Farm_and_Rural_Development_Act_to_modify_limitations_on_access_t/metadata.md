# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4657?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4657
- Title: Next Generation Farmer Act
- Congress: 119
- Bill type: HR
- Bill number: 4657
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-08-07T16:45:31Z
- Update date including text: 2025-08-07T16:45:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4657",
    "number": "4657",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Next Generation Farmer Act",
    "type": "HR",
    "updateDate": "2025-08-07T16:45:31Z",
    "updateDateIncludingText": "2025-08-07T16:45:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:09:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4657ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4657\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Finstad (for himself and Mr. Riley of New York ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to modify limitations on access to farm ownership loans for beginning farmers and ranchers.\n#### 1. Short title\nThis Act may be cited as the Next Generation Farmer Act .\n#### 2. Experience requirements\nSection 302(b) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1922(b) ) is amended\u2014\n**(1)**\nin paragraph (1), in the matter preceding subparagraph (A), by striking 3 years and inserting 1 year ; and\n**(2)**\nby striking paragraph (4) and inserting the following:\n(4) Waiver authority In the case of a qualified beginning farmer or rancher, the Secretary may waive the 1-year requirement in paragraph (1) if the farmer or rancher has\u2014 (A) at least 1 year of experience as hired farm labor with substantial management responsibilities; or (B) an established relationship with an individual who has experience in farming or ranching, or is a retired farmer or rancher, and is participating as a counselor in a Service Corps of Retired Executives program authorized under section 8(b)(1)(B) of the Small Business Act ( 15 U.S.C. 637(b)(1)(B) ), or with a local farm or ranch operator or organization, approved by the Secretary, that is committed to mentoring the farmer or rancher. .",
      "versionDate": "2025-07-23",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-08-07T16:45:31Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4657ih.xml"
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
      "title": "Next Generation Farmer Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T03:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Next Generation Farmer Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consolidated Farm and Rural Development Act to modify limitations on access to farm ownership loans for beginning farmers and ranchers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:21Z"
    }
  ]
}
```
