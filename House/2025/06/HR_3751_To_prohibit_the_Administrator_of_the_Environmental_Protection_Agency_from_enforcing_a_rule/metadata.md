# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3751?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3751
- Title: Reliable Grid Act
- Congress: 119
- Bill type: HR
- Bill number: 3751
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2025-10-04T08:06:01Z
- Update date including text: 2025-10-04T08:06:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3751",
    "number": "3751",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "B001316",
        "district": "7",
        "firstName": "Eric",
        "fullName": "Rep. Burlison, Eric [R-MO-7]",
        "lastName": "Burlison",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Reliable Grid Act",
    "type": "HR",
    "updateDate": "2025-10-04T08:06:01Z",
    "updateDateIncludingText": "2025-10-04T08:06:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:04:00Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "WY"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "PA"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "NC"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "SC"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3751ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3751\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Mr. Burlison (for himself, Mr. Gill of Texas , and Ms. Hageman ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit the Administrator of the Environmental Protection Agency from enforcing a rule or regulation that restricts certain operations of certain electric generating units, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reliable Grid Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nreliable, affordable electricity is a fundamental prerequisite for a healthy human environment and must be a central consideration in all regulations;\n**(2)**\nthe Administrator should prioritize the reliability of the electric grid when considering new regulations and avoid imposing any regulations that may compromise such reliability by prematurely retiring essential electric generating units;\n**(3)**\nNERC has already identified the threats of insufficient dispatchable resources and low capacity reserves across the United States, at the same time as demand increases from electrification, including the forced adoption of electric vehicles and the decline of reliable capacity such as natural gas, coal, petroleum, nuclear, and geothermal energy in favor of unreliable solar and wind capacity;\n**(4)**\nthe operators of major regional power grids in the United States notified former Administrator Regan in August 2023, in response to proposed rulemaking, that energy and environmental policies could well exacerbate the disturbing trends and growing risk wherein the pace of retirements of generation with attributes needed to ensure grid reliability is rapidly exceeding the commercialization of new resources capable of providing those reliability attributes ;\n**(5)**\nadministrators under the Biden administration and certain administrations preceding the Biden administration imposed regulations that forced the premature retirement of reliable power generation capacity, which was not replaced with adequate new reliable capacity, primarily from coal and natural gas electric generating units, causing increased shortages of electricity and challenges to the reliable operation of the power grid;\n**(6)**\nsuch regulations included the\u2014\n**(A)**\nNew Source Performance Standards for Greenhouse Gas Emissions From New, Modified, and Reconstructed Fossil Fuel-Fired Electric Generating Units; Emission Guidelines for Greenhouse Gas Emissions From Existing Fossil Fuel-Fired Electric Generating Units; and Repeal of the Affordable Clean Energy Rule (89 Fed. Reg. 39798 (May 9, 2024));\n**(B)**\nNational Emission Standards for Hazardous Air Pollutants: Coal- and Oil-Fired Electric Utility Steam Generating Units Review of the Residual Risk and Technology Review (89 Fed. Reg. 38508 (May 7, 2024)); and\n**(C)**\nSupplemental Effluent Limitations Guidelines and Standards for the Steam Electric Power Generating Point Source Category (89 Fed. Reg. 40198 (May 9, 2024));\n**(7)**\nsuch regulations have led to the retirement of reliable electric generating units and major capacity inadequacies in Texas, California, and other areas across the United States, and regulations continue to threaten the reliability of the grid in the United States;\n**(8)**\njeopardizing the reliability of the electric grid through regulations that have the potential to prematurely retire reliable electric generating units immediately endangers the human environment, health, and life of all individuals in the United States;\n**(9)**\nsuch jeopardization runs counter to the mission of the Environmental Protection Agency to protect human health and the environment ;\n**(10)**\nthe desire of former Administrator Regan to rapidly retire reliable coal and natural gas electric generating units in favor of unreliable solar and wind electric generating units has exacerbated the shortfall of reliable capacity beyond the alarming projections noted by industry in 2023;\n**(11)**\nthe desire of former Administrator Regan to electrify many energy uses, from cooking and heating to transportation, across the United States has exacerbated the threat of capacity inadequacy and reduced the reliability of the electric grid during peak demand periods;\n**(12)**\nthe Administrator should, in coordination with public utilities and operators of electric generating units\u2014\n**(A)**\nidentify the electric generating units in danger of premature retirement because of existing regulations; and\n**(B)**\nprovide waivers, to the extent possible, to prevent the premature shutdown of such electric generating units due to such regulations and support the supply of reliable electricity, especially given the warnings from Chairman Christie of the Federal Energy Regulatory Commission that the United States is heading for a reliability crisis ;\n**(13)**\nthe Federal Energy Regulatory Commission should coordinate with NERC to develop new standards relating to the reliability of the grid in the United States that acknowledge that unreliable solar and wind electric generating units can perform at near-zero capacity during peak demand and under extreme weather conditions;\n**(14)**\nthe operators of regional power grids have assumed a higher level of power generation from such solar and wind electric generating units, which has caused such operators to plan the electric generation resources and dispatchable reserves of such operators poorly; and\n**(15)**\nthe Administrator should halt the implementation of rules and regulations from former Administrator Regan related to the electric power sector and ensure that any future rules related to the electric power sector are proposed concurrently with sufficient evidence that\u2014\n**(A)**\nsuch rules and regulations do not lead to any further premature retirement of a reliable electric generating unit; and\n**(B)**\nthe bulk-power system across all regional transmission organizations and independent system operators in the United States can reliably meet the demand for electricity without frequent outages and inadequately low capacity safety margins.\n#### 3. Prohibition on enforcement of rules and regulations relating to certain electric generating units\nThe Administrator may not enforce a rule or regulation that restricts the continuous, previously permitted operation of any dispatchable electric generating unit unless and until NERC categorizes all areas served by the bulk-power system as normal risk , pursuant to the assessment published by NERC in December 2023 entitled the 2023 Long-Term Reliability Assessment .\n#### 4. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Bulk-power system**\nThe term bulk-power system has the meaning given such term in section 215(a)(1) of the Federal Power Act ( 16 U.S.C. 824o(a)(1) ).\n**(3) Dispatchable electric generating unit**\nThe term dispatchable electric generating unit means any steam generating unit, integrated gasification combined cycle unit, stationary combustion turbine, or other type of unit that generates electricity that\u2014\n**(A)**\nis connected to the bulk-power system and subject to rules and regulations of the Environmental Protection Agency; and\n**(B)**\ncan, on demand, adjust the generation of such generating unit, combined cycle unit, combustion turbine, or other unit with precision to meet the requirements of the bulk-power system.\n**(4) NERC**\nThe term NERC means the North American Electric Reliability Corporation.",
      "versionDate": "2025-06-05",
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
        "updateDate": "2025-06-24T13:35:37Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3751ih.xml"
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
      "title": "Reliable Grid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reliable Grid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Administrator of the Environmental Protection Agency from enforcing a rule or regulation that restricts certain operations of certain electric generating units, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T03:48:42Z"
    }
  ]
}
```
