# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7895?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7895
- Title: PBM Kickback Prohibition Act
- Congress: 119
- Bill type: HR
- Bill number: 7895
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-05-22T08:08:36Z
- Update date including text: 2026-05-22T08:08:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 0.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-21 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7895",
    "number": "7895",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
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
    "title": "PBM Kickback Prohibition Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:36Z",
    "updateDateIncludingText": "2026-05-22T08:08:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
        "item": [
          {
            "date": "2026-05-21T20:08:48Z",
            "name": "Markup By"
          },
          {
            "date": "2026-03-12T13:34:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7895ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7895\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mr. Allen introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend section 408 of the Employee Retirement Income Security Act of 1974 to prohibit kickbacks to pharmacy benefit managers.\n#### 1. Short title\nThis Act may be cited as the PBM Kickback Prohibition Act .\n#### 2. PBM Kickback prohibition\n##### (a) In general\nSection 408(b)(2)(B) of the Employee Retirement Income Security Act ( 29 U.S.C. 1108(b)(2)(B) ) is amended by adding at the end the following:\n(x) In the case of a contract or arrangement between a covered plan and a covered service provider for pharmacy benefit management services, no amount of compensation may be paid, directly or indirectly, by such service provider to a brokerage firm, broker, consultant, advisor, or any other individual for the referral of the covered plan\u2019s or health insurance issuer's business to the covered service provider. .\n##### (b) Effective date\nThe amendment made by this section shall apply for plan years beginning after the date of enactment of this Act.",
      "versionDate": "2026-03-12",
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
        "name": "Health",
        "updateDate": "2026-04-06T13:23:29Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7895ih.xml"
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
      "title": "PBM Kickback Prohibition Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PBM Kickback Prohibition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 408 of the Employee Retirement Income Security Act of 1974 to prohibit kickbacks to pharmacy benefit managers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:36Z"
    }
  ]
}
```
