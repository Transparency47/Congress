# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1798?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1798
- Title: Autonomous Vehicle Acceleration Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1798
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2025-06-02T13:19:09Z
- Update date including text: 2025-06-02T13:19:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1798",
    "number": "1798",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Autonomous Vehicle Acceleration Act of 2025",
    "type": "S",
    "updateDate": "2025-06-02T13:19:09Z",
    "updateDateIncludingText": "2025-06-02T13:19:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T19:37:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1798is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1798\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Ms. Lummis introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prescribe standards for autonomous vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Autonomous Vehicle Acceleration Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nrapid advancements in autonomous vehicle technology present significant opportunities to improve transportation safety, efficiency, and mobility;\n**(2)**\ncurrent Federal motor vehicle safety standards were not designed with fully autonomous vehicles in mind, creating certification challenges and slowing design and production of vehicles without drivers;\n**(3)**\nmaintaining global leadership in autonomous vehicle technology will enhance the competitiveness of the United States, foster economic growth, and spur innovation across the domestic manufacturing sector; and\n**(4)**\nthe most advanced automated driving systems have demonstrated safety records superior to human drivers in comparable situations, indicating that maintaining regulatory frameworks designed exclusively for human operators may delay lifesaving technological implementation.\n#### 3. Definitions\nIn this Act:\n**(1) Autonomous vehicle**\n**(A) In general**\nThe term autonomous vehicle means a vehicle equipped with an automated driving system that is capable of performing the entire dynamic driving task on a sustained basis without any expected involvement by a human driver.\n**(B) Inclusions**\nThe term autonomous vehicle includes a vehicle equipped with a Level 4 or Level 5 automated driving system.\n**(2) FMVSS**\nThe term FMVSS means a Federal motor vehicle safety standard prescribed under section 30111(a) of title 49, United States Code.\n**(3) SAE International Standard J3016**\nThe term SAE International Standard J3016 means SAE International Recommended Practice entitled Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles , numbered J3016, and dated April 2021 (or a successor standard adopted by the Secretary).\n**(4) SAE terms**\nThe terms automated driving system , Level 4 , and Level 5 have the meanings given those terms in SAE International Standard J3016.\n**(5) Secretary**\nThe term Secretary means the Secretary of Transportation, acting through the Administrator of the National Highway Traffic Safety Administration.\n**(6) Volpe 2016 Report**\nThe term Volpe 2016 Report means the report of the John A. Volpe National Transportation Systems Center of the Department of Transportation entitled Review of Federal Motor Vehicle Safety Standards (FMVSS) for Automated Vehicles: Identifying Potential Barriers and Challenges for the Certification of Automated Vehicles Using Existing FMVSS and dated March 2016.\n#### 4. Implementation of Volpe Center recommendations\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary shall address, in accordance with subsection (b), all certification challenges identified by the Volpe Center 2016 Report relating to\u2014\n**(1)**\nthe presumption of a human driver; and\n**(2)**\nperformance specifications, test procedures, or equipment requirements that do not adequately account for autonomous vehicle designs.\n##### (b) Regulatory updates\nThe Secretary shall, as the Secretary determines appropriate, develop, amend, interpret, exempt from application, or otherwise update any FMVSS requirement or other regulation, guidance, or interpretation under the jurisdiction of the Secretary to ensure that the certification and approval process for Level 4 and Level 5 autonomous vehicles is not unduly obstructed by assumptions of traditional human-driver designs, including requirements relating to seating arrangements, internal cabin configurations, window placement, driver controls, and other features, as determined by the Secretary.\n##### (c) Discretionary compliance determination and rulemaking authority\nAt the discretion of the Secretary, and through such rulemaking as the Secretary determines to be necessary, including by establishing exemption processes for autonomous vehicles consistent with section 30114(a) of title 49, United States Code, autonomous vehicles may be determined to be in compliance with applicable regulations relating to motor vehicle safety, including any FMVSS.\n##### (d) Report\nNot later than 180 days after the date described in subsection (a), the Secretary shall submit to the appropriate committees of Congress a report detailing steps taken by the Secretary under subsection (b) to address the challenges identified by the Volpe Center 2016 described in subsection (a), including any new or revised rules or guidance issued by the Secretary.\n#### 5. Roadmap for future concepts\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary shall develop a roadmap to achieve commercial-scale deployment of Level 4 and Level 5 autonomous vehicles.\n##### (b) Requirements\nThe roadmap required under subsection (a) shall\u2014\n**(1)**\nsupport the design, manufacturing, and deployment of Level 4 and Level 5 autonomous vehicles in the United States;\n**(2)**\npromote United States leadership in global autonomous vehicle markets and supply chains;\n**(3)**\nidentify ways to lower practical, technological, and regulatory barriers to Level 4 and Level 5 autonomous vehicle deployment;\n**(4)**\nrecommend a risk hierarchy involving the use of autonomous vehicles and a standard of safety for autonomous vehicle use;\n**(5)**\nincorporate a supplemental technology assessment, which shall\u2014\n**(A)**\nidentify and address\u2014\n**(i)**\nnew technologies and industry developments since publication of the Volpe 2016 Report;\n**(ii)**\nemerging safety concerns specific to autonomous vehicle operations; and\n**(iii)**\nrecommended updates to the findings or recommendations of the Volpe 2016 Report; and\n**(B)**\non completion, be used by the Secretary to propose any amendments to any existing FMVSS that are necessary to ensure clarity, consistency, and safety for autonomous-vehicle designs; and\n**(6)**\ninclude any additional initiatives or strategies the Secretary determines necessary to achieve the objectives of this Act.\n##### (c) Supplemental technology assessment interim update\nNot later than 180 days after the date of enactment of this Act, the Secretary shall submit to the appropriate committees of Congress a preliminary update describing progress, challenges, and next steps taken by the Secretary to carry out the supplemental technology assessment described in subsection (b)(5).\n##### (d) Roadmap updates\nThe roadmap required under subsection (a) shall be updated periodically, as determined necessary by the Secretary.\n##### (e) Report\nThe Secretary shall submit to the appropriate committees of Congress, and make publicly available, the roadmap required under subsection (a).",
      "versionDate": "2025-05-15",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-02T13:19:09Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1798is.xml"
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
      "title": "Autonomous Vehicle Acceleration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-30T02:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Autonomous Vehicle Acceleration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prescribe standards for autonomous vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:29Z"
    }
  ]
}
```
