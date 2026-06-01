# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3083?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3083
- Title: Providing Complete Information to Retirement Investors Act
- Congress: 119
- Bill type: S
- Bill number: 3083
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2026-01-08T14:07:12Z
- Update date including text: 2026-01-08T14:07:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-30",
    "latestAction": {
      "actionDate": "2025-10-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3083",
    "number": "3083",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Providing Complete Information to Retirement Investors Act",
    "type": "S",
    "updateDate": "2026-01-08T14:07:12Z",
    "updateDateIncludingText": "2026-01-08T14:07:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-10-30T17:41:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3083is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3083\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mr. Banks (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to ensure that pension plans provide notice to participants and beneficiaries on risks associated with certain investments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing Complete Information to Retirement Investors Act .\n#### 2. Brokerage window disclosures\n##### (a) In general\nSection 404(c) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1104(c) ) is amended by adding at the end the following new paragraph:\n(7) Notice requirements for brokerage windows (A) In general In the case of a pension plan which provides for individual accounts and which provides a participant or beneficiary the opportunity to choose from designated investment alternatives, a participant or beneficiary shall not be treated as exercising control over assets in the account of the participant or beneficiary unless, with respect to any investment arrangement that is not a designated investment alternative, each time before such a participant or beneficiary directs an investment into, out of, or within such investment arrangement, such participant is notified of, and acknowledges, each element of the notice described under paragraph (B). (B) Notice The notice described under this paragraph is a 4-part information that is substantially similar to the following information: 1. Your retirement plan offers designated investment alternatives prudently selected and monitored by fiduciaries for the purpose of enabling you to construct an appropriate retirement savings portfolio. In selecting and monitoring designated investment alternatives, your plan\u2019s fiduciary considers the risk of loss and the opportunity for gain (or other return) compared with reasonably available investment alternatives. 2. The investments available through this investment arrangement are not designated investment alternatives, and have not been prudently selected and are not monitored by a plan fiduciary. 3. Depending on the investments you select through this investment arrangement, you may experience diminished returns, higher fees, and higher risk than if you select from the plan\u2019s designated investment alternatives. 4. The following is a hypothetical illustration of the impact of return at 4 percent, 6 percent, and 8 percent on your account balance projected to age 67. (C) Illustration The notice described under paragraph (B) shall also include a graph displaying the projected retirement balances of such participant or beneficiary at age 67 if the account of such individual were to achieve an annual return equal to each of the following: (i) 4 percent. (ii) 6 percent. (iii) 8 percent. .\n##### (b) Designated investment alternative defined\nSection 3 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1002 ) is amended by adding at the end the following new paragraph:\n(46) Designated investment alternative (A) In general The term designated investment alternative means any investment alternative designated by a responsible fiduciary of an individual account plan described in subsection 404(c) into which participants and beneficiaries may direct the investment of assets held in, or contributed to, their individual accounts. (B) Exception The term designated investment alternative does not include brokerage windows, self-directed brokerage accounts, or similar plan arrangements that enable participants and beneficiaries to select investments beyond those designated by a responsible plan fiduciary. .\n##### (c) Effective date\nThe amendment made by subsection (a) shall take effect on January 1, 2026.",
      "versionDate": "2025-10-30",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-30",
        "text": "Placed on the Union Calendar, Calendar No. 367."
      },
      "number": "2988",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Prudent Investment of Retirement Savings Act",
      "type": "HR"
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
        "name": "Labor and Employment",
        "updateDate": "2025-11-25T20:39:44Z"
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
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3083is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Providing Complete Information to Retirement Investors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Providing Complete Information to Retirement Investors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-05T03:53:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Employee Retirement Income Security Act of 1974 to ensure that pension plans provide notice to participants and beneficiaries on risks associated with certain investments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-05T03:48:14Z"
    }
  ]
}
```
