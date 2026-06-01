# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8483?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8483
- Title: Barona Group of Capitan Grande Band of Mission Indians Land Transfer Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8483
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-27T08:06:21Z
- Update date including text: 2026-05-27T08:06:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-12 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2026-05-21 - Committee: Subcommittee Hearings Held
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-05-12 - Committee: Referred to the Subcommittee on Indian and Insular Affairs.
- 2026-05-21 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8483",
    "number": "8483",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Barona Group of Capitan Grande Band of Mission Indians Land Transfer Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:21Z",
    "updateDateIncludingText": "2026-05-27T08:06:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
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
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Indian and Insular Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:02:20Z",
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
                "date": "2026-05-21T18:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-05-12T21:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Indian and Insular Affairs Subcommittee",
          "systemCode": "hsii24"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8483ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8483\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mr. Issa introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo take certain land in the State of California into trust for the benefit of the Barona Group of Capitan Grande Band of Mission Indians of the Barona Reservation, California, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Barona Group of Capitan Grande Band of Mission Indians Land Transfer Act of 2026 .\n#### 2. Land to be taken into trust for the Barona Group of Capitan Grande Band of Mission Indians\n##### (a) In general\nSubject to valid existing rights and the conditions described in subsections (c) and (d)\u2014\n**(1)**\nadministrative jurisdiction of Parcel 2 and Parcel 3 is transferred to the Secretary; and\n**(2)**\nthe covered land is taken into trust for the benefit of an Indian Tribe.\n##### (b) Administration\nThe land taken into trust under subsection (a) shall be\u2014\n**(1)**\npart of the reservation of the Tribe; and\n**(2)**\nadministered in accordance with the laws and regulations generally applicable to property held in trust by the United States for the benefit of an Indian Tribe.\n##### (c) Conditions\nThe land taken into trust under subsection (a) shall be subject to\u2014\n**(1)**\nall valid liens, rights-of-way, reciprocal road rights-of-way agreements, licenses, leases, permits, and easements existing on the date of the enactment of this Act;\n**(2)**\nthe continuing right of the public to access the land for recreational, scenic, scientific, and conservation uses, to motorized access to roads, and to recreational access to trails, including Bureau of Land Management and Forest Service trails codesignated for public passage, existing on the date of the enactment of this Act, subject to reasonable rules and regulations promulgated by the Tribe in consultation with the Secretary; and\n**(3)**\nsuch rights-of-way as the Secretary, in consultation with the Secretary of Agriculture, considers necessary to provide employees of the Bureau of Land Management and the Forest Service access for emergency purposes, including search and rescue, wildfire suppression, and health and safety evacuation operations.\n##### (d) Gaming prohibited\nThe land taken into trust under subsection (a) shall not be used for any class II gaming or class III gaming under the Indian Gaming Regulatory Act (as those terms are defined in section 4 of that Act ( 25 U.S.C. 2703 )).\n##### (e) Water rights and agreements\nNothing in this Act shall alter, or require the alteration of, any existing water rights or service agreements.\n##### (f) Definitions\nIn this Act:\n**(1) Covered land**\nThe term covered land means all right, title, and interest of the United States in and to Parcel 1, Parcel 2, and Parcel 3.\n**(2) Parcel 1**\nThe term Parcel 1 means the approximately 160 acres of land administered by the Bureau of Land Management generally depicted as 3310810100 on the map titled BLM Lands into Trust for the Barona Band of Mission Indians dated July 24, 2025.\n**(3) Parcel 2**\nThe term Parcel 2 means the approximately 160 acres of land identified on the San Diego County Assessor\u2019s Map as APN 331\u2013081\u201302, comprised of the Southeast Quarter of Section 8, Township 14 South, Range 2 East, San Bernardino Meridian (as delineated in the Official Survey accepted on February 26, 1944).\n**(4) Parcel 3**\nThe term Parcel 3 means the approximately 516.21 acres of land identified as APN 331\u2013090\u201312 on the San Diego County Assessor\u2019s Map, comprised of the following portions of Section 9, Township 14 South, Range 2 East, San Bernardino Meridian (documented in Record of Survey No. 13180, dated May 9, 1991):\n**(A)**\nThe South Half.\n**(B)**\nThe Southeast Quarter of the Northwest Quarter.\n**(C)**\nThe South Half of the Northeast Quarter.\n**(D)**\nThe Northeast Quarter of the Northeast Quarter.\n**(5) Secretary**\nThe term Secretary means the Secretary of the Interior.\n**(6) Tribe**\nThe term Tribe means the Barona Group of Capitan Grande Band of Mission Indians of the Barona Reservation, California.\n**(7) Secretary**\nThe term Secretary means the Secretary of the Interior.",
      "versionDate": "2026-04-23",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2026-05-12T23:43:32Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8483ih.xml"
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
      "title": "Barona Group of Capitan Grande Band of Mission Indians Land Transfer Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Barona Group of Capitan Grande Band of Mission Indians Land Transfer Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To take certain land in the State of California into trust for the benefit of the Barona Group of Capitan Grande Band of Mission Indians of the Barona Reservation, California, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:43Z"
    }
  ]
}
```
