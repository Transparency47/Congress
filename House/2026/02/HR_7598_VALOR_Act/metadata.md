# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7598?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7598
- Title: VALOR Act
- Congress: 119
- Bill type: HR
- Bill number: 7598
- Origin chamber: House
- Introduced date: 2026-02-17
- Update date: 2026-05-14T08:07:55Z
- Update date including text: 2026-05-14T08:07:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-17: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2026-02-17: Introduced in House

## Actions

- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-10 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-17",
    "latestAction": {
      "actionDate": "2026-02-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7598",
    "number": "7598",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000593",
        "district": "49",
        "firstName": "Mike",
        "fullName": "Rep. Levin, Mike [D-CA-49]",
        "lastName": "Levin",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "VALOR Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:07:55Z",
    "updateDateIncludingText": "2026-05-14T08:07:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-10",
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
      "actionDate": "2026-02-17",
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
      "actionDate": "2026-02-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-17",
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
          "date": "2026-02-17T16:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-10T17:53:48Z",
              "name": "Referred to"
            }
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "GU"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7598ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7598\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 17, 2026 Mr. Levin (for himself and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to refund the amount of fees for a housing loans guaranteed by the Secretary of Veterans Affairs for certain veterans with pending disability claims, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Assistance for Loan Origination Relief Act or the VALOR Act .\n#### 2. Housing loan fees: clarification on overpayments and refunds for certain veterans with pending disability claims\nSection 3729 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (c), by adding at the end the following new paragraph:\n(3) A fee collected from a person in violation of paragraph (1) shall be treated as an overpayment. In the event that the Secretary collects a fee from a person in violation of paragraph (1), the Secretary shall\u2014 (A) refund the amount of the fee to the person; or (B) in the case of a fee so collected that was paid as part of a loan, credit the amount of the fee to the loan. ; and\n**(2)**\nby adding at the end the following new subsection:\n(d) Treatment of veterans with pending disability claims In the case of a veteran who, as of the date on which the veteran applies for a housing loan guaranteed, insured, or made under this chapter, has submitted a claim for disability compensation under the laws administered by the Secretary or a notice of intent to file such a claim but has not received a decision with respect to the claim, a fee shall be collected from such veteran under subsection (a). If such claim for disability compensation is approved, and the veteran receives disability compensation pursuant to that claim, after the date on which the veteran pays such fee, the Secretary shall reimburse the veteran the amount of the fee. .",
      "versionDate": "2026-02-17",
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
        "updateDate": "2026-02-27T19:05:48Z"
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
      "date": "2026-02-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7598ih.xml"
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
      "title": "VALOR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T09:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VALOR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Assistance for Loan Origination Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to refund the amount of fees for a housing loans guaranteed by the Secretary of Veterans Affairs for certain veterans with pending disability claims, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T09:18:38Z"
    }
  ]
}
```
