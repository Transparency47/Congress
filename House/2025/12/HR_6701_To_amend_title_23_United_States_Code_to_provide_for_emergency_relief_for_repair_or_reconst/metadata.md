# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6701?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6701
- Title: HEAT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6701
- Origin chamber: House
- Introduced date: 2025-12-12
- Update date: 2026-01-08T19:46:33Z
- Update date including text: 2026-01-08T19:46:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-12: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2025-12-12: Introduced in House

## Actions

- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-12",
    "latestAction": {
      "actionDate": "2025-12-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6701",
    "number": "6701",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001211",
        "district": "4",
        "firstName": "Greg",
        "fullName": "Rep. Stanton, Greg [D-AZ-4]",
        "lastName": "Stanton",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "HEAT Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-08T19:46:33Z",
    "updateDateIncludingText": "2026-01-08T19:46:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
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
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-12",
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
          "date": "2025-12-12T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6701ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6701\nIN THE HOUSE OF REPRESENTATIVES\nDecember 12, 2025 Mr. Stanton (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to provide for emergency relief for repair or reconstruction of infrastructure damaged by extreme heat, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Heat Emergency Assistance for Transportation Act of 2025 or the HEAT Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nExtreme heat, particularly heat waves, are an emerging threat to critical transportation infrastructure.\n**(2)**\nExtreme heat is damaging critical transportation infrastructure.\n**(3)**\nResearch indicates that high temperatures cause bridge expansion joints to crack or fail, accelerate the degradation of concrete and steel, and weaken structural integrity over time.\n**(4)**\nAging infrastructure is at heightened risk.\n**(5)**\nAssessments show more than 85,000 girder or movable bridges are over 50 years old in the United States, carrying 860 million vehicle crossings each day.\n**(6)**\nMany such bridges designed for historical conditions and are now experiencing stress beyond their original design.\n**(7)**\nMovable bridges may face operational challenges, including breakdowns during heat waves.\n**(8)**\nSteel expansion during extreme heat can cause drawbridges and similar structures to jam or fail to close properly.\n**(9)**\nEmergency cooling measures, such as spraying bridges with water, have already been required in cities such as New York, Chicago, Portland, and Seattle.\n**(10)**\nExtreme heat threatens economic continuity.\n**(11)**\nUnplanned bridge closures and roadway restrictions caused by thermal stress interrupt freight movement, supply chains, and daily commuting, imposing significant costs on local economies and national productivity.\n**(12)**\nFederal disaster programs omit extreme heat.\n**(13)**\nWhile section 125 of title 23, United States Code, recognizes disasters such as flooding, severe storms, and wildfires, extreme heat is not explicitly identified as a qualifying event for Emergency Relief funding, despite its clear infrastructure consequences.\n**(14)**\nCommunities can face disproportionate risks.\n**(15)**\nRural areas and regions with limited redundancy in transportation networks are particularly at high risk, as heat-related transportation disruptions can isolate entire communities, delay emergency response, and endanger public safety.\n#### 3. Emergency relief\nSection 125 of title 23, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(1), by inserting extreme heat, after severe storm, ;\n**(2)**\nin subsection (b) by inserting This subsection shall not apply to a bridge with respect to which physical deterioration was substantially caused by extreme heat exposure. after the period at the end; and\n**(3)**\nby striking extreme weather, flooding, and other natural disasters each place it appears and inserting extreme weather, heat waves, flooding, and other natural disasters .\n#### 4. Study on extreme heat events\n##### (a) Study required\nNot later than 1 year after the date of enactment of this Act, the Secretary of Transportation shall enter into an agreement with the Transportation Research Board of the National Academies, in coordination with the Secretary of Transportation, shall conduct a study to\u2014\n**(1)**\nevaluate the measurable costs of an extreme heat event, particularly long-duration, high intensity heat waves;\n**(2)**\nprovide recommendations on how to track damage from extreme heat events, separate from regular deterioration over time; and\n**(3)**\nto examine how the Secretary may better assist State departments of transportation, public transit systems, Amtrak, freight rail systems, and other interested parties with tracking damage from extreme heat events.\n##### (b) Consultation requirements\nIn carrying out the study under this section, the Transportation Research Board shall consult with the Secretary, the Administrator of the Environmental Protection Agency, State departments of transportation, public transit systems, Amtrak, freight rail systems, stakeholders with expertise in engineering and natural disaster management, and educational and technical groups in extreme heat and infrastructure safety.\n##### (c) Report required\nThe Transportation Research Board shall submit to the Secretary, the Committee on Transportation and Infrastructure of the House of Representatives, and the Committee on Environment and Public Works of the Senate a report detailing the results of the study under this section.\n#### 5. Best management practices report\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Transportation shall issue a best management practices report to reflect new information and advancements in highway and bridge safety as related to extreme heat.",
      "versionDate": "2025-12-12",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-08T19:46:33Z"
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
      "date": "2025-12-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6701ih.xml"
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
      "title": "HEAT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:24:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEAT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Heat Emergency Assistance for Transportation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to provide for emergency relief for repair or reconstruction of infrastructure damaged by extreme heat, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:21Z"
    }
  ]
}
```
