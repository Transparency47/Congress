# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1814?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1814
- Title: Restoring the VA Home Loan Program in Perpetuity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1814
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2025-04-01T15:30:04Z
- Update date including text: 2025-04-01T15:30:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-10 - Committee: Subcommittee Hearings Held
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-10 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1814",
    "number": "1814",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000135",
        "district": "3",
        "firstName": "Derrick",
        "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
        "lastName": "Van Orden",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Restoring the VA Home Loan Program in Perpetuity Act of 2025",
    "type": "HR",
    "updateDate": "2025-04-01T15:30:04Z",
    "updateDateIncludingText": "2025-04-01T15:30:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
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
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-03-10T19:17:32Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-03-10T19:17:26Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1814ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1814\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Van Orden introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to provide for limitations on the authority of the Secretary of Veterans Affairs to purchase certain loans guaranteed by the Department of Veterans Affairs to avoid default, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring the VA Home Loan Program in Perpetuity Act of 2025 .\n#### 2. Limitations on authority under Department of Veterans Affairs Servicer Purchaser Program\n##### (a) Limitation\nSection 3732(a)(2) of title 38, United States Code, is amended by adding at the end the following new subparagraph:\n(C) During any fiscal year, the Secretary may not exercise the authority under subsections (A) and (B) with respect to more than an aggregate of 250 loans. .\n##### (b) Conforming amendment\nSection 3720(a)(5) of such title is amended by inserting before purchase the following: subject to the limitation under section 3732(a)(2)(C) of this title, .\n##### (c) Study on sale of loans\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committees on Veterans\u2019 Affairs of the Senate and House of Representatives a report containing the plan of the Secretary to sell to a non-Government entity each loan acquired by the Secretary under section 3732(a)(2) of title 38, United States Code, on or after May 31, 2024.",
      "versionDate": "2025-03-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-01T15:29:42Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-04-01T15:30:04Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-01T15:29:21Z"
          },
          {
            "name": "Veterans' loans, housing, homeless programs",
            "updateDate": "2025-04-01T15:29:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-26T15:10:17Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1814ih.xml"
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
      "title": "Restoring the VA Home Loan Program in Perpetuity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restoring the VA Home Loan Program in Perpetuity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to provide for limitations on the authority of the Secretary of Veterans Affairs to purchase certain loans guaranteed by the Department of Veterans Affairs to avoid default, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:28Z"
    }
  ]
}
```
