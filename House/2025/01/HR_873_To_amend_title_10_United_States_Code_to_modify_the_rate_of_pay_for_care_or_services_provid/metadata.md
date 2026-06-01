# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/873?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/873
- Title: To amend title 10, United States Code, to modify the rate of pay for care or services provided under the TRICARE program based on the location at which such care or services were provided.
- Congress: 119
- Bill type: HR
- Bill number: 873
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-06-26T08:06:39Z
- Update date including text: 2025-06-26T08:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/873",
    "number": "873",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001218",
        "district": "7",
        "firstName": "Richard",
        "fullName": "Rep. McCormick, Richard [R-GA-7]",
        "lastName": "McCormick",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "To amend title 10, United States Code, to modify the rate of pay for care or services provided under the TRICARE program based on the location at which such care or services were provided.",
    "type": "HR",
    "updateDate": "2025-06-26T08:06:39Z",
    "updateDateIncludingText": "2025-06-26T08:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:07:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "AZ"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr873ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 873\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. McCormick introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to modify the rate of pay for care or services provided under the TRICARE program based on the location at which such care or services were provided.\n#### 1. TRICARE reimbursement rates\n##### (a) Rates\nSection 1097b(a) of title 10, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by inserting and paragraph (3)(A) after Subject to paragraph (2) ; and\n**(2)**\nin paragraph (3), by striking In establishing and inserting the following:\n(A) (i) Except as provided by paragraph (1), if the Secretary may determine among more than one reimbursement rate to pay a health care provider for care or services provided under the TRICARE program, the Secretary shall pay the lowest rate authorized for such care or services. (ii) The Secretary shall establish reimbursement rates for care or services paid to health care providers under the TRICARE program that are specific with respect to the following locations at which the care or services were provided (regardless of the location of the headquarters of the health care provider): (I) An inpatient hospital. (II) An on-campus hospital outpatient department. (III) An off-campus hospital outpatient department. (IV) An ambulatory surgical center. (V) The office of a physician. (iii) The Secretary shall ensure that a claim for reimbursement includes a unique, geographically specific national provider identifier code that identifies the location of the provider as described in clause (ii). (B) In establishing .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on January 1, 2026.",
      "versionDate": "2025-01-31",
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
            "name": "Health care costs and insurance",
            "updateDate": "2025-04-07T13:38:15Z"
          },
          {
            "name": "Military medicine",
            "updateDate": "2025-04-07T13:38:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-03T16:24:13Z"
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
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr873ih.xml"
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
      "title": "To amend title 10, United States Code, to modify the rate of pay for care or services provided under the TRICARE program based on the location at which such care or services were provided.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:26Z"
    },
    {
      "title": "To amend title 10, United States Code, to modify the rate of pay for care or services provided under the TRICARE program based on the location at which such care or services were provided.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T09:05:42Z"
    }
  ]
}
```
