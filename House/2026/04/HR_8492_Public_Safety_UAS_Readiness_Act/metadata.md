# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8492?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8492
- Title: Public Safety UAS Readiness Act
- Congress: 119
- Bill type: HR
- Bill number: 8492
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-18T16:14:56Z
- Update date including text: 2026-05-18T16:14:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8492",
    "number": "8492",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Public Safety UAS Readiness Act",
    "type": "HR",
    "updateDate": "2026-05-18T16:14:56Z",
    "updateDateIncludingText": "2026-05-18T16:14:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
          "date": "2026-04-23T13:02:25Z",
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
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8492ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8492\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mr. Subramanyam (for himself and Mr. Bresnahan ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Secretary of Transportation to establish a grant program for unmanned aircraft system pilot training, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public Safety UAS Readiness Act .\n#### 2. Unmanned aircraft system pilot training grant program\n##### (a) Establishment\nThe Secretary of Transportation, acting through the Administrator of the Federal Aviation Administration, shall establish a program to award grants to covered entities to carry out activities to support training of unmanned aircraft system pilots.\n##### (b) Eligible activities\nA covered entity in receipt of a grant awarded under this section may use such grant\u2014\n**(1)**\nto establish and develop an unmanned aircraft system training program, including curriculum design, instructional materials, and related resources necessary to carry out\u2014\n**(A)**\ntraining of public safety personnel on aviation safety, Federal Aviation Administration regulations, basic airspace principles, and public safety mission profiles relating to the operation of unmanned aircraft systems;\n**(B)**\ntraining of certified remote pilots on risk management, flight execution, data collection for unmanned aircraft systems;\n**(C)**\nspecialized instruction for certified remote pilots leading unmanned aircraft system missions in complex, multi-agency environments; and\n**(D)**\nthe development and validation of public safety UAS instructors to serve as instructors in certain regions throughout the United States upon completion of such certification;\n**(2)**\nto purchase an unmanned aircraft system that meets all Federal safety standards and regulatory requirements for the purpose of carrying out the training described in this paragraph; and\n**(3)**\nfor reasonable administrative costs directly associated with the delivery of training and program implementation under this section, including support services necessary to ensure student participation and program completion, expenses incurred due to staff attendance, including travel coordination, and local facility use.\n##### (c) Comprehensive plan\nTo be eligible to receive a grant under this section, a covered entity shall demonstrate the ability to manage Federal funds and submit to the Secretary a comprehensive plan describing how such entity will use such funds to develop and sustain unmanned aircraft system training and operations. Such entity shall include in the comprehensive plan information on\u2014\n**(1)**\nadministration and oversight for any program proposed to be established using such grant;\n**(2)**\nrisk management procedures;\n**(3)**\nairspace coordination and safety protocols;\n**(4)**\ncertified personnel rosters;\n**(5)**\nequipment maintenance schedules;\n**(6)**\ndata and privacy protections; and\n**(7)**\nlegal compliance documentation.\n##### (d) Requirements\nWith respect to a training program established with a grant awarded under this section, a covered entity shall\u2014\n**(1)**\noperate or administer such program in accordance with applicable Federal law and regulations, which may include section 44807 of title 49, United States Code, or parts 91 or 107 of title 14, Code of Federal Regulations, as applicable, and\u2014\n**(A)**\nNational Wildfire Coordinating Group Standard A\u2013450 or S\u2013373;\n**(B)**\nASTM International Standard F3266, F3330, or F3370; or\n**(C)**\nNational Fire Protection Association Standard 2400; and\n**(2)**\nensure\u2014\n**(A)**\nthat the curriculum for such program is maintained by, or licensed through, a national nonprofit public safety organization or a nonprofit emergency response training entity;\n**(B)**\nthat such curriculum remains consistent with operational standards and reflects mission specific public safety training needs; and\n**(C)**\nthat any modification to such curriculum is subject to the approval of the organization through which the curriculum is maintained or licensed.\n##### (e) Prioritization\nIn awarding grants under this section, the Secretary shall prioritize selecting covered entities who\u2014\n**(1)**\nengage in high risk operations or operate in underserved regions;\n**(2)**\ndemonstrate multi-agency or regional coordination;\n**(3)**\npropose to carry out training that is consistent with Federal Aviation Administration, National Wildfire Coordinating Group, and National Fire Protection Association standards; and\n**(4)**\nlack the capacity for unmanned aircraft systems training.\n##### (f) Reports\n**(1) Report by recipient**\nEach recipient of a grant awarded under this section shall, not less frequently than annually, submit to the Secretary a report containing the following information:\n**(A)**\nThe number and type of personnel trained using such grant.\n**(B)**\nThe number of certifications of public safety UAS instructors under subsection (b)(4).\n**(C)**\nThe number of instructors participating in any training provided using such grant.\n**(D)**\nThe number of unmanned aircraft system deployments carried out by such recipient after completion of training carried out with such grant.\n**(E)**\nChallenges or recommendations related to a program established using such grant.\n**(2) Report by Secretary**\nNot less frequently than annually, the Secretary shall submit to Congress a report on the grant program carried out under this section that contains the following information:\n**(A)**\nA description of grant recipients, disaggregated by region and type of entity receiving such grant.\n**(B)**\nA summary of progress made in building unmanned aircraft system training capacity across the United States.\n**(C)**\nAny recommendations for improvements to training standards and the grant program established under this section.\n##### (g) Definitions\nIn this section:\n**(1) Certified remote pilot**\nThe term certified remote pilot means a pilot certified to operate an unmanned aircraft system under part 107 of title 14, Code of Federal Regulations, or under a valid public aircraft operation or Federal Aviation Administration authorization.\n**(2) Covered entity**\nThe term covered entity means\u2014\n**(A)**\na governmental or nonprofit fire department, emergency medical service, or law enforcement agency;\n**(B)**\na State or regional public safety training academy;\n**(C)**\nan interagency unmanned aircraft system collaborative; or\n**(D)**\na nonprofit public safety training organization that\u2014\n**(i)**\nhas demonstrated a national presence in public safety education;\n**(ii)**\nmaintains a primary mission focused on emergency response readiness; and\n**(iii)**\nhas a documented history of partnerships with Federal, State, Tribal, territorial, or local public safety agencies.\n**(3) Emergency medical service**\nThe term emergency medical service has the meaning given the term emergency medical services under section 553(e) of the Public Health Service Act ( 42 U.S.C. 290ee\u201310(e) ).\n**(4) High risk operation**\nThe term high risk operation means an unmanned aircraft mission conducted in an environment, condition, or for purposes where a loss of control, system, failure, or operational error could reasonably be expected to result in serious injury or death, substantial property damage, or disruption to public safety or critical infrastructure.\n**(5) Interagency unmanned aircraft system collaborative**\nThe term interagency unmanned aircraft system collaborative means a formal partnership, task force, or mutual aid framework involving 2 or more governmental or nonprofit public safety or emergency response agencies that jointly develop, operate, or coordinate unmanned aircraft system training and deployment to support all-hazards response.\n**(6) Nonprofit**\nThe term nonprofit , with respect to a covered entity, means an entity that is described in section 501(c) of the Internal Revenue Code of 1986 and is exempt from taxation under section 501(a) of such code.\n**(7) Public safety UAS instructor**\nThe term public safety UAS instructor means an instructor providing training for unmanned aircraft system operations conducted for the purpose of emergency response at or on behalf of a covered entity.\n**(8) Unmanned aircraft system**\nThe term unmanned aircraft system has the meaning given such term in section 44801 of title 49, United States Code.\n##### (h) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2026 through 2029.",
      "versionDate": "2026-04-23",
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
        "updateDate": "2026-05-18T16:14:55Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8492ih.xml"
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
      "title": "Public Safety UAS Readiness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T13:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Public Safety UAS Readiness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T13:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Transportation to establish a grant program for unmanned aircraft system pilot training, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T13:03:31Z"
    }
  ]
}
```
