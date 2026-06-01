# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1876?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1876
- Title: Stratton Ridge Air Force Memorial Act
- Congress: 119
- Bill type: S
- Bill number: 1876
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-04-08T23:44:44Z
- Update date including text: 2026-04-08T23:44:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- 2025-10-21 - Committee: Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 215.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- 2025-10-21 - Committee: Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Committee: Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.
- 2025-10-27 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 215.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1876",
    "number": "1876",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Stratton Ridge Air Force Memorial Act",
    "type": "S",
    "updateDate": "2026-04-08T23:44:44Z",
    "updateDateIncludingText": "2026-04-08T23:44:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-27",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 215.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-27",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-27",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Reported by Senator Boozman without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Agriculture, Nutrition, and Forestry. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
            "date": "2025-10-27T22:51:12Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-21T20:01:17Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-22T17:18:28Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "NC"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-01-05",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1876is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1876\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Tillis (for himself and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo authorize the Secretary of Agriculture to relocate a memorial honoring the 9 Air Force crew members who lost their lives in an airplane crash in the Cherokee and Nantahala National Forests during a training mission on August 31, 1982.\n#### 1. Short title\nThis Act may be cited as the Stratton Ridge Air Force Memorial Act .\n#### 2. Relocation of memorial honoring the 9 Air Force crew members who lost their lives in an airplane crash during a training mission on August 31, 1982\n##### (a) In general\nWith the consent of the owner of the private land adjacent to the Cherohala Skyway in the State of North Carolina on which there is located a memorial honoring the 9 members of the Air Force crew of the C\u2013141B transport plane that crashed during a training mission over the Cherokee and Nantahala National Forests on August 31, 1982 (referred to in this section as the memorial ), and subject to subsections (b) through (e), the Secretary of Agriculture (referred to in this section as the Secretary ) may authorize, by special use authorization, the installation and any maintenance associated with the installation of the memorial at an appropriate site at the Stratton Ridge rest area located at mile marker 2 on the Cherohala Skyway in Graham County, North Carolina, in the Nantahala National Forest.\n##### (b) Site approval\nThe site at which the memorial is installed under subsection (a) is subject to approval by the Secretary, in concurrence with\u2014\n**(1)**\nthe North Carolina Department of Transportation; and\n**(2)**\nin a case in which the site is located adjacent to a Federal-aid highway, the Administrator of the Federal Highway Administration.\n##### (c) Funding\nNo Federal funds may be used to relocate, install, or maintain the memorial under subsection (a).\n##### (d) Costs\nThe individual or entity requesting the installation of the memorial on National Forest System land under subsection (a) shall be responsible for the costs associated with the use of National Forest System land for the memorial, including the costs of\u2014\n**(1)**\nprocessing the application for the relocation;\n**(2)**\nissuing a special use authorization for the memorial, including the costs associated with any related environmental analysis; and\n**(3)**\nrelocating, installing, and maintaining the memorial.\n##### (e) Terms and conditions\nThe special use authorization for the installation of the memorial under subsection (a) may include any terms and conditions that are determined to be appropriate by the Secretary, including a provision preventing any enlargement or expansion of the memorial.",
      "versionDate": "2025-05-22",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1876rs.xml",
      "text": "II\nCalendar No. 215\n119th CONGRESS\n1st Session\nS. 1876\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Tillis (for himself and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nOctober 27, 2025 Reported by Mr. Boozman , without amendment\nA BILL\nTo authorize the Secretary of Agriculture to relocate a memorial honoring the 9 Air Force crew members who lost their lives in an airplane crash in the Cherokee and Nantahala National Forests during a training mission on August 31, 1982.\n#### 1. Short title\nThis Act may be cited as the Stratton Ridge Air Force Memorial Act .\n#### 2. Relocation of memorial honoring the 9 Air Force crew members who lost their lives in an airplane crash during a training mission on August 31, 1982\n##### (a) In general\nWith the consent of the owner of the private land adjacent to the Cherohala Skyway in the State of North Carolina on which there is located a memorial honoring the 9 members of the Air Force crew of the C\u2013141B transport plane that crashed during a training mission over the Cherokee and Nantahala National Forests on August 31, 1982 (referred to in this section as the memorial ), and subject to subsections (b) through (e), the Secretary of Agriculture (referred to in this section as the Secretary ) may authorize, by special use authorization, the installation and any maintenance associated with the installation of the memorial at an appropriate site at the Stratton Ridge rest area located at mile marker 2 on the Cherohala Skyway in Graham County, North Carolina, in the Nantahala National Forest.\n##### (b) Site approval\nThe site at which the memorial is installed under subsection (a) is subject to approval by the Secretary, in concurrence with\u2014\n**(1)**\nthe North Carolina Department of Transportation; and\n**(2)**\nin a case in which the site is located adjacent to a Federal-aid highway, the Administrator of the Federal Highway Administration.\n##### (c) Funding\nNo Federal funds may be used to relocate, install, or maintain the memorial under subsection (a).\n##### (d) Costs\nThe individual or entity requesting the installation of the memorial on National Forest System land under subsection (a) shall be responsible for the costs associated with the use of National Forest System land for the memorial, including the costs of\u2014\n**(1)**\nprocessing the application for the relocation;\n**(2)**\nissuing a special use authorization for the memorial, including the costs associated with any related environmental analysis; and\n**(3)**\nrelocating, installing, and maintaining the memorial.\n##### (e) Terms and conditions\nThe special use authorization for the installation of the memorial under subsection (a) may include any terms and conditions that are determined to be appropriate by the Secretary, including a provision preventing any enlargement or expansion of the memorial.",
      "versionDate": "2025-10-27",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-05-23",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "3584",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stratton Ridge Air Force Memorial Act",
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
            "name": "Forests, forestry, trees",
            "updateDate": "2025-12-12T20:54:32Z"
          },
          {
            "name": "Military history",
            "updateDate": "2025-12-12T20:54:32Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2025-12-12T20:54:32Z"
          },
          {
            "name": "North Carolina",
            "updateDate": "2025-12-12T20:54:32Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-12-12T20:54:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-06-18T15:43:31Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1876is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1876rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Stratton Ridge Air Force Memorial Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T12:04:06Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Stratton Ridge Air Force Memorial Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-29T06:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stratton Ridge Air Force Memorial Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Secretary of Agriculture to relocate a memorial honoring the 9 Air Force crew members who lost their lives in an airplane crash in the Cherokee and Nantahala National Forests during a training mission on August 31, 1982.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:33:19Z"
    }
  ]
}
```
