# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1533?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1533
- Title: A bill to amend title 38, United States Code, to make permanent and codify the pilot program for use of contract physicians for disability examinations, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 1533
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2026-03-19T10:56:41Z
- Update date including text: 2026-03-19T10:56:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1533",
    "number": "1533",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "A bill to amend title 38, United States Code, to make permanent and codify the pilot program for use of contract physicians for disability examinations, and for other purposes.",
    "type": "S",
    "updateDate": "2026-03-19T10:56:41Z",
    "updateDateIncludingText": "2026-03-19T10:56:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-30",
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
        "item": [
          {
            "date": "2025-07-30T20:00:34Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-21T20:00:34Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T20:00:34Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-04-30T19:20:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-30",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1533is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1533\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Moran (for himself and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to make permanent and codify the pilot program for use of contract physicians for disability examinations, and for other purposes.\n#### 1. Making permanent and codifying pilot program for use of contract physicians for disability examinations\n##### (a) In general\nSubchapter I of chapter 51 of title 38, United States Code, is amended by inserting after section 5103A the following new section:\n5103B. Use of contract physicians for disability examinations (a) Authority (1) In general Examinations with respect to medical disability of applicants for benefits under laws administered by the Secretary that are carried out through the Under Secretary for Benefits may be made by persons other than employees of the Department. (2) Contracts Any examination by a person under paragraph (1) shall be performed pursuant to a contract entered into by the Under Secretary for Benefits with that person. (b) Licensure of contract health care professionals (1) In general Notwithstanding any provision of law regarding the licensure of health care professionals, a health care professional described in paragraph (2) may conduct an examination pursuant to a contract entered into under subsection (a) at any location in any State so long as the examination is within the scope of the authorized duties under such contract. (2) Health care professional described A health care professional described in this paragraph is a person who is eligible for appointment to a position in the Veterans Health Administration covered by section 7402(b) of this title, who\u2014 (A) has a current unrestricted license to practice the health care profession of the health care professional; (B) is not barred from practicing such health care profession in any State; and (C) is performing authorized duties for the Department pursuant to a contract entered into under subsection (a). (c) Source of funds Expenses of carrying out this section, including payments for examination travel and incidental expenses under the terms and conditions set forth by section 111 of this title, shall be reimbursed to the accounts available for the general operating expenses of the Veterans Benefits Administration and information technology systems from amounts available to the Secretary for payment of compensation and pensions. (d) Mechanism for transmittal of new and material medical evidence introduced by applications during examinations The Secretary shall establish a mechanism whereby a health care professional providing an examination under subsection (a) for an applicant for a benefit described in such subsection can transmit to the Secretary medical evidence introduced by the applicant during such examination that the health care professional considers new and material to the application. .\n##### (b) Clerical amendment\nThe table of sections after the beginning of chapter 51 of such title is amended by inserting after the item relating to section 5103A the following new item:\n5103B. Use of contract physicians for disability examinations. .\n##### (c) Termination of pilot program\nThe pilot program under section 504(a) of the Veterans' Benefits Improvements Act of 1996 ( Public Law 104\u2013275 ; 38 U.S.C. 5101 note) is hereby terminated.\n##### (d) Report to Congress\nNot later than 3 years after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to Congress a report on the effect of the use of the authority provided by section 5103B of such title, as added by subsection (a), on the cost, timeliness, and thoroughness of medical disability examinations.",
      "versionDate": "2025-04-30",
      "versionType": "Introduced in Senate"
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
            "updateDate": "2025-06-05T14:26:50Z"
          },
          {
            "name": "Disability and paralysis",
            "updateDate": "2025-06-05T14:26:41Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-06-05T14:26:21Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-06-05T14:26:14Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-06-05T14:26:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-28T20:57:31Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1533is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to make permanent and codify the pilot program for use of contract physicians for disability examinations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:28Z"
    },
    {
      "title": "A bill to amend title 38, United States Code, to make permanent and codify the pilot program for use of contract physicians for disability examinations, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-01T10:56:16Z"
    }
  ]
}
```
