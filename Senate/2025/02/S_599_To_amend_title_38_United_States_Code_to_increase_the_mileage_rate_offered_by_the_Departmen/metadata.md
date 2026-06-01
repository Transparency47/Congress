# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/599?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/599
- Title: DRIVE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 599
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2026-03-19T11:03:25Z
- Update date including text: 2026-03-19T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/599",
    "number": "599",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "DRIVE Act of 2025",
    "type": "S",
    "updateDate": "2026-03-19T11:03:25Z",
    "updateDateIncludingText": "2026-03-19T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
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
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
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
            "date": "2025-05-21T20:00:08Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T20:00:08Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-13T20:28:58Z",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NV"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "HI"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NH"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MN"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "OR"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NJ"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CO"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "OR"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "SD"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "RI"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "AZ"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-06-05",
      "state": "ME"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "PA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WI"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "GA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-10-01",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s599is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 599\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Welch (for himself, Mr. Padilla , Ms. Cortez Masto , Ms. Hirono , Mrs. Shaheen , Ms. Smith , Mr. Wyden , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to increase the mileage rate offered by the Department of Veterans Affairs through their Beneficiary Travel program for health related travel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Driver Reimbursement Increase for Veteran Equity Act of 2025 or the DRIVE Act of 2025 .\n#### 2. Payments or allowances by Department of Veterans Affairs for beneficiary travel\n##### (a) Minimum payment amount\nSubsection (g) of section 111 of title 38, United States Code, is amended to read as follows:\n(g) The Secretary shall ensure that the mileage rate described in subsection (a) is equal to or greater than the mileage reimbursement rate for the use of privately owned vehicles by Government employees on official business (when no Government vehicle is available), as prescribed by the Administrator of General Services under section 5707(b) of title 5. .\n##### (b) Timely processing of allowances\nSubsection (b) of such section is amended by adding at the end the following new paragraph:\n(5) If, with respect to any fiscal year, the Secretary exercises the authority under this section to make any payments, the Secretary shall take such actions as may be necessary to ensure that an allowance based on mileage paid under subsection (a) is paid not later than 90 days after the date on which a request for such allowance is properly submitted to the Secretary in accordance with such regulations as may be prescribed by the Secretary. .\n##### (c) Conforming amendments\nSuch section is further amended\u2014\n**(1)**\nin subsection (a), by striking (at a rate of 41.5 cents per mile) and inserting (at a rate determined in accordance with subsection (g)) ; and\n**(2)**\nin subsection (b)(1), by striking and notwithstanding subsection (g)(2) of this section .",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-04-11",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "1288",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "DRIVE Act of 2025",
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
            "name": "Transportation costs",
            "updateDate": "2025-06-02T20:15:07Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-06-02T20:15:19Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-02T20:15:25Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-06-02T20:15:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-20T16:40:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119s599",
          "measure-number": "599",
          "measure-type": "s",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2025-03-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s599v00",
            "update-date": "2025-03-25"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Driver Reimbursement Increase for Veteran Equity Act of 2025 or the DRIVE Act of 2025</strong></p><p>This bill increases the mileage reimbursement rate available to beneficiaries for travel to or from Department of Veterans Affairs (VA) facilities in connection with vocational rehabilitation, required counseling, or for the purpose of examination, treatment, or care. Specifically, the bill makes the reimbursement rate for such travel equal to or greater than the mileage reimbursement rate for government employees using private vehicles when no government vehicle is available.</p><p>The bill also requires the VA to ensure that an allowance based on mileage is paid not later than 90 days after the request is properly submitted to the VA.</p>"
        },
        "title": "DRIVE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s599.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Driver Reimbursement Increase for Veteran Equity Act of 2025 or the DRIVE Act of 2025</strong></p><p>This bill increases the mileage reimbursement rate available to beneficiaries for travel to or from Department of Veterans Affairs (VA) facilities in connection with vocational rehabilitation, required counseling, or for the purpose of examination, treatment, or care. Specifically, the bill makes the reimbursement rate for such travel equal to or greater than the mileage reimbursement rate for government employees using private vehicles when no government vehicle is available.</p><p>The bill also requires the VA to ensure that an allowance based on mileage is paid not later than 90 days after the request is properly submitted to the VA.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119s599"
    },
    "title": "DRIVE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Driver Reimbursement Increase for Veteran Equity Act of 2025 or the DRIVE Act of 2025</strong></p><p>This bill increases the mileage reimbursement rate available to beneficiaries for travel to or from Department of Veterans Affairs (VA) facilities in connection with vocational rehabilitation, required counseling, or for the purpose of examination, treatment, or care. Specifically, the bill makes the reimbursement rate for such travel equal to or greater than the mileage reimbursement rate for government employees using private vehicles when no government vehicle is available.</p><p>The bill also requires the VA to ensure that an allowance based on mileage is paid not later than 90 days after the request is properly submitted to the VA.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119s599"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s599is.xml"
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
      "title": "DRIVE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DRIVE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Driver Reimbursement Increase for Veteran Equity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to increase the mileage rate offered by the Department of Veterans Affairs through their Beneficiary Travel program for health related travel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:18:19Z"
    }
  ]
}
```
