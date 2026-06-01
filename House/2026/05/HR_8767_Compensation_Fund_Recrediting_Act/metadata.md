# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8767?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8767
- Title: Compensation Fund Recrediting Act
- Congress: 119
- Bill type: HR
- Bill number: 8767
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-29T16:28:17Z
- Update date including text: 2026-05-29T16:28:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2026-05-12: Introduced in House

## Actions

- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8767",
    "number": "8767",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Compensation Fund Recrediting Act",
    "type": "HR",
    "updateDate": "2026-05-29T16:28:17Z",
    "updateDateIncludingText": "2026-05-29T16:28:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T16:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8767ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8767\nIN THE HOUSE OF REPRESENTATIVES\nMay 12, 2026 Mr. Self introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend the American Recovery and Reinvestment Act of 2009 to wind down the Filipino Veterans Equity Compensation Fund.\n#### 1. Short title\nThis Act may be cited as the Compensation Fund Recrediting Act .\n#### 2. Sunset of the Filipino Veterans Equity Compensation Fund\nSection 1002 of the American Recovery and Reinvestment Act of 2009 ( Public Law 111\u20135 ; 38 U.S.C. 107 note) is amended\u2014\n**(1)**\nin subsection (l), by striking until expended and inserting until the date specified in subsection (m) ; and\n**(2)**\nby adding at the end the following new subsection:\n(m) Sunset On January 1, 2027\u2014 (1) this section shall cease to have any effect; and (2) any amounts in the compensation fund shall be deposited into the general fund of the Treasury. .",
      "versionDate": "2026-05-12",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-05-29T16:28:17Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8767ih.xml"
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
      "title": "Compensation Fund Recrediting Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T03:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Compensation Fund Recrediting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-15T03:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the American Recovery and Reinvestment Act of 2009 to wind down the Filipino Veterans Equity Compensation Fund.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T03:48:37Z"
    }
  ]
}
```
