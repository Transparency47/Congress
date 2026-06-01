# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/134?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/134
- Title: Saving the Civil Service Act
- Congress: 119
- Bill type: S
- Bill number: 134
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2026-03-11T11:03:19Z
- Update date including text: 2026-03-11T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/134",
    "number": "134",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Saving the Civil Service Act",
    "type": "S",
    "updateDate": "2026-03-11T11:03:19Z",
    "updateDateIncludingText": "2026-03-11T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-16",
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
            "date": "2025-01-16T21:05:45Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-16T21:05:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-01-16",
      "state": "VT"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "RI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MD"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "WA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NH"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-01-16",
      "state": "ME"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "OR"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "HI"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CO"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "HI"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "VA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MD"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "MA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "IL"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "CA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NM"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-30",
      "state": "CT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "OR"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NM"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s134is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 134\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Kaine (for himself, Mr. Sanders , Mr. Markey , Mr. Whitehouse , Mr. Van Hollen , Mrs. Murray , Mrs. Shaheen , Mr. King , Ms. Duckworth , Mr. Wyden , Mr. Schatz , Mr. Hickenlooper , Mr. Fetterman , Ms. Hirono , Mr. Warner , Mr. Padilla , and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo place limitations on excepting positions from the competitive service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Saving the Civil Service Act .\n#### 2. Limitations on excepting positions from competitive service and transferring positions\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe term agency means any department, agency, or instrumentality of the Federal Government;\n**(2)**\nthe term competitive service has the meaning given the term in section 2102 of title 5, United States Code;\n**(3)**\nthe term Director means the Director of the Office of Personnel Management; and\n**(4)**\nthe term excepted service has the meaning given the term in section 2103 of title 5, United States Code.\n##### (b) Limitations\nA position in the competitive service may not be excepted from the competitive service unless that position is placed\u2014\n**(1)**\nin any of schedules A through E, as described in section 6.2 of title 5, Code of Federal Regulations, as in effect on September 30, 2020; and\n**(2)**\nunder the terms and conditions under part 6 of title 5, Code of Federal Regulations, as in effect on September 30, 2020.\n##### (c) Transfers\n**(1) Within excepted service**\nA position in the excepted service may not be transferred to any schedule other than a schedule described in subsection (b)(1).\n**(2) OPM consent required**\nAn agency may not transfer any occupied position from the competitive service or the excepted service into schedule C of subpart C of part 213 of title 5, Code of Federal Regulations, or any successor regulations, without the prior consent of the Director.\n**(3) Limit during presidential term**\nDuring any 4-year presidential term, an agency may not transfer from a position in the competitive service to a position in the excepted service the greater of the following:\n**(A)**\nA total number of employees that is more than 1 percent of the total number of employees employed by that agency, as of the first day of that presidential term.\n**(B)**\n5 employees.\n**(4) Employee consent required**\nNotwithstanding any other provision of this section\u2014\n**(A)**\nan employee who occupies a position in the excepted service may not be transferred to an excepted service schedule other than the schedule in which that position is located without the prior written consent of the employee; and\n**(B)**\nan employee who occupies a position in the competitive service may not be transferred to the excepted service without the prior written consent of the employee.\n##### (d) Other matters\n**(1) Application**\nNotwithstanding section 7425(b) of title 38, United States Code, this section shall apply to a position under chapter 73 or 74 of that title.\n**(2) Report**\nNot later than March 15 of each calendar year, the Director shall submit to Congress a report on the immediately preceding calendar year that lists\u2014\n**(A)**\neach position that, during the year covered by the report, was transferred from the competitive service to the excepted service and a justification as to why each such position was so transferred; and\n**(B)**\nany violation of this section that occurred during the year covered by the report.\n##### (e) Regulations\nNot later than 90 days after the date of enactment of this Act, the Director shall issue regulations to implement this section.",
      "versionDate": "2025-01-16",
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
            "updateDate": "2025-03-13T15:59:20Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-03-13T15:59:20Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-13T15:59:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-27T16:42:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119s134",
          "measure-number": "134",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-07-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s134v00",
            "update-date": "2025-07-21"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Saving the Civil Service Act</strong></p><p>This bill generally prohibits changes to the classification of positions in the competitive service and excepted service unless certain conditions are met. (Competitive service positions are subject to competitive examination while excepted service positions are appointed under one of five schedules. Competitive service positions have notice and appeal requirements for adverse actions that are not applicable to most excepted positions, including those of a confidential, policy-determining, policy-making, or policy-advocating character under Schedule C.)</p><p>On October 21, 2020, President Donald Trump issued an executive order that placed executive agency positions that are of a confidential, policy-determining, policy-making, or policy-advocating character, and that are not normally subject to change as a result of a presidential transition, under a new Schedule F in the excepted service. The order was subsequently revoked by President Joe Biden.</p><p>The bill prohibits executive agency positions in the competitive service from being placed in the excepted service, unless such positions are placed in a schedule in the excepted service as in effect on September 30, 2020. The bill also prohibits positions in the excepted service from being placed in any schedule other than the aforementioned schedules.</p><p>Additionally, agencies may not (1) transfer occupied positions from the competitive or excepted service into Schedule C without the consent of the Office of Personnel Management, or (2) transfer employees in the excepted service to another schedule or transfer employees in the competitive service to the excepted service without employee consent.\u00a0</p>"
        },
        "title": "Saving the Civil Service Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s134.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Saving the Civil Service Act</strong></p><p>This bill generally prohibits changes to the classification of positions in the competitive service and excepted service unless certain conditions are met. (Competitive service positions are subject to competitive examination while excepted service positions are appointed under one of five schedules. Competitive service positions have notice and appeal requirements for adverse actions that are not applicable to most excepted positions, including those of a confidential, policy-determining, policy-making, or policy-advocating character under Schedule C.)</p><p>On October 21, 2020, President Donald Trump issued an executive order that placed executive agency positions that are of a confidential, policy-determining, policy-making, or policy-advocating character, and that are not normally subject to change as a result of a presidential transition, under a new Schedule F in the excepted service. The order was subsequently revoked by President Joe Biden.</p><p>The bill prohibits executive agency positions in the competitive service from being placed in the excepted service, unless such positions are placed in a schedule in the excepted service as in effect on September 30, 2020. The bill also prohibits positions in the excepted service from being placed in any schedule other than the aforementioned schedules.</p><p>Additionally, agencies may not (1) transfer occupied positions from the competitive or excepted service into Schedule C without the consent of the Office of Personnel Management, or (2) transfer employees in the excepted service to another schedule or transfer employees in the competitive service to the excepted service without employee consent.\u00a0</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119s134"
    },
    "title": "Saving the Civil Service Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Saving the Civil Service Act</strong></p><p>This bill generally prohibits changes to the classification of positions in the competitive service and excepted service unless certain conditions are met. (Competitive service positions are subject to competitive examination while excepted service positions are appointed under one of five schedules. Competitive service positions have notice and appeal requirements for adverse actions that are not applicable to most excepted positions, including those of a confidential, policy-determining, policy-making, or policy-advocating character under Schedule C.)</p><p>On October 21, 2020, President Donald Trump issued an executive order that placed executive agency positions that are of a confidential, policy-determining, policy-making, or policy-advocating character, and that are not normally subject to change as a result of a presidential transition, under a new Schedule F in the excepted service. The order was subsequently revoked by President Joe Biden.</p><p>The bill prohibits executive agency positions in the competitive service from being placed in the excepted service, unless such positions are placed in a schedule in the excepted service as in effect on September 30, 2020. The bill also prohibits positions in the excepted service from being placed in any schedule other than the aforementioned schedules.</p><p>Additionally, agencies may not (1) transfer occupied positions from the competitive or excepted service into Schedule C without the consent of the Office of Personnel Management, or (2) transfer employees in the excepted service to another schedule or transfer employees in the competitive service to the excepted service without employee consent.\u00a0</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119s134"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s134is.xml"
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
      "title": "Saving the Civil Service Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-11T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Saving the Civil Service Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to place limitations on excepting positions from the competitive service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:20Z"
    }
  ]
}
```
