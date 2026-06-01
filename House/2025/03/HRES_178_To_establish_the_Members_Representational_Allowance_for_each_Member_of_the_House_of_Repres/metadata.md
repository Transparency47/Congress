# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/178?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/178
- Title: Put Your Money Where Your Mouth Is Resolution
- Congress: 119
- Bill type: HRES
- Bill number: 178
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2025-05-07T14:10:08Z
- Update date including text: 2025-05-07T14:10:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-02-27 - IntroReferral: Sponsor introductory remarks on measure. (CR H892)
- 2025-03-03 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-03-03 - Committee: Submitted in House
- Latest action: 2025-02-27: Sponsor introductory remarks on measure. (CR H892)

## Actions

- 2025-02-27 - IntroReferral: Sponsor introductory remarks on measure. (CR H892)
- 2025-03-03 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-03-03 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Sponsor introductory remarks on measure. (CR H892)"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/178",
    "number": "178",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "B001314",
        "district": "4",
        "firstName": "Aaron",
        "fullName": "Rep. Bean, Aaron [R-FL-4]",
        "lastName": "Bean",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Put Your Money Where Your Mouth Is Resolution",
    "type": "HRES",
    "updateDate": "2025-05-07T14:10:08Z",
    "updateDateIncludingText": "2025-05-07T14:10:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H892)",
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
          "date": "2025-03-03T17:07:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres178ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 178\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Bean of Florida submitted the following resolution; which was referred to the Committee on House Administration\nRESOLUTION\nTo establish the Members\u2019 Representational Allowance for each Member of the House of Representatives for fiscal years 2026 and 2027 as the amount of the Allowance for fiscal year 2025, reduced by $100,000.\n#### 1. Short title\nThis resolution may be cited as the Put Your Money Where Your Mouth Is Resolution .\n#### 2. Establishment of Members\u2019 Representational Allowance for Fiscal Years 2026 and 2027\n##### (a) Establishment\nThe Members\u2019 Representational Allowance established under section 101 of the House of Representatives Administrative Reform Technical Corrections Act ( 2 U.S.C. 5341 ) shall, for each Member or Member-elect of the House, be equal to\u2014\n**(1)**\nthe amount of such Allowance with respect to the district from which the Member or Member-elect is elected for fiscal year 2025; reduced by\n**(2)**\n$100,000.\n##### (b) Effective date\nThis section shall apply with respect to fiscal year 2026 and fiscal year 2027.",
      "versionDate": "2025-03-03",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-05-07T14:10:08Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres178ih.xml"
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
      "title": "Put Your Money Where Your Mouth Is Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Put Your Money Where Your Mouth Is Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Members' Representational Allowance for each Member of the House of Representatives for fiscal years 2026 and 2027 as the amount of the Allowance for fiscal year 2025, reduced by $100,000.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:18:31Z"
    }
  ]
}
```
