# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3661?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3661
- Title: Extreme Weather and Heat Response Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 3661
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2025-11-22T09:06:55Z
- Update date including text: 2025-11-22T09:06:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-30 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-30 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3661",
    "number": "3661",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Extreme Weather and Heat Response Modernization Act",
    "type": "HR",
    "updateDate": "2025-11-22T09:06:55Z",
    "updateDateIncludingText": "2025-11-22T09:06:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-30",
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
      "actionDate": "2025-05-29",
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
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-30T19:47:25Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "AZ"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "NY"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "NM"
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
      "sponsorshipDate": "2025-06-20",
      "state": "DC"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "NJ"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MI"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3661ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3661\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Ms. Titus (for herself and Mr. Stanton ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Administrator of the Federal Emergency Management Agency to take certain actions relating to incident periods and extreme weather, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Extreme Weather and Heat Response Modernization Act .\n#### 2. Incident periods\n##### (a) In general\nNot later than 6 months after the date of enactment of this Act, the Administrator of the Federal Emergency Management Agency shall convene an advisory panel consisting of emergency management personnel to assist the Agency in reviewing the process and procedures related to the determination of incident periods for all hazards for emergencies or major disasters declared under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ).\n##### (b) Membership\n**(1) In general**\nThis advisory panel convened under subsection (a) shall consist of at least 2 representatives from national emergency management organizations, at least 2 relevant county officials, at least 1 representative from the National Weather Service, and at least 5 representatives from each of the 10 regions of the Federal Emergency Management Agency selected from emergency management personnel employed by State, local, territorial, or Tribal authorities within each region.\n**(2) Inclusion on panel**\nTo the furthest extent practicable, representation on the advisory panel shall include emergency management personnel from rural, urban, underrepresented, Tribal, and insular jurisdictions and representatives of State or local governments with responsibility for the financial or budgetary impact of disasters.\n##### (c) Considerations\nIn reviewing the process and procedures related to the determination of incident periods under subsection (a), the advisory panel convened under such subsection shall consider the effectiveness of incident periods, including\u2014\n**(1)**\nincident periods for slow on-set disasters;\n**(2)**\nincident periods for correlated non-contiguous disasters;\n**(3)**\nincident periods for compound disasters; and\n**(4)**\nincident periods for cascading disasters.\n##### (d) Interim report\nNot later than 1 year after the date of enactment of this Act, the Administrator shall submit to Congress, and make publicly available, a report regarding the findings of the review under this section that includes any recommendations of the advisory panel convened under subsection (a), including additional legislation that may be necessary to address such findings.\n##### (e) Final report\nNot later than 2 years after the date of enactment of this Act, the Administrator shall submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report discussing\u2014\n**(1)**\na summary of the findings of the advisory panel convened under subsection (a);\n**(2)**\nthe implementation of recommendations from such advisory panel; and\n**(3)**\nany additional legislative recommendations necessary to improve the effectiveness of incident periods.\n##### (f) Rulemaking\nImmediately following a 30 day congressional review period of the report described in subsection (e), the Administrator shall begin a rulemaking to issue such regulations as are necessary to implement the recommendations of the advisory panel.\n#### 3. Mitigation and preparedness\n##### (a) In general\nThe Administrator of the Federal Emergency Management Agency may, under section 203 and 404 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act (42 U.S.C. 5133 and 5170c)\u2014\n**(1)**\nconsider innovative preparedness and mitigation projects eligible for the purposes of mitigating impacts during an extreme heat event, including stockpiling and installing equipment for households, first responders, and public health and health care systems and emergency voucher programs;\n**(2)**\nconsider innovative preparedness and mitigation projects eligible for the purposes of mitigating the impacts of extreme cold; and\n**(3)**\nwith respect to eligible uses of funds authorized, provide, and issue relevant guidance, for the establishment and function of\u2014\n**(A)**\ncommunity cooling centers; and\n**(B)**\nresilience centers.\n##### (b) Supplement not supplant\nAssistance provided under this section shall be used to supplement and not supplant other assistance provided under any other Act.\n##### (c) Definitions\nIn this section:\n**(1) Community cooling center**\nThe term community cooling center means a public serving facility that provides an environment for people to maintain a healthy body temperature during an extreme heat event.\n**(2) Resilience center**\nThe term resilience center means a public serving facility with a hazard resistant design with the purpose of programing, operations, and communication to build community resilience before, during, and after emergency events.\n#### 4. Guidance\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Emergency Management Agency shall issue guidance related to\u2014\n**(1)**\nextreme temperature events, including heat waves and freezes, and publish such guidance in the Federal Emergency Management Agency Public Assistance Program and Policy Guide;\n**(2)**\nhazard mitigation, including eligibility criteria for projects that primarily mitigate the impacts of extreme heat and projects specified in section 3(a)(2); and\n**(3)**\nextreme heat for the purposes of hazard mitigation planning under section 322 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5165 ), the National Preparedness Course Catalog, National Disaster Recovery Framework, National Response Recovery Framework, and Threat and Hazard Identification and Risk Assessment.\n#### 5. Study on extreme heat and cold\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Emergency Management Agency shall conduct a study to measure the impact of extreme heat and recommend guidance on mitigating and responding to extreme heat and cold.\n##### (b) Consultation\nIn conducting the study required under subsection (a), the Administrator shall consult with relevant stakeholders and the heads of other Federal agencies.\n##### (c) Content\nIn conducting the study required under subsection (a), the Administrator shall\u2014\n**(1)**\nexamine and consider solutions to address the impact of extreme heat and cold on\u2014\n**(A)**\ndisadvantaged communities;\n**(B)**\nbuildings, roads, utilities, power generation, air conditioning units, and other relevant infrastructure;\n**(C)**\nshort- and long-term health outcomes; and\n**(D)**\npets and livestock;\n**(2)**\nevaluate the geographical and regional differences in the occurrence and impact of extreme heat and cold;\n**(3)**\nevaluate the effectiveness of emergency alerts and the language used in such alerts to improve public safety during extreme heat and cold events;\n**(4)**\nexamine metrics for defining and communicating the severity of an extreme heat and cold event;\n**(5)**\nexamine the compounding effects and consequential risk of extreme heat and cold and wildfire smoke;\n**(6)**\nrecommend best practices for community education and safety during extreme heat and cold events;\n**(7)**\nexamine the impact extreme heat and cold to the health and safety of the Federal Emergency Management Agency workforce when responding to disasters;\n**(8)**\ndevelop guidance for first responder training protocol for extreme heat and cold emergencies; and\n**(9)**\nrecommend guidance for incorporating extreme heat and cold into local and State government emergency management preparedness plans.\n##### (d) Report to Congress\nNot less than 1 year after the date of enactment of this Act, the Administrator shall submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Homeland Security and Government Affairs of the Senate a report containing\u2014\n**(1)**\nthe results of study required under subsection (a); and\n**(2)**\nany additional recommendations for developing a framework for mitigating and responding to extreme heat and cold emergencies.",
      "versionDate": "2025-05-29",
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
        "updateDate": "2025-06-23T17:39:17Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3661ih.xml"
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
      "title": "Extreme Weather and Heat Response Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Extreme Weather and Heat Response Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T09:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Federal Emergency Management Agency to take certain actions relating to incident periods and extreme weather, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T09:18:19Z"
    }
  ]
}
```
