# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1858?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1858
- Title: Flooding Prevention, Assessment, and Restoration Act
- Congress: 119
- Bill type: HR
- Bill number: 1858
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2025-12-19T09:07:37Z
- Update date including text: 2025-12-19T09:07:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1858",
    "number": "1858",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "D000230",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Davis, Donald G. [D-NC-1]",
        "lastName": "Davis",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Flooding Prevention, Assessment, and Restoration Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:37Z",
    "updateDateIncludingText": "2025-12-19T09:07:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:50:07Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "IA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "HI"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "IA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "IL"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1858ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1858\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Davis of North Carolina (for himself, Mr. Feenstra , Ms. Tokuda , Mr. Nunn of Iowa , Mr. Rouzer , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Credit Act of 1978 with respect to the emergency watershed program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Flooding Prevention, Assessment, and Restoration Act .\n#### 2. Emergency watershed program\nSection 403 of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2203 ) is amended by adding at the end the following:\n(c) Level of restoration In carrying out this section, the Secretary may undertake measures that increase the level of protection above that which would be necessary to address the immediate impairment of the watershed if the Secretary determines that such restoration is\u2014 (1) in the best interest of the long-term health and the protection of the watershed from repetitive impairments; and (2) cost-effective and appropriate, given risks to the environment. .\n#### 3. National agriculture flood vulnerability study\nNot later than 2 years after the date of enactment of this Act, the Secretary of Agriculture shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a national agriculture flood vulnerability report containing the results of a conservation effects assessment project studying flood risk on agricultural lands, including\u2014\n**(1)**\nan analysis of economic losses of crops and livestock resulting from flooding under different recurrence scenarios;\n**(2)**\nan analysis of the downstream effects of mitigation activities carried out as part of a watershed management approach;\n**(3)**\nan analysis of available Federal and State data relating to flood risk, as applicable to agricultural land, including data relating to riverine flooding, coastal flooding, storm surge, extreme precipitation, and flash flooding; and\n**(4)**\na description of ongoing producer-level conservation practices and broader government initiatives to manage flooding impact and flood risk within and across watersheds, and recommendations for additional practices and initiatives to further address such impact and risk.\n#### 4. Rehabilitation of structural measures near, at, or past their evaluated life expectancy\nThe Watershed Protection and Flood Prevention Act is amended\u2014\n**(1)**\nin section 2 ( 16 U.S.C. 1002 ), by striking respectively. and all that follows through must contain and inserting respectively. Each project, other than a rehabilitation project under section 14, must contain ; and\n**(2)**\nin section 14(b)(2) ( 16 U.S.C. 1012(b)(2) ), by striking 65 percent and inserting 90 percent .",
      "versionDate": "2025-03-05",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-03-28T15:16:59Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1858ih.xml"
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
      "title": "Flooding Prevention, Assessment, and Restoration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Flooding Prevention, Assessment, and Restoration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Credit Act of 1978 with respect to the emergency watershed program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:29Z"
    }
  ]
}
```
