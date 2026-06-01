# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3948?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3948
- Title: Offshore Pipeline Safety Act
- Congress: 119
- Bill type: HR
- Bill number: 3948
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-07-02T18:20:36Z
- Update date including text: 2025-07-02T18:20:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3948",
    "number": "3948",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Offshore Pipeline Safety Act",
    "type": "HR",
    "updateDate": "2025-07-02T18:20:36Z",
    "updateDateIncludingText": "2025-07-02T18:20:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:04:50Z",
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
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3948ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3948\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Ms. Brownley introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require the Bureau of Safety and Environmental Enforcement to further develop, finalize, and implement updated regulations for offshore oil and gas pipelines to address long-standing limitations regarding its ability to ensure active pipeline integrity and address safety and environmental risks associated with decommissioning, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Offshore Pipeline Safety Act .\n#### 2. Finalization of regulations related to offshore pipelines\nNot later than 18 months after the date of enactment of this Act, the Secretary of the Interior, acting through the Director of the Bureau of Safety and Environmental Enforcement, shall issue final regulations relating to Oil and Gas and Sulphur Operations in the Outer Continental Shelf\u2014Pipelines and Pipeline Rights-of-Way (72 Fed. Reg. 56,442 (Oct. 3, 2007)). Such regulations shall require owners of oil and gas pipelines subject to such regulations\u2014\n**(1)**\nto provide for internal and external inspections of pipelines by a third-party no less frequently than every two years, unless the Director of the Bureau determines that any such inspection is not required; and\n**(2)**\nto equip such pipelines with a leak detection system or device that provides continuous volumetric comparison between the pipeline\u2019s product input and output and includes alarms and adequate sensitivity to detect variations between input and discharge volumes to enable any leaks from the pipeline to be detected as quickly as possible.\n#### 3. Addressing environmental risks of decommissioning pipelines\n##### (a) Study on environmental risks of decommissioning pipelines versus removing pipelines\n**(1) Study**\nThe Directors of the Bureau of Safety and Environmental Enforcement and the Bureau of Ocean Energy Management shall jointly conduct a study to evaluate the environmental benefits and risks associated with decommissioning oil and gas pipelines in place on the sea floor compared to removing such pipelines. Such study shall include\u2014\n**(A)**\nan evaluation of pipelines that have been decommissioned in place, identifying decommissioned pipelines at high-risk of causing safety and environmental harm, causing obstructions, or otherwise unduly interfering with present or future uses of the outer continental shelf; and\n**(B)**\nrecommendations on the best uses of the revenues generated by the annual pipelines fees as authorized by subsection (d).\n**(2) Report**\nNot later than 18 months after the date of enactment of this Act, the Directors shall transmit a report to the Committee on Natural Resources of the House of Representatives and the Committee on Energy and Natural Resources of the Senate, detailing the findings and determinations of the study, including any recommendations for legislation.\n##### (b) Required considerations in reviewing decommissioning applications\nIn determining whether to permit an owner to decommission an oil or gas pipeline, the Bureau of Safety and Environmental Enforcement, shall fully consider whether the offshore oil and gas pipeline constitutes a hazard to navigation and commercial and recreational fishing operations, unduly interferes with other uses of the outer continental shelf, or has adverse environmental effects.\n##### (c) Ongoing monitoring of decommissioned pipelines\nThe Bureau of Safety and Environmental Enforcement shall continually monitor the condition and location of all oil and gas pipelines that have been decommissioned and remain in place, and shall maintain all relevant records of such monitoring.\n##### (d) Annual pipeline owners fee\nNot later than 180 after the date of enactment of this Act, the Bureau of Safety and Environmental Enforcement shall issue regulations to assess an annual fee on owners of offshore oil and gas pipelines for the purpose of providing the Bureau with funds to decommission or remove such pipelines in the event an owner files for bankruptcy. Such fee shall be no less than\u2014\n**(1)**\n$10,000 per mile for such pipelines in water with a depth of 500 feet or greater; and\n**(2)**\n$1,000 per mile for pipelines in water depth of under 500 feet.\n#### 4. Requirement relating to exposed segments of offshore pipelines\nIf the Bureau of Safety and Environmental Enforcement identifies any exposed segment of any active or decommissioned pipeline, the Bureau shall either remove the pipeline from the ocean or ensure it is properly decommissioned and does not pose a threat. If a segment of any active pipeline is exposed or shifts, the Bureau shall re-secure such segment to the sea floor.\n#### 5. Completion of study relating to environment risks of chemical products used in oil and gas operations\n##### (a) Completion of study\nThe Bureau of Safety and Environmental Enforcement shall complete a study addressing the risks to the environment of chemical products used in oil and gas operations including umbilical lines. In conducting the study, the Bureau shall seek input from chemical suppliers and the oil and gas industry.\n##### (b) Report\nNot later than two years after the date of enactment of this Act, the Bureau shall transmit a report of the findings and determinations in such study to Congress, including any recommendations for legislation.\n#### 6. Effective Date\nNo provision of this Act shall take effect without considering whether such action will result in a reduction of reef fish habitat.",
      "versionDate": "2025-06-12",
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
        "name": "Energy",
        "updateDate": "2025-07-02T18:20:36Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3948ih.xml"
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
      "title": "Offshore Pipeline Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Offshore Pipeline Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Bureau of Safety and Environmental Enforcement to further develop, finalize, and implement updated regulations for offshore oil and gas pipelines to address long-standing limitations regarding its ability to ensure active pipeline integrity and address safety and environmental risks associated with decommissioning, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T04:48:27Z"
    }
  ]
}
```
