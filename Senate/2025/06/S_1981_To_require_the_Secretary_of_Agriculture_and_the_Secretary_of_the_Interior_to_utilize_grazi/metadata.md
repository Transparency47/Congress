# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1981?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1981
- Title: Strategic Grazing to Reduce Risk of Wildfire Act
- Congress: 119
- Bill type: S
- Bill number: 1981
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-02-12 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2026-03-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1981",
    "number": "1981",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Strategic Grazing to Reduce Risk of Wildfire Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
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
            "date": "2026-03-04T16:02:22Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-05T18:31:26Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-12T15:00:20Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1981is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1981\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Ms. Cortez Masto (for herself and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Secretary of Agriculture and the Secretary of the Interior to utilize grazing for wildfire risk reduction, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strategic Grazing to Reduce Risk of Wildfire Act .\n#### 2. Utilizing grazing for wildfire risk reduction\n##### (a) Definitions\nIn this section:\n**(1) National forest system**\nThe term National Forest System has the meaning given the term in section 11(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1609(a) ).\n**(2) Public lands**\nThe term public lands has the meaning given the term in section 103 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1702 ).\n**(3) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of Agriculture, with respect to National Forest System land; and\n**(B)**\nthe Secretary of the Interior, with respect to public lands.\n##### (b) Strategy\n**(1) In general**\nNot later than 18 months after the date of enactment of this Act, the Secretary concerned, in coordination with holders of permits to graze livestock on Federal land under the jurisdiction of the Secretary concerned and in consultation with other relevant stakeholders described in paragraph (3), shall develop a strategy to utilize livestock grazing as a wildfire risk reduction tool consistent with the laws applicable to the Secretary concerned.\n**(2) Considerations**\nThe strategy developed under paragraph (1) shall consider\u2014\n**(A)**\nthe use of grazing on vacant grazing allotments during instances of drought, wildfire, or other natural disasters that disrupt grazing on allotments already permitted;\n**(B)**\nthe use of targeted grazing to reduce hazardous fuels, including on Federal land within the wildland urban interface (as defined in section 101 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6511 )), and other critical areas identified by the Secretaries concerned;\n**(C)**\nrecommending the use of targeted grazing when providing technical assistance to communities and Indian Tribes in their efforts to reduce wildfire risk and implement wildfire management strategies;\n**(D)**\nthe use of temporary permits to promote targeted fuels reduction and reduction of cheatgrass and other invasive annual grasses, including any potential need for the use of grazing outside permitted animal unit months and season of use, as appropriate for the explicit purposes of targeted fuels reduction of cheatgrass and other invasive annual grasses;\n**(E)**\nthe use of targeted grazing to aid in controlling invasive annual grasses, including cheatgrass;\n**(F)**\nthe use of targeted grazing in postfire recovery efforts, as appropriate;\n**(G)**\nan integrated use of advanced technologies such as virtual fencing to dynamically adjust livestock placement;\n**(H)**\nthe use of grazing on Federal land in a manner that\u2014\n**(i)**\navoids conflicts with other uses of that Federal land; and\n**(ii)**\nis consistent with any applicable land management plan;\n**(I)**\na workforce development plan to ensure that Federal workers have the necessary skills to manage livestock grazing programs and deploy technologies;\n**(J)**\nthe use of cooperative agreements with States, local governments, Indian Tribes, and local firefighting agencies to reduce hazardous fuels and invasive annual grasses, including reimbursements authorized under other provisions of law, including under good neighbor agreements under section 8206 of the Agricultural Act of 2014 ( 16 U.S.C. 2113a ); and\n**(K)**\nother applicable statutory or regulatory authorities, as determined by the Secretary concerned.\n**(3) Consultation**\nIn developing the strategy under paragraph (1), the Secretary concerned shall consult with\u2014\n**(A)**\napplicable States;\n**(B)**\napplicable units of local government;\n**(C)**\napplicable Indian Tribes;\n**(D)**\napplicable utility authorities;\n**(E)**\napplicable firefighting agencies;\n**(F)**\nland management organizations;\n**(G)**\noutdoor recreation, conservation, and sportsmen organizations; and\n**(H)**\nother interested members of the applicable community.\n##### (c) Effect on existing grazing programs\nNothing in this section affects any livestock grazing program being carried out as of the date of enactment of this Act by the Secretary concerned.",
      "versionDate": "2025-06-05",
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
            "name": "Fires",
            "updateDate": "2026-02-17T20:18:56Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2026-02-17T20:19:00Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2026-02-17T20:19:14Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-02-17T20:19:09Z"
          },
          {
            "name": "Livestock",
            "updateDate": "2026-02-17T20:19:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-24T21:47:41Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1981is.xml"
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
      "title": "Strategic Grazing to Reduce Risk of Wildfire Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strategic Grazing to Reduce Risk of Wildfire Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-18T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Agriculture and the Secretary of the Interior to utilize grazing for wildfire risk reduction, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-18T05:18:24Z"
    }
  ]
}
```
