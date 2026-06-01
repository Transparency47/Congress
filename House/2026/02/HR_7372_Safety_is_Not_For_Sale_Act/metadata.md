# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7372?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7372
- Title: Safety is Not For Sale Act
- Congress: 119
- Bill type: HR
- Bill number: 7372
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-03-18T15:32:10Z
- Update date including text: 2026-03-18T15:32:10Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7372",
    "number": "7372",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "P000034",
        "district": "6",
        "firstName": "Frank",
        "fullName": "Rep. Pallone, Frank [D-NJ-6]",
        "lastName": "Pallone",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Safety is Not For Sale Act",
    "type": "HR",
    "updateDate": "2026-03-18T15:32:10Z",
    "updateDateIncludingText": "2026-03-18T15:32:10Z"
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
          "date": "2026-02-04T15:03:40Z",
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
                "date": "2026-02-10T21:06:29Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-10T21:05:29Z",
                "name": "Markup by"
              },
              {
                "date": "2026-02-04T21:04:51Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7372ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7372\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Mr. Pallone introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo ensure that lifesaving motor vehicle safety features are offered independently of convenience and luxury features, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safety is Not For Sale Act .\n#### 2. Prohibition on certain sales practices with respect to optional safety features for motor vehicles\n##### (a) Prohibition\n**(1) In general**\nA person may not offer for sale or lease to a first purchaser an optional safety feature unless such person\u2014\n**(A)**\noffers such optional safety feature for sale or lease\u2014\n**(i)**\nseparately from any non-safety feature; or\n**(ii)**\nas standard trim equipment; and\n**(B)**\nclearly and conspicuously discloses to the first purchaser the cost of the optional safety feature separately from any non-safety feature.\n**(2) Effective date**\nParagraph (1) shall take effect on the date that is 180 days after the date of the enactment of this Act.\n##### (b) Enforcement by Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of subsection (a) shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\nThe Commission shall enforce subsection (a) in the same manner, by the same means, and with the same jurisdiction as though all applicable terms and provisions of the Federal Trade Commission Act were incorporated into and made a part of this Act.\n**(3) Rule of construction**\nNothing in this Act shall be construed to limit the authority of the Commission under any other law.\n##### (c) Actions by States\n**(1) In general**\nExcept as provided in paragraph (6), in any case in which the attorney general of a State has reason to believe that an interest of the residents of that State has been or is threatened or adversely affected by an act or practice in violation of subsection (a), or a regulation promulgated under such subsection, the State, as parens patriae, may bring a civil action on behalf of the residents of the State in an appropriate district court of the United States or other court of competent jurisdiction to\u2014\n**(A)**\nenjoin that practice;\n**(B)**\nenforce compliance with such subsection, or such regulation;\n**(C)**\nobtain civil penalties;\n**(D)**\nobtain damages, restitution, or other compensation on behalf of residents of the State; and\n**(E)**\nobtain such other legal and equitable relief as the court may consider to be appropriate.\n**(2) Rights of Commission**\n**(A) Notice**\n**(i) In general**\nExcept as provided in clause (iii), the attorney general of a State shall notify the Commission in writing that the attorney general intends to bring a civil action under paragraph (1) by not later than 60 days before initiating the civil action.\n**(ii) Contents**\nThe notification required by clause (i) with respect to a civil action shall include a copy of the complaint to be filed to initiate the civil action.\n**(iii) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required by clause (i) before initiating a civil action under paragraph (1), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(B) Intervention**\nUpon receiving the notice required by subparagraph (A), the Commission shall have the right\u2014\n**(i)**\nto intervene in the action; and\n**(ii)**\nupon so intervening\u2014\n**(I)**\nto be heard on all matters arising therein; and\n**(II)**\nto file petitions for appeal.\n**(3) Investigatory powers; savings provision**\nNothing in this subsection may be construed to\u2014\n**(A)**\nprevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence; or\n**(B)**\nprohibit the attorney general of a State, or other authorized State officer, from proceeding in State or Federal court on the basis of an alleged violation of any civil or criminal statute of that State.\n**(4) Limitation on state action while Federal action is pending**\nIf the Commission or the Attorney General of the United States has instituted a civil action for violation of this Act (referred to in this subparagraph as the Federal action ), no State attorney general, official, or agency may bring an action under this subsection during the pendency of the Federal action against any defendant named in the complaint in the Federal action for any violation of such subsection alleged in such complaint.\n**(5) Award of costs and fees**\nIf a State prevails in any civil action under paragraph (1), the State may recover reasonable costs and attorney fees.\n##### (d) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) First purchaser; manufacturer; motor vehicle; motor vehicle equipment**\nThe terms first purchaser , manufacturer , motor vehicle , and motor vehicle equipment have the meanings given those terms in section 30102 of title 49, United States Code.\n**(3) Motor vehicle model**\nThe term motor vehicle model means a class of motor vehicles\u2014\n**(A)**\nof the same type and make; and\n**(B)**\nthat share a high degree of commonality in design and construction.\n**(4) Motor vehicle trim**\nThe term motor vehicle trim means a class of motor vehicles\u2014\n**(A)**\nof the same type, make, and motor vehicle model, but not identical to the motor vehicle model; and\n**(B)**\nthat share a high degree of commonality in design and construction.\n**(5) Non-safety feature**\nThe term non-safety feature means optional motor vehicle equipment that is not standard model equipment or an optional safety feature.\n**(6) Optional safety feature**\nThe term optional safety feature means motor vehicle equipment that\u2014\n**(A)**\nis not standard model equipment; and\n**(B)**\neither\u2014\n**(i)**\nperforms the lateral or longitudinal (but not both simultaneously) vehicle motion control subtasks of the dynamic driving task with the expectation that the driver monitors the system to execute a response to an object or event when necessary;\n**(ii)**\nalerts the driver\u2014\n**(I)**\nif there is an unreasonable risk of a collision;\n**(II)**\nto maintain the lane of travel; or\n**(III)**\nif the driver is operating the motor vehicle in a way that indicates the driver may be distracted, disengaged, fatigued, intoxicated, or otherwise impaired;\n**(iii)**\nimproves illumination of the roadway;\n**(iv)**\nenhances the view of the driver of the roadway;\n**(v)**\nalerts emergency services after a crash of the motor vehicle is detected; or\n**(vi)**\nperforms such other safety functions as the Commission, in consultation with the Secretary of Transportation, determines appropriate.\n**(7) Standard model equipment**\nThe term standard model equipment means motor vehicle equipment installed in each motor vehicle within a motor vehicle model, regardless of the motor vehicle trim.\n**(8) Standard trim equipment**\nThe term standard trim equipment means motor vehicle equipment installed in each motor vehicle of a motor vehicle trim.",
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
            "name": "Accidents",
            "updateDate": "2026-03-18T15:32:09Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2026-03-18T15:30:58Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-03-18T15:28:12Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-03-18T15:30:38Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-03-18T15:31:37Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2026-03-18T15:31:45Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-03-18T15:28:02Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2026-03-18T15:27:57Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2026-03-18T15:32:01Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-03-18T15:30:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-02-13T17:08:31Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7372ih.xml"
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
      "title": "Safety is Not For Sale Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-07T05:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safety is Not For Sale Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that lifesaving motor vehicle safety features are offered independently of convenience and luxury features, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-07T05:03:37Z"
    }
  ]
}
```
