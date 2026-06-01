# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/702?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/702
- Title: Veterans Mental Health and Addiction Therapy Quality of Care Act
- Congress: 119
- Bill type: S
- Bill number: 702
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2025-12-11T03:53:20Z
- Update date including text: 2025-12-11T03:53:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported without amendment favorably.
- 2025-12-09 - Committee: Committee on Veterans' Affairs. Reported by Senator Moran without amendment. Without written report.
- 2025-12-09 - Committee: Committee on Veterans' Affairs. Reported by Senator Moran without amendment. Without written report.
- 2025-12-09 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 287.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-03-11 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported without amendment favorably.
- 2025-12-09 - Committee: Committee on Veterans' Affairs. Reported by Senator Moran without amendment. Without written report.
- 2025-12-09 - Committee: Committee on Veterans' Affairs. Reported by Senator Moran without amendment. Without written report.
- 2025-12-09 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 287.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/702",
    "number": "702",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Veterans Mental Health and Addiction Therapy Quality of Care Act",
    "type": "S",
    "updateDate": "2025-12-11T03:53:20Z",
    "updateDateIncludingText": "2025-12-11T03:53:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 287.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Reported by Senator Moran without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Veterans' Affairs. Reported by Senator Moran without amendment. Without written report.",
      "type": "Committee"
    },
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
      "text": "Committee on Veterans' Affairs. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-25",
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
      "actionDate": "2025-02-25",
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
            "date": "2025-12-09T17:50:03Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T20:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-11T14:30:18Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-25T15:27:25Z",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "NH"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "NC"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "LA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CO"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "MI"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "ME"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s702is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 702\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Cornyn (for himself, Ms. Hassan , Mr. Tillis , Mr. Fetterman , Mr. Cassidy , Mr. Bennet , Mr. Peters , and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo require a study on the quality of care difference between mental health and addiction therapy care provided by health care providers of the Department of Veterans Affairs compared to non-Department providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Mental Health and Addiction Therapy Quality of Care Act .\n#### 2. Study on quality of care difference between mental health and addiction therapy care provided by health care providers of Department of Veterans Affairs compared to non-Department providers\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall seek to enter into an agreement with an independent and objective organization outside the Department of Veterans Affairs under which that organization shall\u2014\n**(1)**\nconduct a study on the quality of care difference between mental health and addiction therapy care under the laws administered by the Secretary provided by health care providers of the Department compared to non-Department providers across various modalities, such as telehealth, in-patient, intensive out-patient, out-patient, and residential treatment; and\n**(2)**\nsubmit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives and publish on a publicly available website a report containing the final results of such study.\n##### (b) Timing\nThe Secretary shall ensure that the organization with which the Secretary enters into an agreement pursuant to subsection (a) is able to complete the requirements under such subsection by not later than 18 months after the date on which the agreement is entered into.\n##### (c) Elements\nThe report submitted pursuant to subsection (a)(2) shall include an assessment of the following:\n**(1)**\nThe amount of improvement in health outcomes from start of treatment to completion, including symptom scores and suicide risk using evidence-based scales, including the Columbia-Suicide Severity Rating Scale.\n**(2)**\nWhether providers of the Department and non-Department providers are using evidence-based practices in the treatment of mental health and addiction therapy care, including criteria set forth by the American Society of Addiction Medicine.\n**(3)**\nPotential gaps in coordination between providers of the Department and non-Department providers in responding to individuals seeking mental health or addiction therapy care, including the sharing of patient health records.\n**(4)**\nImplementation of veteran-centric care, including the level of satisfaction of patients with care and the competency of providers with the unique experiences and needs of the military and veteran population.\n**(5)**\nWhether veterans with co-occurring conditions receive integrated care to holistically address their needs.\n**(6)**\nWhether providers monitor health outcomes continually throughout treatment and at regular intervals for up to three years after treatment.\n**(7)**\nThe average length of time to initiate services, which shall include a comparison of the average length of time between the initial point of contact after patient outreach to the point of initial service, as measured or determined by the Secretary.",
      "versionDate": "2025-02-25",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s702rs.xml",
      "text": "II\nCalendar No. 287\n119th CONGRESS\n1st Session\nS. 702\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Cornyn (for himself, Ms. Hassan , Mr. Tillis , Mr. Fetterman , Mr. Cassidy , Mr. Bennet , Mr. Peters , Ms. Collins , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nDecember 9, 2025 Reported by Mr. Moran , without amendment\nA BILL\nTo require a study on the quality of care difference between mental health and addiction therapy care provided by health care providers of the Department of Veterans Affairs compared to non-Department providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Mental Health and Addiction Therapy Quality of Care Act .\n#### 2. Study on quality of care difference between mental health and addiction therapy care provided by health care providers of Department of Veterans Affairs compared to non-Department providers\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall seek to enter into an agreement with an independent and objective organization outside the Department of Veterans Affairs under which that organization shall\u2014\n**(1)**\nconduct a study on the quality of care difference between mental health and addiction therapy care under the laws administered by the Secretary provided by health care providers of the Department compared to non-Department providers across various modalities, such as telehealth, in-patient, intensive out-patient, out-patient, and residential treatment; and\n**(2)**\nsubmit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives and publish on a publicly available website a report containing the final results of such study.\n##### (b) Timing\nThe Secretary shall ensure that the organization with which the Secretary enters into an agreement pursuant to subsection (a) is able to complete the requirements under such subsection by not later than 18 months after the date on which the agreement is entered into.\n##### (c) Elements\nThe report submitted pursuant to subsection (a)(2) shall include an assessment of the following:\n**(1)**\nThe amount of improvement in health outcomes from start of treatment to completion, including symptom scores and suicide risk using evidence-based scales, including the Columbia-Suicide Severity Rating Scale.\n**(2)**\nWhether providers of the Department and non-Department providers are using evidence-based practices in the treatment of mental health and addiction therapy care, including criteria set forth by the American Society of Addiction Medicine.\n**(3)**\nPotential gaps in coordination between providers of the Department and non-Department providers in responding to individuals seeking mental health or addiction therapy care, including the sharing of patient health records.\n**(4)**\nImplementation of veteran-centric care, including the level of satisfaction of patients with care and the competency of providers with the unique experiences and needs of the military and veteran population.\n**(5)**\nWhether veterans with co-occurring conditions receive integrated care to holistically address their needs.\n**(6)**\nWhether providers monitor health outcomes continually throughout treatment and at regular intervals for up to three years after treatment.\n**(7)**\nThe average length of time to initiate services, which shall include a comparison of the average length of time between the initial point of contact after patient outreach to the point of initial service, as measured or determined by the Secretary.",
      "versionDate": "2025-12-09",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-03-27",
        "text": "Referred to the House Committee on Veterans' Affairs."
      },
      "number": "2426",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Veterans Mental Health and Addiction Therapy Quality of Care Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-08T14:04:24Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-04-08T14:04:19Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-08T14:04:00Z"
          },
          {
            "name": "Health care quality",
            "updateDate": "2025-04-08T14:04:13Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-04-08T14:04:09Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-04-08T14:04:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-04-04T19:49:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s702",
          "measure-number": "702",
          "measure-type": "s",
          "orig-publish-date": "2025-02-25",
          "originChamber": "SENATE",
          "update-date": "2025-05-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s702v00",
            "update-date": "2025-05-08"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Veterans Mental Health and Addiction Therapy Quality of Care Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to seek to enter into an agreement with an independent and objective organization to study the difference in quality of mental health and addiction therapy care provided by the VA compared to non-VA providers across various modalities. The organization must publish its findings publicly.</p>"
        },
        "title": "Veterans Mental Health and Addiction Therapy Quality of Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s702.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans Mental Health and Addiction Therapy Quality of Care Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to seek to enter into an agreement with an independent and objective organization to study the difference in quality of mental health and addiction therapy care provided by the VA compared to non-VA providers across various modalities. The organization must publish its findings publicly.</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119s702"
    },
    "title": "Veterans Mental Health and Addiction Therapy Quality of Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans Mental Health and Addiction Therapy Quality of Care Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to seek to enter into an agreement with an independent and objective organization to study the difference in quality of mental health and addiction therapy care provided by the VA compared to non-VA providers across various modalities. The organization must publish its findings publicly.</p>",
      "updateDate": "2025-05-08",
      "versionCode": "id119s702"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s702is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s702rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Veterans Mental Health and Addiction Therapy Quality of Care Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-12-11T03:53:19Z"
    },
    {
      "title": "Veterans Mental Health and Addiction Therapy Quality of Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Mental Health and Addiction Therapy Quality of Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a study on the quality of care difference between mental health and addiction therapy care provided by health care providers of the Department of Veterans Affairs compared to non-Department providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:58Z"
    }
  ]
}
```
