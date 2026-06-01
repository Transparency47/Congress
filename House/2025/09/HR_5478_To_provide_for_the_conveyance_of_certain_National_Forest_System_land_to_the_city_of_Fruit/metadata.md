# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5478?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5478
- Title: Fruit Heights Land Conveyance Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5478
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2026-02-27T16:28:29Z
- Update date including text: 2026-02-27T16:28:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-03 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-02-10 - Committee: Subcommittee Hearings Held
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-03 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-02-10 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5478",
    "number": "5478",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Fruit Heights Land Conveyance Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-27T16:28:29Z",
    "updateDateIncludingText": "2026-02-27T16:28:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
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
      "actionDate": "2026-02-03",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:07:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-10T19:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-02-03T18:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
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
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5478ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5478\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Moore of Utah (for himself and Ms. Maloy ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo provide for the conveyance of certain National Forest System land to the city of Fruit Heights, Utah, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fruit Heights Land Conveyance Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) City**\nThe term City means the city of Fruit Heights, Utah.\n**(2) Map**\nThe term map means the map entitled Fruit Heights City US Forest Service Land Conveyance and dated March, 2024.\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Chief of the Forest Service.\n#### 3. Conveyance of certain National Forest System land to the city of Fruit Heights, Utah\n##### (a) In general\nNot later than 30 days after the date of the enactment of this Act, the Secretary shall convey to the City all right, title, and interest of the United States in and to the property described in subsection (b)(1).\n##### (b) Description of property\n**(1) In general**\nThe property referred to in subsection (a) is the parcel of real property, including all land and improvements, generally depicted as conveyance area on the map, consisting of approximately 295.89 acres of National Forest System land located in the Uinta-Wasatch-Cache National Forest.\n**(2) Map**\n**(A) Minor errors**\nThe Secretary may correct minor errors in the map.\n**(B) Availability**\nA copy of the map shall be on file and available for public inspection in the appropriate offices of the Forest Service.\n##### (c) Survey\n**(1) In general**\nThe exact acreage and legal description of the covered land may be determined by a survey satisfactory to the Secretary.\n**(2) Costs**\nThe City shall pay the reasonable survey costs and other administrative costs associated with a survey conducted under paragraph (1).\n##### (d) Terms and conditions\nThe conveyance under subsection (a) shall be\u2014\n**(1)**\nsubject to valid existing rights;\n**(2)**\nmade without consideration;\n**(3)**\nmade by quitclaim deed;\n**(4)**\nsubject to such other terms and conditions as the Secretary considers appropriate to protect the interests of the United States; and\n**(5)**\nmade with a reservation of an easement for the Bonneville Shoreline Trail.\n##### (e) Use\nAs a condition of the conveyance under subsection (a), the City shall use the covered land only for public purposes.\n##### (f) Reversionary interest\nIf any of the land conveyed under subsection (a) is used in a manner inconsistent with subsection (e), all right, title, and interest in and to the land shall revert to the Secretary, at the discretion of the Secretary.",
      "versionDate": "2025-09-18",
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
            "name": "Geography and mapping",
            "updateDate": "2026-02-27T16:28:28Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2026-02-27T16:28:24Z"
          },
          {
            "name": "Utah",
            "updateDate": "2026-02-27T16:28:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-01T16:36:42Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5478ih.xml"
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
      "title": "Fruit Heights Land Conveyance Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fruit Heights Land Conveyance Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the conveyance of certain National Forest System land to the city of Fruit Heights, Utah, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T04:48:12Z"
    }
  ]
}
```
