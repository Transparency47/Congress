# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7559?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7559
- Title: To amend the Internal Revenue Code of 1986 to deny deduction for outsourcing payments.
- Congress: 119
- Bill type: HR
- Bill number: 7559
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-03-09T19:18:58Z
- Update date including text: 2026-03-09T19:18:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7559",
    "number": "7559",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001189",
        "district": "8",
        "firstName": "Austin",
        "fullName": "Rep. Scott, Austin [R-GA-8]",
        "lastName": "Scott",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to deny deduction for outsourcing payments.",
    "type": "HR",
    "updateDate": "2026-03-09T19:18:58Z",
    "updateDateIncludingText": "2026-03-09T19:18:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7559ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7559\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Austin Scott of Georgia introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to deny deduction for outsourcing payments.\n#### 1. Denial of income tax deduction on outsourcing payments\n##### (a) In general\nPart IX of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n280I. Outsourcing payments (a) In general No deduction shall be allowed under this chapter for any outsourcing payment. (b) Outsourcing payment For purposes of this section\u2014 (1) In general The term outsourcing payment means any premium, fee, royalty, service charge, or other payment made\u2014 (A) in the course of a trade or business, (B) to a foreign person, and (C) with respect to labor or services the benefit of which is directed, directly or indirectly, to consumers located in the United States. (2) Mixed payments In the case of any payment to a foreign person with respect to which labor or services are directed to consumers both within and without the United States, the amount treated as an outsourcing payment shall not exceed the amount equal to the product of such payment and a fraction\u2014 (A) the numerator of which is the amount of labor or services with respect to such payment directed to consumers within the United States, to (B) the labor or services with respect to such payment directed to all consumers. (c) Foreign person For purposes of this section, the term foreign person means any person who is not a United States person, except that such term shall not include any corporation or partnership which is organized under the laws of a possession of the United States. (d) Regulations and other guidance The Secretary shall prescribe such regulations and other guidance as may be necessary or appropriate to carry out this section, including regulations or guidance to prevent the avoidance or abuse of the purposes of this section, including through the use of transfer pricing arrangements. .\n##### (b) Clerical amendment\nThe table of section for part IX of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 280I. Outsourcing payments. .\n##### (c) Effective date\nThe amendments made by this section shall apply to payments made after December 31, 2025, in taxable years ending after such date.",
      "versionDate": "2026-02-12",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-10-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2976",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "HIRE Act",
      "type": "S"
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
        "name": "Taxation",
        "updateDate": "2026-03-09T18:28:36Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7559ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to deny deduction for outsourcing payments.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-05T03:18:23Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to deny deduction for outsourcing payments.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T09:06:34Z"
    }
  ]
}
```
