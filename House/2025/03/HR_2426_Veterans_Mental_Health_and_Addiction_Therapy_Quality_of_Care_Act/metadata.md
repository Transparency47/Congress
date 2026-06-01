# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2426?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2426
- Title: Veterans Mental Health and Addiction Therapy Quality of Care Act
- Congress: 119
- Bill type: HR
- Bill number: 2426
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-01-14T09:07:00Z
- Update date including text: 2026-01-14T09:07:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-13 - Committee: Referred to the Subcommittee on Health.
- 2026-01-13 - Committee: Subcommittee Hearings Held
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-13 - Committee: Referred to the Subcommittee on Health.
- 2026-01-13 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2426",
    "number": "2426",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "F000246",
        "district": "4",
        "firstName": "Pat",
        "fullName": "Rep. Fallon, Pat [R-TX-4]",
        "lastName": "Fallon",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Veterans Mental Health and Addiction Therapy Quality of Care Act",
    "type": "HR",
    "updateDate": "2026-01-14T09:07:00Z",
    "updateDateIncludingText": "2026-01-14T09:07:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
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
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-13",
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
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:07:10Z",
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
                "date": "2026-01-13T17:12:20Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-01-13T17:12:12Z",
                "name": "Referred to"
              }
            ]
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
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "GA"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "SC"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "RI"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "LA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "WI"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "AR"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "VA"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2426ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2426\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Fallon (for himself, Mr. Bishop , Mr. Wilson of South Carolina , Mr. Magaziner , Mr. Gooden , and Mr. Nehls ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo require a study on the quality of care difference between mental health and addiction therapy care provided by health care providers of the Department of Veterans Affairs compared to non-Department providers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Mental Health and Addiction Therapy Quality of Care Act .\n#### 2. Study on quality of care difference between mental health and addiction therapy care provided by health care providers of Department of Veterans Affairs compared to non-Department providers\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall seek to enter into an agreement with an independent and objective organization outside the Department of Veterans Affairs under which that organization shall\u2014\n**(1)**\nconduct a study on the quality of care difference between mental health and addiction therapy care under the laws administered by the Secretary provided by health care providers of the Department compared to non-Department providers across various modalities, such as telehealth, in-patient, intensive out-patient, out-patient, and residential treatment; and\n**(2)**\nsubmit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives and publish on a publicly available website a report containing the final results of such study.\n##### (b) Timing\nThe Secretary shall ensure that the organization with which the Secretary enters into an agreement pursuant to subsection (a) is able to complete the requirements under such subsection by not later than 18 months after the date on which the agreement is entered into.\n##### (c) Elements\nThe report submitted pursuant to subsection (a)(2) shall include an assessment of the following:\n**(1)**\nThe amount of improvement in health outcomes from start of treatment to completion, including symptom scores and suicide risk using evidence-based scales, including the Columbia-Suicide Severity Rating Scale.\n**(2)**\nWhether providers of the Department and non-Department providers are using evidence-based practices in the treatment of mental health and addiction therapy care, including criteria set forth by the American Society of Addiction Medicine.\n**(3)**\nPotential gaps in coordination between providers of the Department and non-Department providers in responding to individuals seeking mental health or addiction therapy care, including the sharing of patient health records.\n**(4)**\nImplementation of veteran-centric care, including the level of satisfaction of patients with care and the competency of providers with the unique experiences and needs of the military and veteran population.\n**(5)**\nWhether veterans with co-occurring conditions receive integrated care to holistically address their needs.\n**(6)**\nWhether providers monitor health outcomes continually throughout treatment and at regular intervals for up to three years after treatment.\n**(7)**\nThe average length of time to initiate services, which shall include a comparison of the average length of time between the initial point of contact after patient outreach to the point of initial service, as measured or determined by the Secretary.",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-12-09",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 287."
      },
      "number": "702",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Veterans Mental Health and Addiction Therapy Quality of Care Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-08T14:04:41Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-04-08T14:04:41Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-08T14:04:41Z"
          },
          {
            "name": "Health care quality",
            "updateDate": "2025-04-08T14:04:41Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-04-08T14:04:41Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-04-08T14:04:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T14:02:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
    "originChamber": "House",
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
          "measure-id": "id119hr2426",
          "measure-number": "2426",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-27",
          "originChamber": "HOUSE",
          "update-date": "2025-06-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2426v00",
            "update-date": "2025-06-25"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Mental Health and Addiction Therapy Quality of Care Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to seek to enter into an agreement with an independent and objective organization to study the difference in quality of mental health and addiction therapy care provided by the VA compared to non-VA providers across various modalities. The organization must publish its findings publicly.</p>"
        },
        "title": "Veterans Mental Health and Addiction Therapy Quality of Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2426.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Mental Health and Addiction Therapy Quality of Care Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to seek to enter into an agreement with an independent and objective organization to study the difference in quality of mental health and addiction therapy care provided by the VA compared to non-VA providers across various modalities. The organization must publish its findings publicly.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr2426"
    },
    "title": "Veterans Mental Health and Addiction Therapy Quality of Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Mental Health and Addiction Therapy Quality of Care Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to seek to enter into an agreement with an independent and objective organization to study the difference in quality of mental health and addiction therapy care provided by the VA compared to non-VA providers across various modalities. The organization must publish its findings publicly.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr2426"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2426ih.xml"
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
      "title": "Veterans Mental Health and Addiction Therapy Quality of Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Mental Health and Addiction Therapy Quality of Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a study on the quality of care difference between mental health and addiction therapy care provided by health care providers of the Department of Veterans Affairs compared to non-Department providers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:44Z"
    }
  ]
}
```
