# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6129?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6129
- Title: Bidirectional Electric Vehicle Charging Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6129
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2026-01-07T09:05:45Z
- Update date including text: 2026-01-07T09:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-20 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6129",
    "number": "6129",
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
    "title": "Bidirectional Electric Vehicle Charging Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:45Z",
    "updateDateIncludingText": "2026-01-07T09:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-20T18:23:46Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-19T15:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6129ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6129\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Ms. Brownley introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of Energy to develop a National Electric Vehicle Bidirectional Charging Roadmap, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bidirectional Electric Vehicle Charging Act of 2025 .\n#### 2. National Electric Vehicle Bidirectional Charging Roadmap\n##### (a) In general\nThe Secretary of Energy shall develop a National Electric Vehicle Bidirectional Charging Roadmap that includes\u2014\n**(1)**\na timeline and strategy for increasing the development and use of bidirectional charging;\n**(2)**\na list of strategies and obstacles to increasing the development and use of bidirectional charging;\n**(3)**\nkey actions for Congress to consider taking with respect to bidirectional charging matters; and\n**(4)**\ncost estimates for increasing the development and use of bidirectional charging, including a cost estimate for such an increase if such an increase were to be done at a pace that is slow, moderate, or fast.\n##### (b) Publication\nNot later than 12 months after the date of enactment of this Act, the Secretary of Energy shall submit to the Committee on Energy and Commerce of the House of Representatives, and make available to the public, including on the public website of the Department of Energy, the National Electric Vehicle Bidirectional Charging Roadmap developed under subsection (a).\n#### 3. Technical standards and requirement for bidirectional charging\n##### (a) Regulations\nNot later than 2 years after the date of enactment of this Act, the Secretary of Energy shall issue regulations\u2014\n**(1)**\nestablishing technical standards for manufacturers of electric vehicles to standardize bidirectional charging technology; and\n**(2)**\nrequiring that all new electric vehicles manufactured beginning in model year 2029 and thereafter be capable of bidirectional charging, including electric vehicles that are light-duty motor vehicles and school buses, except as exempted by the Secretary of Energy, as the Secretary determines appropriate.\n##### (b) Civil penalties\n**(1) In general**\nA person that violates a regulation issued under this section is liable to the United States Government for a civil penalty of not more than $21,000 for each violation. A separate violation occurs for each electric vehicle or item of electric vehicle equipment and for each failure or refusal to allow or perform an act required by this section and the regulations thereunder. The maximum penalty under this subsection for a related series of violations is $105,000,000.\n**(2) Compromise**\n**(A) In general**\nThe Secretary of Energy may compromise the amount of a civil penalty imposed under this section.\n**(B) Relevant Factors in Determining Amount of Penalty or Compromise**\nIn determining the amount of a civil penalty or compromise under this section, the Secretary of Energy shall consider the nature, circumstances, extent, and gravity of the violation. Such determination shall include, as appropriate\u2014\n**(i)**\nthe nature of the defect or noncompliance;\n**(ii)**\nknowledge by the person charged of its obligations under this section;\n**(iii)**\nthe number of electric vehicles or items of electric vehicle equipment distributed with the defect or noncompliance;\n**(iv)**\nactions taken by the person charged to identify, investigate, or mitigate the condition;\n**(v)**\nthe appropriateness of such penalty in relation to the size of the business of the person charged, including the potential for undue adverse economic impacts;\n**(vi)**\nwhether the person has been assessed civil penalties under this section during the most recent 5 years; and\n**(vii)**\nother appropriate factors.\n#### 4. Disaster recovery plans\nThe Administrator of the Federal Emergency Management Agency shall issue such regulations as are necessary to require that hazard mitigation plans submitted by States or local governments under section 322 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5165 ) incorporate bidirectional charging capabilities.\n#### 5. Definitions\nIn this Act:\n**(1) Bidirectional charging**\nThe term bidirectional charging means, with respect to an electric vehicle, that the electric vehicle can receive energy from electric vehicle supply equipment and provide energy to an external load when it is paired with similarly capable electric vehicle supply equipment.\n**(2) Electric vehicle**\nThe term electric vehicle means a vehicle designed to operate exclusively on electricity stored in a rechargeable battery, multiple batteries, or battery pack.",
      "versionDate": "2025-11-19",
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
        "updateDate": "2025-12-06T13:43:40Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6129ih.xml"
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
      "title": "Bidirectional Electric Vehicle Charging Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T10:08:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bidirectional Electric Vehicle Charging Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-03T10:08:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Energy to develop a National Electric Vehicle Bidirectional Charging Roadmap, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-03T10:03:30Z"
    }
  ]
}
```
