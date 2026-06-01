# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/874?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/874
- Title: To amend title 38, United States Code, to modify the rate of pay for care or services provided under the Community Care Program of the Department of Veterans Affairs based on the location at which such care or services were provided, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 874
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-04-07T13:38:34Z
- Update date including text: 2025-04-07T13:38:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-04 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-04 - Committee: Referred to the Subcommittee on Health.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/874",
    "number": "874",
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
    "title": "To amend title 38, United States Code, to modify the rate of pay for care or services provided under the Community Care Program of the Department of Veterans Affairs based on the location at which such care or services were provided, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-04-07T13:38:34Z",
    "updateDateIncludingText": "2025-04-07T13:38:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:09:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-04T22:41:57Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr874ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 874\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. McCormick introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to modify the rate of pay for care or services provided under the Community Care Program of the Department of Veterans Affairs based on the location at which such care or services were provided, and for other purposes.\n#### 1. Rates of pay for a provider of care or services furnished to a veteran under the Community Care Program of the Department of Veterans Affairs\n##### (a) Rates\nSection 1703(i) of title 38, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking Except as provided in paragraph (2), and to the extent practicable and inserting (A) To the extent practicable ; and\n**(B)**\nby adding at the end the following new subparagraphs:\n(B) The Secretary shall establish rates for payments under subparagraph (A) that are specific with respect to the following locations at which the care or services were provided (regardless of the location of the headquarters of the provider): (i) An inpatient hospital. (ii) An on-campus hospital outpatient department. (iii) An off-campus hospital outpatient department. (iv) An ambulatory surgical center. (v) The office of a physician. (C) The Secretary shall ensure that a claim for payment under this paragraph includes a unique, geographically specific national provider identifier code that identifies the location of the provider as described in subparagraph (B). ; and\n**(2)**\nby adding at the end the following new paragraph:\n(7) If the Secretary may pay more than one rate under this paragraph for care or services, the Secretary shall pay the lowest such rate. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on January 1, 2026.",
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
            "updateDate": "2025-04-07T13:38:34Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-04-07T13:38:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-18T18:18:20Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr874ih.xml"
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
      "title": "To amend title 38, United States Code, to modify the rate of pay for care or services provided under the Community Care Program of the Department of Veterans Affairs based on the location at which such care or services were provided, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:18:24Z"
    },
    {
      "title": "To amend title 38, United States Code, to modify the rate of pay for care or services provided under the Community Care Program of the Department of Veterans Affairs based on the location at which such care or services were provided, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T09:06:11Z"
    }
  ]
}
```
