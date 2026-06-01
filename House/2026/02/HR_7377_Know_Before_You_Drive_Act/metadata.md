# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7377?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7377
- Title: Know Before You Drive Act
- Congress: 119
- Bill type: HR
- Bill number: 7377
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-02-26T15:45:35Z
- Update date including text: 2026-02-26T15:45:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-04 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-04 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7377",
    "number": "7377",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001216",
        "district": "8",
        "firstName": "Kim",
        "fullName": "Rep. Schrier, Kim [D-WA-8]",
        "lastName": "Schrier",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Know Before You Drive Act",
    "type": "HR",
    "updateDate": "2026-02-26T15:45:35Z",
    "updateDateIncludingText": "2026-02-26T15:45:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
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
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-10T21:10:24Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-10T21:09:34Z",
                "name": "Markup by"
              },
              {
                "date": "2026-02-04T21:08:21Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7377ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7377\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Ms. Schrier introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo inform consumers about the capabilities and limitations of partially automated vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Know Before You Drive Act .\n#### 2. Consumer education\n##### (a) Prohibition on misleading claims\nNot later than 180 days after the date of the enactment of this Act, a manufacturer may not make any representation that implies or would otherwise lead a reasonable person to believe that\u2014\n**(1)**\na partially automated driving system, or a feature or component of a partially automated driving system, is an automated driving system or a feature or component of an automated driving system; or\n**(2)**\na partially automated driving system, feature, or component\u2014\n**(A)**\ncan function as an automated driving system; or\n**(B)**\notherwise has capabilities beyond what the system, feature, or component is able to perform.\n##### (b) Notification upon first sale\n**(1) Notice required**\nNot later than 2 years after the date of the enactment of this Act, a manufacturer or dealer may not sell a partially automated vehicle or partially automated driving system without providing a clear and conspicuous notice to the purchaser that describes the following:\n**(A)**\nThat the vehicle is equipped with a partially automated driving system.\n**(B)**\nThe features of the partially automated driving system.\n**(C)**\nThe capabilities and limitations of the partially automated driving system, including the operational design domain.\n**(D)**\nThe subtasks of the dynamic driving task the driver is expected to perform while the partially automated driving system is performing part of the dynamic driving task, including the following:\n**(i)**\nThe object event detection and response subtask.\n**(ii)**\nSupervising a partially automated driving system.\n**(iii)**\nResponding to a request to intervene or to a performance-relevant system failure.\n**(2) Information**\nBefore delivering a partially automated vehicle to a dealer, a manufacturer shall provide the dealer with the notice described in paragraph (1).\n**(3) Compliance**\n**(A) Dealer**\nA dealer is not in violation of this section if a manufacturer fails to provide the notice pursuant to paragraph (2) or the notice is not in compliance with paragraph (1).\n**(B) Manufacturer**\nA manufacturer is not in violation of this section if the manufacturer complies with paragraph (2), but the dealer does not provide the notice required in paragraph (1) to a purchaser of a partially automated vehicle.\n##### (c) Updates\nBeginning 2 years after the date of the enactment of this Act and upon the proffer to an owner, lessee, or driver of a partially automated vehicle of a software update that materially affects the performance of the dynamic driving task, including an over-the-air update, a manufacturer shall provide a clear and conspicuous notice to such owner, lessee, or driver that describes each material change to the capabilities and limitations of the partially automated driving system with which the vehicle is equipped.\n##### (d) Enforcement authority\n**(1) Enforcement by NHTSA**\nSection 30165(a)(1) of title 49, United States Code, is amended by inserting after 31137, the following: subsections (a), (b), or (c) of section 2 of the Know Before You Drive Act , .\n**(2) Enforcement by Commission**\n**(A) Unfair or deceptive acts or practices**\nA violation of subsections (a), (b), or (c) shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(B) Powers of commission**\nThe Commission shall enforce subsections (a), (b), and (c) in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of such subsections. Any person who violates such subsections shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(C) Rule of construction**\nNothing in this Act may be construed to limit the authority of the Commission to enforce any other provision of law.\n**(3) Enforcement by States**\n**(A) Civil action**\nIn any case in which the attorney general of a State has reason to believe that an interest of the residents of such State has been, may be, or is adversely affected by an act or practice in violation of subsection (a), (b), or (c), the attorney general may bring a civil action in the name of the State, or as parens patriae on behalf of the residents of the State, in an appropriate district court of the United States to\u2014\n**(i)**\nenjoin such act or practice;\n**(ii)**\nenforce compliance with this Act;\n**(iii)**\nobtain damages, civil penalties, restitution, or other compensation on behalf of the residents of the State;\n**(iv)**\nobtain reasonable attorneys\u2019 fees and other litigation costs reasonably incurred; or\n**(v)**\nobtain such other legal and equitable relief as the court may consider to be appropriate.\n**(B) Notice**\nBefore filing an action under this paragraph, the attorney general of the State involved shall provide to the Commission a written notice of such action and a copy of the complaint for such action. If the attorney general determines that it is not feasible to provide the notice described in this subparagraph before the filing of the action, the attorney general shall provide written notice of the action and a copy of the complaint to the Commission immediately upon the filing of the action.\n**(C) Authority of commission**\n**(i) In general**\nOn receiving notice under subparagraph (B) of an action under this paragraph, the Commission shall have the right\u2014\n**(I)**\nto intervene in the action; and\n**(II)**\nupon so intervening\u2014\n**(aa)**\nto be heard on all matters arising therein; and\n**(bb)**\nto file petitions for appeal.\n**(ii) Limitation on state action while Federal action is pending**\nIf the Commission or the Attorney General of the United States has instituted a civil action for violation of subsection (a), (b), or (c) (referred to in this subparagraph as the Federal action ), no State attorney general may bring an action under this paragraph during the pendency of the Federal action against any defendant named in the complaint in the Federal action for any violation of subsection (a), (b), or (c) alleged in such complaint.\n**(D) Rule of construction**\nNothing in this Act may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of such State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary and other evidence.\n##### (e) Amendment of Automobile Information Disclosure Act\n**(1) Safety labeling requirement**\nSection 3 of the Automobile Information Disclosure Act ( 15 U.S.C. 1232 ) is amended\u2014\n**(A)**\nin subsection (g)(4)(B), by striking ; and and inserting a semicolon;\n**(B)**\nsubsection (h), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(i) if such automobile is equipped with a partially automated driving system or an automated driving system, information (in plain language or graphic icons that allows a purchaser to easily compare between automobiles equipped with such systems), including a short description of each such system that\u2014 (1) is sufficient for a consumer to identify the specific subtasks of the dynamic driving task the system is intended to perform; (2) indicates whether driver supervision is required during the execution of that subtask by the system; (3) describes the conditions that would place the system outside of the operational design domain, including any geographical restriction, time-of-day restriction, and road and environmental condition restriction; and (4) indicates whether such automated driving system requires additional service cost or fee, and if so, the service cost or fee on an annual basis. .\n**(2) Definitions**\nSection 2 of the Automobile Information Disclosure Act ( 15 U.S.C. 1231 ) is amended by adding at the end the following:\n(i) The terms automated driving system , dynamic driving task , operational design domain , partially automated driving system , and purchaser have the meaning given those terms in section 2(h) of the Know Before You Drive Act . .\n##### (f) Regulations\nNot later than 9 months after the date of the enactment of this Act, the Secretary of Transportation shall issue regulations to ensure the labeling requirements under subsection (i) of section 3 of the Automobile Information Disclosure Act, as added by subsection (d), are implemented within 2 years after the date of the enactment of this Act.\n##### (g) Rule of construction\nNothing in this section may be construed to exempt an individual from liability under applicable common or State law.\n##### (h) Definitions\nIn this section:\n**(1) Automated driving system**\nThe term automated driving system means hardware and software that are collectively capable of performing the entire dynamic driving task on a sustained basis, regardless of whether such system is limited to a specific operational design domain.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Dealer**\nThe term dealer has the meaning given that term in section 30102 of title 49, United States Code.\n**(4) Dynamic driving task**\n**(A) In general**\nThe term dynamic driving task means each real-time operational and tactical function required to operate a motor vehicle in on-road traffic.\n**(B) Inclusions**\nThe term dynamic driving task includes the following:\n**(i)**\nControlling the lateral motion of a motor vehicle through steering.\n**(ii)**\nControlling the longitudinal motion of a motor vehicle through acceleration and deceleration.\n**(iii)**\nMonitoring the driving environment through the detection, recognition, and classification of objects and events.\n**(iv)**\nPreparing a response to an object or event.\n**(v)**\nExecuting a response to an object or event.\n**(vi)**\nPlanning a maneuver.\n**(vii)**\nEnhancing conspicuity through lighting, signaling, gesturing, or another indicator.\n**(C) Exclusion**\nThe term dynamic driving task does not include the strategic functions relating to the operation of a motor vehicle, such as\u2014\n**(i)**\ntrip scheduling;\n**(ii)**\nselection of a destination; and\n**(iii)**\nselection of a waypoint.\n**(5) Operational design domain**\nThe term operational design domain means the specific operating conditions under which a given partially automated driving system, automated driving system, or feature of such system is specifically designed to function, including any environmental, geographical, and time-of-day restriction and the requisite presence or absence of certain traffic or roadway characteristics.\n**(6) Partially automated driving system**\nThe term partially automated driving system means a system of which the hardware and software collectively perform the lateral and longitudinal vehicle motion control subtasks of the dynamic driving task with the expectation that the driver monitors the system and completes the object and event detection and response subtask.\n**(7) Partially automated vehicle**\nThe term partially automated vehicle means a motor vehicle that is equipped with a partially automated driving system.\n**(8) Purchaser**\nThe term purchaser means an individual who purchases a motor vehicle or enters into a contract to lease a motor vehicle before first sale and not for resale.",
      "versionDate": "2026-02-04",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-02-26T15:28:29Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-02-26T15:19:05Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2026-02-26T15:44:57Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2026-02-26T15:28:55Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-02-26T15:45:34Z"
          },
          {
            "name": "Hybrid, electric, and advanced technology vehicles",
            "updateDate": "2026-02-26T15:18:51Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2026-02-26T15:44:35Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-02-26T15:18:56Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2026-02-26T15:19:23Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-26T15:28:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2026-02-26T12:49:31Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7377ih.xml"
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
      "title": "Know Before You Drive Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-07T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Know Before You Drive Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To inform consumers about the capabilities and limitations of partially automated vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-07T04:48:19Z"
    }
  ]
}
```
