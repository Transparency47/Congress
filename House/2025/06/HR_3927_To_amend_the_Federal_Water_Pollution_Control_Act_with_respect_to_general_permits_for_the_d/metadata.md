# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3927?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3927
- Title: Nationwide Permitting Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 3927
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2025-06-26T14:41:24Z
- Update date including text: 2025-06-26T14:41:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-13 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-06-11: Introduced in House

## Actions

- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-13 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3927",
    "number": "3927",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "R000603",
        "district": "7",
        "firstName": "David",
        "fullName": "Rep. Rouzer, David [R-NC-7]",
        "lastName": "Rouzer",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Nationwide Permitting Improvement Act",
    "type": "HR",
    "updateDate": "2025-06-26T14:41:24Z",
    "updateDateIncludingText": "2025-06-26T14:41:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-13",
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
      "actionDate": "2025-06-11",
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
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-13T15:19:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3927ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3927\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mr. Rouzer introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Federal Water Pollution Control Act with respect to general permits for the discharge of dredged or fill material, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nationwide Permitting Improvement Act .\n#### 2. Nationwide permitting improvement\n##### (a) In general\nSection 404(e) of the Federal Water Pollution Control Act ( 33 U.S.C. 1344 ) is amended\u2014\n**(1)**\nby striking (e)(1) In carrying and inserting the following:\n(e) General permits on state, regional, or nationwide basis (1) Permits authorized In carrying ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking (2) No general and inserting the following:\n(2) Term No general ; and\n**(B)**\nby striking five years and inserting ten years ; and\n**(3)**\nby adding at the end the following:\n(3) Considerations In determining the environmental effects of an activity under paragraph (1) or (2), the Secretary\u2014 (A) shall consider only the effects of any discharge of dredged or fill material resulting from such activity; and (B) shall consider any effects of a discharge of dredged or fill material into less than 3 acres of navigable waters to be a minimal adverse environmental effect. (4) Nationwide permits for linear infrastructure projects (A) In general Notwithstanding any other provision of this section, the Secretary shall maintain general permits on a nationwide basis for linear infrastructure projects that result in a discharge of dredged or fill material into less than 3 acres of navigable waters for each single and complete project (as defined in section 330.2 of title 33, Code of Federal Regulations (as in effect on the date of enactment of this paragraph)). (B) Definition of linear infrastructure project In this paragraph, the term linear infrastructure project means a project to carry out any activity required for the construction, expansion, maintenance, modification, or removal of infrastructure and associated facilities for the transmission from a point of origin to a terminal point of communications or electricity, or for the transportation from a point of origin to a terminal point of people, water, wastewater, carbon dioxide, or fuel or hydrocarbons (in the form of a liquid, liquescent, gaseous, or slurry substance or supercritical fluid), including oil and gas pipeline facilities. (5) Reissuance of nationwide permits In determining whether to reissue a general permit issued under this subsection on a nationwide basis\u2014 (A) no consultation with an applicable State pursuant to section 6(a) of the Endangered Species Act of 1973 ( 16 U.S.C. 1535(a) ) is required; (B) no consultation with a Federal agency pursuant to section 7(a)(2) of such Act ( 16 U.S.C. 1536(a)(2) ) is required; and (C) the requirements of section 102(2)(C) of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332(2)(C) ) shall be satisfied by preparing an environmental assessment with respect to such general permit. .\n##### (b) Regulatory revisions required\nThe Secretary of the Army, acting through the Chief of Engineers, shall expeditiously revise the regulations applicable to carrying out section 404(e) of the Federal Water Pollution Control Act ( 33 U.S.C. 1344 ) in order to streamline the processes for issuing general permits under such section to promote efficient and consistent implementation of such section.\n##### (c) Administration of nationwide permit program\nIn carrying out section 404(e) of the Federal Water Pollution Control Act ( 33 U.S.C. 1344 ), including in revising regulations under subsection (b) of this section, the Secretary of the Army, acting through the Chief of Engineers, may not finalize or implement any modification to\u2014\n**(1)**\ngeneral condition 15 (relating to single and complete projects), as included in the final rule titled Reissuance and Modification of Nationwide Permits and published on January 13, 2021, by the Department of the Army, Corps of Engineers (86 Fed. Reg. 2868);\n**(2)**\nthe definition of the term single and complete linear project , as included in such final rule (86 Fed. Reg. 2877); or\n**(3)**\nthe definition of the term single and complete project , as included in section 330.2 of title 33, Code of Federal Regulations (as in effect on the date of enactment of this Act).",
      "versionDate": "2025-06-11",
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
        "updateDate": "2025-06-26T14:41:24Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3927ih.xml"
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
      "title": "Nationwide Permitting Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Nationwide Permitting Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T08:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Water Pollution Control Act with respect to general permits for the discharge of dredged or fill material, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T08:18:23Z"
    }
  ]
}
```
