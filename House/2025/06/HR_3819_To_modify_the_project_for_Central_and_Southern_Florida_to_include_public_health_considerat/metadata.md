# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3819?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3819
- Title: PROTECT Florida Act
- Congress: 119
- Bill type: HR
- Bill number: 3819
- Origin chamber: House
- Introduced date: 2025-06-06
- Update date: 2025-09-08T15:46:30Z
- Update date including text: 2025-09-08T15:46:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-06: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-07 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-06-06: Introduced in House

## Actions

- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-07 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-06",
    "latestAction": {
      "actionDate": "2025-06-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3819",
    "number": "3819",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "M001199",
        "district": "21",
        "firstName": "Brian",
        "fullName": "Rep. Mast, Brian J. [R-FL-21]",
        "lastName": "Mast",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "PROTECT Florida Act",
    "type": "HR",
    "updateDate": "2025-09-08T15:46:30Z",
    "updateDateIncludingText": "2025-09-08T15:46:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-07",
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
      "actionDate": "2025-06-06",
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
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-06",
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
          "date": "2025-06-06T13:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-07T20:29:39Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3819ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3819\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Mr. Mast introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo modify the project for Central and Southern Florida to include public health considerations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prioritizing Revised Operations To Eliminate Cyanobacteria Toxins in Florida Act or the PROTECT Florida Act .\n#### 2. Management of the central and southern Florida system\n##### (a) In general\nThe Assistant Secretary of the Army for Civil Works shall direct the Army Corps of Engineers to modify water infrastructure management in Central and Southern Florida to ensure public health shall overlay all authorized project purposes. Such authorized project purposes shall include\u2014\n**(1)**\nflood control;\n**(2)**\nnavigation;\n**(3)**\nwater supply for agricultural irrigation, municipalities, industry, and Everglades National Park;\n**(4)**\nregional groundwater control, and salinity control;\n**(5)**\nenhancement of fish and wildlife; and\n**(6)**\nrecreation.\n##### (b) Public health\nFor the purposes of this Act, the term public health is defined as follows:\n**(1)**\nManaging Lake Okeechobee and the Central and Southern Florida system\u2014\n**(A)**\nto minimize the potential of toxic cyanobacteria and other harmful algal blooms; and\n**(B)**\nprevent discharges containing cyanobacteria or related toxins into the St. Lucie and Caloosahatchee watersheds, downstream users, and other areas where such cyanobacteria or related toxins will cause or exacerbate public health risks.\n**(2)**\nEnsuring the integrity and stability of the Herbert Hoover Dike.\n**(3)**\nMaintaining all provisions of applicable State, Federal, and Tribal water quality laws, policies, and regulations.\n**(4)**\nEnsuring necessary water volume and quality reaches the greater Everglades, Tribal lands, Everglades National Park, Florida Bay and Caloosahatchee Watershed to restore the natural habitat.\n##### (c) Modification of operations\nThe Secretary of the Army shall modify operations of all current project elements to ensure that public health of all citizens, including downstream users, shall overlay the operating regimes of these various elements.\n##### (d) Master operational manual\nThe Secretary of the Army shall update or develop a Master Operational Manual, in cooperation with the State of Florida, to ensure that all of the various existing operational project elements of the Central and Southern Florida project shall be managed as a system to protect public health and Everglades Restoration. As new elements are completed and added to the project, the Master Operational Manual shall be updated to include the new features.\n##### (e) Study\nThe Secretary of the Army, in conjunction with the National Academies of Sciences, shall undertake a study of the legacy of pollution and nutrient loading as well as the impacts of soil amendments from current and past operational regimes. The study shall include\u2014\n**(1)**\nthe components of the nutrient load and soil amendments, and how this nutrient loading is and will continue to impact Everglades restoration efforts; and\n**(2)**\nproposed solutions to ameliorate the impacts of this pollution to downstream watersheds.\n##### (f) Scope\nNothing in this section shall be construed to alter or amend\u2014\n**(1)**\nthe Water Rights Compact between the State of Florida and the Seminole Tribe of Florida;\n**(2)**\nthe water quality standards of the Miccosukee Tribe of Indians of Florida;\n**(3)**\nState water quality standards, applicable National Pollutant Discharge Elimination System discharge permits, and Everglades Forever Act watershed permits; or\n**(4)**\nthe schedule for completion of the Central Everglades Planning Project or Comprehensive Everglades Restoration Plan projects authorized on or before enactment of this Act.\n##### (g) Prohibition on use of restoration funds\nNo restoration funds shall be used by the Secretary to undertake Deep Well Injection (DWI) of flood or any other excess waters.\n##### (h) Authorization of appropriations\nThere are authorized to be appropriated such sums as are necessary to carry out the provisions of this Act.",
      "versionDate": "2025-06-06",
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
        "name": "Water Resources Development",
        "updateDate": "2025-09-08T15:46:30Z"
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
      "date": "2025-06-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3819ih.xml"
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
      "title": "PROTECT Florida Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-14T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROTECT Florida Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prioritizing Revised Operations To Eliminate Cyanobacteria Toxins in Florida Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-14T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To modify the project for Central and Southern Florida to include public health considerations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-14T04:18:17Z"
    }
  ]
}
```
