# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1034?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1034
- Title: Southwestern Power Administration Fund Establishment Act
- Congress: 119
- Bill type: S
- Bill number: 1034
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1034",
    "number": "1034",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
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
    "title": "Southwestern Power Administration Fund Establishment Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
        "item": {
          "date": "2025-03-13T16:59:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:00Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "MO"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1034is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1034\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Moran (for himself, Mr. Hawley , and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo establish the Southwestern Power Administration Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Southwestern Power Administration Fund Establishment Act .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Southwestern Power Administration.\n**(2) Fund**\nThe term Fund means the Southwestern Power Administration Fund established by section 3(a).\n**(3) Secretary**\nThe term Secretary means the Secretary of Energy.\n#### 3. Southwestern power administration fund\n##### (a) Establishment of Fund\nThere is established in the Treasury of the United States a fund, to be known as the Southwestern Power Administration Fund , consisting of\u2014\n**(1)**\nall receipts, collections, and recoveries of the Southwestern Power Administration, including trust funds;\n**(2)**\nappropriations to the Fund;\n**(3)**\namounts transferred to the Fund under subsection (b); and\n**(4)**\namounts deposited in the Fund under the first proviso in the matter under the heading Operation and Maintenance, Southwestern Power Administration under the heading Power Marketing Administrations under the heading Department of Energy in title III of the Energy and Water Development Appropriations Act, 2005 ( 16 U.S.C. 825s\u20134 ).\n##### (b) Transfers to Fund\nThere are transferred to the Fund\u2014\n**(1)**\nunexpended balances in the continuing fund pursuant to the 11th paragraph under the heading OFFICE OF THE SECRETARY in title I of the Act of October 12, 1949 ( 16 U.S.C. 825s\u20131 );\n**(2)**\nunexpended balances in the advanced payment fund pursuant to the first proviso in the matter under the heading Operation and Maintenance, Southwestern Power Administration under the heading Power Marketing Administrations under the heading Department of Energy in title III of the Energy and Water Development Appropriations Act, 2005 ( 16 U.S.C. 825s\u20134 ); and\n**(3)**\nunexpended balances in the offsetting collections fund pursuant to the fourth and fifth provisos in the matter under the heading Operation and Maintenance, Southwestern Power Administration under the heading Power Marketing Administrations under the heading Department of Energy in title III of the Energy and Water Development and Related Agencies Appropriations Act, 2010 ( 16 U.S.C. 825s\u20137 ) (as in effect on the day before the date of enactment of this Act).\n##### (c) Availability\nAmounts in the Fund shall remain available until expended.\n##### (d) Use\nAmounts in the Fund shall be used by the Secretary, acting through the Administrator, for expenses necessary for\u2014\n**(1)**\noperation and maintenance of power transmission facilities;\n**(2)**\nmarketing electric power and energy;\n**(3)**\nconstruction and acquisition of transmission lines, substations, and appurtenant facilities; and\n**(4)**\nadministrative expenses in carrying out the duties of the Secretary under\u2014\n**(A)**\nsection 5 of the Act of December 22, 1944 (commonly known as the Flood Control Act of 1944 ) ( 16 U.S.C. 825s ); and\n**(B)**\nsection 1232 of the Energy Policy Act of 2005 ( 42 U.S.C. 16431 ).\n##### (e) Obligations\nThe Secretary, acting through the Administrator, may incur obligations for authorized purposes in advance of appropriations to be liquidated by the Fund.\n##### (f) Excess funds\nAnnually, the Secretary, acting through the Administrator, shall transfer excess amounts in the Fund to the Treasury of the United States as miscellaneous receipts.\n##### (g) Applicable law\nThe provisions of chapter 91 of title 31, United States Code, shall apply to the Administrator in carrying out this section in the same manner as the provisions apply to a wholly owned Government corporation (as defined in section 9101 of that title).\n##### (h) Conforming amendments\n**(1)**\nThe proviso in the matter under the heading Operation and Maintenance, Southwestern Power Administration under the heading Power Marketing Administrations under the heading Department of Energy in title III of the Energy and Water Development Appropriations Act, 2005 ( 16 U.S.C. 825s\u20134 ), is amended\u2014\n**(A)**\nby striking in fiscal year 2005 and inserting on the date of enactment of the Southwestern Power Administration Fund Establishment Act ; and\n**(B)**\nby striking credited to this account and inserting deposited in the Southwestern Power Administration Fund established by section 3(a) of the Southwestern Power Administration Fund Establishment Act .\n**(2)**\nThe fourth and fifth provisos in the matter under the heading Operation and Maintenance, Southwestern Power Administration under the heading Power Marketing Administrations under the heading Department of Energy in title III of the Energy and Water Development and Related Agencies Appropriations Act, 2010 ( 16 U.S.C. 825s\u20137 ), are repealed.",
      "versionDate": "2025-03-13",
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
        "actionDate": "2025-03-27",
        "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2432",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Southwestern Power Administration Fund Establishment Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-04-04T11:45:31Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1034is.xml"
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
      "title": "Southwestern Power Administration Fund Establishment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Southwestern Power Administration Fund Establishment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the Southwestern Power Administration Fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:22Z"
    }
  ]
}
```
