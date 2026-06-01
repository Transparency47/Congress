# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4961?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4961
- Title: Public Utility Remediation and Enhancement for Water Act
- Congress: 119
- Bill type: HR
- Bill number: 4961
- Origin chamber: House
- Introduced date: 2025-08-12
- Update date: 2025-10-07T08:05:42Z
- Update date including text: 2025-10-07T08:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-12: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-13 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-08-12: Introduced in House

## Actions

- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-13 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-12",
    "latestAction": {
      "actionDate": "2025-08-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4961",
    "number": "4961",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "S001221",
        "district": "3",
        "firstName": "Hillary",
        "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
        "lastName": "Scholten",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Public Utility Remediation and Enhancement for Water Act",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:42Z",
    "updateDateIncludingText": "2025-10-07T08:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-13",
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
      "actionDate": "2025-08-12",
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
      "actionDate": "2025-08-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-12",
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
          "date": "2025-08-12T13:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-08-13T21:35:04Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "PA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "AL"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "MI"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "PA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "TN"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "NY"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "MI"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "TX"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4961ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4961\nIN THE HOUSE OF REPRESENTATIVES\nAugust 12, 2025 Ms. Scholten (for herself, Mr. Fitzpatrick , Ms. Sewell , Ms. Stevens , Mr. Deluzio , Mr. Cohen , Mr. Huffman , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Federal Water Pollution Control Act to direct the Administrator of the Environmental Protection Agency to establish a program to provide grants to owners and operators of publicly owned treatment works for use complying with requirements regarding the treatment of emerging contaminants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Utility Remediation and Enhancement for Water Act .\n#### 2. Grants for treatment of emerging contaminants\nTitle II of the Federal Water Pollution Control Act ( 33 U.S.C. 1281 et seq. ) is amended by adding at the end the following new section:\n228. Emerging contaminants (a) In general Not later than 180 days after the date of enactment of this section, the Administrator shall establish a program under which the Administrator may award grants to an owner or operator of a publicly owned treatment works for use\u2014 (1) in the planning, design, and construction of treatment works to prevent, limit, or treat the discharge of a perfluoroalkyl substance, a polyfluoroalkyl substance, or any other emerging contaminant, as identified by the Administrator; or (2) complying with the requirements of a pretreatment standard or an effluent limitation under this Act that relates to the introduction or discharge of a perfluoroalkyl substance, a polyfluoroalkyl substance, or any other emerging contaminant, as identified by the Administrator. (b) Cost sharing (1) Federal share The Federal share of the cost of activities carried out using grant funds awarded under subsection (a) shall be not less than 75 percent of the total estimated cost of such activities. (2) Non-Federal share The applicable non-Federal share of the total estimated cost of such activities may include, in any amount, public and private funds and in-kind services, and may include, notwithstanding section 603(h), financial assistance, including loans, from a State water pollution control revolving fund. (c) Administrative requirements (1) In general An activity carried out using grant funds awarded under subsection (a) shall be carried out subject to the same requirements as a project that receives assistance from a State water pollution control revolving fund under title VI, except to the extent that the Administrator determines that a requirement of title VI is inconsistent with the purposes of this section. (2) Limitation For the purposes of this subsection, the Administrator may not determine that a requirement of title VI relating to the application of section 513 or 608 are inconsistent with the purposes of this section. (d) Authorization of appropriations There is authorized to be appropriated to the Administrator to carry out this section $200,000,000 for each of fiscal years 2026 through 2028. .",
      "versionDate": "2025-08-12",
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
        "name": "Environmental Protection",
        "updateDate": "2025-09-19T14:20:18Z"
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
      "date": "2025-08-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4961ih.xml"
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
      "title": "Public Utility Remediation and Enhancement for Water Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Public Utility Remediation and Enhancement for Water Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Water Pollution Control Act to direct the Administrator of the Environmental Protection Agency to establish a program to provide grants to owners and operators of publicly owned treatment works for use complying with requirements regarding the treatment of emerging contaminants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T08:18:19Z"
    }
  ]
}
```
