# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1828?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1828
- Title: School Bus Safety Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1828
- Origin chamber: House
- Introduced date: 2025-03-04
- Update date: 2026-04-21T08:05:48Z
- Update date including text: 2026-04-21T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-04: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-04 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-04 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-03-04: Introduced in House

## Actions

- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-04 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-04 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1828",
    "number": "1828",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "School Bus Safety Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-21T08:05:48Z",
    "updateDateIncludingText": "2026-04-21T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T15:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-04T23:04:30Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-04T15:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1828ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1828\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2025 Mr. Cohen introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Transportation to issue rules requiring the inclusion of new safety equipment in school buses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the School Bus Safety Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) 3-point safety belt**\nThe term 3-point safety belt has the meaning given the term Type 2 seat belt assembly in section 571.209 of title 49, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(2) Automatic emergency braking system**\nThe term automatic emergency braking system means a crash avoidance system installed and operational in a vehicle that consists of\u2014\n**(A)**\na forward collision warning function\u2014\n**(i)**\nto detect vehicles and objects ahead of the vehicle; and\n**(ii)**\nto alert the operator of the vehicle of an impending collision; and\n**(B)**\na crash-imminent braking function to provide automatic braking when forward-looking sensors of the vehicle indicate that\u2014\n**(i)**\na crash is imminent; and\n**(ii)**\nthe operator of the vehicle is not reacting in a timely or appropriate manner.\n**(3) Event data recorder**\nThe term event data recorder has the meaning given the term in section 563.5(b) of title 49, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(4) School bus**\nThe term school bus has the meaning given the term schoolbus in section 30125(a) of title 49, United States Code.\n**(5) Secretary**\nThe term Secretary means the Secretary of Transportation.\n#### 3. School bus safety\n##### (a) Seat belt requirement\nNot later than 1 year after the date of enactment of this Act, the Secretary shall issue final rules prescribing or amending motor vehicle safety standards under chapter 301 of title 49, United States Code, to require school buses with a gross vehicle weight rating of greater than 10,000 pounds to be equipped with a 3-point safety belt at each designated seating position.\n##### (b) Fire protection requirements\n**(1) Fire suppression systems**\n**(A) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall issue rules prescribing or amending motor vehicle safety standards under chapter 301 of title 49, United States Code, to require school buses to be equipped with fire suppression systems that, at a minimum, address engine fires.\n**(B) Application**\nThe standards prescribed or amendments made under subparagraph (A) shall apply to school buses manufactured in, or imported into, the United States on or after the effective date of the standards or amendments.\n**(2) Firewalls**\n**(A) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall issue rules prescribing or amending motor vehicle safety standards under chapter 301 of title 49, United States Code, for school buses, especially school buses with engines that extend beyond the firewall, to ensure that no hazardous quantity of gas or flame can pass through the firewall from the engine compartment to the passenger compartment.\n**(B) Application**\nThe standards prescribed or amendments made under subparagraph (A) shall apply to school buses manufactured in, or imported into, the United States on or after the effective date of the standards or amendments.\n**(3) Interior flammability and smoke emissions characteristics**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall amend section 571.302 of title 49, Code of Federal Regulations (relating to Federal Motor Vehicle Safety Standard Number 302), to adopt, with respect to a motor vehicle (as defined in section 30102(a) of title 49, United States Code), performance standards for interior flammability and smoke emissions characteristics that are not less rigorous than the performance standards for interior flammability and smoke emissions characteristics applicable to\u2014\n**(A)**\na compartment occupied by the crew or passengers of a transport category airplane (within the meaning of part 25 of title 14, Code of Federal Regulations (as in effect on the date of enactment of this Act)) under section 25.853 of title 14, Code of Federal Regulations (as in effect on the date of enactment of this Act); and\n**(B)**\na passenger car or locomotive cab (as those terms are defined in section 238.5 of title 49, Code of Federal Regulations (as in effect on the date of enactment of this Act)) under section 238.103 of title 49, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n##### (c) Other safety equipment requirements\nNot later than 1 year after the date of enactment of this Act, the Secretary shall issue final rules\u2014\n**(1)**\nprescribing or amending motor vehicle safety standards under chapter 301 of title 49, United States Code, to require school buses to be equipped with\u2014\n**(A)**\nan automatic emergency braking system;\n**(B)**\nan event data recorder; and\n**(C)**\nan electronic stability control system (as defined in section 571.136 of title 49, Code of Federal Regulations (as in effect on the date of enactment of this Act)); and\n**(2)**\namending part 383 of title 49, Code of Federal Regulations, to require not less than 8 hours of behind-the-wheel instruction for operators of school buses, which shall be accrued\u2014\n**(A)**\non public roads; and\n**(B)**\nwith a trained instructor who possesses a valid commercial driver\u2019s license with a school bus endorsement.\n##### (d) Obstructive sleep apnea\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Federal Motor Carrier Safety Administration and the Administrator of the Federal Railroad Administration shall complete the rulemaking process and publish a final rule with respect to the advance notice of proposed rulemaking entitled Evaluation of Safety Sensitive Personnel for Moderate-to-Severe Obstructive Sleep Apnea (81 Fed. Reg. 12642 (March 10, 2016)).\n##### (e) Effective date\nThe standards prescribed or amendments made under subsections (a) and (c) shall apply with respect to school buses manufactured in, or imported into, the United States on or after the date that is 1 year after the date on which the Secretary issues the rules required under the applicable subsection.\n#### 4. Studies\n##### (a) Motion-Activated detection systems\n**(1) In general**\nNot later than 2 years after the date of enactment of this Act, the Administrator of the National Highway Traffic Safety Administration (referred to in this section as the Administrator ) shall complete a study with respect to the benefits of requiring school buses manufactured in, or imported into, the United States to be equipped with a motion-activated detection system that is capable of\u2014\n**(A)**\ndetecting pedestrians, bicyclists, and other road users located near the exterior of the school bus; and\n**(B)**\nalerting the operator of the school bus of the road users described in subparagraph (A).\n**(2) Regulations**\nNot later than 1 year after the date on which the Administrator completes the study under paragraph (1), the Administrator shall issue rules requiring school buses manufactured in, or imported into, the United States to effectuate that requirement.\n##### (b) Safety belt alert\nNot later than 2 years after the date of enactment of this Act, the Administrator shall complete a study on the benefits of requiring school buses manufactured in, or imported into, the United States to be equipped with a system to alert the operator of the school bus if a passenger in the school bus is not wearing a 3-point safety belt equipped on the school bus.\n#### 5. Safety grant program\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Transportation shall establish a grant program to provide grants to States to make subgrants to local educational agencies\u2014\n**(1)**\nto assist the local educational agencies in purchasing school buses equipped with\u2014\n**(A)**\n3-point safety belts at each designated seating position; or\n**(B)**\nany other school bus safety feature described in section 3 or 4; and\n**(2)**\nto assist the local educational agencies in modifying school buses already owned by the local educational agency to be equipped with\u2014\n**(A)**\n3-point safety belts at each designated seating position; or\n**(B)**\nany other school bus safety feature described in section 3 or 4.\n##### (b) Authorization of appropriations\nThere are authorized to be appropriated such sums as are necessary to carry out this section.",
      "versionDate": "2025-03-04",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-04",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "828",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "School Bus Safety Act of 2025",
      "type": "S"
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
        "updateDate": "2025-03-21T16:37:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-04",
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
          "measure-id": "id119hr1828",
          "measure-number": "1828",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-04",
          "originChamber": "HOUSE",
          "update-date": "2025-07-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1828v00",
            "update-date": "2025-07-29"
          },
          "action-date": "2025-03-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>School Bus Safety Act of\u00a02025</strong></p><p>This bill directs the Department of Transportation (DOT) to issue rules requiring school buses to have certain safety features.\u00a0DOT must also establish a grant program to assist in the implementation of the requirements.</p><p>Specifically, DOT must issue rules requiring school buses to include</p><ul><li>three-point safety belts for all seats,</li><li>a fire suppression system which addresses engine fires,</li><li>a firewall between the engine and passenger compartment\u00a0that prevents hazardous quantities of gas or flames from passing through the firewall,</li><li>increased\u00a0performance standards for interior flammability and smoke emissions,</li><li>an automatic emergency braking system,</li><li>an event data recorder, and</li><li>an electronic stability control system.</li></ul><p>DOT must also require at least eight hours of behind-the-wheel training for school bus operators that meets specified requirements.</p><p>Further, the Federal Motor Carrier Safety Administration and the National Highway Traffic Safety Administration (NHTSA) must issue rules on\u00a0the evaluation of safety sensitive personnel for moderate-to-severe obstructive sleep apnea.</p><p>NHTSA\u00a0must also study the benefits of requiring school buses manufactured in, or imported into, the United States to be equipped with a motion-activated detection system that is capable of\u00a0detecting road users (e.g., pedestrians and bicyclists) and alerting the bus operator of their presence.\u00a0NHTSA must issue rules implementing such a requirement.</p><p>Finally, DOT must establish a grant program to assist local educational agencies in (1) purchasing school buses equipped with three-point safety belts or any of the other safety features required under this bill, and (2) modifying\u00a0existing school buses.</p>"
        },
        "title": "School Bus Safety Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1828.xml",
    "summary": {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>School Bus Safety Act of\u00a02025</strong></p><p>This bill directs the Department of Transportation (DOT) to issue rules requiring school buses to have certain safety features.\u00a0DOT must also establish a grant program to assist in the implementation of the requirements.</p><p>Specifically, DOT must issue rules requiring school buses to include</p><ul><li>three-point safety belts for all seats,</li><li>a fire suppression system which addresses engine fires,</li><li>a firewall between the engine and passenger compartment\u00a0that prevents hazardous quantities of gas or flames from passing through the firewall,</li><li>increased\u00a0performance standards for interior flammability and smoke emissions,</li><li>an automatic emergency braking system,</li><li>an event data recorder, and</li><li>an electronic stability control system.</li></ul><p>DOT must also require at least eight hours of behind-the-wheel training for school bus operators that meets specified requirements.</p><p>Further, the Federal Motor Carrier Safety Administration and the National Highway Traffic Safety Administration (NHTSA) must issue rules on\u00a0the evaluation of safety sensitive personnel for moderate-to-severe obstructive sleep apnea.</p><p>NHTSA\u00a0must also study the benefits of requiring school buses manufactured in, or imported into, the United States to be equipped with a motion-activated detection system that is capable of\u00a0detecting road users (e.g., pedestrians and bicyclists) and alerting the bus operator of their presence.\u00a0NHTSA must issue rules implementing such a requirement.</p><p>Finally, DOT must establish a grant program to assist local educational agencies in (1) purchasing school buses equipped with three-point safety belts or any of the other safety features required under this bill, and (2) modifying\u00a0existing school buses.</p>",
      "updateDate": "2025-07-29",
      "versionCode": "id119hr1828"
    },
    "title": "School Bus Safety Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>School Bus Safety Act of\u00a02025</strong></p><p>This bill directs the Department of Transportation (DOT) to issue rules requiring school buses to have certain safety features.\u00a0DOT must also establish a grant program to assist in the implementation of the requirements.</p><p>Specifically, DOT must issue rules requiring school buses to include</p><ul><li>three-point safety belts for all seats,</li><li>a fire suppression system which addresses engine fires,</li><li>a firewall between the engine and passenger compartment\u00a0that prevents hazardous quantities of gas or flames from passing through the firewall,</li><li>increased\u00a0performance standards for interior flammability and smoke emissions,</li><li>an automatic emergency braking system,</li><li>an event data recorder, and</li><li>an electronic stability control system.</li></ul><p>DOT must also require at least eight hours of behind-the-wheel training for school bus operators that meets specified requirements.</p><p>Further, the Federal Motor Carrier Safety Administration and the National Highway Traffic Safety Administration (NHTSA) must issue rules on\u00a0the evaluation of safety sensitive personnel for moderate-to-severe obstructive sleep apnea.</p><p>NHTSA\u00a0must also study the benefits of requiring school buses manufactured in, or imported into, the United States to be equipped with a motion-activated detection system that is capable of\u00a0detecting road users (e.g., pedestrians and bicyclists) and alerting the bus operator of their presence.\u00a0NHTSA must issue rules implementing such a requirement.</p><p>Finally, DOT must establish a grant program to assist local educational agencies in (1) purchasing school buses equipped with three-point safety belts or any of the other safety features required under this bill, and (2) modifying\u00a0existing school buses.</p>",
      "updateDate": "2025-07-29",
      "versionCode": "id119hr1828"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1828ih.xml"
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
      "title": "School Bus Safety Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "School Bus Safety Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to issue rules requiring the inclusion of new safety equipment in school buses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:33Z"
    }
  ]
}
```
