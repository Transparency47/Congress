# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2074?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2074
- Title: POWER Act
- Congress: 119
- Bill type: HR
- Bill number: 2074
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2026-03-06T20:45:52Z
- Update date including text: 2026-03-06T20:45:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-11 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-11 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-11 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-11 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2074",
    "number": "2074",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "N000189",
        "district": "4",
        "firstName": "Dan",
        "fullName": "Rep. Newhouse, Dan [R-WA-4]",
        "lastName": "Newhouse",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "POWER Act",
    "type": "HR",
    "updateDate": "2026-03-06T20:45:52Z",
    "updateDateIncludingText": "2026-03-06T20:45:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-11T22:07:43Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-11T14:06:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "WA"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "ID"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2074ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2074\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Newhouse (for himself, Mr. Baumgartner , Mr. Fulcher , and Mr. Bentz ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the breaching of federally operated dams in certain circumstances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Our Water Energy Resources Act or the POWER Act .\n#### 2. Prohibition on breaching of federally operated dams\n##### (a) In general\nNotwithstanding any other provision of law, the Secretary of the Army may not breach a federally operated dam\u2014\n**(1)**\nif the Secretary determines that such breach\u2014\n**(A)**\nwould result in an increase in carbon emissions by more than 5 percent;\n**(B)**\nwould make the body of water impacted by the breach less navigable for commercial interests; or\n**(C)**\nwould result in increase of at least 5 percent of the price of any products, including agricultural products, shipped via the body of water impacted by the breach; or\n**(2)**\nif the energy resource intended to replace such dam as a result of such breach would occupy an area of land that is larger in acreage than the area occupied by such dam by at least 5 percent.\n##### (b) Consultation\nIn making the determinations required under subsection (a)(1), the Secretary shall\u2014\n**(1)**\nconsult with the Secretary of Energy with respect to the determination described in subparagraph (A) of such subsection;\n**(2)**\nconsult with the Secretary of Transportation with respect to the determination described subparagraph (B) of such subsection;\n**(3)**\nconsult with the Secretary of Agriculture and the Secretary of Commerce with respect to the determination described in subparagraph (C) of such subsection; and\n**(4)**\nconsult with the relevant agencies in the State in which the dam proposed to be breached is located.\n##### (c) Study required\nIf the Secretary considers breaching a federally operated dam, the Secretary, in coordination with the Secretary of the Interior, shall conduct a study analyzing the number of acres of land such dam occupies.\n#### 3. Prohibition on retirement of energy generation sources\n##### (a) In general\nThe Secretary shall not retire an energy generation source if the retirement of that energy generation source would\u2014\n**(1)**\nraise customer electricity rates by more than 5 percent; or\n**(2)**\ndecrease energy reliability, as determined by the Administrator of the Bonneville Power Administration, in any portion of Washington, Oregon, Idaho, Montana, Wyoming, and California by more than 5 percent of the energy reliability as compared to the 12 month period before the retirement.\n##### (b) Replacement of Baseload Generation\nNot later than 30 days after retiring an energy generation source, the Secretary shall ensure that not less than 100 percent of the baseload generation of the retired energy generation source has been replaced.\n##### (c) Definitions\nIn this section:\n**(1) Baseload generation**\nThe term baseload generation means the the minimum amount of electric power supplied to an electrical grid.\n**(2) Energy generation source**\nThe term energy generation source means a federally operated dam that generates hydropower.\n**(3) Secretary**\nThe term Secretary means\u2014\n**(A)**\nthe Secretary of the Interior, in reference to an energy generation source operated by the Bureau of Reclamation; and\n**(B)**\nthe Secretary of the Army, in reference to an energy generation source operated by the Army Corps of Engineers.",
      "versionDate": "2025-03-11",
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
            "name": "Alternative and renewable resources",
            "updateDate": "2026-03-06T20:45:12Z"
          },
          {
            "name": "California",
            "updateDate": "2026-03-06T20:45:46Z"
          },
          {
            "name": "Dams and canals",
            "updateDate": "2026-03-06T20:45:01Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-03-06T20:45:18Z"
          },
          {
            "name": "Energy prices",
            "updateDate": "2026-03-06T20:45:52Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-03-06T20:45:06Z"
          },
          {
            "name": "Idaho",
            "updateDate": "2026-03-06T20:45:32Z"
          },
          {
            "name": "Montana",
            "updateDate": "2026-03-06T20:45:37Z"
          },
          {
            "name": "Oregon",
            "updateDate": "2026-03-06T20:45:28Z"
          },
          {
            "name": "Washington State",
            "updateDate": "2026-03-06T20:45:24Z"
          },
          {
            "name": "Wyoming",
            "updateDate": "2026-03-06T20:45:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2025-05-20T18:48:28Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2074ih.xml"
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
      "title": "POWER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "POWER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Our Water Energy Resources Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the breaching of federally operated dams in certain circumstances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:58Z"
    }
  ]
}
```
