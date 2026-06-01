# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/437?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/437
- Title: SNOW Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 437
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-03-07T21:36:22Z
- Update date including text: 2025-03-07T21:36:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-16 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-16 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/437",
    "number": "437",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "K000402",
        "district": "26",
        "firstName": "Timothy",
        "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
        "lastName": "Kennedy",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "SNOW Act of 2025",
    "type": "HR",
    "updateDate": "2025-03-07T21:36:22Z",
    "updateDateIncludingText": "2025-03-07T21:36:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-16T15:36:30Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr437ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 437\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Kennedy of New York introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to expand assistance related to winter storms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Support Neighborhoods Offset Winter Damage Act of 2025 or the SNOW Act of 2025 .\n#### 2. Winter storms\n##### (a) Use of assistance for winter storms\nSection 404 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170c ) is amended by adding at the end the following:\n(h) Use of assistance for winter storms Recipients of hazard mitigation assistance provided under this section and section 203 may use the assistance to conduct activities to help reduce the risk of future damage, hardship, loss, or suffering in any area affected by a winter storm, including acquiring equipment to remove snow. (i) Winter storm defined In this section, the term winter storm means a combination of heavy snow, blowing snow, or dangerous wind chills, as determined by the Administrator. .\n##### (b) Waiver of snowfall methodology and damages requirement\nThe Administrator of the Federal Emergency Management Agency shall, by rule, establish a process to waive the methodology related to the amount of snowfall required to declare a winter storm eligible for a major disaster declaration and to waive the statewide total damages required for such eligibility, if at least 2 of the following conditions are met for a response zone or region affected by a winter storm:\n**(1)**\nA State emergency management agency determines in writing that the damages of such winter storm exceed the damages required for such State to issue a disaster declaration for such a response zone or region.\n**(2)**\nThe National Weather Service determines that, during such winter storm, such a response zone or region has experienced\u2014\n**(A)**\nwind speeds that are greater than 58 miles per hour and a wind chill below 0 degrees Fahrenheit; or\n**(B)**\nlake-effect snow and conditions for more than 24 hours.\n**(3)**\nThe Bureau of the Census determines that such a response zone or region\u2014\n**(A)**\nrepresents a population for which the real median household income is below the real median household income in the United States; or\n**(B)**\nis an area that is not an urban area.\n##### (c) Regulations related to winter storms\n**(1) In general**\nThe Administrator of the Federal Emergency Management Agency shall issue such regulations, as may be necessary or appropriate, as follows:\n**(A)**\nTo provide assistance for winter storms authorized under sections 402, 403, 406, 407, 418, 419, 421(d), 502, and 503 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170a , 5170b, 5172, 5173, 5185, 5186, 5188(d), 5192, 5193) related to the following:\n**(i)**\nDebris removal.\n**(ii)**\nRoads and bridges.\n**(iii)**\nWater control facilities.\n**(iv)**\nPublic buildings and contents.\n**(v)**\nPublic utilities.\n**(vi)**\nParks, recreational, and other facilities.\n**(B)**\nTo provide assistance for winter storms authorized under sections 408 and 503 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174 , 5193) when the State emergency management agency determines that the magnitude or estimated threat of an incident in a response zone or region exceeds the capacity of the State or local government (as such term is defined in section 102 of such Act ( 42 U.S.C. 5122 )) with jurisdiction over such response zone or region to respond or recover.\n##### (d) Definitions\nIn this section:\n**(1) Response zone or region**\nThe term response zone or region means an area that a State emergency management agency has listed as a response zone or region for the purpose of determining any damages required for such State to issue a disaster declaration.\n**(2) Winter storm**\nThe term winter storm has the meaning given in section 404(i) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170c(i) ), as added by subsection (a) of this section.\n#### 3. Federal cost share\nThe Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 et seq. ) is amended\u2014\n**(1)**\nin section 403\u2014\n**(A)**\nby amending subsection (b) to read as follows:\n(b) Federal share (1) In general The Federal share of assistance under this section shall be not less than 75 percent of the eligible cost of such assistance. (2) Rural or disadvantaged areas Notwithstanding paragraph (1), the Federal share of assistance under this section shall be not less than 90 percent of the eligible cost of such assistance in a rural or disadvantaged area. ; and\n**(B)**\nby adding at the end the following:\n(e) Rural or disadvantaged area defined In this section, the term rural or disadvantaged area means an area that the Bureau of the Census has determined\u2014 (1) represents a population for which the real median household income is below the real median household income in the United States; or (2) is not an urban area. ;\n**(2)**\nin section 404\u2014\n**(A)**\nby striking (a) In General. \u2014The President and inserting the following:\n(a) Federal share (1) In general The President ; and\n**(B)**\nin subsection (a), by adding at the end the following:\n(2) Disadvantaged urban communities Notwithstanding paragraph (1), the President may contribute up to 90 percent of the cost of hazard mitigation measures which the President has determined are cost effective and which substantially reduce the risk of, or increase resilience to, future damage, hardship, loss, or suffering in a rural or disadvantaged area (as such term is defined in section 403) affected by a major disaster, or by a fire for which assistance was provided under section 420. Such measures shall be identified following the evaluation of natural hazards under section 322 and shall be subject to approval by the President. Subject to section 322, the total of contributions under this section for a major disaster or event under section 420 shall not exceed 15 percent for amounts not more than $2,000,000,000, 10 percent for amounts of more than $2,000,000,000 and not more than $10,000,000,000, and 7.5 percent on amounts of more than $10,000,000,000 and not more than $35,333,000,000 of the estimated aggregate amount of grants to be made (less any associated administrative costs) under this Act with respect to the major disaster or event under section 420. ;\n**(3)**\nby amending section 407(d) to read as follows:\n(d) Federal share (1) In general The Federal share of assistance under this section shall be not less than 75 percent of the eligible cost of debris and wreckage removal carried out under this section. (2) Rural or disadvantaged areas Notwithstanding paragraph (1), the Federal share of assistance under this section shall be not less than 90 percent of the eligible cost of debris and wreckage removal carried out under this section in a rural or disadvantaged area (as such term is defined in section 403). ; and\n**(4)**\nby amending section 503(a) to read as follows:\n(a) Federal share (1) In general The Federal share for assistance provided under this title shall be equal to not less than 75 percent of the eligible costs. (2) Rural or disadvantaged areas Notwithstanding paragraph (1), the Federal share of assistance under this title shall be not less than 90 percent of the eligible costs in a rural or disadvantaged area (as such term is defined in section 403). .",
      "versionDate": "2025-01-15",
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
        "name": "Emergency Management",
        "updateDate": "2025-02-18T20:52:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr437",
          "measure-number": "437",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr437v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Support Neighborhoods Offset Winter Damage Act of 2025 or the SNOW Act of 2025</strong></p><p>This bill authorizes Federal Emergency Management Agency (FEMA) grant funding for winter storm hazard mitigation and requires FEMA rulemaking to expand\u00a0assistance for winter storms. It also increases the federal cost share for various FEMA grants, for any hazard type, in rural or disadvantaged areas.</p><p>The bill specifically authorizes the use of grant funding under the Hazard Mitigation Grant Program (HMGP) and Building Resilient Infrastructure and Communities program\u00a0to reduce the risk of future damage in areas affected by winter storms, such as by\u00a0acquiring snow removal equipment.\u00a0</p><p>Also, under current FEMA policy, in determining eligibility and recommending a presidential major disaster declaration for a snowstorm, FEMA\u2019s considerations include whether data shows record (or near record) snowfall and whether estimated statewide costs meet applicable thresholds. The bill requires FEMA to create regulations waiving these eligibility requirements for a major disaster declaration for a snowstorm in certain circumstances. FEMA must also create regulations to provide certain\u00a0assistance for winter storms, including for debris removal and specified infrastructure, as well as individual and emergency assistance when the state determines the storm exceeds state and local capacity.\u00a0</p><p>In addition, for any hazard type, the bill requires FEMA to increase the federal cost share from 75% to 90% for certain assistance provided in rural or disadvantaged areas.\u00a0It also authorizes\u00a0an increased HMGP federal cost share amount from 75% to 90% for assistance\u00a0in rural or disadvantaged areas.\u00a0</p>"
        },
        "title": "SNOW Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr437.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Support Neighborhoods Offset Winter Damage Act of 2025 or the SNOW Act of 2025</strong></p><p>This bill authorizes Federal Emergency Management Agency (FEMA) grant funding for winter storm hazard mitigation and requires FEMA rulemaking to expand\u00a0assistance for winter storms. It also increases the federal cost share for various FEMA grants, for any hazard type, in rural or disadvantaged areas.</p><p>The bill specifically authorizes the use of grant funding under the Hazard Mitigation Grant Program (HMGP) and Building Resilient Infrastructure and Communities program\u00a0to reduce the risk of future damage in areas affected by winter storms, such as by\u00a0acquiring snow removal equipment.\u00a0</p><p>Also, under current FEMA policy, in determining eligibility and recommending a presidential major disaster declaration for a snowstorm, FEMA\u2019s considerations include whether data shows record (or near record) snowfall and whether estimated statewide costs meet applicable thresholds. The bill requires FEMA to create regulations waiving these eligibility requirements for a major disaster declaration for a snowstorm in certain circumstances. FEMA must also create regulations to provide certain\u00a0assistance for winter storms, including for debris removal and specified infrastructure, as well as individual and emergency assistance when the state determines the storm exceeds state and local capacity.\u00a0</p><p>In addition, for any hazard type, the bill requires FEMA to increase the federal cost share from 75% to 90% for certain assistance provided in rural or disadvantaged areas.\u00a0It also authorizes\u00a0an increased HMGP federal cost share amount from 75% to 90% for assistance\u00a0in rural or disadvantaged areas.\u00a0</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr437"
    },
    "title": "SNOW Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Support Neighborhoods Offset Winter Damage Act of 2025 or the SNOW Act of 2025</strong></p><p>This bill authorizes Federal Emergency Management Agency (FEMA) grant funding for winter storm hazard mitigation and requires FEMA rulemaking to expand\u00a0assistance for winter storms. It also increases the federal cost share for various FEMA grants, for any hazard type, in rural or disadvantaged areas.</p><p>The bill specifically authorizes the use of grant funding under the Hazard Mitigation Grant Program (HMGP) and Building Resilient Infrastructure and Communities program\u00a0to reduce the risk of future damage in areas affected by winter storms, such as by\u00a0acquiring snow removal equipment.\u00a0</p><p>Also, under current FEMA policy, in determining eligibility and recommending a presidential major disaster declaration for a snowstorm, FEMA\u2019s considerations include whether data shows record (or near record) snowfall and whether estimated statewide costs meet applicable thresholds. The bill requires FEMA to create regulations waiving these eligibility requirements for a major disaster declaration for a snowstorm in certain circumstances. FEMA must also create regulations to provide certain\u00a0assistance for winter storms, including for debris removal and specified infrastructure, as well as individual and emergency assistance when the state determines the storm exceeds state and local capacity.\u00a0</p><p>In addition, for any hazard type, the bill requires FEMA to increase the federal cost share from 75% to 90% for certain assistance provided in rural or disadvantaged areas.\u00a0It also authorizes\u00a0an increased HMGP federal cost share amount from 75% to 90% for assistance\u00a0in rural or disadvantaged areas.\u00a0</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr437"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr437ih.xml"
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
      "title": "SNOW Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T12:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SNOW Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T12:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Support Neighborhoods Offset Winter Damage Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T12:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to expand assistance related to winter storms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T12:48:18Z"
    }
  ]
}
```
