# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2437?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2437
- Title: Snow Water Supply Forecasting Program Reauthorization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2437
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2437",
    "number": "2437",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Snow Water Supply Forecasting Program Reauthorization Act of 2025",
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
      "actionDate": "2025-07-24",
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
      "actionDate": "2025-07-24",
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
          "date": "2025-07-24T16:38:01Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:04Z",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2437is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2437\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Mr. Hickenlooper (for himself and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Snow Water Supply Forecasting Program Authorization Act to reauthorize the Snow Water Supply Forecasting Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Snow Water Supply Forecasting Program Reauthorization Act of 2025 .\n#### 2. Snow Water Supply Forecasting Program\nThe Snow Water Supply Forecasting Program Authorization Act ( 43 U.S.C. 1477 ) is amended\u2014\n**(1)**\nin subsection (c)(2)\u2014\n**(A)**\nin subparagraph (A), by striking culminating in the report required under subsection (d)(3) and inserting with an emphasis on development and deployment of technologies that integrate snowpack measuring and modeling ; and\n**(B)**\nin subparagraph (B), by striking after submitting the report required by subsection (d)(3), ;\n**(2)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the paragraph heading, by inserting with integrated modeling after data ;\n**(ii)**\nin the matter preceding subparagraph (A), by striking emerging technologies for snowpack measurement, such as and inserting technologies for snowpack measurements and models, including ;\n**(iii)**\nin subparagraph (B), by striking and at the end; and\n**(iv)**\nby striking subparagraph (C) and inserting the following:\n(C) imaging spectroscopy; (D) machine learning; (E) integrated snowpack and hydrologic modeling; and (F) other technologies that the Secretary determines are likely to provide more accurate or timely snowpack measurement data to inform water management and reservoir operations. ;\n**(B)**\nin paragraph (2), by striking emerging technologies for snowpack measurement and inserting technologies for snowpack measurement, including the Department of Agriculture and the National Oceanic and Atmospheric Administration ; and\n**(C)**\nby striking paragraph (3);\n**(3)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking After submitting the report required under subsection (d)(3), the and inserting The ; and\n**(ii)**\nby inserting and water supply forecasts after snowpack measurement ; and\n**(B)**\nby striking paragraph (2) and inserting the following:\n(2) Focus The program shall focus on activities that will maintain, establish, expand, or advance snowpack measurement and integrated modeling, with an emphasis on\u2014 (A) enhancing activities to achieve improved snow and water supply forecasting results that are more responsive to changing weather and watershed conditions; (B) activities in river basins where activities described in this section relating to snowpack measurement and water supply forecasting can inform water management decisions or models at a multi-water user, multi-basin, or multi-State scale, including interstate water management decisions; and (C) building the capacity of program partners to implement and adapt to the new measurement and forecasting capabilities enabled under the program. ;\n**(4)**\nin subsection (f)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking this Act and inserting the Snow Water Supply Forecasting Program Reauthorization Act of 2025 ;\n**(B)**\nin paragraph (2), by striking or sub-basin ;\n**(C)**\nby redesignating paragraph (2) as paragraph (3); and\n**(D)**\nby striking paragraph (1) and inserting the following:\n(1) a list of basins for which snowpack measurement and integrated modeling technologies are being used under the program, including a description of each application, outcome, and data resource used; (2) an assessment of which technologies best inform water supply forecasting for multiple water districts, communities, or States; and ; and\n**(5)**\nin subsection (g), by striking $15,000,000, in the aggregate, for fiscal years 2022 through 2026 and inserting $6,500,000 for each of fiscal years 2027 through 2031 .",
      "versionDate": "2025-07-24",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-09-15T15:58:30Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-09-15T15:58:30Z"
          },
          {
            "name": "Environmental technology",
            "updateDate": "2025-09-15T15:58:30Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2025-09-15T15:58:30Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2025-09-15T15:58:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2025-09-12T19:51:59Z"
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
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2437is.xml"
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
      "title": "Snow Water Supply Forecasting Program Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Snow Water Supply Forecasting Program Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Snow Water Supply Forecasting Program Authorization Act to reauthorize the Snow Water Supply Forecasting Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:38Z"
    }
  ]
}
```
